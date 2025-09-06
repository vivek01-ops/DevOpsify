import streamlit as st

# Page config
st.set_page_config(page_title="To-Do App", page_icon="📝")

st.title("To-Do Application, Set your goals")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Functions
def add_task():
    task = st.session_state.new_task.strip()
    if task:
        st.session_state.tasks.append({"task": task, "done": False})
        st.session_state.new_task = ""

def toggle_done(index):
    st.session_state.tasks[index]["done"] = not st.session_state.tasks[index]["done"]

def delete_task(index):
    st.session_state.tasks.pop(index)

def edit_task(index):
    st.session_state.edit_index = index
    st.session_state.edit_task_text = st.session_state.tasks[index]["task"]

def update_task():
    st.session_state.tasks[st.session_state.edit_index]["task"] = st.session_state.edit_task_text
    st.session_state.edit_index = None
    st.session_state.edit_task_text = ""

def clear_completed():
    st.session_state.tasks = [t for t in st.session_state.tasks if not t["done"]]

# Input for new task
st.text_input("Add a new task:", key="new_task", on_change=add_task)

# Edit task input
if "edit_index" in st.session_state and st.session_state.edit_index is not None:
    st.text_input("Edit task:", key="edit_task_text", on_change=update_task)

# Task list display
for i, task_item in enumerate(st.session_state.tasks):
    col1, col2, col3, col4 = st.columns([0.1, 0.6, 0.2, 0.1])
    with col1:
        st.checkbox("", value=task_item["done"], key=f"check{i}", on_change=toggle_done, args=(i,))
    with col2:
        task_text = task_item["task"]
        if task_item["done"]:
            st.markdown(f"~~{task_text}~~")
        else:
            st.write(task_text)
    with col3:
        st.button("✏️", key=f"edit{i}", on_click=edit_task, args=(i,))
    with col4:
        st.button("❌", key=f"del{i}", on_click=delete_task, args=(i,))

# Clear completed tasks
if st.button("Clear Completed Tasks"):
    clear_completed()

# Task summary
st.markdown(f"**Total Tasks:** {len(st.session_state.tasks)} | **Remaining:** {len([t for t in st.session_state.tasks if not t['done']])}")
