import streamlit as st
import pandas as pd
import pyttsx3
import time

# Initialize TTS Engine
engine = pyttsx3.init()

st.set_page_config(page_title="Voice-Glove Translator", page_icon="🧤")

st.title("🧤 Gesture-to-Speech Interface")

# Dictionary Mapping (Flex Levels: 0=Flat, 1=Bent)
# Order: Thumb, Index, Middle, Ring, Pinky
gesture_map = {
    "1,1,1,1,1": "Hello, how are you?",
    "0,1,1,0,0": "I need water.",
    "1,0,0,0,0": "Thank you.",
    "0,0,0,0,1": "Help me."
}

if 'history' not in st.session_state:
    st.session_state.history = []

placeholder = st.empty()

# Simulation Loop
for _ in range(5):
    # Simulated gesture input from XIAO
    current_pattern = "0,1,1,0,0" 
    
    if current_pattern in gesture_map:
        phrase = gesture_map[current_pattern]
        st.session_state.history.append(phrase)
        
        with placeholder.container():
            st.success(f"🗣️ Speaking: {phrase}")
            # engine.say(phrase) # Uncomment for local audio
            # engine.runAndWait()
            
            st.subheader("Recent Phrases")
            for p in st.session_state.history[-5:]:
                st.write(f"- {p}")
    
    time.sleep(4)
