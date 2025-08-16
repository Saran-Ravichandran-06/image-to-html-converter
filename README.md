# Image → HTML/CSS Converter

This project converts a UI screenshot image into **HTML and CSS code** using a web interface.  
You can upload an image and instantly get the HTML and CSS layout generated.

## Features

- Upload an image of a web page or UI design.
- Preview the image before conversion.
- Generates HTML code (without inline styles).
- Generates separate CSS (`style.css`) with proper styling.
- Dark-themed, responsive interface for better readability.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask) + Google Gemini API
- **Libraries**: `requests`, `python-dotenv`

## How to Run Locally

1. Clone the repository:

    git clone https://github.com/Saran-Ravichandran-06 /image-to-html-converter.git
    cd image-to-html-converter

2. Install dependencies:

    pip install -r requirements.txt

3. Create a .env file with your Gemini API key:

    GEMINI_API_KEY=your_api_key_here

4. Run the Flask app

    python app.py

5. Open http://127.0.0.1:5000 in your browser.

## Usage

    - Upload an image in the Input Image box.
    - Click Convert.
    - View the generated HTML and CSS in the right panel.
    - Copy the code or save it as needed