import streamlit as st


def render_sticky_header() -> None:
    st.markdown(
        """
        <div class="sticky-header">
            <div class="sticky-header__inner">

                <div class="logo-mark-text">
                    UNIR
                </div>

                <div class="sticky-header__text">
                    <span class="sticky-header__title">
                        Design Tools
                    </span>

                    <span class="sticky-header__divider">
                        /
                    </span>

                    <span class="sticky-header__sub">
                        Prompt Studio
                    </span>
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
            <h1>Prompt generator for UNIR image production</h1>
            <p>
                Generate production-ready prompt variables directly from any UNIR course page.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_empty_state() -> None:
    st.markdown(
        """
        <div class="empty-state">

            <h3>Ready to generate</h3>

            <p>
                Paste a UNIR course URL and configure the visual parameters.
                Your generated blocks will appear here.
            </p>

            <div style="display:flex;gap:12px;margin-top:18px;">

                <span style="
                    color:#16A34A;
                    font-weight:600;
                ">
                    Información específica
                </span>

                <span style="color:#CBD5E1;">•</span>

                <span style="
                    color:#0033FF;
                    font-weight:600;
                ">
                    Características de grupo
                </span>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


def render_course_pill(course_name: str) -> None:
    st.markdown(
        f"""
        <div class="course-pill">
            {course_name}
        </div>
        """,
        unsafe_allow_html=True,
    )
