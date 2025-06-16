# FAQ Chatbot

This is a simple FAQ chatbot web application built using Python, Flask, and NLP techniques. The chatbot uses a CSV file of frequently asked questions and answers to respond to user queries based on text similarity.

## 🧠 Features

- Handles user questions through a web interface.
- Matches input with closest FAQ using TF-IDF and cosine similarity.
- Includes a `faqs.csv` file with 20 sample Q&A pairs.
- Lightweight and easy to run locally.

## 📁 Project Structure

├── app.py # Flask application for the web interface
├── chatbot.py # Chatbot logic and NLP processing
├── faqs.csv # CSV file containing FAQ questions and answers
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # HTML template for the chatbot UI (not included here)


## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/faq-chatbot.git
cd faq-chatbot

2. Install dependencies
Make sure you have Python 3.7+ installed. Then install the required libraries:

bash
Copy
Edit
pip install -r requirements.txt
3. Run the app
bash
Copy
Edit
python app.py
Visit http://127.0.0.1:5000/ in your browser to interact with the chatbot.

📋 How it Works
FAQs are loaded from faqs.csv.

User input is preprocessed (lowercased, tokenized, cleaned).

Input is vectorized and compared with FAQ questions using cosine similarity.

The most relevant answer is returned if the similarity is above a threshold.

📝 Customize
To add your own FAQs, edit the faqs.csv file:

csv
Copy
Edit
Question,Answer
"Your question here","The corresponding answer here"
🛠 Dependencies
Flask

NLTK

NumPy

pandas

scikit-learn

📌 Notes
NLTK data is downloaded at runtime (punkt and stopwords).

If you're deploying to a production server, disable debug=True in app.py.
