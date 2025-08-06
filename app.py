import streamlit as st
from st_supabase_connection import SupabaseConnection
from functools import partial
import time

conn = st.connection("supabase", type=SupabaseConnection)

# Auto-refresh toggle
st.sidebar.subheader("Auto Refresh")
enable_refresh = st.sidebar.toggle("הפעל רענון אוטומטי", value=False)
refresh_interval = 2  # seconds

# Hebrew column names
display_to_column = {
    "ריח רע": "ריח רע",
    "גרפיטי": "גרפיטי",
    "ריפוד קרוע": "ריפוד קרוע",
    "לכלוך אחר בקרון חיצוני": "לכלוך אחר בקרון חיצוני",
    "נזק בצבע הקרון": "נזק בצבע הקרון"
}

# Select column
selected_display = st.selectbox(":בחר תכונה", list(display_to_column.keys()))
column_name = display_to_column[selected_display]

# Get values from DB
try:
    response = conn.table("CRONOT").select(f'id, "{column_name}"').order('id').limit(3).execute()
    rows = response.data
    values_array = [row[column_name] for row in rows]
except Exception as e:
    st.error(f"שגיאה: {e}")
    values_array = [False, False, False]  # fallback

# Toggle function
def toggle_value(row_id, current_state, column_name):
    new_value = not current_state
    conn.table("CRONOT").update({column_name: new_value}).eq("id", row_id).execute()
    st.rerun()  # Refresh view immediately after update

# Display buttons
st.write("### כפתורים:")

cols = st.columns(3)
for i in range(3):
    row_id = i + 1
    state = values_array[i]
    color = "#f28b82" if state else "#d3d3d3"

    with cols[i]:
        st.markdown(
            f"""
            <div style="background-color:{color};padding:10px;border-radius:5px;text-align:center;">
            <b>שורה {row_id}</b>
            </div>
            """, unsafe_allow_html=True
        )
        st.button(
            f"לחצן {row_id}",
            key=f"btn_{row_id}",
            on_click=partial(toggle_value, row_id, state, column_name)
        )

# Auto-refresh
if enable_refresh:
    time.sleep(refresh_interval)
    st.rerun()
