import openai
import json

class SXSCLI_OPENAI:
    def __init__(self):
        self.openai_config = {}
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
                if not (1 <= max_tokens <= 4096):
                    raise ValueError("Max tokens must be between 1 and 4096")
                
                self.parent.openai_config = {
                    "model": data_s.get("model", "gpt-3.5-turbo"),
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

    def configure_openai(self):
        try:
            openai.api_key = self.openai_config.get("api_key")
            return True
        except Exception as e:
            print(f"Error configuring OpenAI API: {e}")
            return False

    def start_chat(self, initial_history=None):
        try:
            if not self.configure_openai():
                return False

            self.chat = {
                "model": self.openai_config.get("model"),
                "messages": initial_history or [],
                "temperature": self.openai_config.get("temperature"),
                "max_tokens": self.openai_config.get("max_tokens")
            }
            
            if self.openai_config.get("personalized_responses"):
                greeting = (f"I understand your name is {self.openai_config.get('full_name')} "
                            f"and you prefer to be called {self.openai_config.get('user_name')}. "
                            "How can I help you today?")
                self.chat["messages"].append({"role": "system", "content": greeting})
            
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
            
            self.chat["messages"].append({"role": "user", "content": prompt})
            
            response = openai.ChatCompletion.create(
                model=self.chat["model"],
                messages=self.chat["messages"],
                temperature=self.chat["temperature"],
                max_tokens=self.chat["max_tokens"]
            )
            
            response_text = response['choices'][0]['message']['content']
            self.chat["messages"].append({"role": "assistant", "content": response_text})
            
            return response_text
        except Exception as e:
            print(f"Error generating response: {e}")
            return "Error: Message could not be sent."