import streamlit as st
import pandas as pd
import pickle

# load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🚚 Logistics Efficiency & Delay Prediction")

# --- USER INPUT ---
st.sidebar.header("Enter Shipment Details")

distance = st.sidebar.number_input("Distance (km)", 0, 2000)
weight = st.sidebar.number_input("Weight (kg)", 0, 1000)
traffic = st.sidebar.slider("Traffic Volume", 0, 100, 50)
cost = st.sidebar.number_input("Cost", 0, 10000)
road_quality = st.sidebar.slider("Road Quality Index", 0.0, 1.0, 0.7)

# --- PREDICTION ---
input_data = pd.DataFrame([[distance, weight, traffic, cost, road_quality]],
                          columns=['distance_km','weight_kg','traffic_volume','cost','road_quality_index'])

prediction = model.predict(input_data)

# --- OUTPUT ---
st.subheader("Prediction Result")

if prediction[0] == 1:
    st.error("⚠️ High Chance of Delay")
else:
    st.success("✅ On-Time Delivery Expected")
