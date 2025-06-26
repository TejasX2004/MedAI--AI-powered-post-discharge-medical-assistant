import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from agents.receptionist_agent import ReceptionistAgent
from agents.clinical_agent import ClinicalAgent

import streamlit as st

st.title("🩺 MedAI Post-Discharge Assistant")

# Init agents
receptionist = ReceptionistAgent()
clinical = ClinicalAgent()

# Input
name = st.text_input("Enter your full name:")
if name:
    report = receptionist.handle_name(name)
    if report:
        st.success(f"Found discharge report for {name}")
        st.markdown(report)

        query = st.text_input("Ask a medical question based on your report:")
        if query:
            if receptionist.forward_to_clinical(query):
                response = clinical.answer_query(query, name)
                st.markdown(response)
    else:
        st.error("Patient not found.")
