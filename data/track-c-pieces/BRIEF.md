# Track C — Generador de Piezas de Marketing

> Brief técnico del Track C del reto VE-1770. Léelo después de decidir que C es tu track.

## Brief

Construye un agente que recibe un **brief de campaña** y genera **piezas multi-canal** consistentes en brand voice, listas para publicar en HubSpot, Meta, LinkedIn y WhatsApp. Más un **reviewer interno** que bloquea las piezas que no pasan umbral de brand voice.

Es generación creativa con disciplina: la creatividad no compromete la marca; el reviewer es el que evita que entreguemos algo "ChatGPT corporativo" al cliente final.

## Inputs entregados

| Archivo | Qué es |
|---|---|
| [`briefs.json`](./briefs.json) | 3 briefs reales de campañas Loggro (DIAN, cross-sell POS, retención Nómina) con objetivo, audiencia, producto, restricciones legales, tono |
| [`good_pieces.json`](./good_pieces.json) | **10 piezas reales** extraídas de Meta Ad Library de Loggro (Restobar 3, Pymes 3, POS 2, Enterprise 1, Alojamientos 1; 7 imagen + 3 video) con `source_url`, `brand_voice_compliance`, `landing_destination` con UTMs originales |
| [`bad_pieces.json`](./bad_pieces.json) | **10 piezas sintéticas con `violations` documentadas** — para entrenar/probar tu reviewer. Cubre 11 violation types (em_dashes, chatgpt_generic, unsupported_claim, tone_mismatch, format_breaks, mock_competitor, pii_leak, mistranslation, dian_compliance, no_cta, forbidden_brief_keyword) |
| [`screenshots/`](./screenshots/) | 10 screenshots (7 imágenes + 3 video posters) de las piezas reales |
| `docs/BRAND_VOICE.md` (del repo) | Brand voice guide condensado de Loggro |
| **Meta Ad Library de Loggro** | https://www.facebook.com/ads/library/?country=CO&q=loggro&active_status=all — referencia adicional viva |
| Virtual key del LLM Broker | En tu `.env` |

## Outputs esperados (por brief, son 3 briefs)

1. **Post LinkedIn** (texto + hook + CTA)
2. **Email outbound** (subject + 3 versiones A/B/C)
3. **Mensaje WhatsApp** (con segmentación por audiencia)
4. **Descripción de anuncio Meta** (headline + body + variaciones)
5. **Hook de landing page** (3 alternativas con razonamiento)
6. **Image prompt detallado** (para Midjourney/DALL-E) por pieza visual

Más:

7. **Reviewer agent** que califica cada pieza contra brand voice y bloquea las que no pasen umbral
8. **README con:**
   - Costo por brief (LLM tokens estimados)
   - Ejemplo de pieza que tu reviewer rechazó y por qué (mostrá el output + el feedback del reviewer)

## Sub-agentes esperados (mínimo 4)

| Sub-agente | Qué hace |
|---|---|
| `Copywriter` | Genera por canal (LinkedIn, email, WhatsApp, Meta, landing) |
| `BrandVoiceReviewer` | Corrige y bloquea piezas que no pasan umbral. Tu sistema lo entrena con `good_pieces.json` (referencia positiva) y `bad_pieces.json` (referencia negativa con violations etiquetadas) |
| `FormatPublisher` | Deja outputs listos para HubSpot / Meta / formato canónico de cada canal |
| `ImagePromptWriter` | Genera briefs visuales para Midjourney/DALL-E por pieza |

## Brand voice — reglas duras de Loggro

Aprende del `good_pieces.json` y `bad_pieces.json` la diferencia. En resumen:

| Violación | Penalización |
|---|---|
| Uso de em-dashes (—) o en-dashes (–) | Alta — es huella típica de AI sin filtro humano. Grego los detesta |
| ChatGPT-genérico ("En el dinámico mundo de los negocios...") | Alta |
| Claims sin sustento ("Aumenta 300% tus ventas en 30 días" sin fuente) | Alta |
| Tone mismatch (informal extremo cuando el ICP es CFO) | Media |
| Format breaks channel (post LinkedIn de 500 chars con tono Instagram) | Media |
| Mock de competidores ("Mejor que Siigo porque Siigo no sirve") | Alta |
| PII leak (mención casual a "Juan Pérez de Acme Corp") | Crítica |
| Mistranslation / typos (facturacíon eléctronica mal acentuado) | Media |
| DIAN compliance violation (claim "no necesitas DIAN") | Crítica |
| Sin CTA o CTA contradictorio | Media |

Tu reviewer debe atrapar al menos los **5 de violación alta/crítica** automáticamente.

## Tests obligatorios sobre tu reviewer

1. Corré tu reviewer contra las **10 piezas de `good_pieces.json`** → debería aprobar al menos 9 (las 10 deberían pasar idealmente)
2. Corré tu reviewer contra las **10 piezas de `bad_pieces.json`** → debería rechazar al menos 8 (las 10 idealmente). Cada rechazo debe identificar correctamente el `violation type`
3. Reportá en tu README: precision + recall + matriz de confusión por violation type

Si tu reviewer aprueba bad pieces o rechaza good pieces → tu sistema necesita ajuste. Documentalo (en qué casos falla + qué cambiarías) en el AI Audit Log.

## Reglas duras del track

1. **Cero em-dashes en tu output.** Hardcodéalo en tu reviewer
2. **Brand voice consistente**: español Colombia natural, sin "ChatGPT corporativo"
3. **No mock competidores** en las piezas que generes
4. **Disclaimers DIAN** cuando aplique (factura electrónica, retención, RUT)
5. **Cifras específicas si las usás** (no redondas tipo "300%", usá "27% en 45 días" con fuente)

## Cómo evaluamos este track

| Dimensión | Qué miramos |
|---|---|
| **Calidad de las piezas generadas** | ¿Pasan brand voice? ¿Adaptan al canal? ¿Hablan al audience del brief? |
| **Precision/recall del reviewer** | ¿Aprueba good pieces? ¿Rechaza bad pieces? ¿Identifica el tipo de violación correcto? |
| **Razonamiento del reviewer** | Cuando rechaza, ¿explica claro qué viola? ¿O solo dice "no pasa"? |
| **Disciplina con brand voice** | ¿Cero em-dashes en tu output? ¿Sin ChatGPT-genérico? |
| **Multi-canal real** | ¿LinkedIn post ≠ WhatsApp? ¿O usaste 1 plantilla con find-replace? |
| **Image prompts** | ¿Son específicos (composición, estilo, paleta) o genéricos ("imagen profesional moderna")? |

## ¿A quién atrae este track?

Creativos técnicos, marketing + IA generativa, content ops, perfiles híbridos copywriter-developer. Si vienes de pura programación sin sensibilidad de marca, este track te muestra los huecos. Si vienes de marketing puro sin código, te toca aprender LLMs aplicados a generación con disciplina (no solo "pídele a ChatGPT").

---

**Vuelve al microsite:** https://labs.loggro.com/growth-engineer
**Carpeta de datos:** [`./`](./)
