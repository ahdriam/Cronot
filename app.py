import streamlit as st
from st_supabase_connection import SupabaseConnection
import time
st.set_page_config(page_title="My App", layout="wide")
conn = st.connection("supabase", type=SupabaseConnection)

# --- Auto-refresh control ---
st.sidebar.subheader("Auto Refresh")
enable_refresh = st.sidebar.toggle("הפעל רענון אוטומטי", value=False)
refresh_interval = 2  # seconds

# --- Display options ---
display_to_column = {
    "ריח רע": "ריח רע",
    "גרפיטי": "גרפיטי",
    "ריפוד קרוע": "ריפוד קרוע",
    "לכלוך אחר בקרון חיצוני": "לכלוך אחר בקרון חיצוני",
    "נזק בצבע הקרון": "נזק בצבע הקרון"
}

selected_display = st.selectbox(":בחר תכונה", list(display_to_column.keys()))
column_name = display_to_column[selected_display]

# --- Fetch current values ---
try:
    response = conn.table("CRONOT").select(f'"מספר קרון", "{column_name}"').order('מספר קרון').execute()
    values_array = [row[column_name] for row in response.data]
except Exception as e:
    st.error(f"שגיאה: {e}")
    values_array = []

# --- Toggle function ---
def toggle_value(i):
    if not values_array:
        st.error("אין נתונים לעדכון.")
        return
    conn.table("CRONOT").update({column_name: values_array[i]}).eq("id", i+1).execute()


#---button 1001---
color1 = '#f28b82' if values_array[0] else '#d3d3d3'
custom_css = f"""
<style>
div[data-testid="stButton"] button {{
    background-color: {color1};
    color: black;
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold;
    border-radius: 8px;
    width: 100%;
}}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
if st.button("קרון 1001", key="train_1001"):
    values_array[0] = not values_array[0]
    toggle_value(0)

#---button 1002---
color2 = '#f28b82' if values_array[1] else '#d3d3d3'
custom_css = f"""
<style>
div[data-testid="stButton"] button {{
    background-color: {color2};
    color: black;
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold;
    border-radius: 8px;
    width: 100%;
}}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
if st.button("קרון 1002", key="train_1002"):
    values_array[1] = not values_array[1]
    toggle_value(1)





# --- Auto-refresh ---
if enable_refresh:
    time.sleep(refresh_interval)
    st.rerun()

















