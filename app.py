import re
from flask import Flask, render_template, request, jsonify
import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")



SYSTEM_PROMPT = """
You are a senior frontend developer.
Rule: Output ONLY a single, complete HTML file. 
Styling: Use Tailwind CSS via CDN (<script src="https://cdn.tailwindcss.com"></script>).
Charts: If the data looks like a list of numbers, use Chart.js via CDN.
Rules:
- No markdown (no ```html).
- Use a professional, modern layout with cards and a sidebar.
- Ensure the background is light gray and cards are white.
- Make it look like a high-end SaaS dashboard.
CRITICAL DATA RULES:
- Use ONLY the numbers present in the provided JSON.
- DO NOT invent, estimate, assume, or simulate any data.
- If a metric is not present in the JSON, DO NOT display it.
- Do not add KPIs like growth, trends, new hires, or percentages unless explicitly present.
- All charts and values MUST be directly derived from the JSON.
- Use the JSON values exactly as provided.
CHART LAYOUT RULES (IMPORTANT):
- Charts must fit within the visible viewport without excessive scrolling.
- Limit chart height to a maximum of 300-350px.
- Use responsive containers with fixed max-height.
- Prefer horizontal bar charts when there are more than 5 categories.
- Do NOT create charts that extend beyond one screen height.
- All charts must be visually compact and readable.
"""



MODEL = "gemini-2.5-flash"
GEMINI_URL = (
    f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={GEMINI_API_KEY}"
)


@app.route("/")
def index():
    return render_template("index.html")

import re

@app.route("/generate", methods=["POST"])
def generate():
    user_json = request.json.get("data")
    user_prompt = request.json.get("prompt")

    try:
        parsed_json = json.loads(user_json)
    except Exception:
        return jsonify({"error": "Invalid JSON format"}), 400

    final_prompt = f"{SYSTEM_PROMPT}\n\nDATA:\n{json.dumps(parsed_json)}\n\nUSER INSTRUCTION:\n{user_prompt}"
    

    payload = {
        "contents": [{"parts": [{"text": final_prompt}]}]
    }

    try:
        response = requests.post(GEMINI_URL, json=payload)
        
        # Handle the 429 Error specifically
        if response.status_code == 429:
            return jsonify({"error": "Rate limit reached. Please wait 60 seconds."}), 429
            
        response.raise_for_status()
        result = response.json()
        
        # Get the raw text
        raw_html = result["candidates"][0]["content"]["parts"][0]["text"]
        
        # CLEANER: Remove markdown code blocks if the AI included them
        clean_html = re.sub(r'^```html\s*|```$', '', raw_html, flags=re.MULTILINE).strip()

        return jsonify({"html": clean_html})

    except Exception as e:
        return jsonify({"error": f"API Error: {str(e)}"}), 500

        
if __name__ == "__main__":
    app.run(debug=True)
