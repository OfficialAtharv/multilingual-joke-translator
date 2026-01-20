# 🎭 Gemini Joke Translator (CLI)

A **command-line AI application** that translates **English jokes** into  
🇫🇷 French, 🇪🇸 Spanish, and 🇸🇦 Arabic using the **Google Gemini free API**.

This project demonstrates **direct LLM integration** without web frameworks or agent abstractions.

---

## 🚀 Features

- 🖥️ Command Line Interface (CLI)
- 🤖 Powered by Google Gemini (free tier)
- 🌍 Translates jokes into:
  - French
  - Spanish
  - Arabic
- 🎯 Preserves humor and meaning
- 🔐 No API keys hardcoded
- 🧠 Simple, stable, and beginner-friendly

---

## 🧠 Why This Project?

Many AI demos rely on heavy frameworks or unstable agent SDKs.  
This project focuses on:

- **Direct Gemini API usage**
- **Minimal dependencies**
- **Clarity and reliability**
- **Easy understanding for beginners**

It is ideal for learning how to work with LLM APIs in real projects.

---
## 🏗️ How It Works
User (CLI Input)
↓
Python Script
↓
Gemini LLM (gemini-2.5-flash)
↓
Translated Joke Output

gemini-joke-translator-cli/
│
├── joke_translator.py
├── requirements.txt
└── README.md


---

## 🔧 Requirements

### System
- Python 3.9+
- Internet connection

### Python Libraries
- google-generativeai

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/gemini-joke-translator-cli.git
cd gemini-joke-translator-cli
```

2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Set Gemini API key

Create a free API key from:
👉 https://aistudio.google.com/apikey
export GOOGLE_API_KEY="YOUR_API_KEY"

▶️ Run the Application
python joke_translator.py

🧪 Example Usage
Input
Why did the computer go to the doctor?
Because it caught a virus.
Output
French:
Pourquoi l’ordinateur est-il allé chez le médecin ?
Parce qu’il a attrapé un virus.

Spanish:
¿Por qué la computadora fue al médico?
Porque contrajo un virus.

Arabic:
لماذا ذهب الكمبيوتر إلى الطبيب؟
لأنه أصيب بفيروس.

🔮 Future Enhancements
🌍 Add more languages
🗂 Save translations to file
🎛 Language selection
🖥️ Optional web version

👨‍💻 Author
Atharv Kulkarni
MCA Student | AI & Backend Development Enthusiast


