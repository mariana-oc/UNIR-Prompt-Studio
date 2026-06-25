import streamlit as st


def render_sticky_header() -> None:
    st.markdown(
        '<div class="sticky-header">'
        '<div class="sticky-header__inner">'
        '<div class="logo-mark-text">UNIR</div>'
        '<div class="sticky-header__text">'
        '<span class="sticky-header__title">Design Tools</span>'
        '<span class="sticky-header__divider">/</span>'
        '<span class="sticky-header__sub">Prompt Studio</span>'
        '</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )


def render_hero() -> None:
    st.markdown(
        '<div class="hero">'
        '<h1>Prompt generator for UNIR image production</h1>'
        '<p>Generate production-ready prompt variables directly from any UNIR course page.</p>'
        '</div>',
        unsafe_allow_html=True,
    )


def render_empty_state() -> None:
    st.markdown(
        '<div class="instruction-grid">'
        '<div class="instruction-card instruction-card--green">'
        '<div class="instruction-card__number">01</div>'
        '<div class="instruction-card__title">Información específica</div>'
        '<div class="instruction-card__copy">'
        'Bloque variable del prompt. Define actitud, acción, vestimenta y dirección artística. '
        'Se marca en verde porque cambia según el enfoque visual de cada generación.'
        '</div>'
        '</div>'
        '<div class="instruction-card instruction-card--blue">'
        '<div class="instruction-card__number">02</div>'
        '<div class="instruction-card__title">Características de grupo</div>'
        '<div class="instruction-card__copy">'
        'Bloque constante del curso. Define buyer persona, contexto, objetos, composición, identidad, materiales y atmósfera. '
        'Se marca en azul porque sostiene la estructura base de la titulación.'
        '</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )


def render_course_pill(course_name: str) -> None:
    st.markdown(
        f'<div class="course-pill">{course_name}</div>',
        unsafe_allow_html=True,
    )
