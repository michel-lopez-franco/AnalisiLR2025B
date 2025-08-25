# AnalisiLR — Animación de análisis LR

Descripción

Proyecto pequeño que contiene una animación y materiales para practicar el análisis LR (ejercicios y ejemplo en PDF). Está pensado como demo estática para visualizar el proceso de análisis.

Supuestos

- Asumí que el proyecto es una demo estática (HTML + recursos). Si deseas que sea una app con build o servidor específico, dime y lo adapto.

Requisitos

- Navegador moderno (Chrome, Firefox, Safari).
- Opcional: Python 3 para servir los archivos localmente.

Archivos principales

- `lr_animation.html` — animación/demo interactiva del análisis LR.
- `EjemplosPractica2.pdf` — material de apoyo / enunciados.

Cómo usar

1. Abrir localmente (forma rápida):

   - Haz doble clic en `lr_animation.html` o ábrelo con tu navegador.

2. Servir con un servidor local (recomendado para evitar restricciones de CORS):

```zsh
# Sirve el directorio actual en http://localhost:8000
python3 -m http.server 8000
# Luego abre en el navegador:
# http://localhost:8000/lr_animation.html
```

Estructura del repositorio

```
/ (raíz)
├─ lr_animation.html    # animación/demo
├─ EjemplosPractica2.pdf # material de apoyo
└─ README.md            # este archivo
```

Contribuciones

Si quieres que añada instrucciones más detalladas, tests, o que convierta esto en un pequeño servidor Node/Python con hot-reload, dime qué prefieres y lo implemento.

Licencia

MIT — véase archivo LICENSE si deseas agregar uno.

Contacto

- Autor: (añade tu nombre o email si quieres que lo incluya)
