#!/bin/bash
echo "Starting the server"

docker build -t "SteamLitApp/v0.1.0" .

docker run -p 8501:8501 -d StreamLitApp/v0.1.0