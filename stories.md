## story 01
* greet
    - utter_greet
* inform
    - action_appointment
    - utter_ask
* affirm
    - utter_gratitude
* goodbye
    - utter_goodbye

## story 02
* greet
    - utter_greet
* inform
    - action_appointment
    - utter_ask
* deny
    - utter_ask_specialization
* inform
    - action_appointment
    - utter_ask
* affirm
    - utter_gratitude
* goodbye
    - utter_goodbye

## story 03
* inform
    - action_appointment
    - utter_ask
* affirm
    - utter_gratitude
* goodbye
    - utter_goodbye

## story04
* inform
    - action_appointment
    - utter_ask
* deny
    - utter_ask_specialization
* inform
    - action_appointment
    - utter_ask
* affirm
    - utter_gratitude
* goodbye
    - utter_goodbye

## story04
* inform
    - utter_ask_specialization
* inform
    - action_appointment
    - utter_ask
* deny
    - utter_ask_specialization
* inform
    - action_appointment
    - utter_ask
* affirm
    - utter_gratitude
* goodbye
    - utter_goodbye

## affirm path
* affirm
    - utter_gratitude
* goodbye
    - utter_goodbye

## deny path
* deny
    - utter_ask_specialization
* inform
    - action_appointment
    - utter_ask
* affirm
    - utter_gratitude
* goodbye
    - utter_goodbye

## greet path
* greet
    - utter_greet

## goodbye path
* goodbye
    - utter_goodbye