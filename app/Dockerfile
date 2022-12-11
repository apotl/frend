FROM python:3

RUN pip install discord
RUN pip install openai
RUN pip install pyyaml

ARG FRENDCONFIG
COPY ${FRENDCONFIG} /app/config.yml

COPY app/ /app

WORKDIR /app



CMD ["python", "app.py"]
