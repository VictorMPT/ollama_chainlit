docker-compose up -d
docker-compose exec ollama-container ollama pull llama3:8b
start "" "http://localhost:8000"