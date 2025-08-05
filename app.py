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
    response = conn.table("CRONOT").select(f'id, "{column_name}"').order('id', asc=True).execute()
    rows = response.data  # List of dicts like [{'id': 0, 'column_name': True}, ...]
    checkbox_values = [str(row[column_name]).lower() in ['true', '1', 'yes'] for row in rows]
    row_ids = [row["id"] for row in rows]
    for i in range(3):
        new_value = st.checkbox(f"תיבה {i + 1}", value=checkbox_values[i], key=f"checkbox_{i}")
        if new_value != checkbox_values[i]:
            update_result = conn.table("CRONOT").update({column_name: new_value}).eq("id", row_ids[i]).execute()
            st.success(f"עודכן בהצלחה: שורה {row_ids[i]} ← {column_name} = {new_value}")


except Exception as e:
    st.error(f"שגיאה: {e}")    
    

if enable_refresh:
    # Wait a bit before rerunning
    time.sleep(refresh_interval)
    st.rerun()





