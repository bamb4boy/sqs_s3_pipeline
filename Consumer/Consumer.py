# importing the relevant modules to run the code
import boto3
import json
import csv
import os

# creating a loop that will go through the messages and continue the pipeline
while True:
    # Create SQS client using boto3 module
    sqs = boto3.client('sqs')
    # The url of my sqs
    queue_url = "https://sqs.us-east-1.amazonaws.com/966444541051/data_pipeline"
    # A condition to start the loop
    if queue_url == queue_url:
        # Receive message from SQS queue
        response = sqs.receive_message(
            QueueUrl=queue_url,
            AttributeNames=[
                'SentTimestamp'
            ],
            MaxNumberOfMessages=1,
            MessageAttributeNames=[
                'All'
            ],
            VisibilityTimeout=0,
            WaitTimeSeconds=0
        )

        # Storing the content of the response to the message variable
        message = response['Messages'][0]
        # Choosing only the body of the message, storing it int the body variable
        # Replacing ' with " in order to run the json.loads
        body = message["Body"].replace("'", '"')
        # Creating variables for the json dictionary
        myDict = json.loads(body)
        user = myDict["user"]
        product_name = myDict["product"]["name"]
        product_version = myDict["product"]["version"]
        myType = myDict["type"]
        pageView = myDict["pageView"]
        timestamp = myDict["timestamp"]
        # Creating a loop to get a unique name for the files
        i = 0
        while os.path.exists("./csv_files/messageFile%s.csv" % i):
            i += 1
        messageFile = open("./csv_files/messageFile%s.csv" % i, "w")
        # Configuring the way the csv will be written
        myCsv_writer = csv.writer(messageFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Writing the header data to the csv file
        myCsv_writer.writerow(['User', 'Product Name', 'Product Version', 'Type', 'Page View', 'Time Stamp'])
        # Writing the data to the csv file
        myCsv_writer.writerow([user, product_name, product_version, myType, pageView, timestamp])
        messageFile.close()

        # Creating the s3 client and
        s3 = boto3.resource('s3')
        # Storing my bucket name in the bucket variable - change this if you used other name
        BUCKET = "glebsqsbucket"
        # Uploading the csv file to the bucket
        s3.Bucket(BUCKET).upload_file("./csv_files/messageFile%s.csv" % i, "post_processing/messageFile%s.csv" % i)



    else:
        print("exiting")
        break