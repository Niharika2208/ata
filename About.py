import streamlit as st
import streamlit_antd_components as sac
from PIL import Image
import time


def about_page():
    st.title("About")
    st.write("""Welcome to the comprehensive engineering solution application! The app is designed to streamline your 
    engineering processes, providing valuable insights into **dimensions, costs, welding, heating processes, 
    project status and generating accurate price quotations**. We aim to simplify complex tasks and enhance your 
    workflow, offering an intuitive and efficient tool for professionals in the engineering field. Explore the 
    various features and functionalities to optimize your work and achieve better results.""")

    @st.cache_data
    def get_images():
        image_paths = [
            "2.jpg",
            "3.jpg",
            "4.jpg",
            "5.jpg"
        ]
        images = [Image.open(image_path) for image_path in image_paths]
        return images

    images = get_images()

    index = st.empty()

    while True:
        for i in range(len(images)):
            # Display an image in the placeholder
            index.image(images[i], caption=f"Image {i + 1} of {len(images)}")

            # Add a delay before switching to the next image
            time.sleep(5)

            # Clear the placeholder before the next iteration
            index.empty()


def usage_page():
    st.title("How to use the app?")



def contact_page():
    st.title("Contact Us")
    st.markdown("Have questions or feedback? Reach out to us:")
    st.markdown("- **Email:** david.hoffmann@ovgu.de")
    st.markdown("- **Email:** niharika.ramanath@ovgu.de")
    st.markdown("- **Email:** pooja.gupta@ovgu.de")
    st.markdown("- **GitHub:** guptapooja10/ata")


def main():
    sac.buttons(
        [sac.ButtonsItem(label='Sign In/Sign Up', href='https://credentials-page.streamlit.app/'),
         ], index=1, align='end')
    st.sidebar.title("Navigation")
    selected_page = st.sidebar.selectbox("Go to", ["About", "Usage", "Contact"])

    if selected_page == "About":
        about_page()
    elif selected_page == "Usage":
        usage_page()
    elif selected_page == "Contact":
        contact_page()


if __name__ == "__main__":
    main()
