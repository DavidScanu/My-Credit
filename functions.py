#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================================================================
# Created By   : Charley ∆. Lebarbier
# Date Created : Wednesday 04 Oct. 2023
# ==============================================================================
# All Function need to streamlit app
# ==============================================================================

import base64
import json
import requests
import streamlit as st


## --- APP --- ##
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


def create_JSON(age, matrimonial, education, work, salary, credit_failure,
                housing_credit, personal_credit, contact, contact_type, 
                nbr_contact_actual, nbr_contact_past, day, month,second):

    if matrimonial == "Marié.e": matrimonial = "marié"
    elif matrimonial == "Divorcé.e": matrimonial = "divorcé"

    for_predict = {
        "age": age, 
        "matrimonial": matrimonial,
        "education": education,
        "work": work,
        "salary": salary, 
        "credit_failure": credit_failure,
        "housing_credit": housing_credit, 
        "personal_credit": personal_credit, 
        "contact": contact, 
        "contact_type": contact_type, 
        "nbr_contact_actual": nbr_contact_actual, 
        "nbr_contact_past": nbr_contact_past,
        "day": day,
        "month": month,
        "second": second
    }

    reponse = requests.post('http://', json=for_predict)

    return reponse
