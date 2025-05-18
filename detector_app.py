
import streamlit as st
import joblib
import numpy as np
import requests

st.title("🛡️ Real-Time Hücum Aşkarlayıcı")

# Modeli yüklə
model = joblib.load("real_time_ids_model.pkl")

# Online JSON-dan son trafiki götür
response = requests.get("https://json.extendsclass.com/bin/cyber-traffic")
if response.status_code == 200:
    data = response.json()
    st.write("Gələn Trafik:", data)

    X = np.array([[
        data["Flow Duration"],
        data["Total Fwd Packets"],
        data["Total Backward Packets"],
        data["Total Length of Fwd Packets"],
        data["Total Length of Bwd Packets"],
        data["Flow Bytes/s"],
        data["Flow Packets/s"]
    ]])

    prediction = model.predict(X)[0]

    if prediction == 1:
        st.error("⚠️ HÜCUM AŞKARLANDI!")
    else:
        st.success("✅ Normal trafik")
else:
    st.warning("Trafik məlumatı alınmadı.")
