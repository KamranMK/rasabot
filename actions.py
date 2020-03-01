# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet

import pandas as pd

class DetectRiskProfileForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "detect_risk_profile_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["age", "education" ,"investment_horizon", "investment_frequency"]


    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "age":[self.from_entity(
                entity="age", 
                intent="inform"),
                self.from_text()],
            "education": [self.from_entity(
                entity="education", 
                intent="inform"), 
                self.from_text()],
            "investment_horizon": [self.from_entity(
                entity="investment_horizon", 
                intent="inform"), 
                self.from_text()],
            "investment_frequency": [self.from_entity(
                entity="investment_frequency", 
                intent="inform"), 
                self.from_text()]
        }


    def submit(self, dispatcher: CollectingDispatcher,\
                tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:

        """Define what the form has to do after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_submit")

        return []


class DetectRiskProfile(Action):
    """Detect the users dialect"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "detect_risk_profile"

    def run(self, dispatcher, tracker, domain):
        """place holder method for guessing dialect """
        # let user know the risk profile identification is running
        dispatcher.utter_message(template="utter_working_on_it")

        # get information from the form
        age = tracker.get_slot("age")
        education = tracker.get_slot("education")
        investment_horizon = tracker.get_slot("investment_horizon")
        investment_frequency = tracker.get_slot("investment_frequency")

        database = pd.read_csv("database/demo_database.csv")

        # always guess US for now
        return [SlotSet("risk_profile", "balanced")]