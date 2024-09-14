#!/bin/sh

echo "Установка зависимостей..."
pip install -r requirements.txt

echo "Запуск приложения..."
python main.py
