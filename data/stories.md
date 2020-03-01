## happy path
* greet
  - utter_start_process
* affirm
  - detect_risk_profile_form
  - form{"name": "detect_risk_profile_form"}
  - form{"name": null}
  - utter_confirm_values
  - utter_working_on_it
* thankyou

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
