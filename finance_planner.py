# Health Diagnosis System
# This program suggests a possible diagnosis and treatment
# based on symptoms, age, and medical history.

def get_diagnosis(symptoms, age, history):
    # dictionary of diseases and treatments
    diseases = {
        "influenza": "Rest and drink a lot of water",
        "cold": "Take warm fluids and rest",
        "migraine": "Pain relievers and avoid bright lights",
        "allergy": "Take antihistamines",
    }

    # nested conditions to guess disease
    if "fever" in symptoms and "headache" in symptoms:
        diagnosis = "influenza"
    elif "sneezing" in symptoms and "runny nose" in symptoms:
        diagnosis = "cold"
    elif "headache" in symptoms and "nausea" in symptoms:
        diagnosis = "migraine"
    elif "itchy eyes" in symptoms or "rash" in symptoms:
        diagnosis = "allergy"
    else:
        diagnosis = "unknown"

    # return result
    if diagnosis in diseases:
        return diagnosis, diseases[diagnosis]
    else:
        return "No clear diagnosis", "Try visiting a doctor"


# main program
try:
    symptoms_input = input("Enter symptoms (comma-separated): ")
    symptoms_list = [s.strip().lower() for s in symptoms_input.split(",")]

    age = int(input("Age: "))
    history = input("Medical history: ")

    diagnosis, treatment = get_diagnosis(symptoms_list, age, history)

    print("Recommended Diagnosis:", diagnosis)
    print("Suggested Treatment:", treatment)

except ValueError:
    print("Invalid input. Please enter correct values.")
