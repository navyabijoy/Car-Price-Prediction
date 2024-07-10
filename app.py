import pandas as pd
import streamlit as st
import datetime
import joblib 

# Load the model once at the start of the script
def load_model():
    with open('car_price_prediction.pkl', 'rb') as f:
        model = joblib.load(f)  # Use joblib.load to load the model
    return model

rf_model = load_model()

def main():
    html_temp = """
        <div style="background-color:white;padding: 16px; border-radius: 20px;">
            <h2 style="color: #101D6B;text-align:center; margin-bottom: 20px;">Car Price Prediction</h2>
        </div>
    """
   
    st.markdown(html_temp, unsafe_allow_html=True)
    st.markdown("\n######")
    
    Car_Name = st.selectbox("Car Name:",['ritz', 'sx4', 'ciaz', 'wagon r', 'swift', 'vitara brezza',
       's cross', 'alto 800', 'ertiga', 'dzire', 'alto k10', 'ignis',
       '800', 'baleno', 'omni', 'fortuner', 'innova', 'corolla altis',
       'etios cross', 'etios g', 'etios liva', 'corolla', 'etios gd',
       'camry', 'land cruiser', 'Royal Enfield Thunder 500',
       'UM Renegade Mojave', 'KTM RC200', 'Bajaj Dominar 400',
       'Royal Enfield Classic 350', 'KTM RC390', 'Hyosung GT250R',
       'Royal Enfield Thunder 350', 'KTM 390 Duke ',
       'Mahindra Mojo XT300', 'Bajaj Pulsar RS200',
       'Royal Enfield Bullet 350', 'Royal Enfield Classic 500',
       'Bajaj Avenger 220', 'Bajaj Avenger 150', 'Honda CB Hornet 160R',
       'Yamaha FZ S V 2.0', 'Yamaha FZ 16', 'TVS Apache RTR 160',
       'Bajaj Pulsar 150', 'Honda CBR 150', 'Hero Extreme',
       'Bajaj Avenger 220 dtsi', 'Bajaj Avenger 150 street',
       'Yamaha FZ  v 2.0', 'Bajaj Pulsar  NS 200', 'Bajaj Pulsar 220 F',
       'TVS Apache RTR 180', 'Hero Passion X pro', 'Bajaj Pulsar NS 200',
       'Yamaha Fazer ', 'Honda Activa 4G', 'TVS Sport ',
       'Honda Dream Yuga ', 'Bajaj Avenger Street 220',
       'Hero Splender iSmart', 'Activa 3g', 'Hero Passion Pro',
       'Honda CB Trigger', 'Yamaha FZ S ', 'Bajaj Pulsar 135 LS',
       'Activa 4g', 'Honda CB Unicorn', 'Hero Honda CBZ extreme',
       'Honda Karizma', 'Honda Activa 125', 'TVS Jupyter',
       'Hero Honda Passion Pro', 'Hero Splender Plus', 'Honda CB Shine',
       'Bajaj Discover 100', 'Suzuki Access 125', 'TVS Wego',
       'Honda CB twister', 'Hero Glamour', 'Hero Super Splendor',
       'Bajaj Discover 125', 'Hero Hunk', 'Hero  Ignitor Disc',
       'Hero  CBZ Xtreme', 'Bajaj  ct 100', 'i20', 'grand i10', 'i10',
       'eon', 'xcent', 'elantra', 'creta', 'verna', 'city', 'brio',
       'amaze', 'jazz'])
    Present_Price = st.slider("Current Price of the Car (in Lakhs)", 2.0, 25.0)
    Driven_kms = st.number_input("Distance Driven (kms)", 100, 50000000, step=100)
    s1 = st.selectbox("Fuel Type", ('Petrol', 'Diesel', 'CNG'))

    if s1 == "Petrol":
        Fuel_Type = 0
    elif s1 == "Diesel":
        Fuel_Type = 1
    elif s1 == "CNG":
        Fuel_Type = 2

    s2 = st.selectbox("Dealer or Individual", ('Dealer', 'Individual'))

    if s2 == "Dealer":
        Selling_type = 0
    elif s2 == "Individual":
        Selling_type = 1
    
    s3 = st.selectbox("Transmission", ('Manual', 'Automatic'))

    if s3 == "Manual":
        Transmission = 0
    elif s3 == "Automatic":
        Transmission = 1
    
    Owner = st.slider("Number of Owners:", 0, 3)

    date_time = datetime.datetime.now()
    years = st.number_input("In which year was the car purchased?", 1990, date_time.year)

    Year = date_time.year - years 


    if st.button("Predict"):
        try:
            pred123 = rf_model.predict([[Year, Present_Price, Driven_kms, Fuel_Type, Selling_type, Transmission, Owner]])
            st.write(f"### The predicted selling price for the car is : Rs. {pred123[0]:.2f} lakhs")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

if __name__ == '__main__':
    main()



# # import pandas as pd
# import streamlit as st
# import datetime
# import pickle
# from sklearn.ensemble import RandomForestRegressor

# # Load the model

# rf_model = RandomForestRegressor(random_state=17)

# def main():
#     html_temp = """
#         <div style = "background-color:white;padding: 16px; border-radius: 20px;">
#         <h2 style = "color: #101D6B;text-align:center;"> Car Price Prediction
#         </div>"""
   
#     st.markdown(html_temp, unsafe_allow_html = True)
#     st.markdown("\n######")
#     Present_Price = st.number_input("Current Price of the Car (in Lakhs)", 2.5, 25.0, step = 1.0)
#     Driven_kms  = st.number_input("Distance Driven (kms)", 100, 50000000, step = 100)
#     s1 = st.selectbox("Fuel Type",('Petrol','Diesel','CNG'))

#     if s1 == "Petrol":
#         Fuel_Type = 0
#     elif s1 == "Diesel":
#         Fuel_Type =1
#     elif s1 == "CNG":
#         Fuel_Type = 2

#     s2 = st.selectbox("Dealer or Individual",('Dealer','Individual'))

#     if s2 == "Dealer":
#         Selling_type = 0
#     elif s2 == "Individual":
#         Selling_type = 1
    
#     s3 = st.selectbox("Transmission",('Manual','Automatic'))

#     if s3 == "Manual":
#         Transmission = 0
#     elif s3 == "Automatic":
#         Transmission = 1
    
#     Owner = st.slider("Number of Owners:",0,3)

#     date_time = datetime.datetime.now()
#     years = st.number_input("In which year was the car purchased?", 1990, date_time.year )

#     Year = date_time.year - years 
    
   

#     if st.button("Predict"):
#         pickle_in = open("car_price_prediction.pkl", "rb")
#         rf_classifier = pickle.load(pickle_in)

#         pred123 = rf_model.predict([[Year, Present_Price, Driven_kms, Fuel_Type, Selling_type, Transmission, Owner]])

#         st.write(f"""

#         ### The predicted selling price for the car is : Rs. {pred123[0]} lakhs

#         """)


# if __name__ == '__main__':
#     main()