import boto3
import logging

def lambda_handler(event, context):
    client = boto3.client('sagemaker')
    client.stop_notebook_instance(NotebookInstanceName='run-prep-job-py')
    return 0
    