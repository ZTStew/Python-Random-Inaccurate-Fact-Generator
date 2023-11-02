import requests, json

# Grabs API key from external file
def get_key(file_location):
  key = open(file_location)
  out = json.load(key)["key"]
  key.close()
  return out

def send_query_to_gpt3(query, api_key):
    endpoint = "https://api.openai.com/v1/engines/gpt-3.5-turbo/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "prompt": query,
        "max_tokens": 50  # Adjust this as needed
    }

    response = requests.post(endpoint, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["text"]
    else:
        print("Request failed with status code:", response.status_code)
        print(response.text)
        return None

# # Replace 'your_api_key' with your actual OpenAI API key
api_key = get_key('./API_Credentials/api_access.json')
query = "provide a random word"

response = send_query_to_gpt3(query, api_key)
if response:
    print(response)
