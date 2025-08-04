import streamlit as st
import streamlit.components.v1 as components
from st_supabase_connection import SupabaseConnection



options = ["ריח רע", "גרפיטי", "ריפוד קרוע", "לכלוך אחר בקרון חיצוני", "נזק בצבע הקרון"]
selected = st.multiselect(
    ":בחר תכונה",
    options,
    max_selections=1
)




# Read toggle state from query param (sent by JS)
query_params = st.experimental_get_query_params()
toggled = query_params.get("toggle", ["false"])[0] == "true"

# Optional: persist state with session_state
st.session_state["rect_toggle"] = toggled

# Show the toggle state in Streamlit
st.write("Toggled:", toggled)

# Render custom HTML + JS
components.html(
    f"""
    <div style="position: relative; width: 160px; height: 60px;">

        <!-- Hidden actual checkbox -->
        <input type="checkbox" id="hiddenToggle" style="display: none;" {'checked' if toggled else ''}>

        <!-- Styled rectangle -->
        <label for="hiddenToggle" style="
            position: absolute;
            top: 0;
            left: 0;
            width: 160px;
            height: 60px;
            background-color: {'#dc3545' if toggled else '#6c757d'};
            color: white;
            font-size: 16px;
            font-weight: bold;
            border-radius: 8px;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            user-select: none;
        ">
            {'ON' if toggled else 'OFF'}
        </label>

    </div>

    <script>
        const toggle = document.getElementById("hiddenToggle");
        toggle.addEventListener("change", () => {{
            // Send a dummy fetch request to update Streamlit state
            fetch(`/?toggle=${{toggle.checked}}`);
        }});
    </script>
    """,
    height=80
)













