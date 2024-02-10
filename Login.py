import streamlit as st
from firebase_init import initialize_firebase_app
from firebase_admin import auth


# Initialize Firebase app if not already initialized
initialize_firebase_app()


def get_session_state():
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False


# Call get_session_state before any Streamlit function
get_session_state()


def login_app():
    st.title('Welcome to :violet[ATA]')

    choice = st.selectbox('Login/Signup', ['Login', 'Signup'])
    if choice == 'Login':
        email = st.text_input('E-Mail Address')
        password = st.text_input('Password', type='password')

        if st.button('Login'):
            # Perform authentication check
            user = auth.get_user_by_email(email)
            if user and user.password == password:
                st.session_state.authenticated = True

                # Show the file upload page
                file_upload_page()

            else:
                st.error("Username/password is incorrect")

    else:
        email = st.text_input('E-Mail Address')
        password = st.text_input('Password', type='password')
        username = st.text_input('Enter your username')

        if st.button('Create my account'):
            user = auth.create_user(email=email, password=password, uid=username)
            st.success('Account created successfully!')
            st.markdown('You can now log in using your E-Mail and Password')
            st.balloons()


def file_upload_page():
    st.header('File Upload Page')
    st.write("Upload your important documents here:")

    uploaded_files = st.file_uploader("Choose a file", type=["pdf", "txt", "csv", "xlsx"])

    if uploaded_files is not None:
        st.success("File uploaded successfully!")



if __name__ == "__main__":
    # Call get_session_state before any Streamlit function
    get_session_state()

    # Call login_app after get_session_state
    login_app()
