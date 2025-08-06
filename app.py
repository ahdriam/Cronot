import streamlit as st
from st_supabase_connection import SupabaseConnection
import time

# --- Connect to Supabase ---
conn = st.connection("supabase", type=SupabaseConnection)

# --- UI control for auto-refresh ---
st.sidebar.subheader("Auto Refresh")
enable_refresh = st.sidebar.toggle("הפעל רענון אוטומטי", value=False)
refresh_interval = 5  # seconds

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

# --- Track if user toggled anything ---
if "user_updated" not in st.session_state:
    st.session_state.user_updated = False

# --- Fetch current values from DB ---
try:
    response = conn.table("CRONOT").select(f'"{column_name}"').limit(3).execute()
    rows = response.data
    checkbox_values = [str(row[column_name]).lower() in ['true', '1', 'yes'] for row in rows]
except Exception as e:
    st.error(f"שגיאה בטעינת הנתונים: {e}")
    checkbox_values = [False, False, False]

# --- Sync session_state only if refreshing or first load ---
for i in range(3):
    key = f"cb_{i}"
    if key not in st.session_state or (enable_refresh and not st.session_state.user_updated):
        st.session_state[key] = checkbox_values[i]

# --- Show checkboxes and track changes ---
st.subheader("מצב תיבות סימון")
checkbox_states = []
user_changed = False

for i in range(3):
    key = f"cb_{i}"
    cb = st.checkbox(f"תיבה {i + 1}", value=st.session_state[key], key=key)
    checkbox_states.append(cb)
    if cb != checkbox_values[i]:
        user_changed = True

# --- Update DB if changed ---
if user_changed:
    st.session_state.user_updated = True
    try:
        for i in range(3):
            conn.table("CRONOT").update({column_name: checkbox_states[i]}).eq("id", i + 1).execute()
        st.success("✅ הנתונים עודכנו בהצלחה")
    except Exception as e:
        st.error(f"שגיאה בעת עדכון הנתונים: {e}")
else:
    st.session_state.user_updated = False

# --- Auto-refresh ---
if enable_refresh and not st.session_state.user_updated:
    time.sleep(refresh_interval)
    st.rerun()

