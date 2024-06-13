Electric Range Predictor
This project is a Streamlit web application that predicts the range of an Electric Vehicle (EV) based on various input features. It utilizes a machine learning model to make predictions and provides an intuitive user interface for seamless interactions.

Features:
Interactive Web Application: Users can input features such as county, car make, EV type, and CAFV eligibility through dropdown menus.
Real-time Predictions: The application makes real-time predictions on the electric range of vehicles using a pre-trained machine learning model.
User-Friendly Interface: Designed with a clean and intuitive interface to ensure a smooth user experience.

Requirements:
Python 3.8 or higher
Streamlit
NumPy
joblib
Scikit-learn
Installation

Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/electric-range-predictor.git
cd electric-range-predictor

Install the required packages:
bash
Copy code
pip install -r requirements.txt

Ensure that the following files are in the project directory:
scalerEV.pkl (Pre-trained scaler)
lr.model.pkl (Pre-trained machine learning model)
Usage

Run the Streamlit application:
bash
Copy code
streamlit run app.py

Open the application in your web browser:
arduino
Copy code
http://localhost:8501

Input Features:
Select the county from the dropdown menu.
Select the car make from the dropdown menu.
Select the EV type from the dropdown menu.
Select the CAFV eligibility status from the dropdown menu.

Get Predictions:
Click the "Calculate" button to predict the electric range.
The predicted range will be displayed on the screen.

Code Overview

Imports and Setup:
Necessary libraries and models are imported and set up, including loading the scaler and model using joblib.

Data Dictionaries:
Dictionaries are created to map input features to their respective indices for model input.

Streamlit UI Components:
Dropdown menus and buttons are created for user interaction.

Prediction Function:
A function predict_range is defined to scale the input features, make predictions using the model, and return the predicted range.
Main App Logic:

The main app logic handles user input, invokes the prediction function upon button click, and displays the result.
Notes
Ensure that the pre-trained scaler (scalerEV.pkl) and model (lr.model.pkl) are in the project directory.
Modify the list of counties, car makes, EV types, and CAFV eligibility statuses as needed to match the data used during model training.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgements:
Thanks to the open-source community for providing the libraries and tools used in this project.
Special thanks to any contributors and collaborators.
Contact
For any questions or inquiries, please contact:

Talon Butler
Talonb129@gmail.com
