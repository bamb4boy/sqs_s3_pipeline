From python:3

LABEL FILE="Producer"

RUN pip install boto3
RUN pip install flask

ADD Producer.py ./

CMD ["python", "./Producer.py" ]

