#!/bin/bash

while true; do
    echo "1. Run the application"
    echo "2. Install the application"
    read -p "Enter choice: " choice

    if [ $choice -eq 1 ]; then
        python main.py
        break
    elif [ $choice -eq 2 ]; then
        cd src
        pip install -r req.txt
        cd ..
        break
    else
        echo "Invalid choice"
    fi
done
