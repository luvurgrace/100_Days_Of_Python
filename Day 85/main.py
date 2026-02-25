import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

image = None
photo = None


def load():
    global image
    file = filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg *.jpeg")])
    if file:
        image = Image.open(file).convert("RGBA")
        show(image)


def watermark():
    global image
    if not image:
        messagebox.showwarning("Error", "Load the image!")
        return

    layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)

    text = entry.get()

    # 📐 Font size = 5% from picture size
    font_size = int(image.width * 0.05)

    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), text, font=font)
    x = image.width - (bbox[2] - bbox[0]) - 40
    y = image.height - (bbox[3] - bbox[1]) - 40

    draw.text((x, y), text, font=font, fill=(255, 255, 255, 150))
    image = Image.alpha_composite(image, layer)
    show(image)


def save():
    if not image:
        return
    file = filedialog.asksaveasfilename(defaultextension=".png")
    if file:
        image.save(file)
        messagebox.showinfo("✓", "Saved!")


def show(img):
    global photo
    img_copy = img.copy()
    img_copy.thumbnail((450, 350))
    photo = ImageTk.PhotoImage(img_copy)
    canvas.delete("all")
    canvas.create_image(225, 175, image=photo)


# === WINDOW ===
root = tk.Tk()
root.title("✨ Watermark")
root.geometry("500x550")
root.configure(bg="#1e1e2e")
root.resizable(False, False)

# === TITLE ===
tk.Label(root, text="🎨 Watermark Application", font=("Helvetica", 20, "bold italic"),
         bg="#1e1e2e", fg="#cdd6f4").pack(pady=15)

# === CANVAS FOR PICTURES ===
canvas = tk.Canvas(root, width=450, height=350, bg="#313244", highlightthickness=0)
canvas.pack(pady=10)
canvas.create_text(225, 175, text="Load the image", fill="#6c7086", font=("Helvetica", 12))

# === INPUT FIELD ===
frame = tk.Frame(root, bg="#1e1e2e")
frame.pack(pady=15)

tk.Label(frame, text="Текст:", bg="#1e1e2e", fg="#a6adc8", font=("Helvetica", 11)).pack(side="left")
entry = tk.Entry(frame, width=25, font=("Helvetica", 12), bg="#45475a", fg="white",
                 insertbackground="white", relief="flat")
entry.insert(0, "© github.com/luvurgrace")
entry.pack(side="left", padx=10, ipady=5)

# === BUTTONS ===
btn_frame = tk.Frame(root, bg="#1e1e2e")
btn_frame.pack(pady=10)

style = {"font": ("Helvetica", 11, "bold"), "relief": "flat", "width": 12, "cursor": "hand2"}

tk.Button(btn_frame, text="📂 Open", bg="#89b4fa", fg="#1e1e2e", command=load, **style).pack(side="left", padx=5)
tk.Button(btn_frame, text="✨ Print", bg="#f38ba8", fg="#1e1e2e", command=watermark, **style).pack(side="left",
                                                                                                     padx=5)
tk.Button(btn_frame, text="💾 Save", bg="#a6e3a1", fg="#1e1e2e", command=save, **style).pack(side="left", padx=5)

root.mainloop()
