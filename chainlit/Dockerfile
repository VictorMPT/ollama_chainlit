FROM python:3.10.11

WORKDIR /app
COPY . /app

# Install Langchain an Chainlit
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["chainlit","run","app.py"]
# docker build -t docstring_chatbot .
# docker run -p 8000:8000 docstring_chatbot

