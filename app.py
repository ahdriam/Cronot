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
    response = conn.table("CRONOT").select(f'"{column_name}"').limit(3).execute()
    rows = response.data
    checkbox_values = [str(row[column_name]).lower() in ['true', '1', 'yes'] for row in rows]
except Exception as e:
    st.error(f"שגיאה בטעינת הנתונים: {e}")
    checkbox_values = [False, False, False]  # fallback if DB fails

# ---- Show checkboxes ----
st.subheader("מצב תיבות סימון")
checkbox_states = []
for i in range(3):
    key = f"cb_{i}"
    if enable_refresh and st.session_state.get(key) != checkbox_values[i]:
        st.session_state[key] = checkbox_values[i]
    cb = st.checkbox(f"תיבה {i + 1}", value=checkbox_values[i], key=key)
    checkbox_states.append(cb)
    
# ---- If any checkbox was pressed, update the DB ----
if any(st.session_state[f"cb_{i}"] != checkbox_values[i] for i in range(3)):
    try:
        for i in range(3):
            # Update row i in column_name to match checkbox i
            conn.table("CRONOT").update({column_name: checkbox_states[i]}).eq("id", i+1).execute()
    except Exception as e:
        st.error(f"שגיאה בעת עדכון הנתונים: {e}")


if enable_refresh:
    # Wait a bit before rerunning
    time.sleep(refresh_interval)
    st.rerun()











