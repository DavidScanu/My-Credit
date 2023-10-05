#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================================================================
# Created By   : Charley ∆. Lebarbier
# Date Created : Wednesday 04 Oct. 2023
# ==============================================================================
# Streamlit Main
# ==============================================================================


import streamlit as st

from functions import *


## -- Config
st.set_page_config(page_title='My-Credit : Simulation de crédit', 
                   page_icon="assets/favicon-32x32.png",
                   layout='wide')

## -- Background (if we want it)
# set_background("assets/background-pawel-czerwinski.jpg")


## -- Form
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    with st.form("My-Credit"):
        head1, head2, head3 = st.columns([1, 1, 1])

        with head2:
            st.header("My-Credit")

        st.markdown("----", unsafe_allow_html=True)

        st.markdown(
            """
            <div style="text-align:center">
                <h4>INFORMATIONS PERSONNELLES</h4>
            </div>
            """, unsafe_allow_html=True
        )

        age = st.slider('Votre âge :', 18, 130, 25)

        marital = st.radio("Situation Maritale", ["Célibataire", "Marié.e", "Divorcé.e"], horizontal=True)
        education = st.radio("Votre niveau d'étude :", ["Inconnu", "secondaire", "primaire", "tertiaire"], horizontal=True)

        job = st.selectbox("emploi",
            ("admin.", "inconnu", "chômeur", "gestion", "femme de ménage", 
             "entrepreneur", "étudiant", "col bleu", "indépendant", "retraité", 
             "technicien", "services"), 
             index=None, placeholder="Catégorie d'emploi", label_visibility="hidden")

        balance = st.slider('Salaire Moyen Annuel :', min_value=0, max_value=100_000, value=30_000)

        subcol1, subcol2, subcol3 = st.columns([1, 1, 1])
        with subcol1:
            default = st.toggle('Crédit en défaut')
        with subcol2:
            housing = st.toggle('Prêt Logement')
        with subcol3:
            loan = st.toggle('Prêt Personnel')

        st.markdown("----", unsafe_allow_html=True)
        st.markdown(
            """
            <div style="text-align:center; margin-bottom:20px;">
                <h4>CONTACT AVEC NOUS</h4>
            </div>
            """, unsafe_allow_html=True
        )

        pdays = st.toggle('Avez vous été contactés par nos services ?')
        contact = st.radio("contact_type", ["inconnu", "téléphone", "cellulaire"], 
                                horizontal=True, label_visibility="hidden")
        campaign = st.number_input("Nombre de contact cette année", step=1)
        previous = st.number_input("Nombre de contact années passées", step=1)

        st.markdown(
            """
            <div style="margin: 20 0 10 0;">
                <p>Dernier contact</p>
            </div>
            """, unsafe_allow_html=True
        )
        day_col, month_col = st.columns([1, 1])
        with day_col:
            day = st.selectbox("day",
                ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", 
                "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", 
                "24", "25", "26", "27", "28", "29", "30", "31"),
                index=None, placeholder="jour", label_visibility="hidden")

        with month_col:
            month = st.selectbox("month",
                ("jan", "feb", "mar", "apr", "may", "jun", 
                "jul", "aug", "sep", "oct", "nov", "dec"),
                index=None, placeholder="mois", label_visibility="hidden")

        duration = st.number_input("Durée du contact (en seconde)", step=10)

        colF1,colF2,colF3 = st.columns([2, 1, 2])
        with colF2:
            if st.form_submit_button("Valider"):
                with st.spinner("Wait a minute"):
                    result = send_to_api(age, job, marital, education, default, 
                        balance, housing, loan, contact, day, month, duration, 
                        campaign, pdays, previous)


