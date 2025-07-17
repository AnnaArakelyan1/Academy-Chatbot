# Academy-Chatbot

A simple and modular chatbot designed to help users with frequently asked questions, resource suggestions, and general academic queries. It uses natural language processing (NLP) techniques and sentence similarity to understand and respond to user inputs intelligently.


## Features

- Handles greetings, FAQs, and resource-related questions
- Uses NLTK and spaCy for text preprocessing and named entity recognition
- Leverages Sentence Transformers to find the most relevant FAQ answers
- Retrieves links and resources based on topics from a CSV file
- Modular design following Object-Oriented Analysis & Design (OOAD) principles


## Project Structure

├── chatbot.py # Main chatbot logic and intent processing
├── faqManager.py # FAQ manager using sentence similarity
├── nlp_processing.py # NLP preprocessing: tokenization, lemmatization, NER
├── resources.py # Resource matcher using CSV data
├── main.py # Entry point to run the chatbot
└── data/
├── faq.csv # Contains questions and answers
└── resource.csv # Contains topics and their associated links
