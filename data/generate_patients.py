import json
import random
from faker import Faker

fake = Faker()

diagnoses = [
    "Chronic Kidney Disease Stage 1",
    "Chronic Kidney Disease Stage 2",
    "Chronic Kidney Disease Stage 3",
    "Acute Kidney Injury",
    "Nephrotic Syndrome",
    "Glomerulonephritis",
    "Hypertensive Nephropathy"
]

medications_pool = [
    "Lisinopril", "Furosemide", "Metoprolol", "Amlodipine", 
    "Losartan", "Hydrochlorothiazide", "Erythropoietin", 
    "Calcium Acetate", "Sodium Bicarbonate"
]

follow_ups = [
    "Follow up in 1 week with nephrologist",
    "Follow up in 2 weeks with primary care",
    "Monitor labs weekly",
    "Next dialysis session in 3 days",
    "Follow up in 1 month for biopsy review"
]

instructions_pool = [
    "Limit sodium and protein intake",
    "Take medications with food",
    "Monitor blood pressure daily",
    "Report any swelling or weight gain",
    "Avoid NSAIDs and nephrotoxic drugs"
]

def generate_patient(i):
    name = fake.name()
    return {
        "patient_id": f"P{i+1:04}",
        "name": name,
        "age": random.randint(25, 85),
        "diagnosis": random.choice(diagnoses),
        "medications": random.sample(medications_pool, k=random.randint(2, 4)),
        "follow_up": random.choice(follow_ups),
        "instructions": random.sample(instructions_pool, k=2)
    }

patients = [generate_patient(i) for i in range(25)]

with open("data/patients.json", "w") as f:
    json.dump(patients, f, indent=2)

print("✅ 25 patient records written to data/patients.json")
