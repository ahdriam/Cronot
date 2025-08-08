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
    response = conn.table("CRONOT").select(f'id, "מספר קרון", "{column_name}"').order('מספר קרון').execute()
    rows = response.data
    values_array = [row[column_name] for row in rows]
except Exception as e:
    st.error(f"שגיאה: {e}")
    values_array = []

# --- Toggle function ---
def toggle_value(i):
    if not values_array:
        st.error("אין נתונים לעדכון.")
        return
    new_val = not values_array[i]
    values_array[i] = new_val  # Update local value for instant UI feedback
    conn.table("CRONOT").update({column_name: new_val}).eq("id", i+1).execute()

# --- Buttons Layout ---
col1, col2 = st.columns(2)

# Button 1001
with col1:
    if st.button("קרון 1001", key="train_1001"):
        toggle_value(0)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[0] else '#d3d3d3'};
            color: black;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 8px;
            text-align: center;
            width: 100%;
        ">
            מצב נוכחי
        </div>
        """,
        unsafe_allow_html=True
    )

# Button 1002
with col2:
    if st.button("קרון 1002", key="train_1002"):
        toggle_value(1)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[1] else '#d3d3d3'};
            color: black;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 8px;
            text-align: center;
            width: 100%;
        ">
            מצב נוכחי
        </div>
        """,
        unsafe_allow_html=True
    )

# --- Auto-refresh ---
if enable_refresh:
    time.sleep(refresh_interval)
    st.rerun()
