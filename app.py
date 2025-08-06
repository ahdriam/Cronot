import streamlit as st
from st_supabase_connection import SupabaseConnection
import time

# Connect to Supabase
conn = st.connection("supabase", type=SupabaseConnection)

# Auto-refresh control
st.sidebar.subheader("Auto Refresh")
enable_refresh = st.sidebar.toggle("הפעל רענון אוטומטי", value=False)
refresh_interval = 2

# Column selection
display_to_column = {
    "ריח רע": "ריח רע",
    "גרפיטי": "גרפיטי",
    "ריפוד קרוע": "ריפוד קרוע",
    "לכלוך אחר בקרון חיצוני": "לכלוך אחר בקרון חיצוני",
    "נזק בצבע הקרון": "נזק בצבע הקרון"
}

selected_display = st.selectbox(":בחר תכונה", list(display_to_column.keys()))
column_name = display_to_column[selected_display]

# Load values
try:
    response = conn.table("CRONOT").select(f'id, "{column_name}"').order('id').execute()
    rows = response.data
    values = [str(row[column_name]).lower() in ['true', '1', 'yes'] for row in rows]
    ids = [row["id"] for row in rows]
except Exception as e:
    st.error(f"שגיאה בטעינת הנתונים: {e}")
    rows, values, ids = [], [], []

# Display colored labels as buttons
st.subheader("שינוי מצב בלחיצה")

for i, val in enumerate(values):
    # Choose color based on value
    color = "#d9534f" if not val else "#5cb85c"  # red / green
    label = f"תיבה {i + 1}"

    button_html = f"""
    <form action="" method="post">
        <button name="toggle" type="submit" style="
            background-color: {color};
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            width: 100%;
            font-size: 16px;
        ">{label}</button>
        <input type="hidden" name="row_index" value="{i}">
    </form>
    """
    st.markdown(button_html, unsafe_allow_html=True)

    # Detect button press
    if f"toggle_{i}" not in st.session_state:
        st.session_state[f"toggle_{i}"] = False

    if st.form_submit_button(f"toggle_{i}"):
        new_value = not val
        try:
            conn.table("CRONOT").update({column_name: new_value}).eq("id", ids[i]).execute()
            st.rerun()
        except Exception as e:
            st.error(f"שגיאה בעדכון תיבה {i+1}: {e}")

# Optional: auto-refresh
if enable_refresh:
    time.sleep(refresh_interval)
    st.rerun()
