import re

from knowledge.domains import DOMAIN_KEYWORDS

_DEFAULT_DOMAIN = {
    "area": "Aprendizaje universitario, desarrollo profesional, pensamiento crítico, recursos académicos y crecimiento personal.",
    "context": "Campus universitario contemporáneo, biblioteca luminosa, espacios de aprendizaje colaborativo o aula moderna con abundante luz natural, vegetación y mobiliario actual.",
    "objects": [
        "Libros, cuadernos, portátil, taza de café, auriculares y bolígrafos.",
        "Libros abiertos, apuntes manuscritos, tablet, post-its, cuadernos y marcapáginas.",
        "Estanterías con libros, plantas, recursos académicos y objetos personales.",
    ],
    "actions": [
        "Escribiendo ideas en un cuaderno.",
        "Leyendo un libro.",
        "Conversando con otra estudiante.",
        "Preparando una presentación.",
        "Subrayando un texto.",
        "Tomando notas.",
        "Trabajando en el portátil.",
        "Compartiendo ideas.",
        "Organizando apuntes.",
        "Reflexionando mientras toma un café.",
    ],
}


def detect_domain(text: str):
    lower = text.lower()
    for pattern, data in DOMAIN_KEYWORDS.items():
        if re.search(pattern, lower):
            return data
    return _DEFAULT_DOMAIN
