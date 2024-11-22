from flask import Flask, render_template_string, request, jsonify, redirect, url_for
from System.genai_core import SXSCLI_GENAI
from System.openai_core import SXSCLI_OPENAI
from System.sxscli_core import System
import sqlite3
import os
import openai
import logging
import webbrowser

class AI_WITH_WEB_INTERFACE:
    def __init__(self):
        self.log_dir="Staff/ai/chat_history/labs_logs.log"
        logging.basicConfig(filename=self.log_dir, level=logging.INFO)
        self.global_core=System.sxscli()
        self.gpt_core=SXSCLI_OPENAI()
        self.app = Flask(__name__)
        self.model = "gemini-1.5-pro"
        self.openai_models=["gpt-3.5-turbo", "gpt-4", "gpt-4o","gpt-4o-mini","gpt-4-turbo","o1-preview","o1-mini"]
        self.sxscli = SXSCLI_GENAI()
        self.database_path = self.global_core.get_database_path()
        self.config_db_path = self.database_path+'config.db'
        self.chat_history_db_path = self.database_path+'chat_history.db'
        self.init_database()
        logging.info("AI_WITH_WEB_INTERFACE: Initialized")
        
    def init_database(self):
        if not os.path.exists(self.config_db_path):
            with sqlite3.connect(self.config_db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''CREATE TABLE IF NOT EXISTS config (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    model TEXT,
                                    api_key TEXT,
                                    temperature REAL,
                                    max_tokens INTEGER
                                )''')
                cursor.execute('''INSERT INTO config (model, api_key, temperature, max_tokens)
                                  VALUES (?, ?, ?, ?)''', 
                               (self.model, "0", 0.5, 10000))
                conn.commit()

        if not os.path.exists(self.chat_history_db_path):
            with sqlite3.connect(self.chat_history_db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''CREATE TABLE IF NOT EXISTS chat_history (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    user_message TEXT,
                                    ai_response TEXT,
                                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                                )''')
                conn.commit()

    def get_config(self):
        with sqlite3.connect(self.config_db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT model, api_key, temperature, max_tokens FROM config ORDER BY id DESC LIMIT 1")
            config = cursor.fetchone()
            logging.info(f"AI_WITH_WEB_INTERFACE: Config: {config}")
            if config:
                return {
                    "model": config[0],
                    "api_key": config[1],
                    "temperature": config[2],
                    "max_tokens": config[3]
                }
            return None

    def save_chat_history(self, user_message, ai_response):
        with sqlite3.connect(self.chat_history_db_path) as conn:
            logging.info(f"AI_WITH_WEB_INTERFACE: Chat history: {user_message} | {ai_response}")
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO chat_history (user_message, ai_response)
                              VALUES (?, ?)''', (user_message, ai_response))
            conn.commit()

    def start(self):
        webbrowser.open("http://127.0.0.1:5000/")
        try:
            self.app.add_url_rule('/', 'index', self.index)
            self.app.add_url_rule('/send_message', 'send_message', self.send_message, methods=['POST'])
            self.app.add_url_rule('/settings', 'settings', self.settings)
            self.app.add_url_rule('/save_settings', 'save_settings', self.save_settings, methods=['POST'])

            self.app.run(debug=False, host='0.0.0.0', port=5000)
            logging.info("AI_WITH_WEB_INTERFACE: Interface started")

            return "Interface started: 0"
        except Exception as e:
            logging.error(f"AI_WITH_WEB_INTERFACE: Error starting interface: {e}")
            return f"Error starting interface: {e}"

    def settings(self):
        config = self.get_config()
        return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>SXSCLI - Settings</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #121212;
                    color: #e0e0e0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .settings-container {
                    background-color: #1f1f1f;
                    padding: 25px;
                    border-radius: 10px;
                    width: 400px;
                    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
                    transition: transform 0.2s;
                }
                .settings-container:hover {
                    transform: scale(1.02);
                }
                .settings-container h2 {
                    margin-top: 0;
                    color: #ffd54f;
                }
                .settings-container label {
                    font-weight: bold;
                    margin-bottom: 5px;
                    display: block;
                }
                .settings-container input, select {
                    width: calc(100% - 20px);
                    padding: 10px;
                    margin-bottom: 15px;
                    background-color: #333;
                    color: #fff;
                    border: 1px solid #555;
                    border-radius: 5px;
                    transition: background-color 0.3s;
                }
                .settings-container input:focus, select:focus {
                    background-color: #444;
                }
                .settings-container button {
                    width: 100%;
                    padding: 12px;
                    background-color: #ffd54f;
                    color: #121212;
                    border: none;
                    border-radius: 8px;
                    cursor: pointer;
                    font-weight: bold;
                    font-size: 16px;
                    transition: background-color 0.3s;
                }
                .settings-container button:hover {
                    background-color: #ffc107;
                }
            </style>
        </head>
        <body>
            <div class="settings-container">
                <h2>Settings</h2>
                <form id="settingsForm" action="/save_settings" method="POST" onsubmit="handleSubmit(event)">

                    <label for="api_key">Gemini API Key:</label>
                    <input type="text" name="api_key" id="api_key" value="{{ config['api_key'] }}" required>

                    <label for="temperature">Temperature:</label>
                    <input type="number" name="temperature" id="temperature" step="0.1" min="0" max="1" value="{{ config['temperature'] }}">

                    <label for="max_tokens">Max Tokens:</label>
                    <input type="number" name="max_tokens" id="max_tokens" value="{{ config['max_tokens'] }}">

                    <button type="submit">Save Settings</button>
                </form>
            </div>

            <script>
                function handleSubmit(event) {
                    event.preventDefault();
                    const form = document.getElementById('settingsForm');

                    fetch(form.action, {
                        method: form.method,
                        body: new FormData(form)
                    })
                    .then(response => {
                        if (response.ok) {
                            setTimeout(() => {
                                window.location.href = "/";
                            }, 1000);
                        } else {
                            alert('Failed to save settings. Please try again.');
                        }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        alert('Error saving settings. Please try again.');
                    });
                }
            </script>
        </body>
        </html>
        ''', config=config)
    
    def save_settings(self):
        api_key = request.form['api_key']
        temperature = float(request.form['temperature'])
        max_tokens = int(request.form['max_tokens'])

        with sqlite3.connect(self.config_db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO config (api_key, temperature, max_tokens)
                              VALUES (?, ?, ?)''', 
                           (api_key, temperature, max_tokens))
            conn.commit()
        logging.info(f"AI_WITH_WEB_INTERFACE: Settings saved: {api_key} | {temperature} | {max_tokens}")
        return redirect(url_for('settings'))
    
    def index(self):
        return render_template_string("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>SXSCLI - Running neural networks with a web interface</title>
            <style>
                body {
                    font-family: 'Arial', sans-serif;
                    background-color: #181818;
                    color: #fff;
                    margin: 0;
                    padding: 0;
                    overflow-x: hidden;
                }
                .container {
                    display: flex;
                    height: 100vh;
                }
                .sidebar {
                    width: 25%;
                    background-color: #2d2d2d;
                    padding: 20px;
                    display: flex;
                    flex-direction: column;
                    border-right: 1px solid #444;
                    transition: width 0.3s;
                }
                .sidebar:hover {
                    width: 20%;
                }
                .chat-list {
                    flex-grow: 1;
                    margin-bottom: 20px;
                    list-style: none;
                    padding: 0;
                    max-height: 75%;
                    overflow-y: auto;
                }
                .chat-item {
                    background-color: #333;
                    padding: 15px;
                    margin: 5px 0;
                    border-radius: 5px;
                    cursor: pointer;
                    transition: background-color 0.3s, transform 0.3s;
                }
                .chat-item:hover {
                    background-color: #444;
                    transform: scale(1.05);
                }
                .sidebar button {
                    background-color: #444;
                    padding: 12px;
                    border: none;
                    color: white;
                    border-radius: 5px;
                    cursor: pointer;
                    text-align: center;
                    transition: background-color 0.3s, transform 0.3s;
                    margin-bottom: 15px;
                }
                .sidebar button:hover {
                    background-color: #555;
                    transform: scale(1.05);
                }
                .sidebar i {
                    margin-right: 8px;
                }
                .chat-container {
                    width: 75%;
                    padding: 25px;
                    background-color: #222;
                    border-radius: 10px;
                    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.7);
                    display: flex;
                    flex-direction: column;
                    justify-content: space-between;
                    transition: all 0.3s;
                }
                .messages {
                    background-color: #2d2d2d;
                    padding: 15px;
                    border-radius: 8px;
                    flex-grow: 1;
                    margin-bottom: 20px;
                    max-height: 80%;
                    overflow-y: auto;
                }
                .message {
                    background-color: #333;
                    margin: 10px 0;
                    padding: 12px;
                    border-radius: 5px;
                    animation: fadeIn 0.6s ease-in-out;
                    transition: background-color 0.3s;
                }
                .message.user {
                    background-color: #444;
                    margin-left: auto;
                    max-width: 60%;
                }
                .message.ai {
                    background-color: #333;
                    margin-right: auto;
                    max-width: 60%;
                }
                .input-container {
                    display: flex;
                    justify-content: space-between;
                    margin-bottom: 15px;
                }
                .input-container input {
                    width: 80%;
                    padding: 12px;
                    background-color: #333;
                    border: 1px solid #444;
                    color: white;
                    border-radius: 5px;
                    font-size: 16px;
                }
                .input-container button {
                    width: 15%;
                    padding: 12px;
                    background-color: #444;
                    border: none;
                    color: white;
                    border-radius: 5px;
                    cursor: pointer;
                    transition: background-color 0.3s;
                    font-size: 16px;
                }
                .input-container button:hover {
                    background-color: #555;
                }
                .model-selector {
                    margin-bottom: 15px;
                }
                .model-selector select {
                    padding: 12px;
                    background-color: #333;
                    color: white;
                    border: 1px solid #444;
                    border-radius: 5px;
                    width: 100%;
                }
                .wlc {
                    text-align: center;
                    font-size: 12px;
                    color: #888;
                    margin-top: 8px;
                }
                .powered-by {
                    text-align: center;
                    font-size: 8px;
                    color: #888;
                    margin-top: 8px;
                }
                .modal {
                    display: none;
                    position: fixed;
                    z-index: 1;
                    left: 0;
                    top: 0;
                    width: 100%;
                    height: 100%;
                    overflow: auto;
                    background-color: rgba(0, 0, 0, 0.4);
                    padding-top: 60px;
                }
                .modal-content {
                    background-color: #222;
                    margin: 5% auto;
                    padding: 20px;
                    border: 1px solid #888;
                    width: 80%;
                    border-radius: 8px;
                    color: white;
                }
                .close {
                    color: #aaa;
                    float: right;
                    font-size: 28px;
                    font-weight: bold;
                }
                .close:hover,
                .close:focus {
                    color: black;
                    text-decoration: none;
                    cursor: pointer;
                }
                @keyframes fadeIn {
                    0% { opacity: 0; }
                    100% { opacity: 1; }
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="sidebar">
                    <h2>Chat History</h2>
                    <ul class="chat-list" id="chatList"></ul>
                    <button class="new-chat-button" onclick="location.reload()"><i class="fas fa-plus"></i>New Chat</button>
                    <button class="settings-button" onclick="window.location.href='/settings'"><i class="fas fa-cogs"></i>Settings</button>
                </div>

                <div class="chat-container">
                    <h2>Chat</h2>
                    <div class="model-selector">
                        <select id="model" onchange="setModel()">
                            <option value="gemini-1.5-pro" selected>Gemini 1.5 PRO</option>
                            <option value="gemini-1.5-pro-002">Gemini 1.5 PRO 002 (NEW!)</option>
                            <option value="gemini-1.5-flash-002">Gemini 1.5 Flash 002 (NEW!)</option>
                            <option value="gemini-1.5-flash">Gemini 1.5 Flash</option>
                            <option value="gemini-1.5-flash-8b">Gemini 1.5 Flash 8B</option>
                            <option value="gemma-2-2b-it">Gemma 2 2B</option>
                            <option value="gemma-2-9b-it">Gemma 2 9B</option>
                            <option value="gemma-2-27b-it">Gemma 2 27B</option>
                            <option value="gemini-1.0-pro">Gemini 1.0 PRO</option>
                            <option value="gpt-3.5-turbo">GPT 3.5 Turbo</option>
                            <option value="gpt-4">GPT 4</option>
                            <option value="gpt-4-turbo">GPT 4 Turbo</option>
                            <option value="gpt-4o">GPT 4o</option>
                            <option value="gpt-4o-mini">GPT 4o Mini</option>
                            <option value="o1-preview">GPT o1 Preview (NEW!)</option>
                            <option value="o1-mini">GPT o1 Mini (NEW!)</option>
                            <option value="nx-0.1-b">NX 0.1 beta</option>
                        </select>
                    </div>

                    <div id="messages" class="messages">
                        <div class="message ai">Hello! How can I assist you?</div>
                    </div>

                    <div class="input-container">
                        <input type="text" id="userInput" placeholder="Type a message...">
                        <button onclick="sendMessage()">Send</button>
                    </div>
                    <div class="wlc">
                        Welcome to the SXSCLI AI ​​lab with a web interface!
                    </div>
                    <div class="powered-by">
                        &copy; 2023-2024 StasX. All rights reserved.
                    </div>
                </div>
            </div>

            <script>
                let selectedModel = "gemini-1.5-pro";

                function setModel() {
                    selectedModel = document.getElementById("model").value;
                    console.log("Selected model:", selectedModel);
                }

                function sendMessage() {
                    const message = document.getElementById("userInput").value;
                    console.log("Model:", selectedModel, "| Message:", message);

                    fetch('/send_message', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ model: selectedModel, message: message })
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data.response) {
                            const aiMessage = document.createElement('div');
                            aiMessage.classList.add('message', 'ai');
                            aiMessage.textContent = data.response;
                            document.getElementById('messages').appendChild(aiMessage);
                        }
                    });

                    const userMessage = document.createElement('div');
                    userMessage.classList.add('message', 'user');
                    userMessage.textContent = message;
                    document.getElementById('messages').appendChild(userMessage);
                    document.getElementById('userInput').value = "";
                }
            </script>
        </body>
        </html>
        """)

    def send_message(self):
        try:
            data = request.get_json()
            config = self.get_config()
            if config["api_key"] == "0":
                return jsonify({"error": "API key not set"})
            
            if config:
                settings_json = {
                    "model": data.get('model', config["model"]),
                    "api_key": config["api_key"],
                    "temperature": config["temperature"],
                    "max_tokens": config["max_tokens"],
                    "type": "chat",
                    "save_history": True,
                    "personalized_responses": True,
                    "user_name": "x",
                    "full_name": "x"
                }
                
                if data.get('model', config["model"]) in self.openai_models:
                    if not self.gpt_core.System(self.gpt_core).config(settings_json):
                        return jsonify({"error": "Failed to configure settings"})
                    
                    if not self.gpt_core.start_chat():
                        return jsonify({"error": "Failed to start chat"})
                    
                    ai_response = self.gpt_core.generate_response(data['message'])
                    
                    self.save_chat_history(data['message'], ai_response)
                    logging.info("AI_WITH_WEB_INTERFACE: AI response: "+ai_response)
                    return jsonify({"response": ai_response})

                elif data.get('model', config["model"]) == "nx-0.1-b":
                    pass
                
                else:
                    if not self.sxscli.System(self.sxscli).config(settings_json):
                        return jsonify({"error": "Failed to configure settings"})
                        
                    if not self.sxscli.start_chat():
                        return jsonify({"error": "Failed to start chat"})
                        
                    ai_response = self.sxscli.generate_response(data['message'])

                    self.save_chat_history(data['message'], ai_response)
                    logging.info("AI_WITH_WEB_INTERFACE: AI response: "+ai_response)
                    return jsonify({"response": ai_response})
            else:
                logging.info("AI_WITH_WEB_INTERFACE: No configuration found")
                return jsonify({"error": "No configuration found"})
        except Exception as e:
            logging.error(f"AI_WITH_WEB_INTERFACE: Error sending message: {e}")
            return jsonify({"error": str(e)})