import requests
import json

# Define the payload (same as the JSON in the curl command)
payload = {
    "eventType": "COMPLETE",
    "eventTime": "2020-12-28T20:52:00.001+10:00",
    "run": {
        "runId": "0176a8c2-fe01-7439-87e6-56a1a1b4029f2"
    },
    "job": {
        "namespace": "my-namespace",
        "name": "my-job"
    },
    "inputs": [{
        "namespace": "my-namespace",
        "name": "my-input",
        "facets": {
            "schema": {
                "_producer": "https://github.com/OpenLineage/OpenLineage/blob/v1-0-0/client",
                "_schemaURL": "https://github.com/OpenLineage/OpenLineage/blob/v1-0-0/spec/OpenLineage.json#/definitions/SchemaDatasetFacet",
                "fields": [
                    {"name": "x", "type": "INTEGER"},
                    {"name": "y", "type": "FLOAT"}
                ]
            }
        }
    }],
    "outputs": [{
        "namespace": "my-namespace",
        "name": "my-output",
        "facets": {
            "schema": {
                "_producer": "https://github.com/OpenLineage/OpenLineage/blob/v1-0-0/client",
                "_schemaURL": "https://github.com/OpenLineage/OpenLineage/blob/v1-0-0/spec/OpenLineage.json#/definitions/SchemaDatasetFacet",
                "fields": [
                    {"name": "a", "type": "VARCHAR"},
                    {"name": "b", "type": "VARCHAR"}
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
