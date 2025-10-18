import requests
import json

# Define the payload for the new job
payload = {
    "eventType": "COMPLETE",
    "eventTime": "2025-10-18T09:10:13.770024",
    "run": {
        "runId": "37eb6006-6780-4abe-bf2d-52007f711943"
    },
    "job": {
        "namespace": "Apache Spark / File System",
        "name": "overwrite"
    },
    "inputs": [
        {
            "namespace": "Apache Spark / File System",
            "name": "parquet.employees",
            "facets": {
                "schema": {
                    "_producer": "https://github.com/OpenLineage/OpenLineage/blob/v1-0-0/client",
                    "_schemaURL": "https://github.com/OpenLineage/OpenLineage/blob/v1-0-0/spec/OpenLineage.json#/definitions/SchemaDatasetFacet",
                    "fields": [
                        {
                            "name": "id",
                            "type": "INTEGER"
                        },
                        {
                            "name": "name",
                            "type": "STRING"
                        },
                        {
                            "name": "steps_to_desk",
                            "type": "FLOAT"
                        }
                    ]
                }
            }
        }
    ],
    "outputs": [
        {
            "namespace": "Apache Spark / File System",
            "name": "csv.loaded_data",
            "facets": {
                "schema": {
                    "_producer": "https://github.com/OpenLineage/OpenLineage/blob/v1-0-0/client",
                    "_schemaURL": "https://github.com/OpenLineage/OpenLineage/blob/v1-0-0/spec/OpenLineage.json#/definitions/SchemaDatasetFacet",
                    "fields": [
                        {
                            "name": "id",
                            "type": "INTEGER"
                        },
                        {
                            "name": "name",
                            "type": "STRING"
                        },
                        {
                            "name": "steps_to_desk",
                            "type": "FLOAT"
                        }
                    ]
                }
            }
        }
    ],
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
