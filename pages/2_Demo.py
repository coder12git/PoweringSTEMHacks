import streamlit as st
import tensorflow as tf

@st.cache
def load_model():
    model = tf.keras.models.load_model("./model/model.h5")
    return model


st.title("Demo")

pic = st.file_uploader(
    label="Upload a picture",
    type=["png", "jpg", "jpeg"],
    accept_multiple_files=False,
    help="Upload a picture of your skin to get a diagnosis",
)

if st.button("Predict"):
    if pic != None:
        st.header("Results")

        cols = st.columns(2)
        with cols[0]:
            st.image(pic, caption="Uploaded Image", use_column_width=True)

        with cols[1]:
            labels = [
                "actinic keratosis",
                "basal cell carcinoma",
                "dermatofibroma",
                "melanoma",
                "nevus",
                "pigmented benign keratosis",
                "seborrheic keratosis",
                "squamous cell carcinoma",
                "vascular lesion",
            ]
            model = load_model()
            image = pic.getvalue()
            result = model.predict(image)
            st.write(result)
            # st.info(labels[result].title())

    else:
        st.error("Please upload an image")
