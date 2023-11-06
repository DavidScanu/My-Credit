#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================================================================
# Created By   : Charley ∆. Lebarbier
# Date Created : Wednesday 04 Oct. 2023
# ==============================================================================
# All Function need to streamlit app
# ==============================================================================

import base64
import plotly.graph_objects as go
import requests
import streamlit as st

from streamlit_card import card
from streamlit_extras.metric_cards import style_metric_cards


#### -- UTILS UI
def center_radio():
    """Center the radio button on the form"""
    st.markdown("""
        <style>
        .stRadio [role=radiogroup]{
            align-items: center;
            justify-content: center;
        }
        </style>
    """, unsafe_allow_html=True)

def center_checkbox():
    st.markdown("""
        <style>
        [data-baseweb="checkbox"]{
            align-items: center;
            justify-content: center;
        }
        </style>
    """, unsafe_allow_html=True)

def right_button():
    st.markdown("""
        <style>
        [data-testid="baseButton-primary"] {
            display: block;
            float: right;
        }
        </style>
    """, unsafe_allow_html=True)

def set_bg_form():
    st.markdown("""
        <style>
        [data-testid="stForm"] {
            background-color: white;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

def set_bg_popover():
    st.markdown("""
        <style>
        .st-fe .st-fg{
            background-color: white;
            color: black;
        }
        </style>
    """, unsafe_allow_html=True)

def set_background(background_img):
    """Set the app background with image in jpg format

    Params
    -------
    background_img: str - required (web url, or local path)
    >>> set_background("img/background.jpg")
    """

    set_bg = 'jpg'

    st.markdown(
        f"""
            <style>
            .stApp {{
                background-image: url(data:image/{set_bg};base64,{base64.b64encode(open(background_img, "rb").read()).decode()});
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            </style>
        """,
        unsafe_allow_html=True,
    )

def space():
    """Add a break line"""
    st.markdown("""
        <style>
            <br>
        </style>
    """, unsafe_allow_html=True)


#### -- PREDICT

def display_score(score):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = score * 100,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Fiabilité du résultat", 'font': {'size': 24}},
        gauge = {
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "#fca311"},
            'bgcolor': "white",
        }))
    fig.update_layout(height=300)

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

def send_to_api(age, job, marital, education, default, balance, housing, loan, 
                contact, day, month, duration, campaign, pdays, previous):
    """
    Send the data from the form to the fast api for prediction

    Params
    ----------
    age: int - required
    job: str - required
    marital: str - required
    education: str - required
    default: bool - required
    balance: int - required
    housing: bool - required
    loan: bool - required
    contact: bool - required
    day: int - required
    month: str - required
    duration: int - required
    campaign: int - required
    pdays: str - required
    previous: int - required


    Example
    ------
    >>> send_to_api(59, "Marié.e", "tertiaire", "entrepreneur", 30000, True,
      True, False, True, "téléphone", 2, 5, 4, jul, 60)
    """

    ## - Job
    dict_job = {"admin.": "admin.", "inconnu": "unknown", "chômeur": "unemployed", 
                "gestion": "management", "femme de ménage": "housemaid", 
                "entrepreneur": "entrepreneur", "étudiant": "student", 
                "col bleu": "blue-collar", "indépendant": "self-employed", 
                "retraité": "retired", "technicien": "technician", "services": "services"}

    job = dict_job[job]

    ## - Marital
    if marital == "Marié.e": marital = "married"
    elif marital == "Divorcé.e": marital = "divorced"
    elif marital == "Célibataire": marital = "single"

    ## - Education
    if education == "Inconnu": education = "unknown"
    elif education == "secondaire": education = "secondary"
    elif education == "tertiaire": education = "tertiary"
    elif education == "primaire": education = "primary"

    ## - Contact
    if contact == "inconnu": contact = "unknown"
    elif contact == "téléphone": contact = "telephone"
    elif contact == "cellulaire": contact = "cellular"

    ## -- Date
    if day == None: day = 0
    if month == None: month = 'jan'

    ## - Boolean transformation to yes / no string
    default = "yes" if default == True else "no"
    loan = "yes" if loan == True else "no"
    housing = "yes" if housing == True else "no"
    pdays = 1 if pdays == True else 0

    ## - Dictionary creation for send to api
    for_predict = {
        "age": age,
        "job": job,
        "marital": marital,
        "education": education,
        "default": default,
        "balance": balance,
        "housing": housing,
        "loan": loan,
        "contact": contact,
        "day": day,
        "month": month,
        "duration": duration,
        "campaign": campaign,
        "pdays": pdays,
        "previous": previous
    }

    response = requests.post('https://api-isen-g4-6efab73bbf58.herokuapp.com/predict', 
                             json=for_predict)
    response = validation_response(response)

    result = response['prediction']
    score = response['score']

    return result, score

def validation_response(response):
    """Valid the response.status_code, if 200 return the response"""
    if response.status_code == 200:
        return response.json()
    else:
        print("Erreur: ", response.status_code)




# ---------------------------------------------------------------------------- #
## --- FORM PAGE --- ##
def forms():
    """Display the 'My-Credit' form"""

    ## - Config Form
    center_radio()
    center_checkbox()
    set_bg_form()
    set_bg_popover()

    ## -- Form
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        with st.form("My-Credit"):
            st.markdown(
                """
                <div style="text-align:center; margin-bottom:20px;">
                    <h2>💳 Simulation de Crédit 💳</h2>
                </div>
                """, unsafe_allow_html=True
            )

            st.markdown("----", unsafe_allow_html=True)

            st.markdown(
                """
                <div style="text-align:center">
                    <h4>📋 INFORMATIONS PERSONNELLES</h4>
                </div>
                """, unsafe_allow_html=True
            )

            age = st.slider('Votre âge :', 18, 90, 30)

            marital = st.radio("Situation Maritale", ["Célibataire", "Marié.e", "Divorcé.e"],
                horizontal=True, label_visibility='hidden')
            space()

            education = st.radio("Votre niveau d'étude :", ["Inconnu", 
                "secondaire", "primaire", "tertiaire"], horizontal=True)

            job = st.selectbox("emploi",
                ("admin.", "inconnu", "chômeur", "gestion", "femme de ménage", 
                "entrepreneur", "étudiant", "col bleu", "indépendant", "retraité", 
                "technicien", "services"), 
                index=None, placeholder="Catégorie d'emploi", label_visibility="hidden")
            space()

            balance = st.slider('Solde Annuel Moyen:', min_value=-10_000, 
                                max_value=80_000, value=30_000, step=500)

            subcol1, subcol2, subcol3 = st.columns([1, 1, 1])
            with subcol1: default = st.toggle('Crédit en défaut')
            with subcol2: housing = st.toggle('Prêt Logement')
            with subcol3: loan = st.toggle('Prêt Personnel')

            st.markdown("----", unsafe_allow_html=True)
            st.markdown(
                """
                <div style="text-align:center; margin-bottom:20px;">
                    <h4>☎️ CONTACT AVEC NOUS</h4>
                </div>
                """, unsafe_allow_html=True
            )

            pdays = st.toggle('Avez vous été contactés par nos services ?')

            contact = st.radio("contact_type", ["inconnu", "téléphone", "cellulaire"],
                                horizontal=True, label_visibility="hidden")
            space()

            campaign = st.number_input("Nombre de contact cette année", step=1)
 
            previous = st.number_input("Nombre de contact années passées", step=1)

            day_col, month_col = st.columns([1, 1])
            with day_col:
                day = st.selectbox("day",
                    (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 
                    18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31),
                    index=None, placeholder="jour du dernier contact", 
                    label_visibility="hidden")

            with month_col:
                month = st.selectbox("month",
                    ("jan", "feb", "mar", "apr", "may", "jun", 
                    "jul", "aug", "sep", "oct", "nov", "dec"),
                    index=None, placeholder="mois du dernier contact", 
                    label_visibility="hidden")

            duration = st.number_input("Durée du contact (en seconde)", 
                                       max_value=5_000, step=5)

            colF1,colF2,colF3 = st.columns([2, 1, 2])
            with colF2:
                space()
                if st.form_submit_button("Valider"):
                    if (job is not None) and (day is not None) and (month is not None):
                        with st.spinner("Wait a minute"):
                            st.session_state['result'], st.session_state['score'] = send_to_api(age, job, marital, education, 
                                default, balance, housing, loan, contact, day, 
                                month, duration, campaign, pdays, previous)
                    else:
                        st.error("Un des champs suivants n'est pas rempli: Catégorie d'emploi, jour et mois")
                        st.stop()

                    ## - pass to result
                    st.session_state.init_form = False
                    st.rerun()




# ---------------------------------------------------------------------------- #
## --- RESPONSE PAGE --- ##
def response_page():
    ## - Config
    right_button()

    ## ------ ##
    st.button("Refaire une simulation", type="primary")
    if st.button:
        st.session_state.init_form = True
        st.rerun

    if st.session_state.result == 1:
        card(
            title="Yeah",
            text="Selon votre situation, c'est good",
        )
        display_score(st.session_state.score)
    else:
        card(
            title="Désolé",
            text="Votre situation ne le permet pas",
        )
        display_score(st.session_state.score)


    col1, col2, col3 = st.columns(3)
    col1.metric(label="Duration", value=800)
    col2.metric(label="Balance", value=790)
    col3.metric(label="Age", value=760)
    style_metric_cards()


