docker-compose build
docker-compose up -d
docker-compose exec ollama-container ollama pull llama3:8b
pause