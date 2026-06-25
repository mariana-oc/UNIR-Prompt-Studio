import streamlit as st

from components.cards import render_section_card
from components.layout import render_course_pill, render_empty_state, render_hero, render_sticky_header
from components.sidebar import render_sidebar
from core.config import ensure_dirs
from core.course import fetch_course
from core.generator import generate_blocks, sections_to_text
from core.history import save_history
from styles.theme import inject_theme

ensure_dirs()

st.set_page_config(
    page_title="UNIR Prompt Studio",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_theme()

url, manual_course, target, age, look, generate = render_sidebar()

render_sticky_header()
render_hero()

if generate:
    course_name, course_text = fetch_course(url) if url else ("Curso UNIR", "")
    if manual_course.strip():
        course_name = manual_course.strip()
        course_text += " " + course_name
    azul_sections, verde_sections = generate_blocks(course_name, course_text, target, age, look)
    azul_text = sections_to_text("AZUL", azul_sections)
    verde_text = sections_to_text("VERDE", verde_sections)
    st.session_state["course_name"] = course_name
    st.session_state["azul_sections"] = azul_sections
    st.session_state["verde_sections"] = verde_sections
    st.session_state["azul_text"] = azul_text
    st.session_state["verde_text"] = verde_text
    save_history(course_name, url, target, age, look, azul_text, verde_text)

if "azul_sections" not in st.session_state:
    render_empty_state()
else:
    st.markdown('<div class="results-section">', unsafe_allow_html=True)
    render_course_pill(st.session_state.get("course_name", "Curso UNIR"))
    col1, col2 = st.columns(2, gap="large")
    with col1:
        render_section_card(
            "Información específica",
            "Variable · VERDE",
            "green",
            st.session_state["verde_sections"],
            st.session_state["verde_text"],
            "verde_copy_text",
        )
    with col2:
        render_section_card(
            "Características de grupo",
            "Constantes · AZUL",
            "blue",
            st.session_state["azul_sections"],
            st.session_state["azul_text"],
            "azul_copy_text",
        )
