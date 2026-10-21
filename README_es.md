# Awesome Nano Banana 2.1 Prompts — Guía en español

Una colección independiente de código abierto creada y mantenida por el **[equipo de aivideoweb.com](https://aivideoweb.com)**. Encuentra recetas para fotografía de producto, anuncios, portadas, diagramas educativos, retratos, guiones gráficos y edición de imágenes.

[English](README.md) · [简体中文](README_zh.md) · [日本語](README_ja.md) · [Español](README_es.md)

![Portada original de la biblioteca de aivideoweb.com](assets/images/cover.webp)

Las 24 recetas añadidas son adaptaciones nuevas basadas en temas de casos públicos de X. El [registro de fuentes](docs/x-case-sources.md) incluye autores, fechas y alcance de la revisión. No son transcripciones de los prompts originales ni resultados reproducidos de forma independiente.

## Qué incluye

Son 72 escenarios originales en 12 categorías. Cada receta tiene versiones completas en inglés y chino simplificado, con composición, texto exacto, restricciones y criterios de revisión. **Esta página ofrece una introducción y un ejemplo en español; no es una traducción completa de las 72 recetas.**

Las imágenes se generaron de nuevo con la herramienta integrada imagegen y sirven como ilustraciones. **No son resultados verificados de Nano Banana 2.1.** Todas las pruebas del modelo de destino figuran como `not_tested`. El [registro de generación](assets/generation-manifest.json) identifica la herramienta y el prompt de cada imagen.

## Cómo usar una receta

1. Elige una tarea del [catálogo en inglés](prompts/en.md) o del [catálogo en chino](prompts/zh.md).
2. Cambia el producto ficticio, los materiales, la paleta y las frases por los de tu proyecto.
3. Selecciona el modelo, la proporción y la resolución en tu herramienta. Escribir «4K» en el prompt no configura la salida.
4. Para editar, sube referencias autorizadas e indica qué aporta cada una.
5. Genera un borrador pequeño. Revisa el criterio de la receta y corrige un problema por turno.

## Ejemplo en español

```text
Uso: cartel de apertura de una librería ficticia.
Escena: una pequeña puerta azul con luz cálida sobre papel crema.
Coloca pilas de libros de distintas alturas a ambos lados.
Mantén una textura de papel visible y espacio libre para el título.
Texto exacto, en azul marino: «Un fin de semana entre libros».
No añadas autores, precios, logotipos, marcas de agua ni otros textos.
Revisión: comprueba las letras, la perspectiva de la puerta y los libros.
```

Comprueba las tildes y los signos en la imagen final. Si una traducción ocupa más espacio, cambia el tamaño de letra o los saltos de línea dentro del área original, sin deformar las letras.

## Elige según tu objetivo

| Necesitas… | Receta |
|---|---|
| Una imagen de producto | [Ceramic travel mug](site/prompts/ceramic-travel-mug.html) |
| Un anuncio | [Coffee launch](site/prompts/coffee-launch.html) |
| Un recurso educativo | [Plant growth](site/prompts/plant-cycle.html) |
| Una historia coherente | [Fox courier](site/prompts/fox-courier.html) |
| Traducir un cartel propio | [Poster localization](site/prompts/poster-localization.html) |

## Galería local y colaboración

Desde la raíz del repositorio, ejecuta `python3 -m http.server 8000` y abre `http://localhost:8000/site/`. La galería permite buscar en inglés o chino y filtrar por categoría. Consulta la [guía de publicación](docs/publishing.md) antes de alojarla.

El texto original y el código usan la licencia [MIT](LICENSE). Consulta el [aviso de imágenes](assets/README.md) para su procedencia y condiciones. No se garantiza exclusividad ni la autorización de derechos de terceros para cualquier uso comercial.

Para aportar escenarios, traducciones revisadas o pruebas reales del modelo, lee [CONTRIBUTING.md](CONTRIBUTING.md). Conserva los identificadores y distingue siempre una traducción completa de una guía inicial.

---

## Acerca de AI VideoWeb

[**AI VideoWeb (aivideoweb.com)**](https://aivideoweb.com) es una plataforma de creación de vídeo, imágenes y música con IA para creadores y equipos de marketing. Ofrece generación de vídeo a partir de texto, imágenes o referencias, además de generación y edición de imágenes para productos, anuncios y redes sociales.

El **equipo de aivideoweb.com** crea y mantiene esta biblioteca abierta. Adapta una receta a tu proyecto y prueba las [herramientas de imágenes con IA](https://aivideoweb.com/ai-image-generator/) y los flujos de vídeo de la plataforma.

### Colabora como afiliado

AI VideoWeb admite **colaboraciones con afiliados**. Creadores, reseñadores, educadores y editores pueden recomendar el producto mediante contenido útil. Consulta cómo participar y las condiciones vigentes en el [**Programa de Afiliados de AI VideoWeb**](https://aivideoweb.com/affiliate-program/).
