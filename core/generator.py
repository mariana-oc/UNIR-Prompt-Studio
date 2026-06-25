from core.domain import detect_domain
from knowledge.looks import LOOKS


DEFAULT_ART_DIRECTIONS = [
    "Luz natural abundante, colores luminosos y frescos, contraste equilibrado, saturación moderadamente alta, tonos de piel naturales, blancos limpios, azul corporativo, verdes naturales y madera clara.",
    "Paleta limpia y contemporánea, colores vivos pero elegantes, ambiente optimista, materiales cálidos, fotografía lifestyle universitaria y sensación de bienestar.",
    "Luz cálida entrando por grandes ventanales, contraste medio, colores vibrantes y naturales, reflejos dorados y sensación de energía.",
    "Contraste medio, sombras abiertas, gradación cálida, colores luminosos, saturación moderadamente alta, ambiente editorial fresco y contemporáneo.",
]


def buyer(target: str, age: str) -> str:
    if target == "Mujeres":
        base = "Mujer española"
        group = "grupo de mujeres españolas"
    elif target == "Hombres":
        base = "Hombre español"
        group = "grupo de hombres españoles"
    else:
        base = "Persona española"
        group = "grupo mixto de personas españolas"

    return f"""1. {base} de {age} años y {group}, rasgos faciales naturales y no hegemónicos, aspecto contemporáneo, de 20 a 30 años.
2. {base} de {age} años y {group}, rasgos faciales naturales y no hegemónicos, aspecto contemporáneo, de 25 a 40 años.
3. {base} de {age} años, rasgos faciales naturales y no hegemónicos, aspecto contemporáneo.
4. {base} de {age} años, rasgos faciales naturales y no hegemónicos, aspecto contemporáneo."""


def numbered(items):
    return "\n".join([f"{i + 1}. {item}" for i, item in enumerate(items)])


def bullets(items):
    return "\n".join([f"* {item}" for item in items])


def generate_blocks(course_name, course_text, target, age, look):
    domain = detect_domain(course_text + " " + course_name)
    look_data = LOOKS[look]
    art = look_data.get("art", DEFAULT_ART_DIRECTIONS)

    azul_sections = {
        "CARACT_BUYER (BUYER PERSONA)": buyer(target, age),
        "CARACT_CTXT (CONTEXTO)": domain["context"],
        "CARACT_OBJ (OBJETOS)": bullets(domain["objects"]),
        "CARACT_COMP (DISTRIBUCIÓN Y COMPOSICIÓN)": "Frontal, clara y funcional, con jerarquía visual limpia, abundante espacio negativo, composición abierta y ambiente luminoso.",
        "CARACT_ID (IDENTIDAD)": domain["area"],
        "CARACT_MAT (MATERIALES)": "Madera clara, cristal, cerámica, papel, textiles naturales, metal mate y vegetación.",
        "CARACT_ATM (ATMÓSFERA)": "Ambiente universitario fresco, optimista y contemporáneo, orientado al aprendizaje, la creatividad, el intercambio de ideas y el crecimiento personal.",
    }

    verde_sections = {
        "INFO_ACTITUD": "1. Curiosa\n2. Inspirada\n3. Cercana",
        "INFO_ACCIÓN": numbered(domain["actions"]),
        "INFO_VEST (VESTIMENTA)": f"1. Ropa casual contemporánea, cómoda, moderna y con estilo.\n2. Camisas oversize, blusas, camisetas básicas, jerséis de punto fino, vaqueros, pantalones rectos y zapatillas blancas.\n3. {look_data['vest']}",
        "INFO_ART (DIRECCIÓN ARTÍSTICA)": f"1. Corporativo: {art[0]}\n\n2. Lifestyle universitario: {art[1]}\n\n3. Claroscuro con gran protagonismo al rayo de sol: {art[2]}\n\n4. Claroscuro suave que permite ver el fondo: {art[3]}",
    }

    return azul_sections, verde_sections


def sections_to_text(title, sections):
    out = [title, ""]

    for k, v in sections.items():
        out.append(f"{k}:\n")
        out.append(v)
        out.append("")

    return "\n".join(out).strip()
