import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏡",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

page_bg = """
<style>

[data-testid="stAppViewContainer"]{
    background-image:url("https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg");
    background-size:cover;
    background-position:center;
    background-attachment:fixed;
}

/* Hide Streamlit menu */
#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

/* Title */

.title{
text-align:center;
font-size:58px;
font-weight:900;
background:linear-gradient(90deg,#FF512F,#DD2476);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

/* Subtitle */

.subtitle{
text-align:center;
font-size:22px;
font-weight:700;
color:white;
text-shadow:2px 2px 6px black;
margin-bottom:30px;
}

/* Hero Card */

.hero{

background:rgba(0,0,0,0.55);

padding:25px;

border-radius:18px;

text-align:center;

margin-bottom:25px;

box-shadow:0px 8px 25px rgba(0,0,0,.4);

}

/* Glass Card */

.card{

background:rgba(255,255,255,.88);

backdrop-filter:blur(10px);

padding:30px;

border-radius:20px;

box-shadow:0px 8px 30px rgba(0,0,0,.35);

}

/* Labels */

label{

font-size:18px!important;

font-weight:bold!important;

}

/* Button */

div.stButton > button{

width:100%;

height:60px;

border-radius:15px;

font-size:22px;

font-weight:bold;

background:#1E8449;

color:white;

transition:0.3s;

}

div.stButton > button:hover{

background:#145A32;

transform:scale(1.04);

}

/* Sidebar */

section[data-testid="stSidebar"]{

background:rgba(20,20,20,.95);

}

/* Footer */

.footer{

text-align:center;

font-size:18px;

color:white;

font-weight:bold;

margin-top:35px;

}

</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🏡 House Price Predictor")

st.sidebar.markdown("---")

st.sidebar.subheader("📊 Model")

st.sidebar.success("Linear Regression")

st.sidebar.metric("R² Score","0.634")

st.sidebar.metric("Features","3")

st.sidebar.metric("Training Samples","1460")

st.sidebar.markdown("---")

st.sidebar.subheader("📌 Features Used")

st.sidebar.write("✅ Living Area")

st.sidebar.write("✅ Bedrooms")

st.sidebar.write("✅ Bathrooms")

st.sidebar.markdown("---")

st.sidebar.subheader("👨‍💻 Developer")

st.sidebar.info("Chirag Kaliyar")

# ---------------- LOAD MODEL ---------------- #

model = joblib.load("model.pkl")

# ---------------- TITLE ---------------- #

st.markdown("<h1 class='title'>🏡 House Price Prediction</h1>",unsafe_allow_html=True)

st.markdown(
"<p class='subtitle'>Predict House Prices using Machine Learning</p>",
unsafe_allow_html=True
)

# ---------------- HERO ---------------- #

st.markdown("""
<div class='hero'>

<h2 style='color:white;'>

Find Your Dream Home's Estimated Price

</h2>

<p style='color:white;font-size:19px;'>

Enter the property details below and let our Machine Learning model estimate its market value.

</p>

</div>

""",unsafe_allow_html=True)

# ---------------- INPUT CARD ---------------- #

st.markdown("<div class='card'>",unsafe_allow_html=True)

left,right=st.columns(2)

with left:

    living_area=st.slider(
        "🏠 Living Area (Square Feet)",
        500,
        5000,
        1500
    )

    bedrooms=st.slider(
        "🛏 Bedrooms",
        1,
        8,
        3
    )

with right:

    bathrooms=st.slider(
        "🚿 Bathrooms",
        1,
        6,
        2
    )

    st.info("""

### 💡 Tips

• Larger homes usually have higher prices.

• More bathrooms generally increase value.

• Prediction is based on your trained ML model.

""")

predict = st.button("🔮 Predict House Price")

st.markdown("</div>",unsafe_allow_html=True)
# -------------------- PREDICTION --------------------

if predict:

    # Create dataframe for prediction
    input_data = pd.DataFrame(
        {
            "GrLivArea": [living_area],
            "BedroomAbvGr": [bedrooms],
            "FullBath": [bathrooms]
        }
    )

    # Predict
    prediction = model.predict(input_data)[0]

    # Balloons Animation
    st.balloons()

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------- RESULT CARD ---------------- #

    st.markdown(
        f"""
        <div style="
        background:linear-gradient(135deg,#11998e,#38ef7d);
        padding:35px;
        border-radius:20px;
        text-align:center;
        box-shadow:0px 8px 25px rgba(0,0,0,0.45);
        ">

        <h2 style="
        color:white;
        margin-bottom:15px;
        ">
        🏡 Estimated House Price
        </h2>

        <h1 style="
        color:white;
        font-size:55px;
        margin-top:10px;
        margin-bottom:10px;
        ">
        ${prediction:,.2f}
        </h1>

        <p style="
        color:white;
        font-size:20px;
        ">
        Prediction generated using a Linear Regression Model
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # ---------------- PROPERTY SUMMARY ---------------- #

    st.subheader("📋 Property Summary")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "🏠 Living Area",
            f"{living_area} sq.ft"
        )

    with c2:
        st.metric(
            "🛏 Bedrooms",
            bedrooms
        )

    with c3:
        st.metric(
            "🚿 Bathrooms",
            bathrooms
        )

    st.write("")

    # ---------------- MODEL DETAILS ---------------- #

    with st.expander("🤖 About This Prediction"):

        st.markdown("""

### Model Used

**Linear Regression**

---

### Features Used

- 🏠 Living Area (GrLivArea)

- 🛏 Number of Bedrooms (BedroomAbvGr)

- 🚿 Number of Bathrooms (FullBath)

---

### Target

House Selling Price (SalePrice)

---

### Dataset

Kaggle House Prices Dataset

---

### Libraries

- Pandas

- NumPy

- Scikit-Learn

- Streamlit

""")

    st.write("")

    # ---------------- PERFORMANCE ---------------- #

    st.subheader("📈 Model Performance")

    p1, p2 = st.columns(2)

    with p1:
        st.metric("R² Score", "0.634")

    with p2:
        st.metric("Features Used", "3")

    st.success(
        "The model explains approximately 63% of the variation in house prices using the selected features."
    )

    st.write("")

    # ---------------- DOWNLOAD ---------------- #

    result = pd.DataFrame({
        "Living Area":[living_area],
        "Bedrooms":[bedrooms],
        "Bathrooms":[bathrooms],
        "Predicted Price":[round(prediction,2)]
    })

    csv = result.to_csv(index=False)

    st.download_button(
        "📥 Download Prediction Report",
        csv,
        file_name="house_price_prediction.csv",
        mime="text/csv"
    )

    st.write("")

    # ---------------- DISCLAIMER ---------------- #

    st.warning(
        """
⚠️ **Disclaimer**

The predicted value is generated using a Machine Learning model trained on historical housing data.

Actual selling prices may vary depending on several factors not included in this model, such as:

- 📍 Location
- 🌳 Neighborhood
- 🏗 Property Condition
- 🚗 Parking
- 🏊 Amenities
- 📈 Current Market Trends
"""
    )

# ---------------- FOOTER ---------------- #

st.markdown("---")

st.markdown(
"""
<div class="footer">

🏡 House Price Prediction using Machine Learning

<br><br>

👨‍💻 Developed by <b>Chirag Kaliyar</b>

<br>

Python • Scikit-Learn • Streamlit

<br><br>

© 2026 All Rights Reserved

</div>
""",
unsafe_allow_html=True
)
  
