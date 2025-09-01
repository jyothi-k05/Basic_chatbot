# Create project folder
mkdir flask-groq-chatbot
cd flask-groq-chatbot

# Create requirements.txt
cat > chatbot_requirement.txt <<EOL
Flask
requests
EOL

# Create README.md
cat > README.md <<EOL
# 🗨️ Flask + Groq Chatbot

A simple chatbot web app built with **Flask** and styled with **HTML/CSS/JavaScript**.  
It connects to the **Groq API (LLaMA-3.1)** for AI-powered responses.  

---

## ✨ Features
- 💬 Real-time chatbot powered by Groq API  
- 🎨 Modern navy blue UI with floating emoji stickers  
- ⚡ Lightweight Flask backend  
- 📱 Responsive design  

---

## 🚀 Getting Started

### 1️⃣ Clone the repository
\`\`\`bash
git clone https://github.com/your-username/flask-groq-chatbot.git
cd flask-groq-chatbot
\`\`\`

### 2️⃣ Create and activate a virtual environment
\`\`\`bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
\`\`\`

### 3️⃣ Install dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

---

## ⚙️ Configuration

1. Get a **Groq API Key** from [Groq Cloud](https://console.groq.com/).  
2. Open \`chatbot.py\` and replace:
   \`\`\`python
   GROQ_API_KEY = "your_api_key_here"
   \`\`\`
3. Save the file.

---

## ▶️ Run the App

\`\`\`bash
python chatbot.py
\`\`\`

Now visit 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser. #it is not exact link but it looks similar 

---

## 📂 Project Structure
\`\`\`
.
├── chatbot.py             # Flask backend
├── chatbot_requirement.txt   # Python dependencies
├── README.md          # Project documentation
\`\`\`

---


## 📜 License
This project is created for **educational/demo purposes**.  
Feel free to fork and modify.  
EOL

echo "✅ Project files created: chatbot_requirement.txt + README.md"
