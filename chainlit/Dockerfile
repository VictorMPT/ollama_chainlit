FROM python:3.10.11

WORKDIR /app
COPY . /app

# Install Langchain an Chainlit
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["chainlit","run","app.py"]

