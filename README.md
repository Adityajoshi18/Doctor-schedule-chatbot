# Doctor-Schedule-Chatbot

## Overview

**Doctor-Schedule-Chatbot** is a chatbot built using **RASA**, an open-source machine learning framework for building conversational AI applications. This chatbot helps patients schedule appointments by providing detailed information about doctors based on their specialization. It is deployed on **Slack** for easy access and usability.

## Features

- Handles user inquiries about doctor availability and specialization.
- Schedules appointments with doctors based on user input.
- Uses **RASA NLU** for intent recognition and entity extraction.
- Utilizes **RASA Core** for dialogue management.
- Integrated with **Slack** for real-time interaction.

## Technologies Used

- **Python**
- **RASA Framework**
    - **RASA NLU** (Natural Language Understanding)
    - **RASA Core** (Dialogue Management)
- **Slack API**
- **Machine Learning** (LSTM-based model)
- **Spacy** (for NLP)
- **TensorFlow** (for deep learning-based intent classification)

## How It Works

1. **User Interaction**
The chatbot interacts with users via **Slack**, understanding their requests regarding doctor availability.

2. **Intent & Entity Recognition**
    - **Intent Recognition**: Determines what the user wants (e.g., booking an appointment, asking about a specialist).
    - **Entity Extraction**: Identifies keywords like doctor specialization.

3. **Dialogue Management**
The chatbot follows pre-defined stories (conversational paths) and generates appropriate responses based on the conversation history.

4. **Action Execution**
Custom actions (defined in actions.py) process user requests, fetch doctor availability from doctor.csv, and respond accordingly.

5. **Response Generation**
The chatbot responds using pre-configured templates in domain.yml, guiding the user through the appointment scheduling process.

## Installation

- Python
- Virtual Environment (recommended)
- RASA framework (pip install rasa)
- Slack API credentials

## Configuration Files

- **domain.yml**: Defines chatbot responses, intents, entities, and actions.
- **data.json**: Contains training examples for intent classification.
- **nlu_tensorflow.yml**: Specifies the NLP pipeline using **Spacy** and **TensorFlow**.
- **policies.yml**: Configures policies like KerasPolicy, MemoizationPolicy, and FallbackPolicy.
- **endpoints.yml**: Links the bot to an external action server.

## Future Enhancements

- Extend the chatbot to support voice-based interactions.
- Integrate with hospital databases for real-time doctor availability.
- Add support for multiple languages.

<!-- Built a Chatbot for the hospital that helps patients for scheduling appointments by giving them detailed information of a doctor of particular specialization.
Implemented the Chatbot on RASA , which is an open source machine learning bot building framework in python and deployed it on Slack.


RASA consists of two components- RASA NLU and RASA Core

RASA NLU is a library for natural language understanding (NLU) which does the classification of intent and extract the entity from the user input.
RASA Core is used for dialogue management by taking the structured input from the NLU and predicts the next best action using a probabilistic model like LSTM neural network. -->

