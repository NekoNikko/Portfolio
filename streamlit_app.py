import streamlit as st

def homepage():
    st.title("Welcome to My GitHub Portfolio!")
    st.write("This is a showcase of some of my GitHub projects.")
    st.write("Use the menu on the left to navigate the different pages.")

def project_page():
    st.title("My GitHub Projects")
    st.write("Here are some of my latest GitHub projects:")
    # Add code here to display your GitHub projects

def contact_page():
    st.title("Contact Me")
    st.write("You can contact me at:")
    st.write("Email: myemail@example.com")
    st.write("Twitter: @mytwitterhandle")

# Create the Streamlit app
def app():
    st.set_page_config(page_title="My GitHub Portfolio", page_icon=":guardsman:", layout="wide")
    st.sidebar.title("Menu")
    menu_items = ["Homepage", "Projects", "Contact"]
    choice = st.sidebar.selectbox("Select a page", menu_items)
    if choice == "Homepage":
        homepage()
    elif choice == "Projects":
        project_page()
    elif choice == "Contact":
        contact_page()

if __name__ == '__main__':
    app()