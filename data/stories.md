## tu van 
* greet
  - utter_greet
* mood_great
  - utter_happy
* tuvan_tochat
  - action_tochat
* tuvan_nn
  - action_nn
* deny
  - utter_goodbye
  
## tc 
* tuvan_tochat
  - action_tochat
* deny
  - utter_goodbye
## nn
* tuvan_nn
  - action_nn
* deny
  - utter_goodbye
  
## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
