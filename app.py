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

selected_display = st.selectbox(":בחר תכונה", list(display_to_column.keys()))
column_name = display_to_column[selected_display]

response = conn.table("CRONOT").select(column_name).execute()
column_data = [row[column_name] for row in response.data]


























