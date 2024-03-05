import requests
import json

# URL of your Flask endpoint
url = 'http://127.0.0.1:5000/get_array'  # Replace with your actual URL

# Make a GET request to the Flask endpoint
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    json_data = response.json()

    # Write the JSON data to a file
    with open('output.json', 'w') as f:
        json.dump(json_data, f)
else:
    print("Error:", response.status_code)
