import requests
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


st.set_page_config(
    page_title="Skin Cancer",
    page_icon="♋",
    layout="wide",
    initial_sidebar_state="expanded",
)

# lottie_health = load_lottieurl(
#     "https://assets3.lottiefiles.com/private_files/lf30_bftsl4ju.json"
# )
lottie_welcome = load_lottieurl(
    "https://assets1.lottiefiles.com/packages/lf20_puciaact.json"
)
# lottie_hi = load_lottieurl(
#     "https://assets1.lottiefiles.com/packages/lf20_1pxqjqps.json"
# )
lottie_healthy = load_lottieurl(
    "https://assets10.lottiefiles.com/packages/lf20_x1gjdldd.json"
)

st.title("Main Page")
st.subheader("Welcome to team Diagnose!")
st_lottie(lottie_welcome, height=300, key="welcome")
st.header("Melanoma detection at your skin images.")

"""
Melanoma is a type of cancer that can be deadly if not detected early. It accounts for 75% of skin cancer deaths. A solution which can evaluate images and alert the dermatologists about the presence of melanoma has the potential to
reduce a lot of manual effort needed in diagnosis.

Our application detects the following diseases:
* Actinic keratosis,
* Basal cell carcinoma,
* Dermatofibroma,
* Melanoma,
* Nevus,
* Pigmented benign keratosis,
* Seborrheic keratosis,
* Squamous cell carcinoma,
* Vascular lesion.

[Learn More >](https://www.researchgate.net/publication/356093241_Characteristics_of_publicly_available_skin_cancer_image_datasets_a_systematic_review)
"""

with st.container():
    st.write("---")
    cols = st.columns(2)
    with cols[0]:
        st.header("How it works?")
        """
        Our application utilizes machine learning to predict what skin disease you may have, from just your skin images!
        We then recommend you specialized doctors based on your type of disease, if our model predicts you're healthy we'll suggest you a general doctor.
        ##
        [Learn More >](https://www.youtube.com/watch?v=qjx9IkM0_-Y)
        """
    with cols[1]:
        st_lottie(lottie_healthy, height=300, key="healthy")

# st.sidebar.success("Select the page above.")
