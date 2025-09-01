from flask import Flask, request, jsonify, render_template_string
import requests

app = Flask(__name__)

# Replace with your Groq API key
GROQ_API_KEY = "your_api_key_here"
MODEL_ID = "llama-3.1-8b-instant"

# HTML for chatbot UI
html = """
<!DOCTYPE html>
<html>
<head>
<title>Basic Chatbot</title>
<style>
  body {
    margin: 0;
    background-color: #001f3f; /* navy blue */
    color: white;
    font-family: Arial, sans-serif;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  #chat-container {
    width: 90%;
    max-width: 600px;
    height: 80vh;
    background-color: #001f3f;
    border-radius: 10px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    position: relative;
    z-index: 2;
  }
  #chat {
    flex-grow: 1;
    padding: 20px;
    overflow-y: auto;
    word-wrap: break-word;
  }
  #chat p {
    margin: 10px 0;
  }
  .user {
    text-align: right;
    color: white;
  }
  .bot {
    text-align: left;
    color: white;
    white-space: pre-wrap;
  }
  #input-container {
    display: flex;
    padding: 10px;
    background-color: #003366;
    border-top: 1px solid #005599;
  }
  #user_input {
    flex-grow: 1;
    padding: 10px;
    border: none;
    border-radius: 5px;
    font-size: 16px;
    background-color: #001f3f;
    color: white;
    outline: none;
  }
  #send-btn {
    background-color: #0074D9;
    color: white;
    border: none;
    border-radius: 5px;
    margin-left: 10px;
    padding: 10px 20px;
    cursor: pointer;
  }
  #send-btn:hover {
    background-color: #005fa3;
  }
  .stickers {
    position: fixed;
    top: 0; left: 0; width: 100vw; height: 100vh;
    pointer-events: none;
    z-index: 1;
  }
  .sticker {
    position: absolute;
    width: 50px;
    opacity: 0.8;
    animation: floaty 6s ease-in-out infinite alternate;
  }
  .top-left { top: 20px; left: 20px; animation-delay: 0s; }
  .top-right { top: 30px; right: 20px; animation-delay: 1.5s; }
  .bottom-left { bottom: 30px; left: 20px; animation-delay: 3s; }
  .bottom-right { bottom: 20px; right: 20px; animation-delay: 4.5s; }
  @keyframes floaty {
    0% { transform: translateY(0); }
    100% { transform: translateY(-15px); }
  }
</style>
</head>
<body>
  <div class="stickers">
    <img src="https://twemoji.maxcdn.com/v/latest/72x72/1f4a1.png" alt="Light Bulb" class="sticker top-left" />
    <img src="https://twemoji.maxcdn.com/v/latest/72x72/1f680.png" alt="Rocket" class="sticker top-right" />
    <img src="https://twemoji.maxcdn.com/v/latest/72x72/1f30d.png" alt="Globe" class="sticker bottom-left" />
    <img src="https://twemoji.maxcdn.com/v/latest/72x72/1f4bb.png" alt="Laptop" class="sticker bottom-right" />
  </div>

  <div id="chat-container">
    <div id="chat"></div>
    <div id="input-container">
      <input id="user_input" type="text" placeholder="Ask something..." />
      <button id="send-btn">Send</button>
    </div>
  </div>

<script>
  function sendMessage() {
    let input = document.getElementById('user_input');
    let text = input.value.trim();
    if(!text) return;
    let chat = document.getElementById('chat');

    chat.innerHTML += `<p class="user"><b>You:</b> ${text}</p>`;
    input.value = '';

    fetch('/chat', {
      method: 'POST',
      body: JSON.stringify({message: text}),
      headers: {'Content-Type': 'application/json'}
    })
    .then(response => response.json())
    .then(data => {
      chat.innerHTML += `<p class="bot"><b>Bot:</b> ${data.reply}</p>`;
      chat.scrollTop = chat.scrollHeight;
    });
  }

  document.getElementById('user_input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
      sendMessage();
      e.preventDefault();
    }
  });

  document.getElementById('send-btn').addEventListener('click', sendMessage);
</script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(html)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    # Send request to Groq API
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL_ID,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.7,
        "max_tokens": 150
    }
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
    else:
        reply = "Sorry, I couldn't process your request."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
