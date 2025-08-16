from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from gemini_service import generate_html_css

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow requests from frontend

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/convert", methods=["POST"])
def convert_image():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image_file = request.files["image"]
    if image_file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    # Save image temporarily
    image_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
    image_file.save(image_path)

    try:
        html_code, css_code = generate_html_css(image_path)
        return jsonify({"html": html_code, "css": css_code})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        # Optional: delete after processing
        if os.path.exists(image_path):
            os.remove(image_path)

if __name__ == "__main__":
    app.run(debug=True)
