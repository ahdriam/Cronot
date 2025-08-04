import streamlit as st
from st_supabase_connection import SupabaseConnection



options = ["ריח רע", "גרפיטי", "ריפוד קרוע", "לכלוך אחר בקרון חיצוני", "נזק בצבע הקרון"]
selected = st.multiselect(
    ":בחר תכונה",
    options,
    max_selections=1
)

on = st.toggle("Turn ON feature")
st.write("Feature is on:", on)

st.markdown(
    """
    <div style="
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        display: inline-block;
        font-size: 16px;
        font-weight: bold;
    ">
        This is a rectangle
    </div>
    """,
    unsafe_allow_html=True
)










