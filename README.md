# Instant Dashboard App

## Description
This project is a simple web application that generates an instant dashboard from raw JSON data using an AI model. The user provides structured data and a short natural language prompt, and the application renders a one-page dashboard preview.

---

## How to run the Application
1. Clone the Repository
 - git clone https://github.com/your-username/instant-dashboard.git
 - cd instant-dashboard

2. Create and activate a virtual environment
 - python -m venv venv
 - venc\Scripts\activate

3. Install Dependencies
 - pip install -r requirements.txt

4. Add API key
 Create a .env file in the project root and add :
 - GEMINI_API_KEY=your_api_key_here

5. Start the Server
 - python app.py

6. Open the app in a browser
 - http://127.0.0.1:5000

## AI API Used
This Application uses the Google Gemini API to generate frontend HTML Dashboards.
Model: Gemini-2.5-flash (generateContent endpoint)
 - The AI is instructed to behave as a frontend developer.
 - It outputs a complete HTML file styled with Tailwind CSS.
 - Strict rules are applied to ensure the AI uses only the data provided in the JSON.

## Notes
 - Invalid JSON input is handled gracefully.
 - The Dashboard preview is rendered inside an iframe.
 - Generated dashboards can be downloaded as an image.