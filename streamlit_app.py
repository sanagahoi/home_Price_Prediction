import streamlit as st
from server import util

@st.cache_resource
def load_model():
    util.load_saved_artifacts()
    return util


def main():
    st.title("Bangalore Home Price Predictor")
    st.write("Enter house details below to estimate the price in Bangalore.")

    util_module = load_model()
    locations = util_module.get_location_names()

    location = st.selectbox("Location", sorted(locations))
    total_sqft = st.number_input("Total square feet area", min_value=100.0, max_value=10000.0, value=1000.0, step=50.0)
    bhk = st.selectbox("BHK", [1, 2, 3, 4, 5, 6])
    bath = st.selectbox("Bathrooms", [1, 2, 3, 4, 5, 6])

    if st.button("Estimate Price"):
        price = util_module.get_estimated_price(location, total_sqft, bhk, bath)
        st.success(f"Estimated price: ₹ {price} lakhs")


if __name__ == "__main__":
    main()
