import requests
import json

# Define the payload for the new job
payload = {
    "eventType": "COMPLETE",
    "eventTime": "2020-12-29T15:30:00.001+10:00",
    "run": {
        "runId": "1234abcd-5678-efgh-9101-ijklmnopqrs2"
    },
    "job": {
        "namespace": "new-namespace",
        "name": "new-job"
    },
    "inputs": [{
        "namespace": "new-namespace",
        "name": "new-input-dataset",
        "facets": {
            "schema": {
                "_producer": "https://github.com/OpenLineage/OpenLineage/blob/v1-0-0/client",
                "_schemaURL": "https://github.com/OpenLineage/OpenLineage/blob/v1-0-0/spec/OpenLineage.json#/definitions/SchemaDatasetFacet",
                "fields": [
                    {"name": "input_col1", "type": "INTEGER"},
                    {"name": "input_col2", "type": "STRING"}
                ]
            }
        }
    }],
    "outputs": [{
        "namespace": "new-namespace",
        "name": "new-output-dataset",
        "facets": {
            "schema": {
                "_producer": "https://github.com/OpenLineage/OpenLineage/blob/v1-0-0/client",
                "_schemaURL": "https://github.com/OpenLineage/OpenLineage/blob/v1-0-0/spec/OpenLineage.json#/definitions/SchemaDatasetFacet",
                "fields": [
                    {"name": "output_col1", "type": "FLOAT"},
                    {"name": "output_col2", "type": "BOOLEAN"}
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
    headers={"Content-Type": "application/json"},
    data=json.dumps(payload)  # Convert the payload to JSON format
)

# Print the response
print("Status Code:", response.status_code)
print("Response Body:", response.text)
