import boto3 # to communicate with amazon aws
import requests
import json

sqs = boto3.client("sqs")

id = requests.get('https://ids.pods.uvarc.io').json().get('id')

#response = sqs.send_message(
#    QueueUrl = 'https://sqs.us-east-1.amazonaws.com/851725600390/myqueue',
#    MessageBody = "Hey Guys!"
#)

response = sqs.send_message(
    QueueUrl = 'https://sqs.us-east-1.amazonaws.com/851725600390/myqueue',
    MessageBody = id,
    MessageAttributes = {
        'Project': {
            'StringValue': 'Project X',
            'DataType': 'String'
        },
        'Flavor': {
            'StringValue': "Raspberry Gelato",
            'DataType': 'String'
        }
    }
)

print(response)