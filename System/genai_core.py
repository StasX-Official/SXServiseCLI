import json
import google.generativeai as genai

class SXSCLI_GENAI:
    def __init__(self):
        self.genai_config = {}
        self.chat = None
    
    class System:
        def __init__(self, parent):
            self.parent = parent
        
        def config(self, settings):
            try:
                data_s = settings if isinstance(settings, dict) else json.loads(settings)
                temperature = float(data_s.get("temperature", 0.7))
                if not (0.1 <= temperature <= 1.0):
                    raise ValueError("Temperature must be between 0.1 and 1.0")

                max_tokens = int(data_s.get("max_tokens", 100))
                if not (1 <= max_tokens <= 125000):
                    raise ValueError("Max tokens must be between 1 and 125000")
                self.parent.genai_config = {
                    "model": data_s.get("model", "default-model"),
                    "api_key": data_s.get("api_key"),
                    "temperature": temperature,
                    "max_tokens": max_tokens,
                    "type": data_s.get("type", "chat"),
                    "save_history": data_s.get("save_history", False),
                    "personalized_responses": data_s.get("personalized_responses", True),
                    "user_name": data_s.get("user_name", "User"),
                    "full_name": data_s.get("full_name", "User Full Name")
                }
                return True
            except (json.JSONDecodeError, TypeError, ValueError) as e:
                print(f"Error parsing settings: {e}")
                return False

    def configure_genai(self):
        try:
            genai.configure(api_key=self.genai_config.get("api_key"))
            return True
        except Exception as e:
            print(f"Error configuring GenAI API: {e}")
            return False

    def start_chat(self, initial_history=None):
        try:
            if not self.configure_genai():
                return False
                
            model = genai.GenerativeModel(self.genai_config.get("model"))
            self.chat = model.start_chat(history=initial_history or [])
            
            if self.genai_config.get("personalized_responses"):
                greeting = (f"I understand your name is {self.genai_config.get('full_name')} "
                          f"and you prefer to be called {self.genai_config.get('user_name')}. "
                          "How can I help you today?")
                self.chat.send_message(greeting)
            
            return True
        except Exception as e:
            print(f"Error starting chat: {e}")
            self.chat = None
            return False

    def generate_response(self, prompt):
        try:
            if not self.chat:
                if not self.start_chat():
                    return "Error: Could not initialize chat."
            
            response = self.chat.send_message(prompt)
            return response.text
            
        except Exception as e:
            print(f"Error sending message: {e}")
            return "Error: Message could not be sent."
