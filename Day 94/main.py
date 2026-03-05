"""
T-Rex Dinosaur Game Bot

Uses OpenCV + Canny edge detection to detect obstacles.
Run: pip install opencv-python pyautogui numpy pynput
"""

import cv2
import numpy as np
import pyautogui
from pynput.keyboard import Key, Controller
import time

# === SETTINGS (ADJUST FOR YOUR SCREEN!) ===

# Game area on screen (left, top, width, height)
GAME_AREA = (100, 300, 800, 200)

# Detection zone relative to game area (x1, y1, x2, y2)
OBSTACLE_ZONE = (150, 80, 280, 170)

# Keyboard
keyboard = Controller()
jumps = 0


def detect_obstacle(frame):
    """Detect obstacle using Canny edge detection"""
    # Crop detection zone
    x1, y1, x2, y2 = OBSTACLE_ZONE
    roi = frame[y1:y2, x1:x2]

    # Convert to grayscale → detect edges → find contours
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 250)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check if any object found
    for c in contours:
        if cv2.contourArea(c) > 10:
            return True
    return False


def jump():
    """Press space to jump"""
    global jumps
    keyboard.press(Key.space)
    time.sleep(0.05)
    keyboard.release(Key.space)
    jumps += 1


# === MAIN LOOP ===

print("T-Rex Bot Starting...")
print("1. Open https://elgoog.im/t-rex/")
print("2. Press SPACE to start the game")
print("3. Press ESC to quit")
print("\nStarting in 3 seconds...")
time.sleep(3)

while True:
    # Capture screen
    screenshot = pyautogui.screenshot(region=GAME_AREA)
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Detect and react
    obstacle = detect_obstacle(frame)

    if obstacle:
        jump()
        time.sleep(0.2)

    # Draw visualization
    color = (0, 0, 255) if obstacle else (0, 255, 0)
    x1, y1, x2, y2 = OBSTACLE_ZONE
    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
    cv2.putText(frame, f'JUMPS: {jumps}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Show window
    cv2.imshow('T-Rex Bot', frame)

    # ESC to quit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
print(f"\nDone! Total jumps: {jumps}")