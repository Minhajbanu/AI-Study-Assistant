

import streamlit as st
from document_loader import extract_text
from rag_pipeline import create_vector_store
from notes_generator import generate_notes
from database import create_table, add_user, login_user
from download_utils import create_pdf
from chatbot import create_chatbot, ask_question

create_table()

# ---------------- SESSION STATE ---------------- #

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None


# ---------------- AUTH PAGE ---------------- #

def auth_page():

    st.title("AI Exam Notes Generator")

    menu = ["Login", "Signup"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Signup":

        st.subheader("Create New Account")

        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type="password")

        if st.button("Signup"):

            if new_user and new_password:
                add_user(new_user, new_password)
                st.success("Account created successfully")

            else:
                st.warning("Please fill all fields")

    elif choice == "Login":

        st.subheader("Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):

            result = login_user(username, password)

            if result:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()

            else:
                st.error("Invalid credentials")


# ---------------- MAIN APP ---------------- #

def main_app():

    st.title("📚 AI Exam Notes Generator")

    st.sidebar.write(f"Welcome **{st.session_state.username}**")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.vectorstore = None
        st.session_state.qa_chain = None
        st.rerun()

    st.write("Upload your study materials and generate exam-ready notes.")

    uploaded_files = st.file_uploader(
        "Upload Study Materials",
        type=["pdf", "pptx", "png", "jpg", "jpeg"],
        accept_multiple_files=True
    )

    # ---------------- DOCUMENT PROCESSING ---------------- #

    if uploaded_files:

        combined_text = ""

        with st.spinner("Processing documents..."):

            for file in uploaded_files:
                text = extract_text(file)
                combined_text += text + "\n"

        st.success("Documents processed successfully")

        index, chunks = create_vector_store(combined_text)

        st.session_state.vectorstore = index
        st.session_state.qa_chain = create_chatbot(index)

        st.success("Vector database created")

        # ---------------- NOTES GENERATION ---------------- #

        if st.button("Generate Exam Notes"):

            with st.spinner("Generating notes..."):

                notes = generate_notes(index, chunks)

            st.subheader("Generated Exam Notes")

            st.markdown(notes)

            pdf_path = create_pdf(notes)

            with open(pdf_path, "rb") as f:

                st.download_button(
                    "⬇ Download Notes as PDF",
                    f,
                    file_name="exam_notes.pdf",
                    mime="application/pdf"
                )

    # ---------------- CHATBOT SECTION ---------------- #

    st.divider()
    st.subheader("💬 Chat With Your Study Material")

    if st.session_state.qa_chain:

        user_question = st.text_input("Ask a question about your documents")

        if st.button("Ask AI"):

            with st.spinner("Thinking..."):

                answer = ask_question(st.session_state.qa_chain, user_question)

            st.write("### 🤖 Answer")
            st.write(answer)

    else:
        st.info("Upload documents first to enable chat.")


# ---------------- ROUTING ---------------- #

if st.session_state.logged_in:
    main_app()
else:

    auth_page()
