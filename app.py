import streamlit as st
import streamlit.components.v1 as components
from st_supabase_connection import SupabaseConnection
conn = st.connection("supabase", type=SupabaseConnection)


options = ["ריח רע", "גרפיטי", "ריפוד קרוע", "לכלוך אחר בקרון חיצוני", "נזק בצבע הקרון"]
selected_option = st.selectbox(":בחר תכונה", options)
st.write("You selected:", selected_option)

if selected_option:
    try:
        # Use double quotes around Hebrew column names
        sql = f'SELECT "{selected_option}" FROM CRONOT'
        rows = conn.execute(sql)

        # Extract values from the result
        column_data = [row[selected_option] for row in rows]

        st.write(f"נתונים לעמודה '{selected_option}':")
        st.write(column_data)

    except Exception as e:
        st.error(f"שגיאה: לא ניתן לשלוף את העמודה '{selected_option}' — {str(e)}")























