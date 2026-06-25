import streamlit as st

from knowledge.looks import LOOKS

LOOK_DESCRIPTIONS = {
    "Executive": "Corporativo · Business · Estructurado",
    "Editorial": "Elegante · Limpio · Mucho aire",
    "Technical": "Tecnología · Precisión · Digital",
    "Healthcare": "Salud · Confianza · Serenidad",
    "Creative": "Diseño · Color · Energía",
    "Contemporary": "Moderno · Fresco · Versátil",
}


def render_sidebar():
    with st.sidebar:

        st.markdown(
            '<div class="sidebar-section-label">INFORMACIÓN DEL CURSO</div>',
            unsafe_allow_html=True,
        )

        url = st.text_input(
            "Link del curso",
            placeholder="https://www.unir.net/...",
        )

        manual_course = st.text_input(
            "Nombre del manual (opcional)",
            placeholder="Solo si el enlace falla",
        )

        st.divider()

        st.markdown(
            '<div class="sidebar-section-label">CONFIGURACIÓN</div>',
            unsafe_allow_html=True,
        )

        target = st.radio(
            "Target",
            ["Mujeres", "Hombres", "Mixto"],
            horizontal=True,
        )

        age = st.selectbox(
            "Edad visual",
            [
                "20–30",
                "25–35",
                "25–40",
                "30–45",
            ],
            index=1,
        )

        look = st.selectbox(
            "Estilo visual",
            list(LOOKS.keys()),
            index=0,
        )

        st.caption(
            LOOK_DESCRIPTIONS.get(
                look,
                "",
            )
        )

        st.write("")

        generate = st.button(
            "Generate Variables",
            use_container_width=True,
        )

        st.caption(
            "Los prompts se guardan automáticamente en el historial."
        )

    return (
        url,
        manual_course,
        target,
        age,
        look,
        generate,
    )
