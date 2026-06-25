import streamlit as st


def render_sticky_header() -> None:
    st.markdown(
        """
        <div class="sticky-header">
          <div class="sticky-header__inner">
            <div class="logo-mark-text">UNIR</div>
            <div class="sticky-header__text">
              <span class="sticky-header__title">UNIR Design Tools</span>
              <span class="sticky-header__divider">/</span>
              <span class="sticky-header__sub">Prompt Studio</span>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_hero() -> None:
    st.markdown(
        """
        <div class="hero">
          <h1>Genera variables listas para Magnific</h1>
          <p>
            Pega una titulación de UNIR, define target y look &amp; feel, y obtén los bloques
            <strong>Información específica</strong> y <strong>Características de grupo</strong>.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_empty_state() -> None:
    st.markdown(
        """
        <div class="empty-state">
          <strong>Todavía no hay variables generadas.</strong>
          Usa el panel lateral para pegar un link de UNIR, elegir target y look &amp; feel,
          y pulsa Generate Variables para ver los bloques VERDE y AZUL aquí.
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_course_pill(course_name: str) -> None:
    st.markdown(
        f'<div class="course-pill">Curso activo · {course_name}</div>',
        unsafe_allow_html=True,
    )
