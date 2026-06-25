import streamlit as st

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

:root {
  --bg: #F8FAFC;
  --surface: #FFFFFF;
  --ink: #00003D;
  --muted: #5B6794;
  --line: #DCE8FF;
  --blue: #0033FF;
  --blue-hover: #002BE0;
  --blue-soft: #EEF4FF;
  --blue-glow: rgba(0, 51, 255, 0.12);
  --green: #22C55E;
  --radius-lg: 22px;
  --radius-md: 16px;
  --shadow-card: 0 10px 28px rgba(0, 51, 255, 0.06);
  --shadow-hover: 0 18px 44px rgba(0, 51, 255, 0.10);
  --sidebar-width: 340px;
}

html, body, [class*="css"] {
  font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  color: var(--ink);
}

.stApp {
  background:
    radial-gradient(circle at top left, rgba(0, 51, 255, 0.10), transparent 34%),
    radial-gradient(circle at top right, rgba(0, 51, 255, 0.07), transparent 30%),
    var(--bg);
}

[data-testid="stHeader"],
#MainMenu,
footer,
header {
  visibility: hidden;
}

.block-container {
  padding-top: 0.75rem;
  padding-bottom: 2rem;
  max-width: 1280px;
}

[data-testid="stVerticalBlock"] {
  gap: 18px;
}

/* Header */
.sticky-header {
  position: sticky;
  top: 0;
  z-index: 50;
  background: rgba(248, 250, 252, 0.86);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--line);
  padding: 10px 0;
  margin-bottom: 12px;
}

.sticky-header__inner {
  display: flex;
  align-items: center;
  gap: 12px;
}

.logo-mark-text {
  color: var(--blue);
  font-weight: 800;
  font-size: 1rem;
  letter-spacing: -0.04em;
  background: transparent;
  box-shadow: none;
  height: auto;
  min-width: auto;
  padding: 0;
  border-radius: 0;
}

.sticky-header__text {
  display: flex;
  align-items: center;
  gap: 8px;
}

.sticky-header__title {
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--ink);
}

.sticky-header__divider {
  color: #AFC7FF;
}

.sticky-header__sub {
  font-size: 0.88rem;
  color: var(--muted);
}

/* Sidebar */
section[data-testid="stSidebar"] {
  width: var(--sidebar-width) !important;
  min-width: var(--sidebar-width) !important;
  max-width: var(--sidebar-width) !important;
  background: transparent !important;
  border-right: 0 !important;
  overflow-y: auto !important;
}

section[data-testid="stSidebar"] > div {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-card);
  margin: 12px;
  padding: 18px;
  width: calc(var(--sidebar-width) - 24px);
}

section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
  gap: 12px;
}

.sidebar-section-label {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--blue);
  margin-top: 4px;
}

/* Type */
h1 {
  font-size: 1.35rem !important;
  line-height: 1.2 !important;
  font-weight: 650 !important;
  letter-spacing: -0.04em !important;
  color: var(--ink) !important;
  margin-bottom: 4px !important;
}

h2, h3, label {
  color: var(--ink) !important;
}

p {
  color: var(--muted) !important;
  line-height: 1.6 !important;
}

.hero {
  padding-bottom: 6px;
  max-width: 680px;
}

.hero p {
  font-size: 0.9rem !important;
  margin-top: 0 !important;
}

/* Inputs */
.stTextInput input,
.stSelectbox [data-baseweb="select"] > div,
.stTextArea textarea {
  background: #FFFFFF !important;
  border: 1px solid var(--line) !important;
  border-radius: var(--radius-md) !important;
  color: var(--ink) !important;
  font-size: 0.9rem !important;
  box-shadow: none !important;
  outline: none !important;
}

.stTextInput input,
.stSelectbox [data-baseweb="select"] > div {
  min-height: 46px !important;
}

.stTextArea textarea {
  min-height: 240px !important;
  padding: 16px !important;
  line-height: 1.65 !important;
  resize: vertical !important;
}

.stTextInput input:focus,
.stSelectbox [data-baseweb="select"]:focus-within > div,
.stTextArea textarea:focus {
  border-color: var(--blue) !important;
  box-shadow: 0 0 0 4px var(--blue-glow) !important;
}

/* Target segmented control */
.stRadio div[role="radiogroup"] {
  display: grid !important;
  grid-template-columns: repeat(3, 1fr);
  gap: 4px !important;
  padding: 4px !important;
  background: var(--blue-soft);
  border: 1px solid var(--line);
  border-radius: 999px;
}

.stRadio div[role="radiogroup"] > label {
  margin: 0 !important;
}

.stRadio div[role="radiogroup"] > label > div:first-child {
  display: none !important;
}

.stRadio div[role="radiogroup"] > label > div:last-child {
  text-align: center;
  padding: 8px 6px !important;
  border-radius: 999px;
  font-size: 0.78rem !important;
  font-weight: 600 !important;
  color: var(--muted) !important;
  white-space: nowrap !important;
}

.stRadio div[role="radiogroup"] > label:has(input:checked) > div:last-child {
  background: #FFFFFF;
  color: var(--blue) !important;
  box-shadow: 0 3px 10px rgba(0, 51, 255, 0.10);
}

/* Buttons */
.stButton > button {
  width: 100%;
  border: 0 !important;
  border-radius: 999px !important;
  min-height: 48px !important;
  background: var(--blue) !important;
  color: white !important;
  font-weight: 700 !important;
  box-shadow: 0 12px 28px rgba(0, 51, 255, 0.22) !important;
}

.stButton > button:hover {
  background: var(--blue-hover) !important;
  transform: translateY(-1px);
}

/* Panels */
.instruction-panel {
  background: var(--blue-soft);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  padding: 14px;
}

.instruction-panel__title {
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--ink);
  margin-bottom: 6px;
}

.instruction-panel ol {
  margin: 0;
  padding-left: 1rem;
  color: var(--muted);
  font-size: 0.76rem;
  line-height: 1.55;
}

.course-pill {
  display: inline-flex;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: #FFFFFF;
  padding: 8px 14px;
  font-size: 0.82rem;
  color: var(--ink);
  margin-bottom: 4px;
}

.empty-state {
  border: 1px dashed var(--line);
  border-radius: var(--radius-lg);
  background: #FFFFFF;
  padding: 22px;
  text-align: left;
  color: var(--muted);
  box-shadow: var(--shadow-card);
}

.empty-state strong {
  color: var(--ink);
  display: block;
  margin-bottom: 6px;
}

/* Result cards */
[data-testid="column"]:has(.result-card-marker) {
  background: #FFFFFF;
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-card);
  padding: 22px;
  transition: all .18s ease;
}

[data-testid="column"]:has(.result-card-marker):hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-hover);
}

.result-card-head {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 8px;
}

.result-card-title-row {
  display: flex;
  gap: 10px;
}

.status-dot {
  width: 9px;
  height: 9px;
  border-radius: 99px;
  margin-top: 7px;
  flex-shrink: 0;
}

.dot-green {
  background: var(--green);
}

.dot-blue {
  background: var(--blue);
}

.result-card-title {
  font-size: 0.98rem;
  font-weight: 700;
  color: var(--ink);
  margin: 0;
}

.result-card-sub,
.result-card-note {
  font-size: 0.8rem;
  color: var(--muted);
  line-height: 1.5;
}

[data-testid="column"]:has(.result-card-marker) .stTextArea textarea {
  min-height: 300px !important;
  font-size: 0.84rem !important;
  line-height: 1.65 !important;
}

/* Utility */
hr {
  border: 0;
  border-top: 1px solid var(--line);
}

@media (max-width: 1100px) {
  section[data-testid="stSidebar"] {
    width: 100% !important;
    max-width: 100% !important;
  }

  section[data-testid="stSidebar"] > div {
    width: auto;
  }
}
</style>
"""

def inject_theme() -> None:
    st.markdown(CSS, unsafe_allow_html=True)
