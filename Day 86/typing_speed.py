import tkinter as tk
from tkinter import messagebox
import time
import random
import requests

# Colors
BG = "#1e1e2e"
FG = "#cdd6f4"
CARD = "#313244"
INPUT = "#45475a"
GREEN = "#a6e3a1"
BLUE = "#89b4fa"
RED = "#f38ba8"
YELLOW = "#f9e2af"
PURPLE = "#cba6f7"

BACKUP_TEXTS = [
    "The quick brown fox jumps over the lazy dog near the river",
    "Programming is the art of telling a computer what to do",
    "Practice makes perfect when learning to type faster every day"
]


def get_speed_level(cpm):
    """Get typing speed level by CPM"""
    if cpm < 100:
        return "Beginner", "Keep practicing!"
    elif cpm < 200:
        return "Slow", "You're getting there!"
    elif cpm < 300:
        return "Average", "Good job!"
    elif cpm < 400:
        return "Above Average", "Nice speed!"
    elif cpm < 500:
        return "Fast", "Impressive!"
    else:
        return "Professional", "Amazing!"


class TypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("700x500")
        self.root.configure(bg=BG)

        self.start_time = None
        self.running = False
        self.current_text = ""

        self.create_widgets()
        self.api_text()

    def create_widgets(self):
        # Title
        tk.Label(self.root, text="Typing Speed Test", font=("Helvetica", 24, "bold"),
                 bg=BG, fg=FG).pack(pady=20)

        # Status
        self.status = tk.Label(self.root, text="", font=("Helvetica", 10), bg=BG, fg=FG)
        self.status.pack()

        # Text to type
        self.text_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg=CARD,
                                   fg=FG, wraplength=600, padx=20, pady=20)
        self.text_label.pack(pady=15, padx=20, fill="x")

        # Input field
        self.entry = tk.Entry(self.root, font=("Helvetica", 14), bg=INPUT, fg="white",
                              insertbackground="white", relief="flat", justify="center")
        self.entry.pack(pady=10, padx=40, fill="x", ipady=10)
        self.entry.bind("<KeyRelease>", self.check_typing)

        # Results
        result_frame = tk.Frame(self.root, bg=BG)
        result_frame.pack(pady=20)

        # CPM, Accuracy, Time
        self.cpm_label = tk.Label(result_frame, text="0", font=("Helvetica", 40, "bold"), bg=BG, fg=GREEN)
        self.acc_label = tk.Label(result_frame, text="100%", font=("Helvetica", 40, "bold"), bg=BG, fg=BLUE)
        self.time_label = tk.Label(result_frame, text="0s", font=("Helvetica", 40, "bold"), bg=BG, fg=RED)

        for i, (label, text) in enumerate(
                [(self.cpm_label, "CPM"), (self.acc_label, "Accuracy"), (self.time_label, "Time")]):
            label.grid(row=0, column=i, padx=35)
            tk.Label(result_frame, text=text, bg=BG, fg=FG).grid(row=1, column=i)

        # Buttons
        btn_frame = tk.Frame(self.root, bg=BG)
        btn_frame.pack(pady=20)

        buttons = [
            ("New Text", YELLOW, self.new_text),
            ("Random Quote", PURPLE, self.api_text),
            ("Random Fact", BLUE, self.fact_text)
        ]

        for text, color, cmd in buttons:
            tk.Button(btn_frame, text=text, font=("Helvetica", 12, "bold"), bg=color,
                      fg=BG, relief="flat", command=cmd, padx=15, pady=5).pack(side="left", padx=10)

    def api_text(self):
        self.status.config(text="Loading...")
        self.root.update()

        try:
            response = requests.get("https://zenquotes.io/api/random", timeout=5)
            self.current_text = response.json()[0]["q"]
            self.status.config(text="Quote loaded!")
        except:
            self.current_text = random.choice(BACKUP_TEXTS)
            self.status.config(text="Using backup text")

        self.reset()

    def fact_text(self):
        self.status.config(text="Loading...")
        self.root.update()

        try:
            response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random", timeout=5)
            self.current_text = response.json()["text"]
            self.status.config(text="Fact loaded!")
        except:
            self.current_text = random.choice(BACKUP_TEXTS)
            self.status.config(text="Using backup text")

        self.reset()

    def new_text(self):
        self.current_text = random.choice(BACKUP_TEXTS)
        self.status.config(text="")
        self.reset()

    def reset(self):
        self.text_label.config(text=self.current_text)
        self.entry.delete(0, tk.END)
        self.entry.config(state="normal", bg=INPUT)
        self.start_time = None
        self.running = False
        self.cpm_label.config(text="0")
        self.acc_label.config(text="100%")
        self.time_label.config(text="0s")
        self.entry.focus()

    def check_typing(self, event):
        typed = self.entry.get()

        # Start timer
        if not self.running and typed:
            self.start_time = time.time()
            self.running = True
            self.update_timer()

        # Highlight
        self.entry.config(bg=INPUT if self.current_text.startswith(typed) else RED)

        # Accuracy
        if typed:
            correct = sum(1 for a, b in zip(typed, self.current_text) if a == b)
            self.acc_label.config(text=f"{int(correct / len(typed) * 100)}%")

        # Complete
        if typed == self.current_text:
            self.finish()

    def update_timer(self):
        if self.running:
            elapsed = time.time() - self.start_time
            self.time_label.config(text=f"{int(elapsed)}s")

            # CPM = characters per minute
            if elapsed > 0:
                cpm = int(len(self.entry.get()) / (elapsed / 60))
                self.cpm_label.config(text=str(cpm))

            self.root.after(100, self.update_timer)

    def finish(self):
        self.running = False
        self.entry.config(state="disabled", bg=GREEN)

        # Calculate results
        elapsed = time.time() - self.start_time
        typed = self.entry.get()
        correct = sum(1 for a, b in zip(typed, self.current_text) if a == b)
        accuracy = int(correct / len(typed) * 100)
        cpm = int(len(typed) / (elapsed / 60))
        wpm = int(cpm / 5)  # WPM = CPM / 5

        # Get speed level
        level, message = get_speed_level(cpm)

        # Show results
        messagebox.showinfo(
            "Complete!",
            f"CPM: {cpm} (characters per minute)\n"
            f"WPM: {wpm} (words per minute)\n"
            f"Accuracy: {accuracy}%\n"
            f"Time: {int(elapsed)}s\n\n"
            f"Level: {level}\n"
            f"{message}"
        )

        self.status.config(text=f"Level: {level} | Click any button for new text")


# Run
root = tk.Tk()
app = TypingTest(root)
root.mainloop()