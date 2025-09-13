import requests
import json

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

def is_json(my_data):
    try:
        json.loads(my_data)
        return True
    except ValueError:
        return False

# ✅ Step 1: Check HTTP status
if response.status_code == 200:
    print("API call successful ✅")

    # ✅ Step 2: Check if response body is valid JSON
    if is_json(response.text):
        data = response.json()
        print("Valid JSON ✅")
        print(json.dumps(data, indent=4))  # pretty print JSON
    else:
        print("Response is not JSON ❌")
        print(response.text)
else:
    print(f"API call failed ❌ Status Code: {response.status_code}")
    print("Response:", response.text)
