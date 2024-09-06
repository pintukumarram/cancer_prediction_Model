# # Save this code as app.py
# import streamlit as st
# import numpy as np
# import joblib

# # Load the trained model and scaler
# model = joblib.load('cancer_model.pkl')  # Load the trained model
# scaler = joblib.load('scaler.pkl')  # Load the scaler

# # Title and description of the app
# st.title("Cancer Detection System")
# st.write("Enter patient data to determine cancer diagnosis, severity, and treatment recommendations.")

# # Input fields for all 30 features used in the training set
# radius_mean = st.number_input('Radius Mean', min_value=0.0)
# texture_mean = st.number_input('Texture Mean', min_value=0.0)
# perimeter_mean = st.number_input('Perimeter Mean', min_value=0.0)
# area_mean = st.number_input('Area Mean', min_value=0.0)
# smoothness_mean = st.number_input('Smoothness Mean', min_value=0.0)
# compactness_mean = st.number_input('Compactness Mean', min_value=0.0)
# concavity_mean = st.number_input('Concavity Mean', min_value=0.0)
# concave_points_mean = st.number_input('Concave Points Mean', min_value=0.0)
# symmetry_mean = st.number_input('Symmetry Mean', min_value=0.0)
# fractal_dimension_mean = st.number_input('Fractal Dimension Mean', min_value=0.0)

# radius_se = st.number_input('Radius SE', min_value=0.0)
# texture_se = st.number_input('Texture SE', min_value=0.0)
# perimeter_se = st.number_input('Perimeter SE', min_value=0.0)
# area_se = st.number_input('Area SE', min_value=0.0)
# smoothness_se = st.number_input('Smoothness SE', min_value=0.0)
# compactness_se = st.number_input('Compactness SE', min_value=0.0)
# concavity_se = st.number_input('Concavity SE', min_value=0.0)
# concave_points_se = st.number_input('Concave Points SE', min_value=0.0)
# symmetry_se = st.number_input('Symmetry SE', min_value=0.0)
# fractal_dimension_se = st.number_input('Fractal Dimension SE', min_value=0.0)

# radius_worst = st.number_input('Radius Worst', min_value=0.0)
# texture_worst = st.number_input('Texture Worst', min_value=0.0)
# perimeter_worst = st.number_input('Perimeter Worst', min_value=0.0)
# area_worst = st.number_input('Area Worst', min_value=0.0)
# smoothness_worst = st.number_input('Smoothness Worst', min_value=0.0)
# compactness_worst = st.number_input('Compactness Worst', min_value=0.0)
# concavity_worst = st.number_input('Concavity Worst', min_value=0.0)
# concave_points_worst = st.number_input('Concave Points Worst', min_value=0.0)
# symmetry_worst = st.number_input('Symmetry Worst', min_value=0.0)
# fractal_dimension_worst = st.number_input('Fractal Dimension Worst', min_value=0.0)

# # Collect all inputs
# input_data = np.array([[
#     radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean,
#     compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean,
#     radius_se, texture_se, perimeter_se, area_se, smoothness_se,
#     compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se,
#     radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst,
#     compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst
# ]])

# # Scale the input data
# input_data_scaled = scaler.transform(input_data)

# # Predict button
# if st.button('Predict'):
#     # Make a prediction
#     prediction = model.predict(input_data_scaled)

#     # Display results based on prediction
#     if prediction == 1:
#         st.error("**Diagnosis**: Malignant (Cancer detected)")
#         st.write("**Severity**: High")
#         st.write("**Recommended Treatment**: Chemotherapy or Surgery")
#         st.write("**Medication Duration**: 6 months")
#         st.write("**Condition**: Critical, requires immediate attention")
#     else:
#         st.success("**Diagnosis**: Benign (No cancer detected)")
#         st.write("**Severity**: None")
#         st.write("**Condition**: Healthy, regular check-ups recommended")



# Save this code as app.py
import streamlit as st
import numpy as np
import joblib

# Load the trained model and scaler
model = joblib.load('cancer_model.pkl')  # Load your trained model
scaler = joblib.load('scaler.pkl')  # Load the scaler

# Custom CSS for animations and styling
st.markdown("""
    <style>
    /* Add a gradient background */
    body {
        background: linear-gradient(to right, #4facfe, #00f2fe);
        color: white;
        font-family: 'Roboto', sans-serif;
    }
    /* Style the title and headers */
    .stApp {
        background-color: transparent;
    }
    h1 {
        font-size: 3rem;
        color: #fff;
        text-align: center;
        animation: fadeIn 2s ease-in-out;
    }
    /* Fade in effect */
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    /* Button styling */
    .stButton > button {
        background-color: #ff4b2b;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 18px;
        transition: transform 0.2s;
    }
    .stButton > button:hover {
        transform: scale(1.05);
        background-color: #ff416c;
    }
    /* Input styling */
    input {
        border-radius: 5px;
        padding: 10px;
        margin-bottom: 10px;
        font-size: 16px;
        color: #333;
    }
    /* Card effect for results */
    .card {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
        animation: slideIn 1s ease-out;
    }
    /* Slide in effect */
    @keyframes slideIn {
        0% { transform: translateY(20px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)

# Title and description of the app
st.title("✨ Cancer Detection System")
st.write("Enter patient data to determine cancer diagnosis, severity, and treatment recommendations.")

# Collect inputs for each feature
features = [
    ('Radius Mean', 0.0), ('Texture Mean', 0.0), ('Perimeter Mean', 0.0), ('Area Mean', 0.0), 
    ('Smoothness Mean', 0.0), ('Compactness Mean', 0.0), ('Concavity Mean', 0.0), ('Concave Points Mean', 0.0), 
    ('Symmetry Mean', 0.0), ('Fractal Dimension Mean', 0.0), ('Radius SE', 0.0), ('Texture SE', 0.0), 
    ('Perimeter SE', 0.0), ('Area SE', 0.0), ('Smoothness SE', 0.0), ('Compactness SE', 0.0), 
    ('Concavity SE', 0.0), ('Concave Points SE', 0.0), ('Symmetry SE', 0.0), ('Fractal Dimension SE', 0.0), 
    ('Radius Worst', 0.0), ('Texture Worst', 0.0), ('Perimeter Worst', 0.0), ('Area Worst', 0.0), 
    ('Smoothness Worst', 0.0), ('Compactness Worst', 0.0), ('Concavity Worst', 0.0), ('Concave Points Worst', 0.0), 
    ('Symmetry Worst', 0.0), ('Fractal Dimension Worst', 0.0)
]

input_data = []
for feature_name, default_value in features:
    value = st.number_input(feature_name, min_value=0.0, value=default_value)
    input_data.append(value)

# Convert input data to the required shape and scale it
input_data = np.array([input_data])
input_data_scaled = scaler.transform(input_data)

# Predict button with styled look
if st.button('🚀 Predict'):
    # Make a prediction
    prediction = model.predict(input_data_scaled)

    # Display results based on prediction
    result_card = '<div class="card">'
    if prediction == 1:
        st.markdown(result_card + """
            <h3>Diagnosis: Malignant (Cancer detected)</h3>
            <p>Severity: High</p>
            <p>Recommended Treatment: Chemotherapy or Surgery</p>
            <p>Medication Duration: 6 months</p>
            <p>Condition: Critical, requires immediate attention</p>
        </div>""", unsafe_allow_html=True)
    else:
        st.markdown(result_card + """
            <h3>Diagnosis: Benign (No cancer detected)</h3>
            <p>Severity: None</p>
            <p>Condition: Healthy, regular check-ups recommended</p>
        </div>""", unsafe_allow_html=True)
