Instant Dashboard Generator

Instant Dashboard Generator is a web application that converts structured JSON data into a clean, professional dashboard using AI. The goal of this project is to reduce the effort required to manually design dashboards by allowing users to paste data and instantly visualize it in a readable format.

The application focuses strongly on data accuracy. The AI is instructed to use only the values present in the input JSON and not to invent, estimate, or simulate any additional metrics.

Project Overview

Users provide:

A JSON dataset

A short instruction describing the desired dashboard

The system then generates:

A complete HTML dashboard

Charts when numerical data is present

A structured layout using cards and sections

The generated dashboard is displayed inside the application and can be downloaded as an image.

Key Features

Generates dashboards directly from raw JSON

Uses only the values present in the input data

Prevents AI hallucination of metrics or numbers

Automatically selects appropriate chart types

Limits chart height to avoid excessive scrolling

Clean and professional UI using Tailwind CSS

Loading indicator during generation

Error handling for invalid input and API limits

Download dashboard as a PNG image

Technologies Used

Backend:

Python

Flask

Requests

python-dotenv

Frontend:

HTML

Tailwind CSS (via CDN)

JavaScript

Visualization:

Chart.js

AI:

Google Gemini API (generateContent)

Screenshot:

html2canvas



Setup Instructions

Clone the repository

git clone https://github.com/your-username/instant-dashboard-generator.git

cd instant-dashboard-generator

Install dependencies

pip install -r requirements.txt

Create environment file

Create a file named .env in the root directory and add:

GEMINI_API_KEY=your_api_key_here

Run the application

python app.py

Open in browser

http://127.0.0.1:5000

How It Works

The user enters JSON data and a prompt

The backend validates the JSON

The system prompt strictly instructs the AI to:

Use only provided data

Avoid adding new metrics

Keep charts compact and readable

Gemini generates a complete HTML dashboard

The dashboard is rendered inside an iframe

The user can download the dashboard as an image

Data Accuracy Policy

This project enforces strict data integrity rules:

No numbers are added or modified

No assumptions or trends are shown unless present in JSON

Charts are built only from provided values

Missing metrics are not displayed

This design choice ensures reliability during evaluation and real-world usage.

Error Handling

Invalid JSON is detected before processing

API rate limits return a clear message

Download is disabled until a dashboard is generated

Loading state prevents duplicate requests

Known Limitations

Requires an active internet connection

Dependent on Gemini API quota and availability

Output quality depends on clarity of user prompt

Future Improvements

Dark mode toggle

Dashboard templates

Editable charts after generation

Export as PDF

Save previously generated dashboards

Live deployment

Author

Akash C
AI and Machine Learning Research Fellow