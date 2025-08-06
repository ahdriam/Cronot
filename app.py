import streamlit as st
from st_supabase_connection import SupabaseConnection
import time

conn = st.connection("supabase", type=SupabaseConnection)

# --- Auto-refresh control ---
st.sidebar.subheader("Auto Refresh")
enable_refresh = st.sidebar.toggle("הפעל רענון אוטומטי", value=False)
refresh_interval = 1  # seconds

# --- Display options ---
display_to_column = {
    "ריח רע": "ריח רע",
    "גרפיטי": "גרפיטי",
    "ריפוד קרוע": "ריפוד קרוע",
    "לכלוך אחר בקרון חיצוני": "לכלוך אחר בקרון חיצוני",
    "נזק בצבע הקרון": "נזק בצבע הקרון"
}

selected_display = st.selectbox(":בחר תכונה", list(display_to_column.keys()))
column_name = display_to_column[selected_display]

# --- Fetch current values ---
try:
    response = conn.table("CRONOT").select(f'"מספר קרון", "{column_name}"').order('מספר קרון').execute()
    values_array = [row[column_name] for row in response.data]
except Exception as e:
    st.error(f"שגיאה: {e}")
    values_array = []

# --- Toggle function ---
def toggle_value(i):
    if not values_array:
        st.error("אין נתונים לעדכון.")
        return
    new_value = not values_array[i]
    conn.table("CRONOT").update({column_name: new_value}).eq("id", i+1).execute()
    

# Layout: 6 side-by-side columns
col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)

with col1:
    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[0] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1001
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("סמן", key="btn_0"):
        toggle_value(0)

with col2:
    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[1] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1002
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("סמן", key="btn_1"):
        toggle_value(1)

with col3:
    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[2] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1003
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("סמן", key="btn_2"):
        toggle_value(2)

with col4:
    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[3] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1004
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("סמן", key="btn_3"):
        toggle_value(3)

with col5:
    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[4] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1005
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("סמן", key="btn_4"):
        toggle_value(4)

with col6:
    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[5] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1006
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("סמן", key="btn_5"):
        toggle_value(5)

with col7:
    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[6] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1007
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("סמן", key="btn_6"):
        toggle_value(6)

with col8:
    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[7] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1008
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("סמן", key="btn_7"):
        toggle_value(7)

with col9:
    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[8] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1009
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("סמן", key="btn_8"):
        toggle_value(8)

with col10:
    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[9] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1010
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("סמן", key="btn_9"):
        toggle_value(9)



# --- Auto-refresh ---
if enable_refresh:
    time.sleep(refresh_interval)
    st.rerun()









