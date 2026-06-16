# Social Media Sentiment Analysis

A simple web application that performs sentiment analysis on user-provided text using a Hugging Face Transformer model.

## Features

- Sentiment Analysis using Hugging Face Transformers
- Flask-based backend
- HTML frontend interface
- Displays sentiment label and confidence score
- Easy to use and beginner-friendly

## Tech Stack

- Python
- Flask
- Hugging Face Transformers
- HTML
- PyTorch

## Project Structure

```text
social_media_analysis/
│
├── app.py
├── requirements.txt
├── README.md
│
└── templates/
    └── index.html
```

## Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project directory

```bash
cd social_media_analysis
```

3. Create a virtual environment

```bash
python -m venv venv
```

4. Activate the virtual environment

```bash
venv\Scripts\activate
```

5. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## How It Works

1. User enters text in the web interface.
2. The text is sent to the Flask backend.
3. A Hugging Face sentiment analysis model processes the text.
4. The predicted sentiment and confidence score are displayed.

## Example Output

Input:

```text
This company provides excellent service.
```

Output:

```text
Sentiment: POSITIVE
Confidence: 99.8%
```

## Learning Outcomes

This project helped me learn:

- Flask web development
- Hugging Face Transformers
- Sentiment Analysis
- Frontend and Backend integration
- Deploying and managing Python projects using Git and GitHub

## Author

Arjun K
