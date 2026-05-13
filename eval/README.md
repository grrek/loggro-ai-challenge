# eval/

Contrato de evaluacion automatica para tu entregable.

## Archivos

| Archivo | Que es | Quien lo toca |
|---|---|---|
| `judge_prompt.md` | Prompt publico para LLM-as-judge. Rubrica de 5 dimensiones | Lo lees; lo extiendes en Apendice.5 |
| `eval.py` | Skeleton del eval harness. Implementa `run_track` | Lo completas tú |
| `held_out/` | Dataset secreto. Provisto por Loggro al evaluarte | NO commitees nada aca (esta en `.gitignore`) |

## Contrato de `eval.py`

`run_track(track, cases)` debe retornar:

```python
{
    "total": int,
    "passed": int,
    "reasoning_quality": float,  # 0-1
    "details": [
        {"case_id": str, "passed": bool, "reasoning_quality": float, "notes": str}
    ]
}
```

## Threshold publicado

Para pasar el gate code-based:

- `passed >= 3` (de los 5 casos held_out)
- `reasoning_quality >= 0.7`

## Que es held_out

Loggro tiene 5 casos secretos por track que no estan en este repo. Cada uno tiene `ground_truth` conocido. Cuando entregas tu pipeline, dropeamos los casos a `eval/held_out/cases.json` en tu repo y corremos `python eval/eval.py --track {x}` (o `make eval`). El comando reporta cuantos pasaron.

**No intentes adivinar el contenido del held_out.** Es secreto para que el eval sea AI-resistant.

## Schema de cada `case` por track

Para que puedas implementar `run_track` sin adivinar, asi se ve la estructura (ejemplos dummy, no son los held_out reales):

### Track A — Outbound
```json
{
  "case_id": "a1",
  "account": {
    "company": "Acme S.A.S.",
    "size": 120,
    "sector": "manufactura",
    "decision_maker": {"role": "Director Financiero", "linkedin": "https://..."}
  },
  "incoming_response": "Gracias, pero ahora no es momento. Tal vez en Q4.",
  "ground_truth": {
    "intent": "no_interesado_temporal",
    "should_followup_date": "2026-10-01"
  }
}
```
**Tu `run_track` debe:** clasificar `incoming_response` segun el intent correcto.

### Track B — Insights
```json
{
  "case_id": "b1",
  "campaigns_subset": [...30 campañas activas con metricas],
  "ground_truth": {
    "anomaly_id": "CAMP-007",
    "anomaly_type": "audience_fatigue",
    "key_metric_signal": "ctr_decay_>30pct_last_7d"
  }
}
```
**Tu `run_track` debe:** identificar la anomalia plantada y reportar el `anomaly_id` correcto + explicacion.

### Track C — Piezas
```json
{
  "case_id": "c1",
  "brief": {
    "campaign": "DIAN-Q1-2026",
    "objective": "awareness para contadores PYME",
    "tone": "tecnico-cercano"
  },
  "channel": "linkedin_post",
  "ground_truth": {
    "brand_voice_must_pass": true,
    "max_chars": 600,
    "must_include_keywords": ["DIAN", "facturacion electronica"],
    "must_exclude": ["em_dashes", "ChatGPT-generic_phrases"]
  }
}
```
**Tu `run_track` debe:** generar la pieza y correr tu reviewer interno; reportar `passed=true` solo si pasa todos los criterios.

### Track D — Conversaciones
```json
{
  "case_id": "d1",
  "audio_url": "https://labs.loggro.com/audio-test/d1.mp3",
  "transcript_expected_fragments": ["DIAN", "competidor X", "presupuesto Q2"],
  "ground_truth": {
    "objections_detected": ["precio_alto", "necesita_aprobacion_CFO"],
    "competitors_mentioned": ["Siigo"],
    "risk_score_range": [0.4, 0.7],
    "followup_email_must_address": ["precio", "comparativa_Siigo"]
  }
}
```
**Tu `run_track` debe:** transcribir, extraer objeciones+competidores, calcular risk, generar email follow-up. Reportar matches contra ground_truth.

### Criterio comun de "passed"

Cada case se marca `passed: true` si tu output matchea los campos clave del `ground_truth`. La `reasoning_quality` (0-1) es un score que tu codigo puede calcular con un LLM-as-judge interno O con metricas determinísticas (F1, recall, etc.). Es tu decision como medirlo, pero documentalo en tu Apendice.

## Judge extension (Apendice.5)

Pasos:

1. Lee `judge_prompt.md` completo
2. Identifica 2-3 criterios adicionales especificos de tu track
3. Extiende el prompt y guardalo como `judge_prompt_extended.md`
4. Genera 2 outputs deliberadamente malos para tu track (cada uno falla en algo distinto)
5. Corre tu judge extendido contra los 2 outputs malos
6. Reporta en tu README:
   - ¿Que criterios anadiste y por que?
   - ¿Tu judge atrapo el sabotaje? Si NO, ¿que ajustaste para que lo atrapara?

Este sub-ejercicio es el de **mas alto signal** de toda la prueba. Si lo haces bien, suma puntos en `ai_fluency` y `eval_discipline`.

## Tip de costo del judge

El judge usa Claude API por candidato. Con prompt caching del system + rubrica (es la misma para todos), el caching hit rate puede llegar a 90%. Costo por candidato: ~$0.20 USD. Sin caching: ~$2 USD.
