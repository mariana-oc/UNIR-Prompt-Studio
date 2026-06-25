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
        '<div class="empty-state">'
        '<strong>Ready to generate.</strong>'
        '<p>Paste a UNIR course URL, configure the visual parameters, and click '
        '<strong>Generate Variables</strong>.</p>'
        '<div class="empty-state-tags">'
        '<span class="empty-state-tag empty-state-tag--green">Información específica</span>'
        '<span class="empty-state-tag empty-state-tag--blue">Características de grupo</span>'
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )


def render_course_pill(course_name: str) -> None:
    st.markdown(
        f'<div class="course-pill">{course_name}</div>',
        unsafe_allow_html=True,
    )
