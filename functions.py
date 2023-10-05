#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================================================================
# Created By   : Charley ∆. Lebarbier
# Date Created : Wednesday 04 Oct. 2023
# ==============================================================================
# All Function need to streamlit app
# ==============================================================================

import base64
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


def send_to_api(age, matrimonial, education, work, salary, credit_failure,
                housing_credit, personal_credit, contact, contact_type, 
                nbr_contact_actual, nbr_contact_past, day, month,second):
    """
    Send the data from the form to the fast api for prediction

    Params
    ----------
    age: int - required
    matrimonial: str - required
    education: str - required
    work: str - required
    salary: int - required
    credit_failure: bool - required
    housing_credit: bool - required
    personal_credit: bool - required
    contact: bool - required
    contact_type: str - required
    nbr_contact_actual: int - required
    nbr_contact_past: int - required
    day: int - required
    month: str - required
    second: int - required

    Example
    ------
    >>> send_to_api(59, "Marié.e", "tertiaire", "entrepreneur", 30000, True,
      True, False, True, "téléphone", 2, 5, 4, jul, 60)
    """

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
    print(for_predict)
    # response = requests.post('http://', json=for_predict)

    # return response
