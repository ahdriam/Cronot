import streamlit as st
import json
import os
import time

DATA_FILE = "data.json"
TIMESTAMP_FILE = "last_updated.txt"
CORRECT_PASSWORD = "333"

# ---- Timestamp handling ----
def update_timestamp():
    with open(TIMESTAMP_FILE, "w") as f:
        f.write(str(time.time()))

def get_last_update_time():
    if os.path.exists(TIMESTAMP_FILE):
        with open(TIMESTAMP_FILE, "r") as f:
            try:
                return float(f.read().strip())
            except ValueError:
                return 0.0
    return 0.0

# ---- Data handling functions ----
def create_default_data():
    return [
        {
            "id": f"{i+1} קרון",
            "אורות בלם מלוכלכים": False,
            "אי הימצאות מדבקת אזהרה לנוסע בגין אי תשלום דמי הנסיעה": False,
            "אי הימצאות מידע כללי": False,
            "אי הימצאות ערכת מילוט": False,
            "אי הימצאות שילוט ציוד מגן רפואה": False,
            "אי הימצאות שלט איסור/אזהרה": False,
            "אי הימצאות שלט חירום": False,
            "גרפיטי": False,
            "חלקים וחיבורים בולטים או מסוכנים": False,
            "כתמי בוץ/אבק כבד/כתמי שמן/כתמי דבק": False,
            "לוגו/פרסומת/מדבקות פרסום רופפים/קרועים": False,
            "לכלוך אחר בקרון חיצוני": False,
            "מדבקות/שלטים/פוסטרים לא מורשים": False,
            "מעקות, ידיות ועמודי אחיזה שבורים": False,
            "נזק בצבע הקרון": False,
            "ריהוט/מתקן בקרון מלוכלך עם בוץ/אבק כבד/אחר": False,
            "ריהוט/מתקן בקרון עם גרפיטי": False,
            "ריהוט/מתקן בקרון עם דבק/כתמים קשים": False,
            "ריח רע": False,
            "ריפוד קרוע": False,
            "שאריות מדבקות/מדבקות": False,
            "שילוט קו אחורי אינו תקין": False,
            "שילוט קו צדדי אינו תקין": False,
            "שימשה פנימית מלוכלכת": False,
            "שמשה קדמית מלוכלכת": False,
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
    update_timestamp()

# ---- Auto-refresh logic (based on timestamp) ----
if "last_seen_timestamp" not in st.session_state:
    st.session_state.last_seen_timestamp = get_last_update_time()

current_timestamp = get_last_update_time()
if current_timestamp > st.session_state.last_seen_timestamp:
    st.session_state.last_seen_timestamp = current_timestamp
    st.experimental_rerun()

# ---- Session state setup ----
if "data" not in st.session_state:
    st.session_state.data = load_data()

if "message" not in st.session_state:
    st.session_state.message = ""

data = st.session_state.data

# ---- UI: Title ----
st.title(" ______🚆 מיטוב קרונות")
password = st.text_input("Type your password and press ENTER", type="password")
if st.button("Logoff"):
    st.session_state.message = ""
    password = ""
if password and password != CORRECT_PASSWORD:
    st.session_state.message = "wrong password"
elif password == CORRECT_PASSWORD:
    st.session_state.message = "correct password"
st.write(st.session_state.message)
enabled = password == CORRECT_PASSWORD

# ---- Sidebar: Single Object Editing ----
st.sidebar.header("✏️ ערוך קרון מסויים")

object_ids = [obj["id"] for obj in data]

# Persist selected car ID
if "selected_id" not in st.session_state:
    st.session_state.selected_id = object_ids[0]

selected_id = st.sidebar.selectbox("בחר קרון", object_ids, index=object_ids.index(st.session_state.selected_id), key="selected_id_dropdown")
st.session_state.selected_id = selected_id
selected_index = object_ids.index(selected_id)
obj = data[selected_index]

st.sidebar.subheader(f"{selected_id} :עורך את")
for key in obj:
    if key != "id":
        new_val = st.sidebar.checkbox(key, value=obj[key], key=f"{selected_id}_{key}", disabled=not enabled)
        if new_val != obj[key]:
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

# Persist property_to_edit selection
if "property_to_edit" not in st.session_state:
    st.session_state.property_to_edit = boolean_keys[0]

selected_property = st.selectbox(":בחר תכונה", boolean_keys,
                                 index=boolean_keys.index(st.session_state.property_to_edit),
                                 key="bulk_property_select")

st.session_state.property_to_edit = selected_property
property_to_edit = selected_property

# Select/Deselect All Buttons
col1, col2, col3 = st.columns([1, 1, 5])
with col1:
    if st.button("🔘 אפס הכל", disabled=not enabled):
        for obj in st.session_state.data:
            for key in obj:
                if key != "id":
                    obj[key] = False
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

    if checked != obj[property_to_edit]:
        st.session_state.data[i][property_to_edit] = checked
        save_data(st.session_state.data)
        st.rerun()
