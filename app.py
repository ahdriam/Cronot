import streamlit as st
from st_supabase_connection import SupabaseConnection



options = ["ריח רע", "גרפיטי", "ריפוד קרוע", "לכלוך אחר בקרון חיצוני", "נזק בצבע הקרון"]
selected = st.multiselect(
    ":בחר תכונה",
    options,
    max_selections=1
)

# on = st.toggle("Turn ON feature")
# st.write("Feature is on:", on)



# Toggle widget
on = st.toggle("", key="my_toggle")  # Empty label

# Custom styled label
label_color = "#d1e7dd"  # light green background
label_text = "Turn ON feature"

# Place label and toggle on the same row using columns
col1, col2 = st.columns([0.1, 1])  # adjust ratio as needed

with col1:
    st.toggle("", key="my_toggle")  # toggle only

with col2:
    st.markdown(
        f"""
        <div style="
            background-color: {label_color};
            padding: 8px 12px;
            border-radius: 6px;
            display: inline-block;
            font-weight: 500;
        ">{label_text}</div>
        """,
        unsafe_allow_html=True
    )

# Optional: show current state
st.write("Feature is on:", st.session_state.my_toggle)





