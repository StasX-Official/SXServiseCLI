import requests

class Search:
    def __init__(self, data):
        required_keys = ["engine", "google_search_engine_api_key", "google_search_engine_cse_id", "bing_search_api_key"]
        for key in required_keys:
            if key not in data or not data[key]:
                raise ValueError(f"Missing or invalid value for {key}")
        
        self.mode = data["mode"]        
        self.engine = data["engine"]
        self.google_search_engine_api_key = data["google_search_engine_api_key"]
        self.google_search_engine_cse_id = data["google_search_engine_cse_id"]
        self.bing_search_api_key = data["bing_search_api_key"]
        
    def analyze(self, query):
        search_engines = {
            'google': self.google_search,
            'bing': self.bing_search,
            'duckduckgo': self.duckduckgo_search
        }

        search_function = search_engines.get(self.engine)
        if not search_function:
            return {"error": "Invalid search engine."}

        search_results = search_function(query)
        
        # Перевірка на порожні результати
        if not search_results:
            return {"error": "No results found for the query."}
        
        print(search_results)

        abstract = search_results.get('Abstract', 'No description available.')
        abstract_url = search_results.get('AbstractURL', '')

        # Формування додаткової інформації
        wiki_info = f"Main description available on [Wikipedia]({abstract_url})" if abstract_url else 'Main description is missing.'

        # Формування списку related topics
        related_topics = [
            f"[{topic.get('Text', 'No Text Available')}]({topic.get('FirstURL', '')})"
            for topic in search_results.get('RelatedTopics', [])
        ]
        
        # Форматування результату
        result = f"""
    Description: {abstract}

    Related Topics:
    {'  '.join(related_topics) if related_topics else 'No additional information.'}

    Additional Info: {wiki_info}
    """

        return result



                

    
    def search(self, query):
        if self.engine == 'google':
            if self.mode == 'json':
                return self.google_search(query)
            elif self.mode == 'analyze':
                return self.analyze(query)
            else:
                return {"error": "Invalid mode. Supported modes are 'json' and 'analyze'"}
                
        elif self.engine == 'bing':
            if self.mode == 'json':
                return self.bing_search(query)
            elif self.mode == 'analyze':
                return self.analyze(query)
            else:
                return {"error": "Invalid mode. Supported modes are 'json' and 'analyze'"}
        elif self.engine == 'duckduckgo':
            if self.mode == 'json':
                return self.duckduckgo_search(query)
            elif self.mode == 'analyze':
                return self.analyze(query)
            else:
                return {"error": "Invalid mode. Supported modes are 'json' and 'analyze'"}
            
        else:
            raise ValueError(f"Search engine '{self.engine}' is not supported.")

    def google_search(self, query):
        url = f'https://www.googleapis.com/customsearch/v1?q={query}&key={self.google_search_engine_api_key}&cx={self.google_search_engine_cse_id}'
        response = requests.get(url)
        return self._handle_response(response)

    def bing_search(self, query):
        url = f'https://api.bing.microsoft.com/v7.0/search?q={query}'
        headers = {'Ocp-Apim-Subscription-Key': self.bing_search_api_key}
        response = requests.get(url, headers=headers)
        return self._handle_response(response)

    def duckduckgo_search(self, query):
        url = f'https://api.duckduckgo.com/?q={query}&format=json'
        response = requests.get(url)
        return self._handle_response(response)

    def _handle_response(self, response):
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            return {"error": f"HTTP error occurred: {e}"}
        except requests.exceptions.RequestException as e:
            return {"error": f"Request error occurred: {e}"}
        except ValueError:
            return {"error": "Invalid JSON response"}