#!/bin/zsh
set -e

# Go to project folder
cd /Users/novosoftsolutions/CodingProjects/PythonProjects/NaukriAutomation/

# Activate venv
source .venv/bin/activate

# Run script
python3 telegramsender.py
