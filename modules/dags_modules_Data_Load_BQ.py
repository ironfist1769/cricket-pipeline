from google.cloud import storage, bigquery

def load_csv_to_bigquery(bucket_name, file_name, dataset_id, table_id):
    # Initialize BigQuery and Cloud Storage clients
    storage_client = storage.Client()
    bigquery_client = bigquery.Client()

    # Specify the GCS URI of the file
    gcs_uri = f"gs://{bucket_name}/{file_name}"
    
    schema = [
        bigquery.SchemaField("Rank", "INTEGER"),
        bigquery.SchemaField("Name", "STRING"),
        bigquery.SchemaField("Country", "STRING"),
        # Add additional fields as needed
    ]


    # Configure the load job
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,  # Skip header row if present
        schema=schema
    )

    # Specify the BigQuery table reference
    table_ref = f"{dataset_id}.{table_id}"

    # Load data from GCS to BigQuery
    load_job = bigquery_client.load_table_from_uri(
        gcs_uri, table_ref, job_config=job_config
    )

    # Wait for the load job to complete
    load_job.result()
    print(f"Loaded {file_name} from {bucket_name} to {table_ref}.")

