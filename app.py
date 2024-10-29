import streamlit as st
import base64

# Load the image from the specified file path
def load_image(image_file):
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

image_path = load_image("images\IMG_20241025_205634.jpg")  # Adjust path to your image

# Function to create circular images
def circular_image(image_path):
    return f"""
    <style>
        .circle {{
            width: 200px;  /* Adjust size as needed */
            height: 200px; /* Adjust size as needed */
            border-radius: 50%;
            overflow: hidden;
            display: inline-block;
            border: 5px solid #f0f0f0; /* Optional: border styling */
        }}
        .circle img {{
            width: 100%;
            height: auto;
        }}
    </style>
    <div class="circle">
        <img src="data:image/jpeg;base64,{image_path}" alt="Circular Image"/>
    </div>
    """

# Set page configuration
st.set_page_config(page_title="Vaaruni Desai Portfolio", page_icon=":wave:", layout="wide")

# Custom CSS for background color and text styles
st.markdown(
    """
    <style>
        /* Set background color to black */
        .reportview-container {
            background-color: black;  /* This affects the whole app */
        }
        .stApp {
            background-color: black;  /* This affects the app's main area */
        }
        /* Text colors */
        h1 {
            color: yellow;  /* Title color */
        }
        h2 {
            color: yellow;  /* Subheader color */
        }
        h3 {
            color: yellow;  /* Smaller header color */
        }
        p {
            color: white;  /* Paragraph text color */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Tabs for Navigation
tab1, tab2, tab3, tab4 = st.tabs(["Home", "Projects", "Skills", "Contact"])
with tab1:# Create a two-column layout for the title and image
    col1, col2 = st.columns([1, 2])  # Adjust ratios as needed for layout balance

    with col1:
        # Display the circular image
        st.markdown(circular_image(image_path), unsafe_allow_html=True)

    with col2:
        # Title and Introduction
        st.title("Hi, I'm Vaaruni Desai")
        st.write("""
        I am a Data Scientist with a Master’s in Data Science and Engineering from the University of California, San Diego.
        My career has been focused on building scalable data solutions and advancing machine learning capabilities to solve complex problems. 
        I have professional experience with REST API development, role-based access control, and data privacy compliance, 
        along with academic experience in applying large language models for knowledge structuring.
        """)
        st.write("Feel free to view my [LinkedIn profile](https://www.linkedin.com/in/vaaruni-desai/) or check out my [GitHub](https://github.com/Vaaruni2797).")

# Projects Section
with tab2:
    st.header("Projects")

    # Project 1: PhysioAI Companion
    st.subheader("PhysioAI Companion")
    st.write("""
        Led the development of a real-time posture analysis tool using pose estimation algorithms with over 95% accuracy.
        This computer vision project incorporated advanced machine learning techniques to enhance patient assessments.
    """)
    st.markdown("[Project Demo](https://book-genre-prediction.streamlit.app)")

    # Project 2: Book Genre Prediction
    st.subheader("Book Genre Prediction")
    st.write("""
        Built a machine learning model to predict book genres using natural language processing (NLP) techniques.
        Deployed the model on Streamlit for easy interaction and visualization.
    """)
    st.markdown("[Project Demo](https://book-genre-prediction.streamlit.app) | [GitHub Repository](https://github.com/Vaaruni2797/book-genre-prediction)")

    # Project 3: Math Score Prediction
    st.subheader("Math Score Prediction")
    st.write("""
        Created a regression model to predict students' math scores based on various factors, deployed on Streamlit.
        The project demonstrates proficiency in regression modeling and interactive dashboards.
    """)
    st.markdown("[Project Demo](https://math-score-prediction.streamlit.app)")

# Skills Section
with tab3:
    st.header("Skills")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Programming Languages")
        st.write("- Python\n- SQL\n- Cypher")

    with col2:
        st.subheader("Machine Learning Tools")
        st.write("- scikit-learn\n- TensorFlow\n- PyTorch\n- pandas\n- NumPy")

    with col3:
        st.subheader("Technologies & Tools")
        st.write("- Flask, FastAPI, Docker\n- AWS Sagemaker, S3\n- Grafana, Tableau")

    st.subheader("Additional Skills")
    st.write("- Data Visualization\n- Scalable Data Analysis\n- Knowledge Graphs with Neo4j\n- Experience in REST API Development")

# Contact Section
with tab4:
    st.header("Contact")
    st.write("Feel free to reach out to me via [LinkedIn](https://www.linkedin.com/in/vaaruni-desai/) or email at [v1desai@ucsd.edu](mailto:v1desai@ucsd.edu).")
