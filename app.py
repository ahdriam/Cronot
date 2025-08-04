import streamlit as st
from st_supabase_connection import SupabaseConnection



options = ["ריח רע", "גרפיטי", "ריפוד קרוע", "לכלוך אחר בקרון חיצוני", "נזק בצבע הקרון"]
selected = st.multiselect(
    ":בחר תכונה",
    options,
    max_selections=1
)

import streamlit as st

# Step 1: Create a toggle
on = st.toggle("Toggle feature")

# Step 2: Determine the background color
bg_color = "#dc3545" if on else "#6c757d"  # red if True, grey if False
label_text = "Feature is ON" if on else "Feature is OFF"

# Step 3: Show the rectangle with dynamic color
st.markdown(
    f"""
    <div style="
        background-color: {bg_color};
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        display: inline-block;
        font-size: 16px;
        font-weight: bold;
        margin-top: 10px;
    ">
        {label_text}
    </div>
    """,
    unsafe_allow_html=True
)











