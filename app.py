import streamlit as st
import joblib
import pandas as pd
import time

# Load the trained model (Check for push)
model = joblib.load('car_model_compressed.joblib')

# Custom CSS for styling
def add_custom_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Raleway:wght@400;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Raleway', sans-serif;
            background: linear-gradient(to bottom right, #cce9ff, #e1f7d5); /* Gradient background */
            color: #222;
        }
        
        .stButton button {
            background-color: #FF7F50;
            color: white;
            padding: 0.75rem 2rem;
            border-radius: 15px;
            font-size: 18px;
            transition: transform 0.2s, background-color 0.3s ease;
        }
        
        .stButton button:hover {
            background-color: #FF4500;
            transform: scale(1.05);
        }

        input, select {
            padding: 0.75rem;
            margin: 0.5rem 0;
            border-radius: 8px;
            border: 2px solid #ddd;
        }

        .divider {
            height: 3px;
            background-color: #ff7f50;
            margin: 2rem 0;
            border-radius: 5px;
        }

        .icon {
            width: 30px;
            height: 30px;
            margin-right: 8px;
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

# Home page function
def show_home():
    st.title('Welcome to the Car Price Prediction App!')
    st.write("""
        This application allows you to predict the price of cars based on various parameters.
        Please use the sidebar to navigate to different sections of the app.
    """)

# Future updates page function
def show_future_updates():
    st.title('🔮 Future Updates')
    st.write("""
        - *Car Comparison:* Compare different car models based on features and price.
        - *Car Value Depreciation Rate:* Analyze how different factors affect the depreciation of car value over time.
        - *Car Recommendation System:* Provide personalized car recommendations based on user preferences.
        - *User Reviews and Ratings:* Allow users to submit and view reviews for different car models.
        - *Car Financing Calculator:* Estimate monthly payments based on loan amount, interest rate, and loan duration.
    """)

# About page function
def show_about():
    st.title('About Me')
    st.write("""
        Hello! I'm Anirudh, a highly motivated student with a deep passion for data science and programming. My journey into the world of data began with a fascination for how data shapes our decisions and drives innovation. I thrive on the challenge of transforming raw data into meaningful insights and developing solutions that can make a positive impact.

Currently, I'm honing my skills at IIT Madras and SRM University, where I'm immersing myself in the latest tools and techniques in data science and machine learning. I am dedicated to continuous learning, always eager to tackle complex problems and expand my knowledge base.

I believe that collaboration fuels creativity, so I actively seek opportunities to engage in innovative projects with fellow enthusiasts. My goal is not just to improve my own skills but also to contribute to cutting-edge solutions that can solve real-world challenges.

In my free time, I enjoy exploring new programming languages, participating in hackathons, and staying updated on industry trends. I'm excited about the future of data science and look forward to the possibilities it holds.

Thank you for visiting my Web App, and feel free to connect with me!
    """)

# Contact page function
def show_contact():
    st.title('📞 Contact Me')
    st.write("""
        Feel free to reach out through any of the following platforms:
    """)
    
    # Contact details with icons
    st.write(
        '<div style="display: flex; align-items: center;">'
        '<img src="https://img.icons8.com/material-outlined/24/000000/github.png" class="icon"/>' 
        '<a href="https://github.com/your-github-username">GitHub</a>'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        '<div style="display: flex; align-items: center;">'
        '<img src="https://img.icons8.com/material-outlined/24/000000/linkedin.png" class="icon"/>' 
        '<a href="https://linkedin.com/in/your-linkedin-username">LinkedIn</a>'
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
        'Contact Number: +91 9363645900'
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
    st.title('🚗 Car Price Prediction')
    st.write('Predict the price of your car using our model')

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
        km_driven = st.number_input('Kilometers Driven', min_value=0, step=100, help="Total kilometers the car has been driven")
        fuel = st.selectbox('Fuel Type', ['Choose'] + ['Diesel', 'Petrol', 'LPG', 'CNG'])
        mileage = st.number_input('Mileage', min_value=0.0, step=0.1, help="Fuel efficiency in kilometers per liter")

    with col2:
        seller_type = st.selectbox('Seller Type', ['Choose'] + ['Individual', 'Dealer', 'Trustmark Dealer'])
        transmission = st.selectbox('Transmission', ['Choose'] + ['Manual', 'Automatic'])
        owner = st.selectbox('Owner', ['Choose'] + ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'])
        engine = st.number_input('Engine CC', min_value=0, step=100)
        max_power = st.number_input('Max Power', min_value=0.0, step=0.1)
        seats = st.number_input('Seats', min_value=1, step=1)

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
    selection = st.sidebar.radio("", ["Home", "Car Prediction", "Future Updates", "About", "Contact"], key="menu_selection")

    # Show the selected page based on sidebar selection
    if selection == "Home":
        show_home()
    elif selection == "Car Prediction":
        show_car_prediction()
    elif selection == "Future Updates":
        show_future_updates()
    elif selection == "About":
        show_about()
    elif selection == "Contact":
        show_contact()

if __name__ == '__main__':
    main()
