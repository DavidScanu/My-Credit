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

        matrimonial = st.radio("Situation Maritale", ["Célibataire", "Marié.e", "Divorcé.e"], horizontal=True)
        education = st.radio("Votre niveau d'étude :", ["Inconnu", "secondaire", "primaire", "tertiaire"], horizontal=True)

        work = st.selectbox("emploi",
            ("admin.", "inconnu", "chômeur", "gestion", "femme de ménage", 
             "entrepreneur", "étudiant", "col bleu", "indépendant", "retraité", 
             "technicien", "services"), 
             index=None, placeholder="Catégorie d'emploi", label_visibility="hidden")

        salary = st.slider('Salaire Moyen Annuel :', min_value=0, max_value=100_000, value=30_000)

        subcol1, subcol2, subcol3 = st.columns([1, 1, 1])
        with subcol1:
            credit_failure = st.toggle('Crédit en défaut')
        with subcol2:
            housing_credit = st.toggle('Prêt Logement')
        with subcol3:
            personal_credit = st.toggle('Prêt Personnel')

        st.markdown("----", unsafe_allow_html=True)
        st.markdown(
            """
            <div style="text-align:center; margin-bottom:20px;">
                <h4>CONTACT AVEC NOUS</h4>
            </div>
            """, unsafe_allow_html=True
        )

        contact = st.toggle('Avez vous été contactés par nos services ?')
        contact_type = st.radio("contact_type", ["inconnu", "téléphone", "cellulaire"], 
                                horizontal=True, label_visibility="hidden")
        nbr_contact_actual = st.number_input("Nombre de contact cette année", step=1)
        nbr_contact_past = st.number_input("Nombre de contact années passées", step=1)

        st.write("Dernier contact")
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

        second = st.number_input("Durée du contact (en seconde)", step=10)

        colF1,colF2,colF3 = st.columns([2, 1, 2])
        with colF2:
            if st.form_submit_button("Valider"):
                submit_button = send_to_api(age, matrimonial, education, work, salary, 
                credit_failure, housing_credit, personal_credit, contact, contact_type, 
                nbr_contact_actual, nbr_contact_past, day, month, second)