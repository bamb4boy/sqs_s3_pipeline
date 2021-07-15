#This is a repo for a simple Producer>SQS>Consumer>s3 pipeline

#Components:
1 - Producer - Dockerized flask app that listening to POST requests 

2 - SQS - AWS Simple queue service

3 - Consumer - Dockerized python app that checks a SQS for messages

4 - S3 bucket that stores a csv file sent from the Consumer 




#Steps of running the pipeline

1 - Install all of the following tools on the instance or the machine you are working
apt update -y
apt install unzip -y
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
apt install docker.io -y
apt install python3 -y
apt install python3-pip -y
pip3 install boto3
pip3 install flask

2 - Go to your aws account and create the following:
- IAM role with the right permissions
- SQS named data_pipeline
- s3 bucket named glebsqsbucket (or your name, you will just need to change it in the consumer script )
- make sure the bucket is private and it has a folder named post_processing

3 - Configure your aws cli (aws configure) with the IAM role creds - notice the region(us-east-1)

4 - Go to the Producer folder and run the Producer.py script, after its running send a POST request
to your local host and see if you receive any errors
If everything is working properly you will see a message in the SQS
Leave the producer running

5 - Go to Consumer folder and run the Consumer.py script
if the script runs as intended it will print the message you sent with the POST request from sqs
and it will save it in the bucket

6 - Close the consumer and the producer

7 - Go to the Producer folder, there you will see a text file with two commands for running the docker
Run them one by one
Check again with POST request that the producer works fine

8 - Go to the Consumer folder, there you will see a text file with two commands for running the docker
Run them one by one
if the script runs as intended it will print the message you sent with the POST request from sqs
and it will save it in the bucket

9 - Cleanup
