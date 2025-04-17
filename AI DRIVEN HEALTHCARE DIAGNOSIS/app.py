import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Change Name & Logo
st.set_page_config(page_title="Diagnosis", page_icon="⚕️")

# Hiding Streamlit add-ons
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Adding Background Image
background_image_url = "https://i.postimg.cc/G3WQF5Jr/ai-healthcare.png"

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url({background_image_url});
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stAppViewContainer"]::before {{
content: "";
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
background-color: rgba(0, 0, 0, 0.7);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Load the saved models
models = {
    'diabetes': pickle.load(open('Models/diabetes_model.sav', 'rb')),
    'heart_disease': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('Models/parkinsons_model.sav', 'rb')),
    'lung_cancer': pickle.load(open('Models/lungs_disease_model.sav', 'rb')),
    'thyroid': pickle.load(open('Models/Thyroid_model.sav', 'rb'))
}

# Create a dropdown menu for disease prediction
st.markdown("<label style='color: pink; font-size: 20px; font-weight: bold;'>Select a Disease to Predict</label>", unsafe_allow_html=True)

selected = st.selectbox(
    '',
    ['Diabetes Prediction',
     'Heart Disease Prediction',
     'Parkinsons Prediction',
     'Lung Cancer Prediction',
     'Hypo-Thyroid Prediction']
)


def display_input(label, tooltip, key, type="text"):
    if type == "text":
        return st.text_input(label, key=key, help=tooltip)
    elif type == "number":
        return st.number_input(label, key=key, help=tooltip, step=1)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    import streamlit as st

    st.markdown("<h1 style='color: black;'>Diabetes</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: pink; font-size:18px;'>Enter the following details to predict diabetes:</p>", unsafe_allow_html=True)

    #st.title('Diabetes')
    #st.write("Enter the following details to predict diabetes:")

    st.markdown("<label style='color: purple; font-size: 18px;'>Number of Pregnancies</label>", unsafe_allow_html=True)
    Pregnancies = display_input('', 'Enter number of times pregnant', 'Pregnancies', 'number')

    st.markdown("<label style='color: purple; font-size: 18px;'>Glucose Level</label>", unsafe_allow_html=True)
    Glucose = display_input('', 'Enter glucose level', 'Glucose', 'number')

    st.markdown("<label style='color: purple; font-size: 18px;'>Blood Pressure value</label>", unsafe_allow_html=True)
    BloodPressure = display_input('', 'Enter blood pressure value', 'BloodPressure', 'number')

    st.markdown("<label style='color: purple; font-size: 18px;'>Skin Thickness value</label>", unsafe_allow_html=True)
    SkinThickness = display_input('', 'Enter skin thickness value', 'SkinThickness', 'number')

    st.markdown("<label style='color: purple; font-size: 18px;'>Insulin Level</label>", unsafe_allow_html=True)
    Insulin = display_input('', 'Enter insulin level', 'Insulin', 'number')

    st.markdown("<label style='color: purple; font-size: 18px;'>BMI value</label>", unsafe_allow_html=True)
    BMI = display_input('', 'Enter Body Mass Index value', 'BMI', 'number')

    st.markdown("<label style='color: purple; font-size: 18px;'>Diabetes Pedigree Function value</label>", unsafe_allow_html=True)
    DiabetesPedigreeFunction = display_input('', 'Enter diabetes pedigree function value', 'DiabetesPedigreeFunction', 'number')

    st.markdown("<label style='color: purple; font-size: 18px;'>Age of the Person</label>", unsafe_allow_html=True)
    Age = display_input('', 'Enter age of the person', 'Age', 'number')


    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        diab_prediction = models['diabetes'].predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
        st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    
    st.markdown("<h1 style='color: black;'>Heart Disease</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: pink; font-size:18px;'>Enter the following details to predict heart disease:</p>", unsafe_allow_html=True)

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Age</label>", unsafe_allow_html=True)
    age = display_input('', 'Enter age of the person', 'age', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Sex (1 = male; 0 = female)</label>", unsafe_allow_html=True)
    sex = display_input('', 'Enter sex of the person', 'sex', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Chest Pain types (0, 1, 2, 3)</label>", unsafe_allow_html=True)
    cp = display_input('', 'Enter chest pain type', 'cp', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Resting Blood Pressure</label>", unsafe_allow_html=True)
    trestbps = display_input('', 'Enter resting blood pressure', 'trestbps', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Serum Cholesterol in mg/dl</label>", unsafe_allow_html=True)
    chol = display_input('', 'Enter serum cholesterol', 'chol', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)</label>", unsafe_allow_html=True)
    fbs = display_input('', 'Enter fasting blood sugar', 'fbs', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Resting Electrocardiographic results (0, 1, 2)</label>", unsafe_allow_html=True)
    restecg = display_input('', 'Enter resting ECG results', 'restecg', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Maximum Heart Rate achieved</label>", unsafe_allow_html=True)
    thalach = display_input('', 'Enter maximum heart rate', 'thalach', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Exercise Induced Angina (1 = yes; 0 = no)</label>", unsafe_allow_html=True)
    exang = display_input('', 'Enter exercise induced angina', 'exang', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>ST depression induced by exercise</label>", unsafe_allow_html=True)
    oldpeak = display_input('', 'Enter ST depression value', 'oldpeak', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Slope of the peak exercise ST segment (0, 1, 2)</label>", unsafe_allow_html=True)
    slope = display_input('', 'Enter slope value', 'slope', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Major vessels colored by fluoroscopy (0-3)</label>", unsafe_allow_html=True)
    ca = display_input('', 'Enter number of major vessels', 'ca', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)</label>", unsafe_allow_html=True)
    thal = display_input('', 'Enter thal value', 'thal', 'number')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        heart_prediction = models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
        st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    
    st.markdown("<h1 style='color: black;'>Parkinson's Disease</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: pink; font-size:18px;'>Enter the following details to predict Parkinson's disease:</p>", unsafe_allow_html=True)


    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>**MDVP:Fo(Hz)**</label>", unsafe_allow_html=True)
    fo = display_input('', 'Enter MDVP:Fo(Hz) value', 'fo', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>**MDVP:Flo(Hz)**</label>", unsafe_allow_html=True)
    fhi = display_input('', 'Enter MDVP:Fhi(Hz) value', 'fhi', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>**MDVP:Fhi(Hz)**</label>", unsafe_allow_html=True)
    flo = display_input('', 'Enter MDVP:Flo(Hz) value', 'flo', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>**MDVP:Jitter(%)**</label>", unsafe_allow_html=True)
    Jitter_percent = display_input('', 'Enter MDVP:Jitter(%) value', 'Jitter_percent', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>**MDVP:Jitter(Abs)**</label>", unsafe_allow_html=True)
    Jitter_Abs = display_input('', 'Enter MDVP:Jitter(Abs) value', 'Jitter_Abs', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>**MDVP:RAP**</label>", unsafe_allow_html=True)
    RAP = display_input('', 'Enter MDVP:RAP value', 'RAP', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>**MDVP:PPQ**</label>", unsafe_allow_html=True)
    PPQ = display_input('', 'Enter MDVP:PPQ value', 'PPQ', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>**Jitter:DDP**</label>", unsafe_allow_html=True)
    DDP = display_input('', 'Enter Jitter:DDP value', 'DDP', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>**MDVP:Shimmer**</label>", unsafe_allow_html=True)
    Shimmer = display_input('', 'Enter MDVP:Shimmer value', 'Shimmer', 'number')                            

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>**MDVP:Shimmer(dB)**</label>", unsafe_allow_html=True)
    Shimmer_dB = display_input('', 'Enter MDVP:Shimmer(dB) value', 'Shimmer_dB', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>**Shimmer:APQ3**</label>", unsafe_allow_html=True)
    APQ3 = display_input('', 'Enter Shimmer:APQ3 value', 'APQ3', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>**Shimmer:APQ5**</label>", unsafe_allow_html=True)
    APQ5 = display_input('', 'Enter Shimmer:APQ5 value', 'APQ5', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>**MDVP:APQ**</label>", unsafe_allow_html=True)
    APQ = display_input('', 'Enter MDVP:APQ value', 'APQ', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>**Shimmer:DDA**</label>", unsafe_allow_html=True)
    DDA = display_input('', 'Enter Shimmer:DDA value', 'DDA', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>**NHR**</label>", unsafe_allow_html=True)
    NHR = display_input('', 'Enter NHR value', 'NHR', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>**HNR**</label>", unsafe_allow_html=True)
    HNR = display_input('', 'Enter HNR value', 'HNR', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>**RPDE**</label>", unsafe_allow_html=True)
    RPDE = display_input('', 'Enter RPDE value', 'RPDE', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>**DFA**</label>", unsafe_allow_html=True)
    DFA = display_input('', 'Enter DFA value', 'DFA', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>**Spread1**</label>", unsafe_allow_html=True)
    spread1 = display_input('', 'Enter spread1 value', 'spread1', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>**Spread2**</label>", unsafe_allow_html=True)
    spread2 = display_input('', 'Enter spread2 value', 'spread2', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>**D2**</label>", unsafe_allow_html=True)
    D2 = display_input('', 'Enter D2 value', 'D2', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>**PPE**</label>", unsafe_allow_html=True)
    PPE = display_input('', 'Enter PPE value', 'PPE', 'number')

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = models['parkinsons'].predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
        st.success(parkinsons_diagnosis)

# Lung Cancer Prediction Page
if selected == "Lung Cancer Prediction":

    st.markdown("<h1 style='color: black;'>Lung Cancer</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: pink; font-size:18px;'>Enter the following details to predict Lung Cancer:</p>", unsafe_allow_html=True)

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Gender (1 = Male; 0 = Female)</label>", unsafe_allow_html=True)
    GENDER = display_input('', 'Enter gender of the person', 'GENDER', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Age</label>", unsafe_allow_html=True)
    AGE = display_input('', 'Enter age of the person', 'AGE', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Smoking (1 = Yes; 0 = No)</label>", unsafe_allow_html=True)
    SMOKING = display_input('', 'Enter if the person smokes', 'SMOKING', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Yellow Fingers (1 = Yes; 0 = No)</label>", unsafe_allow_html=True)
    YELLOW_FINGERS = display_input('', 'Enter if the person has yellow fingers', 'YELLOW_FINGERS', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Anxiety (1 = Yes; 0 = No)</label>", unsafe_allow_html=True)
    ANXIETY = display_input('', 'Enter if the person has anxiety', 'ANXIETY', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Peer Pressure (1 = Yes; 0 = No)</label>", unsafe_allow_html=True)
    PEER_PRESSURE = display_input('', 'Enter if the person is under peer pressure', 'PEER_PRESSURE', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Chronic Disease (1 = Yes; 0 = No)</label>", unsafe_allow_html=True)
    CHRONIC_DISEASE = display_input('', 'Enter if the person has a chronic disease', 'CHRONIC_DISEASE', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Fatigue (1 = Yes; 0 = No)</label>", unsafe_allow_html=True)
    FATIGUE = display_input('', 'Enter if the person experiences fatigue', 'FATIGUE', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Allergy (1 = Yes; 0 = No)</label>", unsafe_allow_html=True)
    ALLERGY = display_input('', 'Enter if the person has allergies', 'ALLERGY', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Wheezing (1 = Yes; 0 = No)</label>", unsafe_allow_html=True)
    WHEEZING = display_input('', 'Enter if the person experiences wheezing', 'WHEEZING', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Alcohol Consuming (1 = Yes; 0 = No)</label>", unsafe_allow_html=True)
    ALCOHOL_CONSUMING = display_input('', 'Enter if the person consumes alcohol', 'ALCOHOL_CONSUMING', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Coughing (1 = Yes; 0 = No)</label>", unsafe_allow_html=True)
    COUGHING = display_input('', 'Enter if the person experiences coughing', 'COUGHING', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Shortness Of Breath (1 = Yes; 0 = No)</label>", unsafe_allow_html=True)
    SHORTNESS_OF_BREATH = display_input('', 'Enter if the person experiences shortness of breath', 'SHORTNESS_OF_BREATH', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Swallowing Difficulty (1 = Yes; 0 = No)</label>", unsafe_allow_html=True)
    SWALLOWING_DIFFICULTY = display_input('', 'Enter if the person has difficulty swallowing', 'SWALLOWING_DIFFICULTY', 'number')

    st.markdown("<label style='color: darkred; font-size: 16px; font-weight: bold;'>Chest Pain (1 = Yes; 0 = No)</label>", unsafe_allow_html=True)
    CHEST_PAIN = display_input('', 'Enter if the person experiences chest pain', 'CHEST_PAIN', 'number')


    lungs_diagnosis = ''
    if st.button("Lung Cancer Test Result"):
        lungs_prediction = models['lung_cancer'].predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
        lungs_diagnosis = "The person has lung cancer disease" if lungs_prediction[0] == 1 else "The person does not have lung cancer disease"
        st.success(lungs_diagnosis)

# Hypo-Thyroid Prediction Page
if selected == "Hypo-Thyroid Prediction":
   
    st.markdown("<h1 style='color: black;'>Hypo-Thyroid</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: pink; font-size:18px;'>Enter the following details to predict Hypo-Thyroid:</p>", unsafe_allow_html=True)

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>Age</label>", unsafe_allow_html=True)
    age = display_input('', 'Enter age of the person', 'age', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>Sex (1 = Male; 0 = Female)</label>", unsafe_allow_html=True)
    sex = display_input('', 'Enter sex of the person', 'sex', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>On Thyroxine (1 = Yes; 0 = No)</label>", unsafe_allow_html=True)
    on_thyroxine = display_input('', 'Enter if the person is on thyroxine', 'on_thyroxine', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>TSH Level</label>", unsafe_allow_html=True)
    tsh = display_input('', 'Enter TSH level', 'tsh', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>T3 Measured (1 = Yes; 0 = No)</label>", unsafe_allow_html=True)
    t3_measured = display_input('', 'Enter if T3 was measured', 't3_measured', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>T3 Level</label>", unsafe_allow_html=True)
    t3 = display_input('', 'Enter T3 level', 't3', 'number')

    st.markdown("<label style='color: purple; font-size: 16px; font-weight: bold;'>TT4 Level</label>", unsafe_allow_html=True)
    tt4 = display_input('', 'Enter TT4 level', 'tt4', 'number')

    thyroid_diagnosis = ''
    if st.button("Thyroid Test Result"):
        thyroid_prediction = models['thyroid'].predict([[age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]])
        thyroid_diagnosis = "The person has Hypo-Thyroid disease" if thyroid_prediction[0] == 1 else "The person does not have Hypo-Thyroid disease"
        st.success(thyroid_diagnosis)
