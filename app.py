import streamlit as st
import streamlit.components.v1 as components
from st_supabase_connection import SupabaseConnection
conn = st.connection("supabase", type=SupabaseConnection)

display_to_column = {
    "ריח רע": "ריח רע",
    "גרפיטי": "גרפיטי",
    "ריפוד קרוע": "ריפוד קרוע",
    "לכלוך אחר בקרון חיצוני": "לכלוך אחר בקרון חיצוני",
    "נזק בצבע הקרון": "נזק בצבע הקרון"
}

selected_option = st.selectbox(":בחר תכונה", options)

if selected_option:
    try:
        # Use the Supabase client syntax, not raw SQL
        response = conn.table("CRONOT").select(selected_option).execute()
        column_data = [row[selected_option] for row in response.data]

        st.write(f"נתונים לעמודה '{selected_option}':")
        st.write(column_data)

    except Exception as e:
        st.error(f"שגיאה: {e}")


























