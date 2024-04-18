import boto3 # to communicate with amazon aws
import requests
import json

sqs = boto3.client("sqs")
QueueURL = 'https://sqs.us-east-1.amazonaws.com/851725600390/myqueue'

response = sqs.get_queue_attributes(
    QueueUrl = QueueURL,
    AttributeNames=[
        "All"
    ]
)


print(response)
print(response['Attributes']['ApproximateNumberOfMessages'])