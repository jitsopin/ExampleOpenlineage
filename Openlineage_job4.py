import os
import glob
import requests
import json

# Define a function to delete datasets
def delete_datasets(url, datasets):
    for dataset in datasets:
        namespace = dataset["namespace"]
        name = dataset["name"]
        delete_url = f"{url}/namespaces/{namespace}/datasets/{name}"
        # Send DELETE request for each dataset
        response = requests.delete(delete_url, headers={'Accept': 'application/json'})
        print(f"Deleting dataset: {name} from namespace: {namespace}")
        print("Status Code:", response.status_code)
        if response.status_code == 200:
            print(f"Dataset {name} successfully deleted.")
        else:
            print(f"Failed to delete dataset {name}. Response: {response.text}")

# Define the API endpoint
url = "http://localhost:5000/api/v1/lineage"

# Get the list of all JSON files in the directory
json_directory = './json_content/'
json_files = glob.glob(os.path.join(json_directory, '*.json'))  # List all .json files

# Iterate through each JSON file
for filepath in json_files:
    print(f"Processing file: {filepath}")
    
    # Read the JSON content from the file
    with open(filepath, 'r') as file:
        payload = json.load(file)  # Load JSON content into a Python dictionary
        print("Payload:", json.dumps(payload, indent=4))
    
    # If there are datasets to delete, call the delete_datasets function
    if "inputs" in payload:
        delete_datasets(url, payload["inputs"])  # Delete input datasets
    if "outputs" in payload:
        delete_datasets(url, payload["outputs"]) # Delete output datasets
    
    # Send the HTTP POST request
    response = requests.post(
        url,
        headers={'Content-Type': 'application/json'},
        data=json.dumps(payload)  # Convert the payload to JSON format
    )
    
  # Print the response
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)