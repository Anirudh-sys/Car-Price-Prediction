import streamlit as st
import joblib
import pandas as pd
import time

# Load the trained model 
model = joblib.load('car_model_compressed.joblib')

# Custom CSS for styling
def add_custom_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Raleway:wght@400;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Raleway', sans-serif;
            background-color: #a39274 !important; /* Earthy color */
            color: #222;
        }

        /* Sidebar Styles */
        .css-1d391kg {  /* Adjusted to target sidebar */
            background-color: #a39274 !important;  /* Match the body background */
        }

        /* Remove button styles and apply hover effects */
        .stSidebar .stSelectbox,
        .stSidebar .stButton {
            background: transparent !important; /* Remove button background */
            color: black !important; /* Set default text color */
            border: none !important; /* Remove border */
            cursor: pointer; /* Change cursor on hover */
            padding: 10px 20px; /* Add padding for spacing */
            display: block; /* Ensure block display for hover effect */
            transition: background-color 0.3s; /* Transition for hover effect */
        }

        .stSidebar .stSelectbox:hover,
        .stSidebar .stButton:hover {
            background-color: rgba(255, 127, 80, 0.2); /* Light coral background on hover */
        }

        /* Sidebar text links */
        .stSidebar a {
            text-decoration: none; /* Remove underline */
            color: black; /* Default link color */
            padding: 10px 20px; /* Add padding for links */
            display: block; /* Block display for hover effect */
            transition: background-color 0.3s; /* Transition for hover effect */
        }

        .stSidebar a:hover {
            background-color: rgba(255, 127, 80, 0.2); /* Light coral background on hover */
        }

        /* Button Styles */
        .stButton button {
            background-color: #FF7F50;
            color: black;
            padding: 0.75rem 2rem;
            border-radius: 15px;
            font-size: 18px;
            transition: transform 0.2s, background-color 0.3s ease;
        }
        
        .stButton button:hover {
            background-color: #D3D9D4;
            transform: scale(1.05);
        }

        /* Input Field Styles */
        input, select {
            padding: 0.75rem;
            margin: 0.5rem 0;
            border-radius: 8px;
            border: 2px solid #ddd;
        }

        /* Divider Styles */
        .divider {
            height: 3px;
            background-color: #ff7f50;
            margin: 2rem 0;
            border-radius: 5px;
        }

        /* Icon Styles */
        .icon {
            width: 30px;
            height: 30px;
            margin-right: 8px;
        }

        /* Hero Section */
        .hero {
            padding: 60px;
            text-align: center;
            background: None /* Hero background */
            color: black;
            border-radius: 10px;
            margin-bottom: 20px;
        }

        /* Footer */
        .footer {
            text-align: center;
            margin-top: 40px;
            padding: 20px 0;
            background-color: None; /* Light gray background for footer */
            border-top: 1px solid #eaeaea;
            font-size: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )



# Prediction function
def predict_price(features):
    input_data = pd.DataFrame([features])
    prediction = model.predict(input_data)
    return prediction[0]

# Hero section for all pages
def show_hero(title, description):
    st.markdown(f'<div class="hero"><h1>{title}</h1><p>{description}</p></div>', unsafe_allow_html=True)

# Footer function
def show_footer():
    st.markdown(
        """
        <div class="footer">
            <p>Connect with me:</p>
            <div style="display: flex; justify-content: center;">
                <a href="https://github.com/Anirudh-sys" target="_blank">
                    <img src="https://img.icons8.com/material-outlined/24/000000/github.png" class="icon"/>
                </a>
                <a href="https://linkedin.com/in/anirudh-r-4b5038278" target="_blank">
                    <img src="https://img.icons8.com/material-outlined/24/000000/linkedin.png" class="icon"/>
                </a>
                <a href="mailto:anirudhr2509@gmail.com">
                    <img src="https://img.icons8.com/material-outlined/24/000000/gmail.png" class="icon"/>
                </a>
        """, unsafe_allow_html=True)

# Home page function
def show_home():
    show_hero('Welcome to the Car Price Prediction App!', 
               'This application allows you to predict the price of cars based on various parameters.')

# Future updates page function
def show_future_updates():
    show_hero('🔮 Future Updates', 'Upcoming features and improvements for the app.')
    st.write(""" 
        - *Car Comparison:* Compare different car models based on features and price.
        - *Car Value Depreciation Rate:* Analyze how different factors affect the depreciation of car value over time.
        - *Car Recommendation System:* Provide personalized car recommendations based on user preferences.
        - *User Reviews and Ratings:* Allow users to submit and view reviews for different car models.
        - *Car Financing Calculator:* Estimate monthly payments based on loan amount, interest rate, and loan duration.
    """)
    show_footer()

# About page function
def show_about():
    show_hero('About Me', 'Learn more about the developer behind this app.')
    st.write("""
        Hello! I'm Anirudh, a highly motivated student with a deep passion for data science and programming. My journey into the world of data began with a fascination for how data shapes our decisions and drives innovation. I thrive on the challenge of transforming raw data into meaningful insights and developing solutions that can make a positive impact.

        Currently, I'm honing my skills at IIT Madras and SRM University, where I'm immersing myself in the latest tools and techniques in data science and machine learning. I am dedicated to continuous learning, always eager to tackle complex problems and expand my knowledge base.

        I believe that collaboration fuels creativity, so I actively seek opportunities to engage in innovative projects with fellow enthusiasts. My goal is not just to improve my own skills but also to contribute to cutting-edge solutions that can solve real-world challenges.

        In my free time, I enjoy exploring new programming languages, participating in hackathons, and staying updated on industry trends. I'm excited about the future of data science and look forward to the possibilities it holds.

        Thank you for visiting my Web App, and feel free to connect with me!
    """)
    show_footer()

# Contact page function
def show_contact():
    show_hero('Contact Me', 'Feel free to reach out through any of the following platforms:')
    # Contact details with icons
    st.write(
        '<div style="display: flex; align-items: center;">'
        '<img src="https://img.icons8.com/material-outlined/24/000000/github.png" class="icon"/>' 
        '<a href="https://github.com/Anirudh-sys">GitHub</a>'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        '<div style="display: flex; align-items: center;">'
        '<img src="https://img.icons8.com/material-outlined/24/000000/linkedin.png" class="icon"/>' 
        '<a href="https://linkedin.com/in/anirudh-r-4b5038278">LinkedIn</a>'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        '<div style="display: flex; align-items: center;">'
        '<img src="https://img.icons8.com/material-outlined/24/000000/gmail.png" class="icon"/>' 
        '<a href="mailto:anirudhr2509@gmail.com">Email</a>'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        '<div style="display: flex; align-items: center;">'
        '<img src="https://img.icons8.com/material-outlined/24/000000/phone.png" class="icon"/>' 
        ' +91 9363645900'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        '<div style="display: flex; align-items: center;">'
        '<img src="https://img.icons8.com/material-outlined/24/000000/portfolio.png" class="icon"/>' 
        '<a href="https://your-portfolio-link.com">Portfolio</a>'
        '</div>',
        unsafe_allow_html=True
    )

# Car prediction function
def show_car_prediction():
    show_hero('🚗 Car Price Prediction', 'Predict the price of your car using our model.')

    # Add a divider line
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # Input fields split into columns
    col1, col2 = st.columns(2)

    with col1:
        name = st.selectbox('Name', ['Choose'] + ['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
                                                  'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz',
                                                  'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus',
                                                  'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force',
                                                  'Ambassador', 'Ashok', 'Isuzu', 'Opel'])
        year = st.slider('Year', min_value=1990, max_value=2024, step=1)
        km_driven = st.number_input('Kilometers Driven', min_value=0, step=5000, help="Total kilometers the car has been driven")
        fuel = st.selectbox('Fuel Type', ['Choose'] + ['Diesel', 'Petrol', 'CNG'])
        mileage = st.number_input('Mileage', min_value=0.0, step=1.0, help="Fuel efficiency in kilometers per liter")

    with col2:
        seller_type = st.selectbox('Seller Type', ['Choose'] + ['Individual', 'Dealer', 'Trustmark Dealer'])
        transmission = st.selectbox('Transmission', ['Choose'] + ['Manual', 'Automatic'])
        owner = st.selectbox('Owner', ['Choose'] + ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'])
        engine = st.slider('Engine CC', min_value=500, max_value=4000, step=1)
        max_power = st.number_input('Max Power', min_value=0.0, max_value=300.0, step=1.0)
        seats = st.number_input('Seats', min_value=2, step=1)

    # Create a dictionary from user inputs
    features = {
        'name': name,
        'year': year,
        'km_driven': km_driven,
        'fuel': fuel,
        'seller_type': seller_type,
        'transmission': transmission,
        'owner': owner,
        'mileage': mileage,
        'engine': engine,
        'max_power': max_power,
        'seats': seats
    }

    # Check if all fields are filled in
    if 'Choose' in features.values():
        st.warning('Please fill in all the required fields')
    else:
        # Predict button with animation and result
        if st.button('💡 Predict Price'):
            with st.spinner('Predicting...'):
                time.sleep(2)  # Simulate a delay
                price = predict_price(features)
            st.success(f'🚙 The predicted price is: *Rs {price:.2f}*')

# Main function for the Streamlit app
def main():
    # Apply custom CSS
    add_custom_css()

    # Sidebar navigation (closed by default)
    selection = st.sidebar.radio("", ["Home", "Car Price Predictor", "Future Updates", "About", "Contact"], key="menu_selection")

    # Show the selected page based on sidebar selection
    if selection == "Home":
        show_home()
    elif selection == "Car Price Predictor":
        show_car_prediction()
    elif selection == "Future Updates":
        show_future_updates()
    elif selection == "About":
        show_about()
    elif selection == "Contact":
        show_contact()

if __name__ == '__main__':
    main()
