# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import pandas as pd
import json

# actions_tochat
class Actiontuvan(Action):

     def name(self) -> Text:
         return "action_tochat"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         x = tracker.get_slot("nganh_intent")
         print(x)

         with open('dmnganhadd.json', encoding="utf8") as f:
                 data = json.load(f)

         columns = ["Nhóm ngành",
                    "Mã số",
                    "Tên ngành",
                    "Mã tổ hợp",
                    "Thời gian đào tạo",
                    "Danh hiệu",
                    "Chỉ tiêu dự kiến",
                    "Điểm TT 2018",
                    "Việc làm sau khi tốt nghiệp",
                    "Tố chất cần có",
                    "Lương", "tdn0", "tdn1", "tdn2", "tdn3"]
         df = pd.DataFrame(data, columns=columns)

         def tdn(x):
             op = "Tố chất cần có"
             tn = df["Tên ngành"].tolist()
             tc = df["Tố chất cần có"].tolist()

             for i in df["Tên ngành"]:
                 if (i == x):
                     for j in df:
                         if (j == op):
                             dispatcher.utter_message("Để học tốt ngành {} , {}".format(i, tc[tn.index(x)]))

         def tdn_0(x):
             op = "Tố chất cần có"
             tn = df["tdn0"].tolist()
             tn1 = df["Tên ngành"].tolist()
             tc = df["Tố chất cần có"].tolist()

             for i in df["tdn0"]:
                 if (i == x):
                     for j in df:
                         if (j == op):
                             dispatcher.utter_message("Để học tốt ngành {} , {}".format(tn1[tn.index(x)], tc[tn.index(x)]))

         def tdn_1(x):
             op = "Tố chất cần có"
             tn = df["tdn1"].tolist()
             tn1 = df["Tên ngành"].tolist()
             tc = df["Tố chất cần có"].tolist()

             for i in df["tdn1"]:
                 if (i == x):
                     for j in df:
                         if (j == op):
                             dispatcher.utter_message("Để học tốt ngành {} , {}".format(tn1[tn.index(x)], tc[tn.index(x)]))

         def tdn_2(x):
             op = "Tố chất cần có"
             tn = df["tdn2"].tolist()
             tn1 = df["Tên ngành"].tolist()
             tc = df["Tố chất cần có"].tolist()

             for i in df["tdn2"]:
                 if (i == x):
                     for j in df:
                         if (j == op):
                             dispatcher.utter_message("Để học tốt ngành {} , {}".format(tn1[tn.index(x)], tc[tn.index(x)]))

         def tdn_3(x):
             op = "Tố chất cần có"
             tn = df["tdn3"].tolist()
             tn1 = df["Tên ngành"].tolist()
             tc = df["Tố chất cần có"].tolist()

             for i in df["tdn3"]:
                 if (i == x):
                     for j in df:
                         if (j == op):
                             dispatcher.utter_message("Để học tốt ngành {} , {}".format(tn1[tn.index(x)], tc[tn.index(x)]))
         for i in df["tdn0"]:
             if x == i:
                 tdn_0(i)

         for j in df["tdn1"]:
             if x == j:
                 tdn_1(j)

         for k in df["tdn2"]:
             if x == k:
                 tdn_2(k)

         for h in df["tdn3"]:
             if x == h:
                 tdn_3(h)

         for i in df["Tên ngành"]:
             if x == i:
                 tdn(i)
         return []


# action_nn
class Actionnn(Action):

    def name(self) -> Text:
        return "action_nn"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        x = tracker.get_slot("nn")
        print(x)

        with open('dmnganhadd.json', encoding="utf8") as f:
            data = json.load(f)

        columns = ["Nhóm ngành",
                   "Mã số",
                   "Tên ngành",
                   "Mã tổ hợp",
                   "Thời gian đào tạo",
                   "Danh hiệu",
                   "Chỉ tiêu dự kiến",
                   "Điểm TT 2018",
                   "Việc làm sau khi tốt nghiệp",
                   "Tố chất cần có",
                   "Lương", "tdn0", "tdn1", "tdn2", "tdn3"]
        df = pd.DataFrame(data, columns=columns)

        def tdn(x):
            op = "Nhóm ngành"
            tn = df["Tên ngành"].tolist()
            tc = df["Nhóm ngành"].tolist()

            for i in df["Tên ngành"]:
                if (i == x):
                    for j in df:
                        if (j == op):
                            dispatcher.utter_message("Nhóm ngành của ngành {} là {}".format(i, tc[tn.index(x)]))

        def tdn_0(x):
            op = "Nhóm ngành"
            tn = df["tdn0"].tolist()
            tn1 = df["Tên ngành"].tolist()
            tc = df["Nhóm ngành"].tolist()

            for i in df["tdn0"]:
                if (i == x):
                    for j in df:
                        if (j == op):
                            dispatcher.utter_message("Nhóm ngành của ngành {} là {}".format(tn1[tn.index(x)], tc[tn.index(x)]))

        def tdn_1(x):
            op = "Nhóm ngành"
            tn = df["tdn1"].tolist()
            tn1 = df["Tên ngành"].tolist()
            tc = df["Nhóm ngành"].tolist()

            for i in df["tdn1"]:
                if (i == x):
                    for j in df:
                        if (j == op):
                            dispatcher.utter_message("Nhóm ngành của ngành {} là {}".format(tn1[tn.index(x)], tc[tn.index(x)]))

        def tdn_2(x):
            op = "Nhóm ngành"
            tn = df["tdn2"].tolist()
            tn1 = df["Tên ngành"].tolist()
            tc = df["Nhóm ngành"].tolist()

            for i in df["tdn2"]:
                if (i == x):
                    for j in df:
                        if (j == op):
                            dispatcher.utter_message("Nhóm ngành của ngành {} là {}".format(tn1[tn.index(x)], tc[tn.index(x)]))

        def tdn_3(x):
            op = "Nhóm ngành"
            tn = df["tdn3"].tolist()
            tn1 = df["Tên ngành"].tolist()
            tc = df["Nhóm ngành"].tolist()

            for i in df["tdn3"]:
                if (i == x):
                    for j in df:
                        if (j == op):
                            dispatcher.utter_message("Nhóm ngành của ngành {} là {}".format(tn1[tn.index(x)], tc[tn.index(x)]))

        for i in df["tdn0"]:
            if x == i:
                tdn_0(i)

        for j in df["tdn1"]:
            if x == j:
                tdn_1(j)

        for k in df["tdn2"]:
            if x == k:
                tdn_2(k)

        for h in df["tdn3"]:
            if x == h:
                tdn_3(h)

        for i in df["Tên ngành"]:
            if x == i:
                tdn(i)
        return []
