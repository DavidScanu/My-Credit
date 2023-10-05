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

    if marital == "Marié.e": marital = "marié"
    elif marital == "Divorcé.e": marital = "divorcé"

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

    print(for_predict)
    # response = requests.post('http://', json=for_predict)

    # return response


def display_score():
    pass