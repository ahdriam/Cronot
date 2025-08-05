import streamlit as st
import streamlit.components.v1 as components
from st_supabase_connection import SupabaseConnection
import time
# --- Sidebar: Auto-refresh toggle ---
st.sidebar.subheader("Auto Refresh")
enable_refresh = st.sidebar.toggle("הפעל רענון אוטומטי", value=True)
refresh_interval = 2  # seconds

# --- Column selection ---
display_to_column = {
    "ריח רע": "ריח רע",
    "גרפיטי": "גרפיטי",
    "ריפוד קרוע": "ריפוד קרוע",import streamlit as st
import streamlit.components.v1 as components
from st_supabase_connection import SupabaseConnection
import time
conn = st.connection("supabase", type=SupabaseConnection)
# --- UI control for auto-refresh ---
st.sidebar.subheader("Auto Refresh")
enable_refresh = st.sidebar.toggle("הפעל רענון אוטומטי", value=False)
refresh_interval = 2  # seconds

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

if enable_refresh:
    # Wait a bit before rerunning
    time.sleep(refresh_interval)
    st.experimental_rerun()


    "לכלוך אחר בקרון חיצוני": "לכלוך אחר בקרון חיצוני",
    "נזק בצבע הקרון": "נזק בצבע הקרון"
}
selected_display = st.selectbox(":בחר תכונה", list(display_to_column.keys()))
column_name = display_to_column[selected_display]

# --- Fetch data ---
conn = st.connection("supabase", type=SupabaseConnection)
try:
    response = conn.table("CRONOT").select(f'"{column_name}"').execute()
    values_array = [row[column_name] for row in response.data]
except Exception as e:
    st.error(f"שגיאה: {e}")
    values_array = []

# --- Display data (after fetching, before rerun) ---
st.write("📦 מערך נתונים:")
st.write(values_array)

# --- Trigger rerun BEFORE finishing rendering ---
if enable_refresh:
    time.sleep(refresh_interval)
    st.experimental_rerun()











































