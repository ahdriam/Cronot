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
    rows = response.data
    values_array = [bool(row[column_name]) for row in rows]
except Exception as e:
    st.error(f"שגיאה: {e}")

checkbox_states = []
for i in range(3):
    cb = st.checkbox(f"תיבה {i + 1}", value=checkbox_values[i], key=f"checkbox_{i}")
    checkbox_states.append(cb)



labels = ["לחצן 1", "לחצן 2", "לחצן 3"]

# Use columns for layout
columns = st.columns(3)

for i in range(3):
    row_id = row_ids[i]
    label = labels[i]
    state = values_array[i]
    color = "#f28b82" if state else "#d3d3d3"

    with columns[i]:
        # Form to wrap each button for individual detection
        with st.form(key=f"form_{i}"):
            submitted = st.form_submit_button(label=label, use_container_width=True)
            if submitted:
                new_value = not state  # Toggle the boolean
                conn.table("CRONOT").update({column_name: new_value}).eq("id", row_id).execute()
                st.success(f"שורה {row_id} עודכנה ל־{new_value}")

        # Render background color bar below button
        st.markdown(
            f"""
            <div style="
                margin-top: -50px;
                background-color: {color};
                height: 40px;
                border-radius: 5px;
                z-index: -1;
            "></div>
            """,
            unsafe_allow_html=True
        )


if enable_refresh:
    time.sleep(refresh_interval)
    st.rerun()













