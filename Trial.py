import streamlit as st

# STYLES FOR MARKDOWN
st.markdown("""
    <style>
    .header1 {
            font-size: 36px;
            text-align: center;
            background-color: green;
            border-radius: 10px;
            padding: 10px;
            color: white;
            text-transform: uppercase;
            font-weight: bold;
    }
    .header2 {
            font-size: 20px;
            text-align: left; 
            font-weight: bold;           
    }
    .subheader {
            font-size: 30px;
            text-align: center;
            font-weight: bold;
    }
    .column {
            background-color: #f0f0f0; /* Set your desired background color */
            border-radius: 10px;
            padding: 8px;
            margin: 3px;
    }
    button{
            background-color: green;
            color:white;
            border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

#HEADER
st.markdown('<p class="header1">Prediction</p>', unsafe_allow_html=True)
st.markdown("<hr style='border: 2px solid rainbow; margin-top: 10px'>", unsafe_allow_html=True)  # Add a rainbow divider

#COLUMNS
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('''
                <div class="column">
                <p class="header2">Current</p>
                <hr style="border: 2px solid green; margin-top:-15px">
                <p class="subheader">80 Amp</p></div>
                ''', unsafe_allow_html=True)

with col2:
    st.markdown('''
                <div class="column">
                <p class="header2">Voltage</p>
                <hr style="border: 2px solid green; margin-top:-15px">
                <p class="subheader">80 Amp</p></div>
                ''', unsafe_allow_html=True)

with col3:
    st.markdown('''
                <div class="column">
                <p class="header2">Temperature</p>
                <hr style="border: 2px solid green; margin-top:-15px;">
                <p class="subheader">80 °C</p></div>
                ''', unsafe_allow_html=True)

with col4:
    st.markdown('''
                <div class="column">
                <p class="header2">Cycle</p>
                <hr style="border: 2px solid green; margin-top:-15px;">
                <p class="subheader">80</p></div>
                ''', unsafe_allow_html=True)

# Add the "Predict" button
predict_button = st.button("Predict")

# Check if the button is clicked
if predict_button:
    # Add your prediction logic here
    st.write("Test.")
    