import streamlit as st
import streamlit.components.v1 as components
from st_supabase_connection import SupabaseConnection
import time
from functools import partial
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
    rows = response.data
    values_array = [bool(row[column_name]) for row in rows]
except Exception as e:
    st.error(f"שגיאה: {e}")



labels = ["לחצן 1", "לחצן 2", "לחצן 3"]
row_ids = [1, 2, 3]

def toggle_value(row_id, current_state, column_name):
    new_value = not current_state
    conn.table("CRONOT").update({column_name: new_value}).eq("id", row_id).execute()
    st.success(f"שורה {row_id} עודכנה ל־{new_value}")




cols = st.columns(3)
for i in range(3):
    row_id = row_ids[i]
    label = labels[i]
    current_state = values_array[i]
    color = "#f28b82" if current_state else "#d3d3d3"

    with cols[i]:
        # HTML-styled button for color
        st.markdown(
            f"""
            <style>
            .my-button-{i} {{
                background-color: {color};
                color: black;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                width: 100%;
                font-size: 16px;
            }}
            </style>
            """, unsafe_allow_html=True)

        # Real button with function binding
        if st.button(label, key=f"btn_{i}", on_click=partial(toggle_value, row_id, current_state, column_name)):
            pass


if enable_refresh:
    time.sleep(refresh_interval)
    st.rerun()
















