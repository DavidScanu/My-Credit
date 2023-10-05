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


## -- Page Config
st.set_page_config(page_title='My-Credit : Simulation de crédit', 
                   page_icon="assets/favicon-32x32.png",
                   layout='wide')

## -- Background (if we want it)
# set_background("assets/background-pawel-czerwinski.jpg")


if 'init_form' not in st.session_state:
    st.session_state.init_form = True

if st.session_state.init_form:
        forms()
else:
    response_page()
