import logging
import sys
import os
from tools.patient_lookup import lookup_patient_by_name

# Logging setup
logging.basicConfig(filename="logs/receptionist.log", level=logging.INFO)

class ReceptionistAgent:
    def __init__(self):
        self.patient = None
    
    def get_patient_report(self):
        if self.patient:
            return self._summarize_patient()
    


    def greet(self):
        return "👋 Hello! I'm your post-discharge assistant. Can I have your full name to access your report?"

    def handle_name(self, name: str):
        matches = lookup_patient_by_name(name)
        if not matches:
            return f"❌ Sorry, I couldn’t find any patient named '{name}'. Please check and try again."

        if len(matches) > 1:
            options = "\n".join([f"{i+1}. {m['name']} (age: {m['age']})" for i, m in enumerate(matches)])
            self.multiple_matches = matches
            return f"🔍 I found multiple matches:\n{options}\nPlease type the number of your record."

        self.patient = matches[0]
        return self._summarize_patient()

    def select_match(self, index: int):
        if hasattr(self, 'multiple_matches'):
            try:
                self.patient = self.multiple_matches[index - 1]
                return self._summarize_patient()
            except IndexError:
                return "❌ Invalid number. Please try again."
        return "❌ No multiple options to choose from."

    def _summarize_patient(self):
        p = self.patient
        logging.info(f"Patient selected: {p['name']} (ID: {p['patient_id']})")

        summary = (
            f"📄 Found your discharge summary:\n"
            f"Name: {p['name']}\n"
            f"Age: {p['age']}\n"
            f"Diagnosis: {p['diagnosis']}\n"
            f"Medications: {', '.join(p['medications'])}\n"
            f"Follow-up: {p['follow_up']}\n"
            f"Instructions: {', '.join(p['instructions'])}\n\n"
            f"How have you been feeling since your discharge?\n"
            f"(You can also ask any medical questions, and I’ll bring in our clinical expert.)"
        )
        return summary

    def forward_to_clinical(self, question: str):
        logging.info(f"Forwarding to Clinical Agent: {question}")
        return f"🔄 Routing your question to our clinical expert: “{question}”"
