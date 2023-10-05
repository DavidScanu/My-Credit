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
import time

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


def send_to_api(age, marital, education, job, balance, default, housing, loan, 
                contact, pdays, campaign, previous, day, month, duration):
    """
    Send the data from the form to the fast api for prediction

    Params
    ----------
    age: int - required
    marital: str - required
    education: str - required
    job: str - required
    balance: int - required
    default: bool - required
    housing: bool - required
    loan: bool - required
    contact: bool - required
    pdays: str - required
    campaign: int - required
    previous: int - required
    day: int - required
    month: str - required
    duration: int - required

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
        "job": job,
        "balance": balance,
        "default": default,
        "housing": housing,
        "loan": loan,
        "contact": contact,
        "pdays": pdays,
        "campaign": campaign,
        "previous": previous,
        "day": day,
        "month": month,
        "duration": duration
    }

    print(for_predict)
    # response = requests.post('http://', json=for_predict)

    # return response
