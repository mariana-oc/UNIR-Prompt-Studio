import streamlit as st

from knowledge.looks import LOOKS


def render_sidebar():
    with st.sidebar:
        st.markdown('<div class="sidebar-section-label">Curso</div>', unsafe_allow_html=True)
        url = st.text_input("Link UNIR", placeholder="https://www.unir.net/...")
        manual_course = st.text_input("Nombre manual", placeholder="Solo si el link falla")

        st.markdown('<div class="sidebar-section-label">Parámetros</div>', unsafe_allow_html=True)
        target = st.radio("Target", ["Mujeres", "Hombres", "Mixto"], horizontal=True)
        age = st.selectbox("Edad visual", ["20 a 30", "25 a 35", "25 a 40", "30 a 45"], index=1)
        look = st.selectbox("Look & Feel", list(LOOKS.keys()), index=0)

        st.markdown('<div class="generate-action"></div>', unsafe_allow_html=True)
        generate = st.button("Generate Variables", use_container_width=True)
        st.caption("Los resultados se guardan automáticamente en data/history.xlsx")

        st.markdown(
            """
            <div class="instruction-panel instruction-panel--footer">
              <div class="instruction-panel__title">Cómo funciona</div>
              <ol>
                <li>Pega el link del curso UNIR.</li>
                <li>Completa target, edad visual y look &amp; feel.</li>
                <li>Genera los bloques AZUL y VERDE.</li>
                <li>Copia cada bloque y pégalo en Magnific.</li>
              </ol>
            </div>
            """,
            unsafe_allow_html=True,
        )

    return url, manual_course, target, age, look, generate
