from flask import Flask, render_template, request
from PIL import Image
from collections import Counter
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

os.makedirs('uploads', exist_ok=True)


def get_colors(image_path, num_colors=10):
    # Open image and resize for speed
    img = Image.open(image_path)
    img = img.convert('RGB')
    img = img.resize((150, 150))

    # Get all pixels
    pixels = list(img.getdata())

    color_counts = Counter(pixels)

    top_colors = color_counts.most_common(num_colors)

    # Convert to HEX
    colors = []
    for color, count in top_colors:
        hex_color = '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])
        percent = round(count / len(pixels) * 100, 1)
        colors.append({
            'hex': hex_color,
            'rgb': f'rgb{color}',
            'percent': percent
        })

    return colors


@app.route('/', methods=['GET', 'POST'])
def home():
    colors = None
    image_url = None

    if request.method == 'POST':
        file = request.files.get('image')
        if file and file.filename:
            # Save file
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            colors = get_colors(filepath)
            image_url = filepath

    return render_template('index.html', colors=colors, image_url=image_url)


if __name__ == '__main__':
    app.run(debug=True)
