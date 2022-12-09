FROM python:3

RUN pip install discord
RUN pip install openai
RUN pip install pyyaml

COPY app/ /app
COPY config.yml /app/
WORKDIR /app


CMD ["python", "app.py"]
