# Escenario C — Generador de Piezas de Marketing (dataset hibrido real + sintetico)

Dataset golden para el reto tecnico VE-1770 (Analista de Automatizacion y RevOps). Sirve como base para que el candidato construya un agente generador de copy con un reviewer que bloquee piezas fuera de brand voice.

> **Importante:** las `good_pieces` son anuncios REALES de Loggro extraidos de Meta Ad Library (2026-05-13). Las `bad_pieces` son sinteticas, generadas con LLM para violar brand voice o restricciones de brief. No usar piezas malas en campanas reales.

## Indice de archivos

| Archivo | Contenido |
|---------|-----------|
| `briefs.json` | 3 briefs realistas (FE-DIAN, cross-sell POS, retencion Nomina) |
| `good_pieces.json` | 10 piezas reales de Loggro extraidas de Meta Ad Library con screenshots |
| `bad_pieces.json` | 10 piezas sinteticas LLM-generadas con violations estructuradas |
| `screenshots/PIECE-XXX.jpg` | Creativos visuales descargados desde Facebook CDN (formato JPEG) |
| `README.md` | Este archivo |

## Extraccion de good_pieces (real Ad Library)

Realizada el 2026-05-13 con OpenTabs MCP (browser automation):

1. Navegacion a `https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=CO&q=loggro` (Colombia, todos los estados, keyword `loggro`).
2. Total de resultados visibles: ~120 anuncios activos/inactivos.
3. Extraccion DOM de 19 cards iniciales via `Library ID` text nodes y subida hasta el card container.
4. Curacion de 10 piezas optimizando diversidad: 3 productos principales (Restobar 3, Pymes 3, POS 2, Enterprise 1, Alojamientos 1) + 1 cross-product (Restobar+Pymes); formatos 7 imagen + 3 video.
5. Descarga de creatives (600x600 para imagenes, video poster 1080x1920 para videos) directo desde Facebook CDN URLs (URLs firmadas con expiry ~6 meses).

Schema enriquecido por el prompt handoff `prompts-handoff/track-c-meta-adlibrary.md`.

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

### good_pieces.json (piezas reales Meta Ad Library)
```jsonc
{
  "pieces": [
    {
      "id": "PIECE-XXX",
      "source": "meta_ad_library",
      "source_url": "https://www.facebook.com/ads/library/?id=<library_id>",
      "library_id": "string",
      "advertiser": "Loggro",
      "platforms": ["facebook", "instagram"],
      "format": "image" | "video" | "carousel",
      "video_duration_seconds": number,         // solo si format=video
      "product_line": "Restobar" | "Pymes" | "POS" | "Enterprise" | "Alojamientos" | "Nomina" | "Contadores",
      "first_seen": "YYYY-MM-DD",
      "still_active": boolean,
      "multi_version": boolean,
      "versions_count": number,
      "copy": {
        "primary_text": "string (texto principal del anuncio)",
        "headline": "string",
        "description": "string",
        "cta_button": "Get Quote" | "Get quote" | "Learn more" | "Send WhatsApp Message"
      },
      "visual_description": "string (1 linea descriptiva del creative)",
      "landing_destination": "https://...",
      "brand_voice_compliance": {
        "no_em_dashes": boolean,
        "claims_with_substance": boolean,
        "tone_matches_audience": boolean,
        "format_respects_channel": boolean
      },
      "why_good": "string (justificacion para curacion)",
      "screenshot_path": "data/track-c-pieces/screenshots/PIECE-XXX.jpg"
    }
  ]
}
```

### bad_pieces.json (piezas sinteticas con violations)
```jsonc
{
  "pieces": [
    {
      "id": "PIECE-B-XXX",
      "brief_ref": "BRIEF-XXX" | null,
      "channel": "linkedin_post" | "email_outbound" | "whatsapp" | "meta_ad" | "landing_hook",
      "content": "string (copy completo)",
      "tone_tags": ["string"],
      "why_bad": "string (prose explicando violaciones)",
      "violations": [
        {
          "type": "em_dashes_used" | "chatgpt_generic_phrasing" | "unsupported_claim" |
                  "tone_mismatch_audience" | "format_breaks_channel" | "mock_competitor_unfair" |
                  "pii_leak" | "mistranslation_or_typos" | "dian_compliance_violation" |
                  "no_cta_or_broken_cta" | "forbidden_brief_keyword",
          "evidence": "string (texto exacto o regla violada)",
          "severity": "high" | "medium" | "low"
        }
      ],
      "expected_reviewer_action": "reject"
    }
  ]
}
```

## Brand voice de Loggro (resumen)

- Profesional pero cercano. Vos Colombia (`tu`) por default; `usted` aceptable para segmentaciones formales (PIECE-005 lo usa para retail de ropa).
- Concreto: datos, numeros, ejemplos reales antes que adjetivos. Ejemplo: "elegido por mas de 15.000 negocios" (PIECE-001) vs "lider del mercado".
- Cero AI hype. Cero jerga sin traducir.
- **Palabras prohibidas en brand voice**: revolucionamos, ecosistema, innovador, disruptivo, world-class, holistico, sinergia, paradigma.
- **Em-dashes (— o –) prohibidos**: usar parentesis, comas, dos puntos o punto seguido. Hyphens normales `-` para bullets estan OK.
- Tono adaptado al canal: LinkedIn mas formal, WhatsApp casual, email balance, meta_ad conciso.
- Uso de emojis funcional (📲 ⏳ 🤯 📊 ☁️) acepable y comun en Meta Ads de Loggro. NO usar emojis decorativos en exceso.

## Reglas de longitud por canal

| Canal | Limite |
|-------|--------|
| linkedin_post | 150 a 400 palabras |
| email_outbound | 80 a 250 palabras |
| whatsapp | < 120 palabras |
| meta_ad (headline) | < 40 caracteres |
| meta_ad (body) | < 125 caracteres |
| landing_hook | 3 variaciones de H1 |

## Cobertura del dataset

### Good pieces (reales) — cobertura por producto
| Producto | Count | IDs |
|----------|-------|-----|
| Restobar | 3 | PIECE-001, PIECE-009, PIECE-010 (cross con Pymes) |
| Pymes | 3 | PIECE-002, PIECE-003, PIECE-006 |
| POS | 2 | PIECE-004, PIECE-005 |
| Enterprise | 1 | PIECE-007 |
| Alojamientos | 1 | PIECE-008 |
| **Total** | **10** | |

### Good pieces — cobertura por formato
| Formato | Count |
|---------|-------|
| image | 7 |
| video | 3 (PIECE-002, PIECE-005, PIECE-010) |

### Bad pieces — cobertura por canal
| Canal | Count |
|-------|-------|
| linkedin_post | 3 |
| email_outbound | 2 |
| whatsapp | 2 |
| meta_ad | 2 |
| landing_hook | 1 |
| **Total** | **10** |

### Bad pieces — cobertura por brief
| Brief cubierto | Count |
|----------------|-------|
| BRIEF-001 (FE-DIAN) | 4 |
| BRIEF-002 (POS cross-sell) | 4 |
| BRIEF-003 (Nomina retencion) | 1 |
| Sin brief (general) | 1 |

### Bad pieces — cobertura de violations (11 tipos cubiertos)

| Violation type | Piezas que la cubren |
|----------------|----------------------|
| `em_dashes_used` | B-002, B-006, B-007, B-010 |
| `chatgpt_generic_phrasing` | B-001, B-003, B-004, B-007, B-008, B-010 |
| `unsupported_claim` | B-001, B-003, B-004, B-009 |
| `tone_mismatch_audience` | B-003, B-004, B-006, B-007 |
| `format_breaks_channel` | B-005, B-007, B-008, B-009 |
| `mock_competitor_unfair` | B-005 (mock a Siigo) |
| `pii_leak` | B-005 (Juan Perez de Almacenes Cordoba SAS), B-006 (tickets por cuenta) |
| `mistranslation_or_typos` | B-002 (ingles sin traducir) |
| `dian_compliance_violation` | B-001, B-004, B-008, B-010 |
| `no_cta_or_broken_cta` | B-002, B-003, B-005, B-007, B-008, B-009 |
| `forbidden_brief_keyword` | B-001, B-002, B-006, B-008, B-009, B-010 |

**Total: 11/10 tipos cubiertos** (el prompt pedia 7+).

## Uso esperado por el candidato

1. **Few-shot prompting del generador**: tomar 3 a 5 piezas reales del producto correspondiente como ejemplos en el prompt. Para canales no-meta (linkedin, email, whatsapp), el candidato puede inferir el tono desde las good pieces y adaptarlo.
2. **Eval del reviewer**: alimentar las 10 bad pieces al reviewer y verificar que las rechace (`expected_reviewer_action: reject`) con justificacion que matchee al menos 1 violation type del array `violations`.
3. **Eval del generador**: dar los 3 briefs al generador y comparar las piezas producidas contra las reales del mismo producto (similitud de tono, cobertura de mandatory_keywords, ausencia de forbidden_keywords).
4. **Reglas duras automatizables**: las palabras prohibidas (`em_dashes_used`, `chatgpt_generic_phrasing`, `forbidden_brief_keyword`) y limites de longitud son chequeables por regex/funcion, no requieren LLM. El reviewer LLM se enfoca en tono, claims sin evidencia, `dian_compliance_violation`, `pii_leak`, `mock_competitor_unfair`.

## Notas para el evaluador

- Las good pieces son **anuncios reales en produccion** de Loggro. Pueden tener detalles que no son perfect-AI (ej. PIECE-007 tiene error gramatical menor "demasiado complejo" cuando deberia ser "demasiado compleja"). Esto es deliberado: el reviewer no debe ser tan estricto que rechace contenido humano legitimo.
- Las bad pieces estan disenadas para que **al menos 1 regla automatizable** las atrape (em-dashes, palabra prohibida, longitud). Varias tambien violan reglas de juicio (tono robot, PII leak, mock competitor) que solo un reviewer LLM detecta bien.
- El reviewer del candidato deberia bloquear el 100% de las malas y dejar pasar idealmente el 90%+ de las buenas. Mas falsos positivos en buenas que falsos negativos en malas es preferible (mejor pedir reescribir que publicar fuera de marca).
- Screenshots de las 10 piezas reales estan en `screenshots/PIECE-001.jpg` a `PIECE-010.jpg`. Imagenes son 338x600 a 1080x1920 (videos posters). Las URLs de Facebook CDN expiran en ~6 meses; los locales son la fuente fiable.

## Hallazgos interesantes de la extraccion

- Loggro pauta agresivamente en Meta Ads con **5 productos en simultaneo** (Restobar, Pymes, POS, Enterprise, Alojamientos) + 1 anuncio cross-product Restobar+Pymes integrado.
- Mezcla `tu` y `usted` por segmentacion: B2C/retail usa `tu`; Enterprise y un video POS especifico usan `usted` formal.
- Promo activa al momento de la extraccion: **2x1 en planes** (POS) y **descuentos por tiempo limitado** (Pymes). Estas piezas se incluyeron como good a pesar de los promos porque no violan brand voice global, solo el `forbidden_keywords` ficticio de algunos briefs sinteticos del dataset.
- Display URL `PROMO.LOGGRO.COM` es el handle publico; los UTMs revelan campanas internas (`POS029_VetSimilares`, `Pymes_032_Webinar_Leads_V5`, etc.) que confirman segmentacion por vertical (veterinarias, licores, hoteles rurales).
- Anuncios mas recientes (May 11, 2026): Restobar con tablet/celular (PIECE-009). Mas antiguos (Nov 24, 2025): POS retail formal (PIECE-005 base creative).
