from flask import Flask, render_template, request, send_file
import numpy as np
import matplotlib.pyplot as plt
import os
import base64
from io import BytesIO

app = Flask(__name__)

def mandelbrot(x, y, zoom, width=800, height=600, max_iter=256):
    x_min = x - 2 / zoom
    x_max = x + 2 / zoom
    y_min = y - 1.5 / zoom
    y_max = y + 1.5 / zoom
    
    img = np.zeros((height, width), dtype=np.uint8)

    for j in range(height):
        for i in range(width):
            c = complex(x_min + i * (x_max - x_min) / width, y_min + j * (y_max - y_min) / height)
            z = 0
            n = 0
            while abs(z) <= 2 and n < max_iter:
                z = z*z + c
                n += 1
            img[j, i] = n

    return img

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        x = float(request.form['x'])
        y = float(request.form['y'])
        zoom = float(request.form['zoom'])
    except ValueError:
        # Girdi değerleri hatalıysa, varsayılan değerleri kullan
        x, y, zoom = 0, 0, 1
    
    img = mandelbrot(x, y, zoom)
    
    # Görüntüyü oluştur ve base64 formatına dönüştür
    buffer = BytesIO()
    plt.imshow(img, cmap='inferno')
    plt.axis('off')
    plt.savefig(buffer, format='png')
    plt.close()
    image_data = base64.b64encode(buffer.getvalue()).decode()

    # Görüntüyü dosya olarak kaydet
    image_path = os.path.join(app.root_path, 'static', 'mandelbrot.png')
    plt.imshow(img, cmap='inferno')
    plt.axis('off')
    plt.savefig(image_path)
    plt.close()

    return send_file(image_path)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
