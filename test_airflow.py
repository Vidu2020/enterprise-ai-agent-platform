# test_airflow.py

import requests

response = requests.get(
    "http://localhost:8080/api/v2/dags",
    auth=("admin", "3GhGtWKKhtV8PVFw")
)

print("Status:", response.status_code)
print("Response:", response.text)