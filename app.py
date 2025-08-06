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
    response = conn.table("CRONOT").select(f'"{column_name}"').execute()
    # Save values to Python array
    values_array = [row[column_name] for row in response.data]
    checkbox_values = [str(v).lower() in ["true", "1", "yes"] for v in values_array]

    # Show the array
    st.write("📦 מערך נתונים:")
    st.write(values_array)

except Exception as e:
    st.error(f"שגיאה: {e}")

checkbox_states = []
for i in range(3):
    cb = st.checkbox(f"תיבה {i + 1}", value=checkbox_values[i], key=f"checkbox_{i}")
    checkbox_states.append(cb)


if enable_refresh:
    time.sleep(refresh_interval)
    st.rerun()





