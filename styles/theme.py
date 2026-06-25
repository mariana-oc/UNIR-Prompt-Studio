import streamlit as st

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

:root {
  --bg: #F8FAFC;
  --card: #FFFFFF;
  --ink: #00003D;
  --muted: #5B6794;
  --line: #DCE8FF;
  --blue: #0033FF;
  --blue-soft: #EEF4FF;
  --blue-glow: rgba(0, 51, 255, 0.12);
  --green-dot: #22C55E;
  --blue-dot: #0033FF;
  --field-shadow: 0 1px 2px rgba(0, 51, 255, 0.04), 0 8px 24px rgba(0, 51, 255, 0.05);
  --shadow-soft: 0 16px 40px rgba(0, 51, 255, 0.07);
  --shadow-panel: 0 20px 50px rgba(0, 0, 61, 0.08);
  --shadow-hover: 0 28px 64px rgba(0, 51, 255, 0.11);
  --radius-lg: 24px;
  --radius-md: 18px;
  --space-section: 20px;
  --space-card: 24px;
  --sidebar-width: 300px;
}

html, body, [class*="css"] {
  font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  color: var(--ink);
}

.stApp {
  background: var(--bg);
  color: var(--ink);
}

.stApp::before,
.stApp::after {
  content: "";
  position: fixed;
  border-radius: 999px;
  filter: blur(88px);
  pointer-events: none;
  z-index: 0;
}

.stApp::before {
  width: 440px;
  height: 440px;
  top: -140px;
  left: -100px;
  background: rgba(0, 51, 255, 0.12);
}

.stApp::after {
  width: 380px;
  height: 380px;
  top: 140px;
  right: -80px;
  background: rgba(0, 51, 255, 0.08);
}

[data-testid="stAppViewContainer"],
[data-testid="stAppViewContainer"] > section {
  position: relative;
  z-index: 1;
}

[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer, header { visibility: hidden; }

.block-container {
  padding-top: 0;
  padding-bottom: 2rem;
  max-width: 1280px;
}

[data-testid="stMainBlockContainer"] [data-testid="stVerticalBlock"] {
  gap: var(--space-section);
}

/* Sticky header */
.sticky-header {
  position: sticky;
  top: 0;
  z-index: 200;
  margin: 0 0 12px 0;
  padding: 10px 0;
  background: rgba(248, 250, 252, 0.82);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--line);
}

.sticky-header__inner {
  display: flex;
  align-items: center;
  gap: 16px;
}

.logo-mark-text {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 44px;
  height: 44px;
  padding: 0 12px;
  border-radius: 14px;
  background: linear-gradient(135deg, #001F99 0%, var(--blue) 100%);
  color: #FFFFFF;
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  box-shadow: 0 10px 28px rgba(0, 51, 255, 0.22);
}

.sticky-header__text {
  display: flex;
  align-items: baseline;
  flex-wrap: wrap;
  gap: 8px;
}

.sticky-header__title {
  font-size: 1.05rem;
  font-weight: 600;
  color: var(--ink);
  letter-spacing: -0.03em;
  line-height: 1.2;
}

.sticky-header__divider {
  color: #C7D4F5;
  font-weight: 300;
}

.sticky-header__sub {
  font-size: 0.95rem;
  font-weight: 400;
  color: var(--muted);
  letter-spacing: -0.02em;
}

/* Floating sidebar */
section[data-testid="stSidebar"] {
  background: transparent !important;
  border-right: 0 !important;
  box-shadow: none !important;
  position: sticky !important;
  top: 0 !important;
  height: 100vh !important;
  max-height: 100vh !important;
  width: var(--sidebar-width) !important;
  min-width: var(--sidebar-width) !important;
  max-width: var(--sidebar-width) !important;
  overflow-y: auto !important;
  overflow-x: hidden !important;
  align-self: flex-start !important;
}

section[data-testid="stSidebar"] > div {
  background: #FFFFFF;
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-panel);
  margin: 12px 10px 12px 12px;
  padding: 18px 16px;
  width: calc(var(--sidebar-width) - 22px);
  box-sizing: border-box;
}

section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
  gap: 14px;
}

section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] li {
  color: var(--muted);
}

section[data-testid="stSidebar"] label {
  font-size: 0.78rem !important;
  font-weight: 600 !important;
  color: var(--ink) !important;
  letter-spacing: 0.01em;
  margin-bottom: 8px !important;
}

section[data-testid="stSidebar"] .stCaption {
  color: var(--muted) !important;
  font-size: 0.78rem !important;
  line-height: 1.65 !important;
}

/* Typography */
h1, h2, h3, p, label {
  color: var(--ink) !important;
  letter-spacing: -0.02em;
}

h1 {
  font-size: 1.95rem !important;
  line-height: 1.2 !important;
  font-weight: 600 !important;
  margin-bottom: 12px !important;
}

h2 {
  font-size: 1rem !important;
  font-weight: 600 !important;
}

h3 {
  font-size: 0.95rem !important;
  font-weight: 600 !important;
}

.small-muted,
.muted-copy {
  color: var(--muted);
  font-size: 0.88rem;
  line-height: 1.75;
  font-weight: 400;
}

/* Unified fields: input, select, textarea */
.stTextInput > div > div,
.stSelectbox > div > div,
.stTextArea > div > div,
.stTextInput [data-baseweb="input"],
.stSelectbox [data-baseweb="select"],
.stTextArea [data-baseweb="textarea"] {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}

.stTextInput input,
.stSelectbox [data-baseweb="select"] > div,
.stSelectbox div[data-baseweb="select"] > div,
.stTextArea textarea {
  background: #FFFFFF !important;
  border: 1px solid var(--line) !important;
  border-radius: var(--radius-md) !important;
  min-height: 48px !important;
  box-shadow: var(--field-shadow) !important;
  color: var(--ink) !important;
  font-size: 0.92rem !important;
  line-height: 1.65 !important;
  outline: none !important;
}

.stTextArea textarea {
  min-height: 420px !important;
  padding: 16px 18px !important;
  resize: none !important;
}

.stTextInput input:focus,
.stTextInput input:focus-visible,
.stSelectbox [data-baseweb="select"]:focus-within > div,
.stTextArea textarea:focus,
.stTextArea textarea:focus-visible {
  border-color: var(--blue) !important;
  box-shadow: 0 0 0 4px var(--blue-glow), var(--field-shadow) !important;
  outline: none !important;
}

.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
  color: #8A96BF !important;
}

/* Segmented radio / pill selector */
.stRadio > label {
  font-size: 0.78rem !important;
  font-weight: 600 !important;
  color: var(--ink) !important;
  margin-bottom: 10px !important;
}

.stRadio div[role="radiogroup"] {
  display: flex !important;
  flex-direction: row !important;
  align-items: stretch !important;
  width: 100% !important;
  gap: 0 !important;
  padding: 4px !important;
  background: var(--blue-soft) !important;
  border: 1px solid var(--line) !important;
  border-radius: 999px !important;
  box-shadow: var(--field-shadow) !important;
}

.stRadio div[role="radiogroup"] > label {
  flex: 1 1 0 !important;
  margin: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
  justify-content: center !important;
}

.stRadio div[role="radiogroup"] > label > div:first-child {
  display: none !important;
}

.stRadio div[role="radiogroup"] > label > div:last-child {
  width: 100%;
  text-align: center;
  padding: 8px 4px !important;
  border-radius: 999px !important;
  font-size: 0.74rem !important;
  font-weight: 500 !important;
  color: var(--muted) !important;
  transition: background 0.15s ease, color 0.15s ease, box-shadow 0.15s ease;
}

.stRadio div[role="radiogroup"] > label:has(input:checked) > div:last-child {
  background: #FFFFFF !important;
  color: var(--ink) !important;
  box-shadow: 0 4px 14px rgba(0, 51, 255, 0.10) !important;
}

.stRadio div[role="radiogroup"] > label:focus-within > div:last-child {
  box-shadow: 0 0 0 3px var(--blue-glow) !important;
}

/* Buttons */
.stButton > button {
  border: 0 !important;
  border-radius: 999px !important;
  min-height: 50px !important;
  padding: 0.8rem 1.35rem !important;
  font-weight: 600 !important;
  letter-spacing: -0.01em !important;
  color: #FFFFFF !important;
  background: var(--blue) !important;
  box-shadow: 0 14px 32px rgba(0, 51, 255, 0.24) !important;
  transition: transform 0.15s ease, box-shadow 0.15s ease, background 0.15s ease;
  outline: none !important;
}

.stButton > button:hover {
  transform: translateY(-1px);
  box-shadow: 0 18px 36px rgba(0, 51, 255, 0.28) !important;
  background: #002BE0 !important;
}

.stButton > button:focus,
.stButton > button:focus-visible {
  box-shadow: 0 0 0 4px var(--blue-glow), 0 14px 32px rgba(0, 51, 255, 0.24) !important;
  outline: none !important;
}

.stButton > button:active {
  transform: translateY(0);
}

section[data-testid="stSidebar"] .stButton > button {
  width: 100% !important;
}

.generate-action {
  margin-top: 4px;
}

/* Hero */
.hero {
  padding: 0 0 12px 0;
  max-width: 680px;
}

.hero h1 {
  font-size: 1.45rem !important;
  line-height: 1.2 !important;
  margin-bottom: 6px !important;
}

.hero p {
  font-size: 0.9rem !important;
  color: var(--muted) !important;
  line-height: 1.6 !important;
  margin-top: 0 !important;
  font-weight: 400 !important;
}

.instruction-panel {
  background: var(--blue-soft);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  padding: 16px;
  box-shadow: var(--field-shadow);
}

.instruction-panel--footer {
  margin-top: 8px;
}

.instruction-panel__title {
  color: var(--ink);
  font-size: 0.78rem;
  font-weight: 600;
  margin-bottom: 8px;
}

.instruction-panel ol {
  margin: 0;
  padding-left: 1.1rem;
  color: var(--muted);
  font-size: 0.76rem;
  line-height: 1.55;
}

.instruction-panel li + li {
  margin-top: 6px;
}

.sidebar-section-label {
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--blue);
  margin: 4px 0 2px 0;
}

.results-section {
  margin-top: 12px;
}

.course-pill {
  display: inline-flex;
  align-items: center;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: #FFFFFF;
  padding: 10px 16px;
  font-size: 0.84rem;
  font-weight: 500;
  color: var(--ink);
  box-shadow: var(--field-shadow);
  margin-bottom: 8px;
}

.empty-state {
  border: 1px dashed var(--line);
  border-radius: var(--radius-lg);
  background: rgba(255, 255, 255, 0.88);
  padding: 28px var(--space-card);
  text-align: center;
  color: var(--muted);
  line-height: 1.65;
  box-shadow: var(--field-shadow);
}

.empty-state strong {
  display: block;
  color: var(--ink);
  font-size: 1.02rem;
  font-weight: 600;
  margin-bottom: 10px;
}

/* Premium result cards */
[data-testid="column"]:has(.result-card-marker) {
  background: #FFFFFF;
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-soft);
  padding: var(--space-card);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

[data-testid="column"]:has(.result-card-marker):hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-hover);
}

[data-testid="column"]:has(.result-card-marker) [data-testid="stVerticalBlock"] {
  gap: 16px;
}

.result-card-head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 4px;
}

.result-card-title-row {
  display: flex;
  align-items: flex-start;
  gap: 12px;
}

.status-dot {
  width: 10px;
  height: 10px;
  border-radius: 999px;
  margin-top: 6px;
  flex-shrink: 0;
}

.dot-green {
  background: var(--green-dot);
  box-shadow: 0 0 0 4px rgba(34, 197, 94, 0.14);
}

.dot-blue {
  background: var(--blue-dot);
  box-shadow: 0 0 0 4px rgba(0, 51, 255, 0.12);
}

.result-card-title {
  font-size: 1.02rem;
  font-weight: 600;
  color: var(--ink);
  margin: 0;
  line-height: 1.45;
}

.result-card-sub {
  font-size: 0.82rem;
  font-weight: 500;
  color: var(--muted);
  margin-top: 4px;
  line-height: 1.5;
}

.result-card-note {
  font-size: 0.8rem;
  color: var(--muted);
  margin: 0 0 4px 26px;
  line-height: 1.65;
}

[data-testid="column"]:has(.result-card-marker) .stTextArea {
  margin-top: 0 !important;
}

[data-testid="column"]:has(.result-card-marker) .stTextArea textarea {
  background: #FFFFFF !important;
  border: 1px solid var(--line) !important;
  border-radius: var(--radius-md) !important;
  color: var(--ink) !important;
  font-family: 'Inter', sans-serif !important;
  font-size: 0.86rem !important;
  line-height: 1.75 !important;
  padding: 18px !important;
  box-shadow: var(--field-shadow) !important;
  min-height: 420px !important;
}

[data-testid="column"]:has(.result-card-marker) .stTextArea textarea:focus,
[data-testid="column"]:has(.result-card-marker) .stTextArea textarea:focus-visible {
  border-color: var(--blue) !important;
  box-shadow: 0 0 0 4px var(--blue-glow), var(--field-shadow) !important;
  outline: none !important;
}

hr, .stMarkdown hr {
  border: 0;
  border-top: 1px solid var(--line);
  margin: var(--space-section) 0;
}

@media (max-width: 1100px) {
  .sticky-header__inner {
    align-items: flex-start;
    flex-direction: column;
    gap: 12px;
  }
}
</style>
"""


def inject_theme() -> None:
    st.markdown(CSS, unsafe_allow_html=True)
