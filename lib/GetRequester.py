import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            
            return response.content
        except requests.exceptions.RequestException as e:
            print(f'Error {e}')
            return b""

    def load_json(self):
        response_body = self.get_response_body()
        if response_body:
            try:
                return json.loads(response_body)
            except ValueError as e:
                print(f"Error decoding {e}")
        return None
    
if __name__ == "__main__":
    requester = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")
    data = requester.load_json()
    print("Final Data:", data) 