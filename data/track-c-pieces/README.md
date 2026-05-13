# Track C — Generador de Piezas de Marketing (dataset sintetico)

Dataset golden para el reto tecnico VE-1770 (Analista de Automatizacion y RevOps). Sirve como base para que el candidato construya un agente generador de copy con un reviewer que bloquee piezas fuera de brand voice.

> Advertencia: estas piezas son **sinteticas**, generadas para evaluacion del reto. **No usar en campanas reales** de Loggro sin pasar por revision del equipo Marketing/Growth.

## Indice de archivos

| Archivo | Contenido |
|---------|-----------|
| `briefs.json` | 3 briefs realistas (FE-DIAN, cross-sell POS, retencion Nomina) |
| `good_pieces.json` | 10 piezas que SI suenan Loggro (ground truth positivo) |
| `bad_pieces.json` | 10 piezas que NO suenan Loggro (ground truth negativo) |
| `README.md` | Este archivo |

## Schema

### briefs.json
```jsonc
{
  "briefs": [
    {
      "id": "BRIEF-XXX",
      "name": "string",
      "product": "string",
      "audience": "string",
      "objective": "string",
      "kpi": "string",
      "start_date": "YYYY-MM-DD",
      "budget_cop": number,
      "tone": "string",
      "mandatory_keywords": ["string"],
      "forbidden_keywords": ["string"],
      "legal_constraints": ["string"],
      "deliverables_expected": ["linkedin_post" | "email_outbound" | "whatsapp" | "meta_ad" | "landing_hook"]
    }
  ]
}
```

### good_pieces.json y bad_pieces.json
```jsonc
{
  "pieces": [
    {
      "id": "PIECE-G-XXX" | "PIECE-B-XXX",
      "brief_ref": "BRIEF-XXX" | null,
      "channel": "linkedin_post" | "email_outbound" | "whatsapp" | "meta_ad" | "landing_hook",
      "content": "string (copy completo, sin Lorem Ipsum)",
      "tone_tags": ["string"],
      "why_good": "string"   // solo en good_pieces
      "why_bad": "string"    // solo en bad_pieces
    }
  ]
}
```

## Brand voice de Loggro (resumen)

- Profesional pero cercano. Vos Colombia cuando aplica B2C o comercial.
- Concreto: datos, numeros, ejemplos reales antes que adjetivos.
- Cero AI hype. Cero jerga sin traducir.
- **Palabras prohibidas**: revolucionamos, ecosistema, innovador, disruptivo, world-class, holistico, sinergia, paradigma.
- **Em-dashes (— o –) prohibidos**: usar parentesis, comas, dos puntos o punto seguido.
- Tono adaptado al canal: LinkedIn mas formal, WhatsApp casual, email balance.

## Reglas de longitud por canal

| Canal | Limite |
|-------|--------|
| linkedin_post | 150 a 400 palabras |
| email_outbound | 80 a 250 palabras |
| whatsapp | < 120 palabras |
| meta_ad (headline) | < 40 caracteres |
| meta_ad (body) | < 125 caracteres |
| landing_hook | 3 variaciones de H1 |

## Uso esperado por el candidato

1. **Few-shot prompting**: tomar 3 a 5 piezas buenas del canal correspondiente como ejemplos en el prompt del generador.
2. **Eval del reviewer**: alimentar las 10 piezas malas al reviewer y verificar que las rechace con justificacion. Idealmente que la justificacion mencione la regla violada (em-dash, palabra prohibida, claim sin asterisco, etc.).
3. **Eval del generador**: dar los 3 briefs al generador y comparar las piezas producidas contra las buenas del mismo brief_ref (similitud de tono, cobertura de mandatory_keywords, ausencia de forbidden_keywords).
4. **Reglas duras automatizables**: las palabras prohibidas, em-dashes y limites de longitud son chequeables por regex/funcion, no requieren LLM. El reviewer LLM se enfoca en tono, claims sin evidencia y adaptacion al canal.

## Cobertura del dataset

| Canal | Buenas | Malas |
|-------|--------|-------|
| linkedin_post | 3 | 3 |
| email_outbound | 2 | 2 |
| whatsapp | 2 | 2 |
| meta_ad | 2 | 2 |
| landing_hook | 1 | 1 |
| **Total** | **10** | **10** |

| Brief cubierto | Buenas | Malas |
|----------------|--------|-------|
| BRIEF-001 (FE-DIAN) | 4 | 4 |
| BRIEF-002 (POS cross-sell) | 4 | 3 |
| BRIEF-003 (Nomina retencion) | 1 | 1 |
| Sin brief (general) | 1 | 2 |

## Notas para el evaluador

- Las piezas buenas son deliberadamente concretas; piden datos o ejemplos verificables. El generador del candidato puede sustituir `[Nombre]`, `[link]`, `[numero]` por placeholders, o pedirlos al brief.
- Las piezas malas estan disenadas para que **al menos una regla automatizable** las atrape (em-dashes, palabra prohibida, longitud). Pero varias tambien violan reglas de juicio (tono robot, asunto pobre, falta de CTA) que solo un reviewer LLM detecta bien.
- El reviewer del candidato deberia bloquear el 100% de las malas y dejar pasar idealmente el 90%+ de las buenas. Mas falsos positivos en buenas que falsos negativos en malas es preferible (mejor pedir reescribir que publicar fuera de marca).
