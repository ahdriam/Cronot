import streamlit as st
import streamlit.components.v1 as components
from st_supabase_connection import SupabaseConnection
import time
conn = st.connection("supabase", type=SupabaseConnection)
# --- UI control for auto-refresh ---
st.sidebar.subheader("Auto Refresh")
enable_refresh = st.sidebar.toggle("הפעל רענון אוטומטי", value=False)
refresh_interval = 2  # seconds

display_to_column = {
    "ריח רע": "ריח רע",
    "גרפיטי": "גרפיטי",
    "ריפוד קרוע": "ריפוד קרוע",
    "לכלוך אחר בקרון חיצוני": "לכלוך אחר בקרון חיצוני",
    "נזק בצבע הקרון": "נזק בצבע הקרון"
}

# Step 3: Let user select
selected_display = st.selectbox(":בחר תכונה", list(display_to_column.keys()))

# Step 4: Get the real column name
column_name = display_to_column[selected_display]


try:
    response = conn.table("CRONOT").select(f'id, "{column_name}"').order('id').execute()
    values_array = [row[column_name] for row in response.data]

except Exception as e:
    st.error(f"שגיאה: {e}")

def toggle_value(row_id, current_state, column_name):
    # new_value = not current_state
    # conn.table("CRONOT").update({column_name: new_value}).eq("id", row_id).execute()
    st.write("Button was clicked! Toggling value...")

if st.button("Toggle"):
    toggle_value()





if enable_refresh:
    time.sleep(refresh_interval)
    st.rerun()
