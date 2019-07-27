# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from datetime import datetime

import logging
import requests
import json
from rasa_sdk.interfaces import Action
import pandas as pd

logger = logging.getLogger(__name__)

class ActionAppointment(Action):
    def name(self):
        return "action_appointment"

    def run(self, dispatcher, tracker, domain):
        specialist = tracker.get_slot('specialist')
        df = pd.read_csv("doctor.csv")
        doc = df.where(df['Specialization'].str.lower() == specialist.lower())
        doc = doc.dropna()
        if not doc.empty:
            doctorname = doc.iloc[0,0]
            weeklydays = doc.iloc[0,2]
            timings = doc.iloc[0,3]
            contactnumber = int(doc.iloc[0,4])
            response = """The doctor for {} is {}\nThe doctor is available on {} from {}\nThe contact number is {}""".format(specialist, doctorname,
                                weeklydays, timings, contactnumber)
        else:
            response = """Could not find the doctor for {}""".format(specialist)
        dispatcher.utter_message(response)
        return []