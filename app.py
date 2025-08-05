import streamlit as st
import streamlit.components.v1 as components
from st_supabase_connection import SupabaseConnection
from streamlit_autorefresh import st_autorefresh
conn = st.connection("supabase", type=SupabaseConnection)
st_autorefresh(interval=2000)

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
# try:
#     response = conn.table("CRONOT").select(f'"{column_name}"').execute()
#     column_data = [row[column_name] for row in response.data]
#     st.write(f"נתונים לעמודה '{column_name}':")
#     st.write(column_data)

# except Exception as e:
#     st.error(f"שגיאה בשליפת נתונים לעמודה '{column_name}': {e}")

try:
    response = conn.table("CRONOT").select(f'"{column_name}"').execute()
    # Save values to Python array
    values_array = [row[column_name] for row in response.data]

    # Show the array
    st.write("📦 מערך נתונים:")
    st.write(values_array)

except Exception as e:
    st.error(f"שגיאה: {e}")






































