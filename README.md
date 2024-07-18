# ollama_chainlit
Run locally Ollama models in a nice chainlit user interface.

![]("demo.png")

**Step 1 :** Make sure docker/docker-compose is installed on your machine

**Step 2 :** Build and start the chatbot using the following command :

On Windows :
```sh
start_chatbot
```

On Linux : 
```sh
docker-compose up -d
docker-compose exec ollama-container ollama pull llama3:8b
```

Your chatbot should now be available at the following adress http://localhost:8000


**Step 3 :** Change the Ollama model. By default **llama3:8b** model is pulled and used by the chatbot.

You can pull other models from Ollama using the command :
```sh
docker-compose exec ollama-container ollama pull $model_name
```

To specify the model used by the chatbot you can modify **app.py** script :

```python
model = Ollama(model=$model_name, base_url="http://ollama-container:11434")
```

**Step 4:** Modify prompt engineering according to your needs. Modify this part in **app.py** :

```python
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an expert in python code, every time you write a function you"
                "try to respect code conventions like PEP8",
            ),
            (
                "human",
                "{question}",
            ),
        ],
    )
```

Note : In this chainlit app each prompt is runned indepently therefore the chatbot has no memory of the conversion. Feel free to implement this memory feature.

**Step 5 :** Stop the app using the following command :

```sh
docker-compose down
```

