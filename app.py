from pathlib import Path
import json
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="State Machine Workshop", page_icon="⚙️", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>
#MainMenu,footer,header {visibility:hidden}
.block-container {padding:0!important;max-width:100%!important}
[data-testid="stAppViewContainer"] {background:#f3f7fb}
</style>""", unsafe_allow_html=True)
folder=Path(__file__).parent
page=(folder/"workshop.html").read_text(encoding="utf-8")
cooling=(folder/"cooling.html").read_text(encoding="utf-8")
page=page.replace("/*COOLING_JSON*/",json.dumps(cooling).replace("</","<\\/"))
components.html(page,height=2350,scrolling=True)
