# 📝 Day 11 Notes – Streamlit Basics

## 1. What is Streamlit?

Streamlit is an open-source Python framework used to build interactive web applications for Data Science, Machine Learning, and AI with minimal code.

---

## 2. Why is Streamlit Popular?

* Easy to learn and use
* No HTML, CSS, or JavaScript required
* Quickly builds AI and ML web apps
* Interactive user interface
* Integrates easily with AI models and Python libraries

---

## 3. Session State

Session State stores data during a user's session, allowing information such as chat history, user inputs, and settings to persist while the app is running.

**Example:**

```python
if "history" not in st.session_state:
    st.session_state.history = []
```

---

## 4. Sidebar

The sidebar is used to place menus, settings, and controls separately from the main content.

**Example:**

```python
with st.sidebar:
    mode = st.selectbox(
        "Select Mode",
        ["Teacher", "Coder", "Creative"]
    )
```

---

## 5. Widgets

Widgets allow users to interact with the application.

Common Streamlit widgets:

* `st.button()`
* `st.text_input()`
* `st.text_area()`
* `st.selectbox()`
* `st.slider()`
* `st.checkbox()`
* `st.download_button()`

---

## 6. Spinner

A spinner displays a loading animation while a task is running.

**Example:**

```python
with st.spinner("Thinking..."):
    response = model.generate_content(prompt)
```

---

## 7. Difference Between FastAPI and Streamlit

| FastAPI                        | Streamlit                           |
| ------------------------------ | ----------------------------------- |
| Backend API framework          | Frontend web app framework          |
| Builds REST APIs               | Builds interactive web applications |
| Returns JSON responses         | Displays UI components              |
| Used for backend services      | Used for AI dashboards and demos    |
| Accessed through API endpoints | Accessed through a web browser      |

---

