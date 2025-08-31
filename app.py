import streamlit as st
from st_supabase_connection import SupabaseConnection
import time
st.set_page_config(page_title="My App", layout="wide")
conn = st.connection("supabase", type=SupabaseConnection)

# --- Auto-refresh control ---
st.sidebar.subheader("Auto Refresh")
enable_refresh = st.sidebar.toggle("הפעל רענון אוטומטי", value=False)
refresh_interval = 2  # seconds

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
    new_value = values_array[i]
    conn.table("CRONOT").update({column_name: new_value}).eq("id", i+1).execute()
    

# Layout: 10 side-by-side columns
col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)

with col1:
    if st.button("סמן", key="btn_0"):
        values_array[0] = not values_array[0]
        toggle_value(0)
        
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
    
        

with col2:
    if st.button("סמן", key="btn_1"):
        values_array[1] = not values_array[1]
        toggle_value(1)
        
        
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
    
        

with col3:
    if st.button("סמן", key="btn_2"):
        values_array[2] = not values_array[2]
        toggle_value(2)
        
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
    

with col4:
     if st.button("סמן", key="btn_3"):
        values_array[3] = not values_array[3]
        toggle_value(3)
        
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

# Layout: 10 side-by-side columns
col11, col12, col13, col14, col15, col16, col17, col18, col19, col20 = st.columns(10)

with col11:
    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[10] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1011
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("סמן", key="btn_10"):
        toggle_value(10)

with col12:
    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[11] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1012
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("סמן", key="btn_11"):
        toggle_value(11)

with col13:
    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[12] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1013
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("סמן", key="btn_12"):
        toggle_value(12)

with col14:
    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[13] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1014
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("סמן", key="btn_13"):
        toggle_value(13)

with col15:
    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[14] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1015
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("סמן", key="btn_14"):
        toggle_value(14)

with col16:
    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[15] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1016
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("סמן", key="btn_15"):
        toggle_value(15)

with col17:
    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[16] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1017
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("סמן", key="btn_16"):
        toggle_value(16)

with col18:
    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[17] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1018
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("סמן", key="btn_17"):
        toggle_value(17)

with col19:
    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[18] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1019
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("סמן", key="btn_18"):
        toggle_value(18)

with col20:
    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[19] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1020
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("סמן", key="btn_19"):
        toggle_value(19)




# --- Auto-refresh ---
if enable_refresh:
    time.sleep(refresh_interval)
    st.rerun()

















