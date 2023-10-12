# -*- coding: utf-8 -*-


import pickle
import streamlit as st



# Load the saved model from Google Drive
with open("random_forest_classifier_model.pkl", "rb") as f:
    model = pickle.load(f)

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py

def welcome():
  return Hi

def predict_financial_distress(sector, shareholder_concentration, CEO_duality,
       corporate_borrowing, independence_indicator, retained_earnings,
       board_of_directors_size, director_renumeration, company_age,
       interest_paid):

    prediction = model.predict([[sector, shareholder_concentration, CEO_duality,
       corporate_borrowing, independence_indicator, retained_earnings,
       board_of_directors_size, director_renumeration, company_age,
       interest_paid]])
    print(prediction)
    return prediction

def main():
    # Webpage title
    st.title("Financial Distress Prediction")

    # Front end elements of the web page
    # The font and background color, padding, and text to be displayed
    html_temp = """
    <div style ="background-color: blue; padding: 13px">
    <h1 style ="color: black; text-align: center;">Streamlit Financial Distress Prediction ML App</h1>
    </div>
    """

    # Display the front end aspects
    st.markdown(html_temp, unsafe_allow_html=True)

    # Data required to make the prediction
    sector = st.selectbox("SECTOR: Business Services-2, Construction-6, Mining & Extraction-12, [Chemicals, Petroleum, Rubber & Plastic]-3, Wholesale-24, [Industrial, Electric & Electronic Machinery]-8, Computer Software -5, [Travel, Personal & Leisure]-21, Retail-17,[Transport, Freight & Storage]-20, [Metals & Metal Products]-11, [Food & Tobacco Manufacturing]-7, Property Services-15, [Biotechnology and Life Sciences]-1,[Public Administration, Education, Health Social Services]-16, Communications-4, [Printing & Publishing]-14, Utilities-22, [Transport Manufacturing]-19, [Media & Broadcasting]-10, [Leather, Stone, Clay & Glass products]-9, [Agriculture, Horticulture & Livestock]-0, Miscellaneous Manufacturing-13, [Textiles & Clothing Manufacturing]-18, [Wood, Furniture & Paper Manufacturing]-25, Waste Management & Treatment-23", [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
    shareholder_concentration = st.number_input('Shareholder Concentration in percentage(%):')
    CEO_duality = st.selectbox('Does the CEO of your company also serve as the chairman of the board of directors? (0 = NO, 1 = YES):', [0, 1])
    corporate_borrowing = st.selectbox('Corporate Borrowing (0 = NO, 1 = YES):', [0, 1])
    independence_indicator = st.number_input('Independence Indicator (on a scale of 1-10):', min_value=1, max_value=10)
    retained_earnings = st.number_input('Retained Earnings (£)')
    board_of_directors_size = st.number_input('Board of Directors Size (in Figures):')
    director_renumeration = st.number_input('Director Remuneration (in million Euros (£million):)')
    company_age = st.number_input('Company Age (in years)')
    interest_paid = st.number_input('Interest Paid (£)')

    if st.button("Predict"):
        # Call the function that predicts financial distress
        prediction_result = predict_financial_distress(sector, shareholder_concentration, CEO_duality,
       corporate_borrowing, independence_indicator, retained_earnings,
       board_of_directors_size, director_renumeration, company_age,
       interest_paid)

        if prediction_result == 1:
            result = 'Warning: Financial Distress Detected'
        else:
            result = 'No Indication of Financial Distress Detected'

        st.success(result)

if __name__ == '__main__':
    main()


