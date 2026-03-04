#!/bin/zsh
set -e

# Load env vars
source ~/.zshrc

# Go to project folder
cd ~/CodingProjects/PythonProjects/NaukriAutomation/

# Activate venv
source .venv/bin/activate

# Run script
python3 main.py
