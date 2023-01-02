# Diagnose

This project is submitted for [PoweringSTEMHacks](https://poweringstemhacks.devpost.com/)

---

**Melanoma** is a type of cancer that can be deadly if not detected early. It accounts for 75% of skin cancer deaths. A solution which can evaluate images and alert the dermatologists about the presence of melanoma has the potential to reduce a lot of manual effort needed in diagnosis.

Our application detects the following diseases:
- Actinic keratosis
- Basal cell carcinoma
- Dermatofibroma
- Melanoma
- Nevus
- Pigmented benign keratosis
- Seborrheic keratosis
- Squamous cell carcinoma
- Vascular lesion

---

# Technology Stack Used:

<a href="#" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original-wordmark.svg" alt="html5" width="40" height="40"/> </a>

- Streamlit
- Machine Learning

### APIs used

- [Google maps API for places](https://maps.googleapis.com): Our website will calculate latitude and longitude values of current location and it will fetch all nearby 
dermatologists.

---

## How it works?

Our application utilizes machine learning to predict what skin disease you may have, from just your skin images!
We then recommend you specialized doctors based on your type of disease, if our model predicts you're healthy we'll 
suggest you a general doctor.

---

## Installation/Execution

1. Create a virtual environment

    ```bash
    python3 -m venv venv
    ```

2. Activate the virtual environment

    for Linux and Mac:

    ```bash
    source venv/bin/activate
    ```

    for Windows:

    ```bash
    venv\Scripts\activate
    ```

3. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

4. Run the app

    ```bash
    streamlit run ./About.py
    ```
    
    ---
    
## Challenges we ran into 
1. Fetching, Installing Dependencies and Fixing Backend Errors.
2. Creating a model for detecting Melanoma and various other skin diseases than can lead to skin cancer.

## Accomplishments that we're proud of 
We were able to successfully create an application to solve problems for those who are suffering from skin cancer mainly **Melanoma**. Team Work was something we were really proud of specially when we had errors we worked together to fix them.

## What's next for Diagnose?
We plan to finish this challenge and create a complete web application and help the user to experience the best out of it.

## Team Members:
<a href="https://github.com/coder12git/PoweringSTEMHacks/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=coder12git/PoweringSTEMHacks"/>
</a>


## Show your support

Please ⭐ this repository if this project helped you!
