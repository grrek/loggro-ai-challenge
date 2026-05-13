# Prompts versionados

Aca van los prompts que tu pipeline realmente usa en runtime. No los del Audit Log (esos son notas / reflexion), sino los strings que tus sub-agentes consumen.

## Por que versionados

Tu eval es solo tan bueno como tu prompt. Si itera el prompt en un commit, queremos verlo. Si lo refactoreas, queremos ver el diff. Si lo cambias 8 veces hasta que pasa el threshold, eso es señal de criterio, no falla.

## Estructura sugerida

Un archivo por agente o por tarea, con metadata:

```
prompts/
  classifier-system.md          system prompt del ResponseClassifier
  classifier-few-shot.md        ejemplos few-shot que le pegamos
  enricher-extract.md           prompt de extraccion del Enricher
  writer-followup-v2.md         v2 del prompt del MessageWriter
  README.md                     este archivo
```

## Plantilla por prompt

```markdown
# {nombre} — {agente}

**Modelo:** claude-sonnet-4-6 (estable) / gpt-5 (fallback)
**Version:** v2 (cambio: agregue ejemplos de doble negacion)
**Token budget aprox:** 1.2k input / 400 output
**Cache key:** {si aplica}

## Prompt

\`\`\`
Eres un clasificador de respuestas comerciales en espanol Colombia.
Tu tarea es ...

Ejemplos:
...
\`\`\`

## Por que asi

3 lineas: que problema resuelve, que descarte, que medi.
```

## Referencias en codigo

Cuando tu codigo carga el prompt, usa el path como single source of truth:

```python
from pathlib import Path
SYSTEM_PROMPT = Path("prompts/classifier-system.md").read_text()
```

Asi cualquier cambio al prompt queda en el `git diff` del PR.

## Nota sobre prompts inline

Si un prompt es de 2 lineas y solo lo usas en un lugar, dejalo inline en el codigo. No infles `prompts/` con triviales. La regla: si tiene parrafos o lo iteras, va al archivo.
