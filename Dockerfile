FROM python:3.12

RUN apt-get update
RUN apt-get install npm -y --no-install-recommends
RUN npm install -g aws-cdk@>=2.0.0

COPY requirements.txt .
COPY src/requirements-lambda.txt src/
RUN pip3 install --upgrade -r requirements.txt
RUN pip3 install --upgrade -r src/requirements-lambda.txt -t src/

COPY . /app/
WORKDIR /app

COPY config.yml src/

ENTRYPOINT ["cdk"]
