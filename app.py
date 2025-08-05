import streamlit as st
import streamlit.components.v1 as components
from st_supabase_connection import SupabaseConnection



options = ["ריח רע", "גרפיטי", "ריפוד קרוע", "לכלוך אחר בקרון חיצוני", "נזק בצבע הקרון"]
selected = st.multiselect(
    ":בחר תכונה",
    options,
    max_selections=1
)
selected_option = selected[0] if selected else None
st.write("You selected:", selected_option)



















