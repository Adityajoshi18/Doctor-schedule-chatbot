# Doctor-schedule-chatbot
Built a Chatbot for the hospital that helps patients for scheduling appointments by giving them detailed information of a doctor of particular specialization.
Implemented the Chatbot on RASA , which is an open source machine learning bot building framework in python and deployed it on Slack.


RASA consists of two components- RASA NLU and RASA Core

RASA NLU is a library for natural language understanding (NLU) which does the classification of intent and extract the entity from the user input.
RASA Core is used for dialogue management by taking the structured input from the NLU and predicts the next best action using a probabilistic model like LSTM neural network.

