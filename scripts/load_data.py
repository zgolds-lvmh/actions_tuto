import os
import json
import requests
from google.cloud import bigquery
from google.oauth2 import service_account

# Fetch data from DigitalOcean Status API
API_URL = 'https://status.digitalocean.com/api/v2/summary.json'

response = requests.get(API_URL)

# Check if the response is successful
if response.status_code != 200:
    print(f"API request failed with status code {response.status_code}")
    print("Response content:", response.text)
    exit(1)

data = response.json()

print(data)

# Decide which parts of the data to load into BigQuery
# For example, let's focus on the 'components' data
components_data = data.get('components', [])

# # Authenticate with BigQuery using environment variable
# credentials_info = os.environ.get('GCP_SERVICE_ACCOUNT_JSON')
# if not credentials_info:
#     print("GCP_SERVICE_ACCOUNT_JSON environment variable not set.")
#     exit(1)

# credentials = service_account.Credentials.from_service_account_info(
#     json.loads(credentials_info)
# )
# client = bigquery.Client(credentials=credentials, project=credentials.project_id)

# # Define BigQuery dataset and table
# dataset_id = 'jungle_scout_amazon'
# table_id = 'digitalocean_status_components'

# # Reference to the dataset
# dataset_ref = client.dataset(dataset_id)

# # Create the dataset if it does not exist
# try:
#     client.get_dataset(dataset_ref)
#     print(f"Dataset {dataset_id} already exists.")
# except Exception:
#     print(f"Dataset {dataset_id} does not exist. Creating it now.")
#     dataset = bigquery.Dataset(dataset_ref)
#     dataset.location = "US"  # Adjust the location if needed
#     client.create_dataset(dataset)
#     print(f"Dataset {dataset_id} created.")

# # Reference to the table
# table_ref = dataset_ref.table(table_id)

# # Load data into BigQuery with auto schema detection
# job_config = bigquery.LoadJobConfig(
#     autodetect=True,
#     write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,  # Replace the table data
# )

# load_job = client.load_table_from_json(
#     components_data,
#     table_ref,
#     job_config=job_config
# )

# load_job.result()  # Waits for the job to complete

# if load_job.errors:
#     print("Errors occurred while loading data:")
#     for error in load_job.errors:
#         print(error)
#     exit(1)

print("Data loaded successfully.")
