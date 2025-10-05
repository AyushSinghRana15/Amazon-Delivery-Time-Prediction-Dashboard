# Amazon-Delivery-Time-Prediction-Dashboard

## Overview

This project delivers a machine learning-powered dashboard to predict customer order delivery times using agent details, location, weather, traffic conditions, and order attributes. It employs an end-to-end pipeline—from preprocessing to feature selection and Random Forest modeling—deployed with Streamlit for real-time predictions.

## Problem Statement

Accurately forecasting delivery times is vital for operational efficiency and customer satisfaction. This project aims to provide reliable delivery time estimates by leveraging operational, contextual, and environmental data to optimize last-mile logistics.

## Features

- End-to-end data science pipeline: preprocessing, feature selection, model training
- Interactive Streamlit dashboard for instant delivery time predictions
- Focused use of important numeric and categorical (one-hot encoded) features
- User-friendly interface for live input and visualization

## Dataset

The dataset includes:
- Agent and order information (e.g., age, rating, IDs)
- Geographical coordinates (store/drop-off)
- Time stamps (order, pickup, delivery)
- Weather, traffic, vehicle, and order categories (often one-hot encoded)

> Ensure all feature columns are cleaned (no extra spaces) and match pipeline requirements.

## Model

The pipeline uses a Random Forest Regressor, robust data preprocessing, and relevant feature selection based on importance analysis, maximizing predictive accuracy and usability.

## Installation

git clone https://github.com/yourusername/amazon-delivery-time-prediction-dashboard.git

cd amazon-delivery-time-prediction-dashboard 

pip install -r requirements.txt


## Usage

streamlit run app.py

- Enter delivery details and context in the sidebar.
- Click **Predict Delivery Time** to see real-time predictions and results.

## Results

- Model achieves high accuracy (see notebook/evaluation for RMSE, MAE, R²).
- Streamlit dashboard supports live, actionable estimates for end-users and operations teams.

## Example

![Dashboard Screenshot](screenshot.png)

## Contributing

Contributions and suggestions are welcome! Open an issue or submit a pull request.

## License

MIT License

## Acknowledgments

- Original datasets and prior research on delivery time prediction
- scikit-learn, pandas, Streamlit, and open-source contributors

## Screenshot of the dashboard

<img width="1470" height="956" alt="Screenshot 2025-10-05 at 1 30 51 PM" src="https://github.com/user-attachments/assets/b1f6914a-2e6e-495d-8a13-5366f9905c0e" />


