import streamlit as st
from st_supabase_connection import SupabaseConnection

# Create the connection in Streamlit Secrets or GUI
conn: SupabaseConnection = st.connection("supabase", type=SupabaseConnection)

# Use the .client attribute to get the underlying Supabase client
supabase = conn.client

# Now use the Supabase client to query your table
response = supabase.table("CRONOT").select("*").execute()

# Display the results
st.write(response.data)


