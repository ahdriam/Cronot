import streamlit as st
import json
import os

DATA_FILE = "data.json"

# ---- Data handling functions ----
def create_default_data():
    return [
        {
            "id": f"{i+1} קרון",
            "ריהוט/מתקן בקרון עם דבק/כתמים קשים": False,
            "כתמים קלים": False,
            "כתמים קשים": False,
            "פח מלא": False,
		"כתמי שמן": False,
        }
        for i in range(90)
    ]

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            st.warning("⚠️ data.json is empty or corrupted. Creating fresh data.")
            return create_default_data()
    else:
        return create_default_data()

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

# ---- Session state setup ----
if "data" not in st.session_state:
    st.session_state.data = load_data()

data = st.session_state.data
CORRECT_PASSWORD = "333"
if "message" not in st.session_state:
    st.session_state.message = ""
	
# ---- UI: Title ----
st.title(" ______🚆 מיטוב קרונות")
password = st.text_input("Type your password and press ENTER", type="password")
if st.button("Logoff"):
    st.session_state.message = ""
    password = 0
if password and password != CORRECT_PASSWORD:
    st.session_state.message = "wrong password"
elif password == CORRECT_PASSWORD:
    st.session_state.message = "correct password"
st.write(st.session_state.message)	
enabled = password == CORRECT_PASSWORD

# ---- Sidebar: Single Object Editing ----
st.sidebar.header("✏️ ערוך קרון מסויים")

object_ids = [obj["id"] for obj in data]
selected_id = st.sidebar.selectbox("בחר קרון", object_ids)
selected_index = object_ids.index(selected_id)
obj = data[selected_index]

st.sidebar.subheader(f"{selected_id} :עורך את")
for key in obj:
    if key != "id":
        new_val = st.sidebar.checkbox(key, value=obj[key], key=f"{selected_id}_{key}", disabled=not enabled)
        st.session_state.data[selected_index][key] = new_val
        save_data(st.session_state.data)

# ---- Section: Filter Objects ----
st.header("🔍 סינון קרונות")

boolean_keys = [k for k in data[0] if k != "id"]
filter_values = {}

cols = st.columns(2)
for i, key in enumerate(boolean_keys):
    with cols[i % 2]:
        filter_enabled = st.checkbox(f"  סנן לפי `{key}`", key=f"filter_{key}")
        if filter_enabled:
            indent = st.columns([0.15, 0.85])
            with indent[1]:
                val = st.radio(
                    label="ערך",
                    options=[True, False],
                    horizontal=True,
                    key=f"value_{key}"
                )
                filter_values[key] = val

if st.button("🔎 הצג"):
    if not filter_values:
        st.warning("⚠️ לא נבחרו מסננים")
    else:
        matching_objects = [
            obj for obj in data if all(obj.get(k) == v for k, v in filter_values.items())
        ]
	
        st.success(f"✅ נמצאו {len(matching_objects)} קרונות")

        if matching_objects:   
            for obj in matching_objects:
                with st.expander(obj["id"]):
                    st.json(obj)
	    
        else:
            st.info("❌ אין קרונות עם התכונות המבוקשות")

# ---- Section: Bulk Edit ----
st.markdown("---")
st.header("🛠️ ערוך אוסף קרונות לפי תכונה מסויימת")

property_to_edit = st.selectbox(":בחר תכונה", boolean_keys, key="bulk_property")

# Select/Deselect All Buttons
col1, col2, col3 = st.columns([1, 1, 5])
with col1:
    if st.button("🔘 אפס הכל", disabled=not enabled):
        for obj in st.session_state.data:
            for key in obj:
                if key != "id":
                    obj[key] = False  # Set all attributes to False
        save_data(st.session_state.data)
        st.rerun()

with col2:
    if st.button("⚪ אפס תכונה", disabled=not enabled):
        for obj in st.session_state.data:
            obj[property_to_edit] = False
        save_data(st.session_state.data)
        st.rerun()

with col3:
    st.markdown(f".False ללא סימון וי משמע .True = בחר קרונות כדי לעדכן בהם  `{property_to_edit}` ")

# Display checkboxes grid
columns = st.columns(6)
for i, obj in enumerate(st.session_state.data):
    col = columns[i % 6]
    key = f"bulk_checkbox_{property_to_edit}_{obj['id']}"

    checked = col.checkbox(obj["id"], value=obj[property_to_edit], key=key, disabled=not enabled)

    # Immediate update and UI sync
    if checked != obj[property_to_edit]:
        st.session_state.data[i][property_to_edit] = checked
        save_data(st.session_state.data)
        st.rerun()
