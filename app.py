import streamlit as st
from st_supabase_connection import SupabaseConnection
import time

# --- Connect to Supabase ---
conn = st.connection("supabase", type=SupabaseConnection)

# --- UI control for auto-refresh ---
st.sidebar.subheader("Auto Refresh")
enable_refresh = st.sidebar.toggle("הפעל רענון אוטומטי", value=False)
refresh_interval = 2  # seconds

# --- Column name mapping ---
display_to_column = {
    "ריח רע": "ריח רע",
    "גרפיטי": "גרפיטי",
    "ריפוד קרוע": "ריפוד קרוע",
    "לכלוך אחר בקרון חיצוני": "לכלוך אחר בקרון חיצוני",
    "נזק בצבע הקרון": "נזק בצבע הקרון"
}

# --- Column selection ---
selected_display = st.selectbox(":בחר תכונה", list(display_to_column.keys()))
column_name = display_to_column[selected_display]

# --- Fetch current values from DB ---
try:
    response = conn.table("CRONOT").select(f'"{column_name}"').limit(3).execute()
    rows = response.data
    checkbox_values = [str(row[column_name]).lower() in ['true', '1', 'yes'] for row in rows]
except Exception as e:
    st.error(f"שגיאה בטעינת הנתונים: {e}")
    checkbox_values = [False, False, False]  # fallback if DB fails

# --- Update checkboxes in session_state ---
for i in range(3):
    key = f"cb_{i}"
    # Only update session state from DB if refreshing
    if enable_refresh or key not in st.session_state:
        st.session_state[key] = checkbox_values[i]

# --- Show checkboxes and track user changes ---
st.subheader("מצב תיבות סימון")
user_changed = False
checkbox_states = []

for i in range(3):
    key = f"cb_{i}"
    cb = st.checkbox(f"תיבה {i + 1}", value=st.session_state[key], key=key)
    checkbox_states.append(cb)
    if cb != checkbox_values[i]:  # If changed compared to DB
        user_changed = True

# --- Update DB if user made changes ---
if user_changed:
    try:
        for i in range(3):
            conn.table("CRONOT").update({column_name: checkbox_states[i]}).eq("id", i + 1).execute()
        # Re-fetch from DB to sync everything
        response = conn.table("CRONOT").select(f'"{column_name}"').limit(3).execute()
        rows = response.data
        checkbox_values = [str(row[column_name]).lower() in ['true', '1', 'yes'] for row in rows]
        for i in range(3):
            st.session_state[f"cb_{i}"] = checkbox_values[i]
        st.success("✅ הנתונים עודכנו בהצלחה")
    except Exception as e:
        st.error(f"שגיאה בעת עדכון הנתונים: {e}")

# --- Auto-refresh ---
if enable_refresh:
    time.sleep(refresh_interval)
    st.rerun()
