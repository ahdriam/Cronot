import streamlit as st
import streamlit.components.v1 as components
from st_supabase_connection import SupabaseConnection



options = ["ריח רע", "גרפיטי", "ריפוד קרוע", "לכלוך אחר בקרון חיצוני", "נזק בצבע הקרון"]

selected_option = st.selectbox(":בחר תכונה", options)

st.write("You selected:", selected_option)





















