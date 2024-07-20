import streamlit as st
import numpy as np
import pandas as pd
import joblib
import itertools

# Load models and scaler
try:
    scaler = joblib.load("scalerEV.pkl")
    models = joblib.load("lr.model.pkl")
    st.write("Models loaded successfully.")
except Exception as e:
    st.error(f"Error loading models: {e}")

def read_list_from_file(filename):
    try:
        with open(filename, 'r') as f:
            items = f.read().splitlines()
        return items
    except Exception as e:
        st.error(f"Error reading file {filename}: {e}")

def create_mapping_dict(items):
    return {item: i for i, item in enumerate(items)}

def predict_range(county_idx, make_idx, ev_type_idx, cafv_eligibility_idx):
    X = np.array([[county_idx, make_idx, ev_type_idx, cafv_eligibility_idx]])
    X_scaled = scaler.transform(X)
    prediction = models.predict(X_scaled)
    return prediction[0]

def batch_predict(counties, car_makes, cafv_options, county_dict, car_makes_dict, cafv_dict):
    combinations = list(itertools.product(counties, car_makes, [0, 1], cafv_options))
    results = []
    for county, make, ev_type, cafv in combinations:
        county_idx = county_dict[county]
        make_idx = car_makes_dict[make]
        ev_type_idx = ev_type
        cafv_eligibility_idx = cafv_dict[cafv]
        prediction = predict_range(county_idx, make_idx, ev_type_idx, cafv_eligibility_idx)
        results.append({
            'County': county,
            'Car Make': make,
            'EV Type': ev_type,
            'CAFV Eligibility': cafv,
            'Predicted Range': prediction
        })
    df = pd.DataFrame(results)
    df.to_csv('predicted_range_full.csv', index=True)
    return df

def main():
    st.title("Electric Range Predictor")

    counties = read_list_from_file('counties.txt')
    car_makes = read_list_from_file('Make.txt')
    cafv_options = ['Eligible', 'Not Eligible', 'Unknown']

    county_dict = create_mapping_dict(counties)
    car_makes_dict = create_mapping_dict(car_makes)
    cafv_dict = create_mapping_dict(cafv_options)

    selected_county = st.selectbox("Select County", counties)
    selected_make = st.selectbox("Select Car Make", car_makes)
    selected_ev_type = st.number_input("Enter EV Type (0 or 1)", min_value=0, max_value=1, step=1)
    selected_cafv_eligibility = st.selectbox("Select CAFV Eligibility", cafv_options)

    if st.button("Calculate Range"):
        county_idx = county_dict[selected_county]
        make_idx = car_makes_dict[selected_make]
        ev_type_idx = selected_ev_type
        cafv_eligibility_idx = cafv_dict[selected_cafv_eligibility]

        prediction = predict_range(county_idx, make_idx, ev_type_idx, cafv_eligibility_idx)
        st.write(f"Predicted electric range: {prediction} miles")

        results = {
            'County': [selected_county],
            'Car Make': [selected_make],
            'EV Type': [selected_ev_type],
            'CAFV Eligibility': [selected_cafv_eligibility],
            'Predicted Range': [prediction]
        }
        if 'results' not in st.session_state:
            st.session_state.results = pd.DataFrame(results)
        else:
            st.session_state.results = pd.concat([st.session_state.results, pd.DataFrame(results)], ignore_index=True)

    if st.button("Export Predictions to CSV"):
        df = batch_predict(counties, car_makes, cafv_options, county_dict, car_makes_dict, cafv_dict)
        st.success("Predictions exported to predicted_range_full.csv")

if __name__ == "__main__":
    main()