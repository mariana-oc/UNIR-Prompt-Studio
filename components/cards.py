import json

import streamlit as st
import streamlit.components.v1 as components


def _render_copy_button(text: str, element_key: str) -> None:
    payload = json.dumps(text)
    components.html(
        f"""
        <style>
          .copy-btn-wrap {{
            display: flex;
            justify-content: flex-end;
            margin: 0;
          }}
          .copy-btn {{
            appearance: none;
            border: 1px solid #DCE8FF;
            background: #FFFFFF;
            color: #0033FF;
            border-radius: 999px;
            padding: 10px 16px;
            font-family: Inter, system-ui, sans-serif;
            font-size: 0.82rem;
            font-weight: 600;
            cursor: pointer;
            box-shadow: 0 1px 2px rgba(0, 51, 255, 0.04), 0 8px 24px rgba(0, 51, 255, 0.05);
            transition: background 0.15s ease, box-shadow 0.15s ease, transform 0.15s ease;
          }}
          .copy-btn:hover {{
            background: #EEF4FF;
            border-color: #C7D9FF;
            transform: translateY(-1px);
          }}
          .copy-btn:focus,
          .copy-btn:focus-visible {{
            outline: none;
            box-shadow: 0 0 0 4px rgba(0, 51, 255, 0.12);
          }}
          .copy-btn.is-copied {{
            color: #00003D;
            background: #EEF4FF;
          }}
        </style>
        <div class="copy-btn-wrap">
          <button id="copy-{element_key}" type="button" class="copy-btn">Copiar</button>
        </div>
        <script>
          (function () {{
            const btn = document.getElementById("copy-{element_key}");
            if (!btn) return;
            btn.addEventListener("click", async function () {{
              try {{
                await navigator.clipboard.writeText({payload});
                btn.textContent = "Copiado";
                btn.classList.add("is-copied");
                setTimeout(function () {{
                  btn.textContent = "Copiar";
                  btn.classList.remove("is-copied");
                }}, 1800);
              }} catch (err) {{
                btn.textContent = "Selecciona el texto";
                setTimeout(function () {{
                  btn.textContent = "Copiar";
                }}, 1800);
              }}
            }});
          }})();
        </script>
        """,
        height=48,
    )


def render_section_card(kind, subtitle, color, sections, full_text, key):
    marker_class = "result-card-marker-verde" if color == "green" else "result-card-marker-azul"
    dot_class = "dot-green" if color == "green" else "dot-blue"

    st.markdown(f'<div class="result-card-marker {marker_class}"></div>', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="result-card-head">
          <div class="result-card-title-row">
            <span class="status-dot {dot_class}"></span>
            <div>
              <p class="result-card-title">{kind}</p>
              <div class="result-card-sub">{subtitle}</div>
            </div>
          </div>
        </div>
        <div class="result-card-note">Texto listo para copiar y pegar en Magnific.</div>
        """,
        unsafe_allow_html=True,
    )

    _render_copy_button(full_text, key)
    st.text_area("", full_text, height=420, key=key, label_visibility="collapsed")
