import streamlit as st
from st_supabase_connection import SupabaseConnection

# Create the connection in Streamlit Secrets or GUI
conn: SupabaseConnection = st.connection("supabase", type=SupabaseConnection)

# Use the .client attribute to get the underlying Supabase client
supabase = conn.client

  # -----query your table
  # response = supabase.table("CRONOT").select("*").execute()
  # data = response.data
  
  # # Display the results
  # st.write(response.data)

options = ["ריח רע", "גרפיטי", "ריפוד קרוע", "לכלוך אחר בקרון חיצוני", "נזק בצבע הקרון"]
selected = st.multiselect(
    ":בחר תכונה",
    options,
    max_selections=1
)


<button id="toggleBtn">State: OFF</button>
<script>
  let isOn = false;
  const button = document.getElementById("toggleBtn");

  button.addEventListener("click", () => {
    isOn = !isOn;
    button.textContent = `State: ${isOn ? "ON" : "OFF"}`;
  });
</script>
