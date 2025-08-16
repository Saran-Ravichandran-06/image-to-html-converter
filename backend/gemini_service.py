import os
import base64
import json
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Endpoint for Gemini
MODEL_NAME = "gemini-2.0-flash"  # <-- using your curl model
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent"

def generate_html_css(image_path: str):
    """
    Sends an image to Google Gemini API and requests HTML + CSS code.
    Returns a tuple: (html_code, css_code)
    """
    try:
        # Read image as base64
        with open(image_path, "rb") as f:
            image_data = base64.b64encode(f.read()).decode("utf-8")

        prompt = """
        You are a web developer AI. Convert the given UI screenshot into HTML and CSS seperately.
        Predict the font color, font size, tag's background color, tag's position and layout based on the image.
        Return only the code without extra explanations.

        Format your response as:

        [HTML]
        <html> ... </html>

        [CSS]
        body { ... }
        """

        headers = {
            "Content-Type": "application/json",
            "X-goog-api-key": GEMINI_API_KEY,
        }

        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt},
                        {
                            "inline_data": {
                                "mime_type": "image/png",
                                "data": image_data,
                            }
                        },
                    ]
                }
            ]
        }

        # Send POST request
        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code != 200:
            raise Exception(f"API Error {response.status_code}: {response.text}")

        result = response.json()

        # Extract text safely
        output_text = ""
        if "candidates" in result and len(result["candidates"]) > 0:
            parts = result["candidates"][0]["content"]["parts"]
            output_text = " ".join(p.get("text", "") for p in parts).strip()

        # Parse HTML and CSS
        html_code, css_code = "", ""
        if "[HTML]" in output_text and "[CSS]" in output_text:
            html_part = output_text.split("[HTML]")[1].split("[CSS]")[0].strip()
            css_part = output_text.split("[CSS]")[1].strip()
            html_code, css_code = html_part, css_part
        else:
            # If no clear separation, return entire text as HTML
            html_code = output_text
            css_code = ""

        return html_code, css_code

    except Exception as e:
        return f"<!-- Error: {str(e)} -->", "/* Error generating CSS */"