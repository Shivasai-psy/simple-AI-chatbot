# simple-AI-chatbot
 ---

## ✨ Features

- 🤖 AI-powered chatbot using Google Gemini API
- 💬 Real-time conversational responses
- 🌐 Responsive and modern user interface
- 🔒 Secure API key management

---

## 🛠 Technologies Used
- Python 3
- Flask
- Google Generative AI (Gemini API)
- HTML5
- CSS3
- JavaScript
- Visual Studio Code
---

## 📁 Project Structure

```
simple-AI-chatbot/
│
├── app.py               
├── main.py              
├── config.py               
├── requirements.txt        
├── README.md
|-templates/
│   └── index.html          
│
├── static/
│   ├── style.css           
│   └── script.js           
│
└── screenshots 
```

---

## 🚀 Installation

### 1️⃣ Clone the Repository

``` 
git clone https://github.com/yourusername/simple-AI-Chatbot.git
```

Move into the project directory.

``` 
cd simple-AI-chatbot
```

---

### 2️⃣ Create a Virtual Environment

#### Windows

```
python -m venv venv
```

Activate the virtual environment

```
venv\Scripts\activate
```

---

Activate

```
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a file named

```
config.py
```

Add your Gemini API key.

```python
API_KEY = "YOUR_GEMINI_API_KEY"
```

## ▶ Running the Project

```
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000/
```

## 📦 Required Dependencies

```
Flask
google-generativeai
python-dotenv
```
---

## 💻 Sample Output

```
----------------------------------------
🤖 simple-AI-chatbot
----------------------------------------

You:
Hello

Bot:
Hello! How can I assist you today?

----------------------------------------

You:
What is Artificial Intelligence?

Bot:
Artificial Intelligence (AI) is a branch of computer science that enables machines to simulate human intelligence, including learning, reasoning, problem-solving, and decision-making.

----------------------------------------

You:
Explain Machine Learning.

Bot:
Machine Learning is a subset of AI that allows computers to learn patterns from data and improve their performance without being explicitly programmed.

----------------------------------------
```

---

## 📸 Sample Interface

```
+------------------------------------------------------+
|                 🤖 AI Chatbot                         |
|------------------------------------------------------|
| You : Hello                                          |
|                                                      |
| Bot : Hello! How can I help you today?              |
|                                                      |
| You : Explain AI                                     |
|                                                      |
| Bot : Artificial Intelligence is...                 |
|                                                      |
|------------------------------------------------------|
| Type your message...                    [ Send ]     |
+------------------------------------------------------+
```

*(Replace this section with an actual screenshot if available.)*

---

---

## 📈 Future Enhancements

- User authentication
- Chat history
- Streaming responses
- Dark mode
- Voice input
- Voice output
---
---
