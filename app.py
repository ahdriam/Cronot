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
    "נזק בצבע הקרון": "נזק בצבע הקרון",
    "כתמים קשים": "כתמים קשים"
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
  if st.button("סמן", key="btn_4"):
        values_array[4] = not values_array[4]
        toggle_value(4)
        
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

with col6:
  if st.button("סמן", key="btn_5"):
        values_array[5] = not values_array[5]
        toggle_value(5)
        
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

with col7:
    if st.button("סמן", key="btn_6"):
        values_array[6] = not values_array[6]
        toggle_value(6)

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

with col8:
    if st.button("סמן", key="btn_7"):
        values_array[7] = not values_array[7]
        toggle_value(7)

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

with col9:
    if st.button("סמן", key="btn_8"):
        values_array[8] = not values_array[8]
        toggle_value(8)

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

with col10:
    if st.button("סמן", key="btn_9"):
        values_array[9] = not values_array[9]
        toggle_value(9)

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
# Layout: 10 side-by-side columns
col11, col12, col13, col14, col15, col16, col17, col18, col19, col20 = st.columns(10)

with col11:
    if st.button("סמן", key="btn_10"):
        values_array[10] = not values_array[10]
        toggle_value(10)

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

with col12:
    if st.button("סמן", key="btn_11"):
        values_array[11] = not values_array[11]
        toggle_value(11)

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

with col13:
    if st.button("סמן", key="btn_12"):
        values_array[12] = not values_array[12]
        toggle_value(12)

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

with col14:
    if st.button("סמן", key="btn_13"):
        values_array[13] = not values_array[13]
        toggle_value(13)

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

with col15:
    if st.button("סמן", key="btn_14"):
        values_array[14] = not values_array[14]
        toggle_value(14)

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

with col16:
    if st.button("סמן", key="btn_15"):
        values_array[15] = not values_array[15]
        toggle_value(15)

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

with col17:
    if st.button("סמן", key="btn_16"):
        values_array[16] = not values_array[16]
        toggle_value(16)

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

with col18:
    if st.button("סמן", key="btn_17"):
        values_array[17] = not values_array[17]
        toggle_value(17)

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

with col19:
    if st.button("סמן", key="btn_18"):
        values_array[18] = not values_array[18]
        toggle_value(18)

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

with col20:
    if st.button("סמן", key="btn_19"):
        values_array[19] = not values_array[19]
        toggle_value(19)

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






















