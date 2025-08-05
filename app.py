import streamlit as st
import streamlit.components.v1 as components
from st_supabase_connection import SupabaseConnection



options = ["ריח רע", "גרפיטי", "ריפוד קרוע", "לכלוך אחר בקרון חיצוני", "נזק בצבע הקרון"]
selected_option = st.selectbox(":בחר תכונה", options)
st.write("You selected:", selected_option)

if selected_option:
    try:
        response = supabase.table("CRONOT").select(selected_option).execute()
        column_data = [row[selected_option] for row in response.data]

        st.write(f"נתונים לעמודה '{selected_option}':")
        st.write(column_data)

    except Exception as e:
        st.error(f"שגיאה: לא ניתן לשלוף את העמודה '{selected_option}' — {str(e)}")






















