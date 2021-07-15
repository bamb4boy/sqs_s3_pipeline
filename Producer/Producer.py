#importing all the relevant modules to run the server and the code
from flask import Flask, json, request
import boto3

# Name of the api server
api = Flask(__name__)

# The route of the api server and the POST method
@api.route('/api', methods=['POST'])
# Defining the function of the post message that we will be sending
def post_messages():
    # Create SQS client using the boto3 module
    sqs = boto3.client('sqs')
    # The url of my sqs
    queue_url = "https://sqs.us-east-1.amazonaws.com/966444541051/data_pipeline"
    # Sends message to SQS queue using boto3 with the body of the message as a string
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=str(request.json)
    )
    # Printing the sqs message ID and the status code
    print(response['MessageId'])
    return json.dumps({"success": True}), 201

# Running the flask app ensuring it runs on port 8000 and using the localhost network (dor docker)
if __name__ == '__main__':
    api.run(host="localhost", port=8000, debug=True)