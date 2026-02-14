# 🧤 Gesture-to-Speech-Glove

An IoT-enabled assistive wearable designed for individuals with speech impairments. The glove converts finger flex movements into predefined words and phrases.

## 🚀 Features
- **Flex Pattern Recognition:** Maps specific finger combinations to a dictionary of phrases.
- **Real-Time Text-to-Speech (TTS):** Python backend synthesizes voice output instantly upon gesture detection.
- **Ultra-Compact Design:** Powered by the XIAO ESP32C3 for a minimal wearable profile.
- **Custom Dictionary:** Users can map new gestures to custom phrases via the dashboard.

## ⚙️ Engineering Logic
- **Hardware:** Five flex sensors (voltage dividers) measure the bend angle of each finger.
- **Software:** Python monitors the sensor "Signatures" and uses the `pyttsx3` library to convert text strings into audible speech.
