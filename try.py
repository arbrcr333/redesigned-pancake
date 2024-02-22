import streamlit as st

# Define questions and options
questions = [
    "You find it easy to introduce yourself to other people.",
    "You often get so lost in thoughts that you ignore or forget your surroundings.",
    "You try to respond to your e-mails as soon as possible and cannot stand a messy inbox.",
    "You find it easy to stay relaxed and focused even when there is some pressure.",
    "You do not usually initiate conversations."
]

options = [
    "Strongly disagree", 
    "Disagree", 
    "Neutral", 
    "Agree", 
    "Strongly agree"
]

# Function to diagnose personality based on responses
def diagnose_personality(responses):
    # This is a simplified example. You could add more sophisticated analysis here.
    extroversion = introversion = 0
    for response in responses:
        if response > 3:
            extroversion += 1
        elif response < 3:
            introversion += 1
    
    if extroversion > introversion:
        return "Your responses suggest you might be more extroverted."
    elif introversion > extroversion:
        return "Your responses suggest you might be more introverted."
    else:
        return "Your responses suggest you have a balanced personality between extroversion and introversion."

# Streamlit app layout
st.title('Personality Diagnosis')

# Store responses
responses = []

for i, question in enumerate(questions):
    response = st.radio(question, options, key=i)
    responses.append(options.index(response) + 1)  # Convert options to a scale of 1-5

if st.button('Diagnose Personality'):
    personality_type = diagnose_personality(responses)
    st.success(personality_type)
