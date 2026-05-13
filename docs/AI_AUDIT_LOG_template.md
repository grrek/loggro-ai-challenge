# AI Audit Log

> **Obligatorio.** Sin esto, tu entrega no se evalua. Esa es la unica regla dura del Apendice.
>
> Minimo 10 entradas. Si la tabla dice "todo perfecto, la IA hizo todo bien", la nota baja. Buscamos criterio, no fanboys de Claude.

## Tabla

| # | Herramienta | Tarea | Output util? | Que tuviste que corregir | Aprendizaje |
|---|-------------|-------|--------------|--------------------------|-------------|
| 1 | Claude Code (Opus 4.7) | Scaffolding inicial del TranscriptionAgent | Si, 80% | Whisper retornaba speakers mezclados; agregue diarization con pyannote-audio aparte | Claude default no incluye diarization. Conviene siempre testear con audio multi-speaker antes de confiar en el output |
| 2 |  |  |  |  |  |
| 3 |  |  |  |  |  |
| 4 |  |  |  |  |  |
| 5 |  |  |  |  |  |
| 6 |  |  |  |  |  |
| 7 |  |  |  |  |  |
| 8 |  |  |  |  |  |
| 9 |  |  |  |  |  |
| 10 |  |  |  |  |  |

## Reflexion final (300 palabras max)

<!--
Tres preguntas que el evaluador busca responder leyendo esto:

1. Que aprendiste sobre TU propio uso de IA durante estas 48 horas?
2. Donde te diste cuenta de que la IA te estaba dando algo mediocre y lo cambiaste?
3. Que decisiones tomaste sin la IA, y por que?

No tiene que ser confesional. Tiene que ser honesto y especifico.
-->


## Tips para llenar bien esto

- **"Output util"** acepta valores: Si, No, Parcial (X%). El "parcial" honesto suma.
- **"Que tuviste que corregir"** es la columna mas importante. Si todas dicen "nada", no estas mirando suficiente.
- **"Aprendizaje"** debe ser **generalizable**, no especifico a esta tarea. Algo que aplicarias en otro proyecto.
- Cita el modelo + version cuando puedas (Opus 4.7, Sonnet 4.6, GPT-5.4, etc.). Las generalizaciones tipo "Claude" no dicen nada.
- Si descartaste un enfoque entero de la IA, eso es una entrada valida con "Output util? No, descarte"
- Si encontraste que un prompt cuesta 3 veces lo razonable y lo refactorizaste, eso es una entrada valida

## Anti-patrones a evitar

- "Le pedi codigo a Claude y funciono al primer intento" en 9 de 10 entradas (no es creible)
- "La IA me ahorro 5 horas" sin decir EN QUE
- Entradas vacias o de relleno
- Misma herramienta en todas las entradas (usa Stack diverso es bueno; mostralo)
- Em-dashes en cualquier celda (es huella de texto AI-generated sin filtrar; restamos 0.5 por cada uno)
