import boto3
import requests
import json

sqs = boto3.client("sqs")
QueueURL = 'https://sqs.us-east-1.amazonaws.com/851725600390/myqueue'

def delete_msg(handle):
    delete = sqs.delete_message(
        QueueUrl=QueueURL,
        ReceiptHandle= handle
    )

response = sqs.receive_message(
    QueueUrl = QueueURL,
    AttributeNames=[
        "All"
    ]
)

print(response['Messages'][0]['ReceiptHandle'])
print(response)

handle = response['Messages'][0]['ReceiptHandle']



