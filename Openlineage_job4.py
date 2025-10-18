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
# Define the payload for the new job
payload = {
    "eventType": "COMPLETE",
    "eventTime": "2025-10-18T09:10:13.770024+10:00",
    "run": {
        "runId": "37eb6006-6780-4abe-bf2d-52007f711943"
    },
    "job": {
        "namespace": "ApacheSparkFileSystem",
        "name": "overwrite>"
    },
    "inputs": [{
        "namespace": "new-namespace",
        "name": "parquet-employees",
        "facets": {
            "schema": {
                "_producer": "https://github.com/OpenLineage/OpenLineage/blob/v1-0-0/client",
                "_schemaURL": "https://github.com/OpenLineage/OpenLineage/blob/v1-0-0/spec/OpenLineage.json#/definitions/SchemaDatasetFacet",
                "fields": [
                    {"name": "id", "type": "INTEGER"},
                    {"name": "name", "type": "STRING"}
                ]
            }
        }
    }],
    "outputs": [{
        "namespace": "new-namespace",
        "name": "csv-loaded_data",  # Updated name of the output dataset
        "facets": {
            "schema": {
                "_producer": "https://github.com/OpenLineage/OpenLineage/blob/v1-0-0/client",
                "_schemaURL": "https://github.com/OpenLineage/OpenLineage/blob/v1-0-0/spec/OpenLineage.json#/definitions/SchemaDatasetFacet",
                "fields": [
                    {"name": "id", "type": "FLOAT"},      # Updated field name/type
                    {"name": "name", "type": "BOOLEAN"}  # Updated field name/type
                ]
            }
        }
    }],
    "producer": "https://github.com/OpenLineage/OpenLineage/blob/v1-0-0/client",
    "schemaURL": "https://openlineage.io/spec/1-0-5/OpenLineage.json#/definitions/RunEvent"
}

# Define the API endpoint
url = "http://localhost:5000/api/v1/lineage"

# Send the HTTP POST request
response = requests.post(
    url,
    headers={'Content-Type': 'application/json'},
    json=payload
)

# Print the response
print("Status Code:", response.status_code)
print("Response Body:", response.text)
