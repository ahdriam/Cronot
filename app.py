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


#  Layout: 10 side-by-side columns
col21, col22, col23, col24, col25, col26, col27, col28, col29, col30 = st.columns(10)


with col21:
    if st.button("סמן", key="btn_20"):
        values_array[20] = not values_array[20]
        toggle_value(20)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[20] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1021
        </div>
        """,
        unsafe_allow_html=True
    )

with col22:
    if st.button("סמן", key="btn_21"):
        values_array[21] = not values_array[21]
        toggle_value(21)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[21] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1022
        </div>
        """,
        unsafe_allow_html=True
    )

with col23:
    if st.button("סמן", key="btn_22"):
        values_array[22] = not values_array[22]
        toggle_value(22)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[22] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1023
        </div>
        """,
        unsafe_allow_html=True
    )

with col24:
    if st.button("סמן", key="btn_23"):
        values_array[23] = not values_array[23]
        toggle_value(23)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[23] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1024
        </div>
        """,
        unsafe_allow_html=True
    )

with col25:
    if st.button("סמן", key="btn_24"):
        values_array[24] = not values_array[24]
        toggle_value(24)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[24] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1025
        </div>
        """,
        unsafe_allow_html=True
    )

with col26:
    if st.button("סמן", key="btn_25"):
        values_array[25] = not values_array[25]
        toggle_value(25)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[25] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1026
        </div>
        """,
        unsafe_allow_html=True
    )

with col27:
    if st.button("סמן", key="btn_26"):
        values_array[26] = not values_array[26]
        toggle_value(26)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[26] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1027
        </div>
        """,
        unsafe_allow_html=True
    )

with col28:
    if st.button("סמן", key="btn_27"):
        values_array[27] = not values_array[27]
        toggle_value(27)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[27] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1028
        </div>
        """,
        unsafe_allow_html=True
    )

with col29:
    if st.button("סמן", key="btn_28"):
        values_array[28] = not values_array[28]
        toggle_value(28)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[28] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1029
        </div>
        """,
        unsafe_allow_html=True
    )

with col30:
    if st.button("סמן", key="btn_29"):
        values_array[29] = not values_array[29]
        toggle_value(29)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[29] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1030
        </div>
        """,
        unsafe_allow_html=True
    )

col31, col32, col33, col34, col35, col36, col37, col38, col39, col40 = st.columns(10)

with col31:
    if st.button("סמן", key="btn_30"):
        values_array[30] = not values_array[30]
        toggle_value(30)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[30] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1031
        </div>
        """,
        unsafe_allow_html=True
    )

with col32:
    if st.button("סמן", key="btn_31"):
        values_array[31] = not values_array[31]
        toggle_value(31)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[31] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1032
        </div>
        """,
        unsafe_allow_html=True
    )

with col33:
    if st.button("סמן", key="btn_32"):
        values_array[32] = not values_array[32]
        toggle_value(32)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[32] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1033
        </div>
        """,
        unsafe_allow_html=True
    )

with col34:
    if st.button("סמן", key="btn_33"):
        values_array[33] = not values_array[33]
        toggle_value(33)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[33] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1034
        </div>
        """,
        unsafe_allow_html=True
    )

with col35:
    if st.button("סמן", key="btn_34"):
        values_array[34] = not values_array[34]
        toggle_value(34)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[34] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1035
        </div>
        """,
        unsafe_allow_html=True
    )

with col36:
    if st.button("סמן", key="btn_35"):
        values_array[35] = not values_array[35]
        toggle_value(35)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[35] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1036
        </div>
        """,
        unsafe_allow_html=True
    )

with col37:
    if st.button("סמן", key="btn_36"):
        values_array[36] = not values_array[36]
        toggle_value(36)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[36] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1037
        </div>
        """,
        unsafe_allow_html=True
    )

with col38:
    if st.button("סמן", key="btn_37"):
        values_array[37] = not values_array[37]
        toggle_value(37)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[37] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1038
        </div>
        """,
        unsafe_allow_html=True
    )

with col39:
    if st.button("סמן", key="btn_38"):
        values_array[38] = not values_array[38]
        toggle_value(38)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[38] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1039
        </div>
        """,
        unsafe_allow_html=True
    )

with col40:
    if st.button("סמן", key="btn_39"):
        values_array[39] = not values_array[39]
        toggle_value(39)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[39] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1040
        </div>
        """,
        unsafe_allow_html=True
    )

col41, col42, col43, col44, col45, col46, col47, col48, col49, col50 = st.columns(10)

with col41:
    if st.button("סמן", key="btn_40"):
        values_array[40] = not values_array[40]
        toggle_value(40)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[40] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1041
        </div>
        """,
        unsafe_allow_html=True
    )

with col42:
    if st.button("סמן", key="btn_41"):
        values_array[41] = not values_array[41]
        toggle_value(41)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[41] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1042
        </div>
        """,
        unsafe_allow_html=True
    )

with col43:
    if st.button("סמן", key="btn_42"):
        values_array[42] = not values_array[42]
        toggle_value(42)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[42] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1043
        </div>
        """,
        unsafe_allow_html=True
    )

with col44:
    if st.button("סמן", key="btn_43"):
        values_array[43] = not values_array[43]
        toggle_value(43)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[43] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1044
        </div>
        """,
        unsafe_allow_html=True
    )

with col45:
    if st.button("סמן", key="btn_44"):
        values_array[44] = not values_array[44]
        toggle_value(44)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[44] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1045
        </div>
        """,
        unsafe_allow_html=True
    )

with col46:
    if st.button("סמן", key="btn_45"):
        values_array[45] = not values_array[45]
        toggle_value(45)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[45] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1046
        </div>
        """,
        unsafe_allow_html=True
    )

with col47:
    if st.button("סמן", key="btn_46"):
        values_array[46] = not values_array[46]
        toggle_value(46)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[46] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1047
        </div>
        """,
        unsafe_allow_html=True
    )

with col48:
    if st.button("סמן", key="btn_47"):
        values_array[47] = not values_array[47]
        toggle_value(47)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[47] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1048
        </div>
        """,
        unsafe_allow_html=True
    )

with col49:
    if st.button("סמן", key="btn_48"):
        values_array[48] = not values_array[48]
        toggle_value(48)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[48] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1049
        </div>
        """,
        unsafe_allow_html=True
    )

with col50:
    if st.button("סמן", key="btn_49"):
        values_array[49] = not values_array[49]
        toggle_value(49)

    st.markdown(
        f"""
        <div style="
            background-color: {'#f28b82' if values_array[49] else '#d3d3d3'};
            color: black;
            padding: 10px 8px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 4px;
        ">
            קרון 1050
        </div>
        """,
        unsafe_allow_html=True
    )


col51, col52, col53, col54, col55, col56, col57, col58, col59, col60 = st.columns(10)

col61, col62, col63, col64, col65, col66, col67, col68, col69, col70 = st.columns(10)

col71, col72, col73, col74, col75, col76, col77, col78, col79, col80 = st.columns(10)

col81, col82, col83, col84, col85, col86, col87, col88, col89, col90 = st.columns(10)



























