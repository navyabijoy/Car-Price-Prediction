# Car Price Prediction

This project is a web application that predicts the selling price of a car based on various features like the car's present price, distance driven, fuel type, seller type, transmission type, number of owners, and the year it was purchased. The application is built using Streamlit and a trained machine learning model.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Features](#features)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/car-price-prediction.git
    cd car-price-prediction
    ```

2. Create a virtual environment:
    ```sh
    python -m venv myenv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        myenv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source myenv/bin/activate
        ```

4. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

5. Train the model (if not already trained):
    ```sh
    python train_model.py
    ```

6. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

## Usage

1. Open your browser and go to `https://car-price-prediction-nb.streamlit.app/`.
2. Enter the required information about the car:
    - Name of the Car
    - Current Price of the Car (in Lakhs)
    - Distance Driven (kms)
    - Fuel Type (Petrol, Diesel, CNG)
    - Dealer or Individual
    - Transmission (Manual, Automatic)
    - Number of Owners
    - Year of Purchase
3. Click on the "Predict" button to get the predicted selling price of the car.

## Model Training

The model is trained using a RandomForestRegressor on the provided dataset. To train the model:

1. Load your dataset (e.g., `car_data.csv`).
2. Run the `app.py` script to train and save the model:
    ```sh
    python app.py
    ```

## Features

- Predicts the selling price of a car based on user input.
- Interactive and user-friendly interface built with Streamlit.
- Supports various car features for a comprehensive prediction.

## Dependencies

- Python 3.x
- joblib==1.2.0
- scikit-learn==1.3.2
- streamlit==1.22.0
- pandas
- numpy
- datetime

## Contributing

Contributions are welcome! Please fork this repository and open a pull request to add more features or improve the code.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
