import streamlit as st
import functions


def add_todo():
    todo = st.session_state['new_todo']
    todos = functions.getTodos()
    todos.append(todo.strip()+"\n")
    functions.writeTodos(todos)
    st.session_state['new_todo'] = ""


st.title("To-Do App")
todos = functions.getTodos()
for i, todo in enumerate(todos):
    st.checkbox(todo, key=str(i))
    if st.session_state[f"{i}"]:
        todos.pop(i)
        functions.writeTodos(todos)
        st.experimental_rerun()


st.text_input(label="Add To-Do", label_visibility="hidden", placeholder="Add a todo...",
              on_change=add_todo, key="new_todo")
