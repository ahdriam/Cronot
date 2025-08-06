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
    checkbox_values = [str(v).lower() in ["true", "1", "yes"] for v in values_array]

except Exception as e:
    st.error(f"שגיאה: {e}")

checkbox_states = []
for i in range(3):
    cb = st.checkbox(f"תיבה {i + 1}", value=checkbox_values[i], key=f"checkbox_{i}")
    checkbox_states.append(cb)




labels = ["לחצן 1", "לחצן 2", "לחצן 3"]

# Define colors
def get_color(state):
    return "#f28b82" if state else "#d3d3d3"  # light red if True, gray if False

# 3 columns for layout
columns = st.columns(3)

for i in range(3):
    color = get_color(values_array[i])

    with columns[i]:
        # Each button in its own form so Streamlit can detect individual clicks
        with st.form(key=f"form_{i}"):
            st.markdown(
                f"""
                <button type="submit" style="
                    background-color: {color};
                    color: black;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    width: 100%;
                    font-size: 16px;
                    cursor: pointer;"
                >{labels[i]}</button>
                """,
                unsafe_allow_html=True
            )
            submitted = st.form_submit_button(label="", use_container_width=True)
            if submitted:
                st.write(f"Button {i + 1} clicked")

if enable_refresh:
    time.sleep(refresh_interval)
    st.rerun()










