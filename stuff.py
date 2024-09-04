import streamlit as st
import numpy as np
import pandas as pd
import time

st.set_page_config(layout="wide")

#st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background: url("https://wallpapers.com/images/high/green-landscape-1920-x-1080-wallpaper-90adzognw79vw2u7.webp");
#             background-size: cover
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

file_path = 'synthetic_data_with_biiiiig_noise.csv'
data = pd.read_csv(file_path)

# Remove rows with null values
data = data.dropna().reset_index()

# Parameters
data_points = len(data) - 1  # Total number of data points to simulate

if "track" not in st.session_state:
    st.session_state.track = 0

# Streamlit app layout
st.title("AGRIWATCH Dashboard")
tree_image = "LcKaq8pca.png"  # Adjust path as necessary

cols = st.columns(8)
for col in cols:
    col.image(tree_image, use_column_width=True)  # Adjust width as necessary

# Loop to update data
for i in range(st.session_state.track, st.session_state.track+8):
    relative_index = i - st.session_state.track
    cols2 = cols[relative_index].columns(2)
    cols2[0].metric(label="Ethylene", value=round(data.loc[i,"Ethylene"],2))
    cols2[0].metric(label="Temperature", value=round(data.loc[i,"Temperature"],2))
    cols2[1].metric(label="Humidity", value=round(data.loc[i,"Humidity"],2))
    cols2[1].metric(label="VOC", value=round(data.loc[i,"VOC"],2))
    #value = data[sensor.lower()]
    #label = data['label']
    color = "Not Healthy" if data.loc[i,"Label"] == 1 else "Healthy"
    if color == "Healthy":
        cols[relative_index].success("Healthy")
    else:
        cols[relative_index].error("Not Healthy")  
    ##.metric(label="label", value=f"{data["label"]:.2f}", delta="Positive" if data["label"] == 1 else "Negative", delta_color=color)

st.number_input(label="Tree Index", min_value=0, max_value=data_points-7, key="track")

