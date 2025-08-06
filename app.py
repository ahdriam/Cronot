import streamlit as st
from st_supabase_connection import SupabaseConnection
import time

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
    response = conn.table("CRONOT").select(f'id, "{column_name}"').order('id').execute()
    values_array = [row[column_name] for row in response.data]
except Exception as e:
    st.error(f"שגיאה: {e}")
    values_array = []

# --- Toggle function ---
def toggle_value():
    if not values_array:
        st.error("אין נתונים לעדכון.")
        return
    new_value = not values_array[0]
    conn.table("CRONOT").update({column_name: new_value}).eq("id", 1).execute()
    st.success(f"תא עודכן ל- {new_value}")

# --- Button ---
if values_array:
    if st.button("Toggle"):
        toggle_value()
        st.rerun()
else:
    st.warning("לא הוחזרו נתונים מהמסד.")

# --- Auto-refresh ---
if enable_refresh:
    time.sleep(refresh_interval)
    st.rerun()

