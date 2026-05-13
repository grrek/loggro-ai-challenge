# eval/

Aquí vive el lente automatizado de evaluación de tu entregable: **LLM-as-judge**.

## Qué contiene

| Archivo | Qué es | Quién lo toca |
|---|---|---|
| `judge_prompt.md` | Prompt versionado de la rúbrica de 5 dimensiones que un LLM aplica sobre tu entrega | Lo lees; lo **extiendes en el Apéndice.A5** |

## Por qué no hay `eval.py` ni `held_out/`

Los 4 tracks son tan heterogéneos (scraping vs analítica vs generativo vs multi-modal audio) que un harness automatizado unificado no agrega señal real. **El threshold automatizado se eliminó** del proceso de evaluación.

En vez, te evaluamos así:

| Lente | Cómo |
|---|---|
| **LLM-as-judge async** | Corremos Claude con `judge_prompt.md` contra tu repo + apéndice escrito. Score 0-10. Threshold: >= 7 |
| **Human review en frío** | Líder del rol + Tech Lead califican por separado, sin hablar entre ellos. Sobre tu repo + Loom. |
| **LLM review de la sesión live** | Grabación de Parte C procesada con Claude usando rúbrica predefinida. |
| **Tu Judge extension + sabotage test (Apéndice.A5)** | Lo evalúa otro LLM. ¿Tu judge atrapó tus outputs malos? Lo más alto signal. |

## Cómo correrlo localmente para auto-evaluarte (opcional)

Si querés saber cómo te calificaría un LLM sobre tu entrega antes de mandarla:

```bash
# Pseudocódigo, el script real lo tenés que armar vos según tu setup
# 1. Lee judge_prompt.md
# 2. Empaqueta tu repo (sin secrets) o pega tu README + key files
# 3. Llama a Claude API con system=judge_prompt, user=tu_entrega
# 4. Lee el score y los notes
```

No es requisito. Es una forma de cerrar el ciclo vos mismo antes de entregar.

## Judge extension (Apéndice.A5)

Pasos:

1. Lee `judge_prompt.md` completo
2. Identifica 2-3 criterios adicionales específicos de tu track (ej. Track A: cobertura sectorial; Track D: precisión del STT)
3. Extiende el prompt y guardalo como `judge_prompt_extended.md`
4. Genera 2 outputs deliberadamente malos para tu track (cada uno falla en algo distinto)
5. Corre tu judge extendido contra los 2 outputs malos
6. Reporta en tu README:
   - ¿Qué criterios añadiste y por qué?
   - ¿Tu judge atrapó el sabotaje? Si NO, ¿qué ajustaste para que lo atrapara?

Este sub-ejercicio es el de **más alto signal** de toda la prueba. Si lo hacés bien, suma puntos en `ai_fluency` y `eval_discipline`.

## Tip de costo del judge

El judge que corremos nosotros usa Claude API por candidato. Con prompt caching del system + rúbrica (es la misma para todos), el caching hit rate puede llegar a 90%. Costo por candidato: ~$0.20 USD. Sin caching: ~$2 USD.
