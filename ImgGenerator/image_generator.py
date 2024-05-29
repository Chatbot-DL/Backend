from flask import Flask, request, jsonify, render_template, send_file
import requests
import io
from PIL import Image
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
HEADERS = {"Authorization": "Bearer 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"}

@app.route('/generate_image', methods=['POST'])
def generate_image():
    data = request.get_json()
    story = data.get('story', '')
    prompt = f"Generate a picture depicting the hero of my story. The hero is {story}."

    try:
        response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})
        image_bytes = response.content

        # Save the image to a file-like object
        image = Image.open(io.BytesIO(image_bytes))
        img_io = io.BytesIO()
        image.save(img_io, 'PNG')
        img_io.seek(0)

        return send_file(img_io, mimetype='image/png')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
