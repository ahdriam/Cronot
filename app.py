import streamlit as st
import streamlit.components.v1 as components
from st_supabase_connection import SupabaseConnection
conn = st.connection("supabase", type=SupabaseConnection)

# options = ["ריח רע", "גרפיטי", "ריפוד קרוע", "לכלוך אחר בקרון חיצוני", "נזק בצבע הקרון"]

# selected_option = st.selectbox(":בחר תכונה", options)

# if selected_option:
#     try:
#         # Use the Supabase client syntax, not raw SQL
#         response = conn.table("CRONOT").select(f'"{column_name}"').execute()
#          column_data = [row[column_name] for row in response.data]

#         st.write(f"נתונים לעמודה '{selected_option}':")
#         st.write(column_data)

#     except Exception as e:
#         st.error(f"שגיאה: {e}")

display_to_column = {
    "ריח רע": "ריח רע",
    "גרפיטי": "גרפיטי",
    "ריפוד קרוע": "ריפוד קרוע",
    "לכלוך אחר בקרון חיצוני": "לכלוך אחר בקרון חיצוני",
    "נזק בצבע הקרון": "נזק בצבע הקרון"
}

# Step 3: Let user select
selected_display = st.selectbox(":בחר תכונה", list(display_to_column.keys()))

# Step 4: Get the real column name
column_name = display_to_column[selected_display]

# Step 5: Query Supabase
try:
    response = conn.table("CRONOT").select(f'"{column_name}"').execute()
    column_data = [row[column_name] for row in response.data]
    st.write(f"נתונים לעמודה '{column_name}':")
    st.write(column_data)

except Exception as e:
    st.error(f"שגיאה בשליפת נתונים לעמודה '{column_name}': {e}")



































