import streamlit as st
from streamlit import session_state

import functions

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    functions.write_todos(todos)

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my First Python project app")

# Display checkboxes with unique keys
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todo_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        st.rerun()

# Input to add a new todo
st.text_input(label="", placeholder="Enter a Todo", on_change=add_todo, key="new_todo")

