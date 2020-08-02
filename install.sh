#!/bin/bash

echo "Installing all dependencies\n"

sudo apt -y update
sudo apt -y install espeak
sudo apt -y install python3-pip

pip3 install pyttsx3

chmod +x speak.py
sudo cp speak.py /usr/bin/speak.py
