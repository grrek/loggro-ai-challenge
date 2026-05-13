# Track A — Prospección Automatizada (Outbound)

> Brief técnico del Track A del reto VE-1770. Léelo después de decidir que A es tu track.

## Brief

Construye un pipeline de outbound end-to-end:

1. **Identificás ~100 cuentas nuevas** desde un ICP escrito, usando fuentes públicas.
2. **Las enriquecés** con datos verificables (LinkedIn, web propia, RUES, prensa).
3. **Escribís secuencia outbound** (email + WhatsApp) adaptada por sector y rol del decisor.
4. **Clasificás respuestas entrantes** contra un sample con ground_truth.

**NO te damos las cuentas.** Las generas vos desde el ICP. Esa es la diferencia con un take-home clásico.

## Inputs entregados

| Archivo | Qué es |
|---|---|
| [`ICP.md`](./ICP.md) | Ideal Customer Profile escrito — sector + tamaño + ciudad + señales de pain + fuentes sugeridas (RUES, LinkedIn, Apollo trial, etc.) |
| [`accounts_example.json`](./accounts_example.json) | 30 cuentas YA enriquecidas en el formato canónico. **Solo referencia de formato**, NO es tu input |
| [`responses_sample.json`](./responses_sample.json) | 10 respuestas sintéticas con `groundtruth_intent` para entrenar/probar el clasificador |
| `docs/BRAND_VOICE.md` (del repo) | Brand voice guide de Loggro |
| Virtual key del LLM Broker | En tu `.env` (te llegó por correo) |

**Buyer persona objetivo:** dueño de empresa / director de finanzas / emprendedor (PYME-mid market Colombia).

## Outputs esperados

1. **`accounts.json`** — ~100 cuentas nuevas que matchean el ICP, con:
   - `sources` (URLs reales por cuenta)
   - `confidence` (high/medium/low)
   - `icp_match_score` (0-1) con lógica clara, no random
2. **Pipeline reproducible** que genera esas cuentas desde fuentes públicas (RUES, LinkedIn con cuidado, web propia, Apollo/Clearbit trial, o LLM con web search documentado)
3. **Secuencia outbound 2-touchpoint** (email + WhatsApp):
   - Cold initial (open)
   - Bump 1 (follow-up 3-5 días después)
   - Adaptada por sector + rol (NO 1 plantilla para todos)
4. **Clasificador de respuestas** que procesa los 10 cases de `responses_sample.json` y reporta accuracy vs `groundtruth_intent`
5. **README con:**
   - % de tus 100 cuentas que cumplen el ICP
   - Diversidad sectorial (qué sectores cubriste y conteo)
   - Tasa de duplicados detectados por tu pipeline
   - Costo agregado (LLM tokens + APIs externas si usaste)
   - Latencia (tiempo medio para enriquecer 1 cuenta)
   - Plan de escalamiento a 1.000 cuentas/mes

## Sub-agentes esperados (mínimo 3)

| Sub-agente | Qué hace |
|---|---|
| `AccountFinder + Enricher` | Identifica cuentas que matchean el ICP + las enriquece con datos públicos (web propia, LinkedIn, RUES, prensa) |
| `MessageWriter` | Genera mensajes outbound personalizados por sector + rol. No plantilla inflada |
| `ResponseClassifier` | Intent detection: `interesado` / `objecion` / `fuera_de_scope` / `pedir_reunion`. Tu output se compara contra `groundtruth_intent` |

**Si querés single-agent con tool use:** justificalo en <100 palabras por qué es la decisión correcta para este track.

## Reglas duras del track

1. **No hacemos outreach real.** El reto es construir el pipeline, no enviar correos.
2. **Cita fuentes en cada cuenta.** Sin fuente verificable → `confidence: low` + justificación en el campo.
3. **Respeta TOS** de las plataformas que uses (LinkedIn especialmente — scraping agresivo está prohibido; Phantombuster / Apify con rate limits sensatos o uso manual está OK).
4. **Empresas reales en tu output** se tratan como hipotéticas, no como leads. Si las citás en tu Loom o demo, decílo explícito.
5. **No inventes datos** que se puedan verificar (ingresos exactos, número de empleados específico). Usá bandas y rangos.

## ¿Puedo usar IA para generar las cuentas?

Sí, totalmente. **Pero documentalo en tu AI Audit Log.** Por ejemplo, si usás Claude con web search para encontrar 30 cuentas en el sector hospitalidad, escribilo. Lo medimos como uso de IA bueno (apalancarla para search), no como "inventaste cuentas con LLM".

Si **generaste** cuentas (no encontraste, las inventaste con justificación porque el ICP es muy específico y no hay muchas reales), marcalas con `verified: false` en tu output y explicá tu razonamiento en el README.

## Cómo evaluamos este track

| Dimensión | Qué miramos |
|---|---|
| **Calidad del ICP match** | De tus 100 cuentas, ¿qué % realmente cumple el ICP? Si decís que tienes 100 pero 30 son <50 empleados o de otro país, baja la nota |
| **Diversidad sectorial** | ¿Concentraste en un solo sector o tenés mix balanceado? |
| **Fuentes citadas** | ¿Las URLs realmente existen? ¿Las señales son verificables? |
| **Dedupe** | ¿Tu pipeline detecta empresas duplicadas (mismo dominio, mismo NIT)? |
| **Justificación del scoring** | Tu `icp_match_score` y `confidence` deben tener lógica clara, no ser random |
| **Secuencia outreach** | Email + WhatsApp adaptados al sector y rol del destinatario. No 1 plantilla para todos |
| **Clasificador de respuestas** | Funciona contra `responses_sample.json` (incluido) — accuracy + manejo de los casos `confidence: low` ambiguos |

## ¿A quién atrae este track?

SDR / growth con experiencia en prospección en frío. Alguien que entiende que un asunto malo mata cualquier secuencia y que sabe scrapear fuentes públicas con criterio. Si vienes de RevOps puro / data-only, sentís que falta drama. Si vienes de copywriting puro, sentís que falta data.

## Lo que NO querés hacer

- ❌ Enviar correos reales (NO)
- ❌ Pagar herramientas de scraping (gratuitas o trial son suficientes)
- ❌ Generar 1.000 cuentas (100 con calidad > 500 con basura)
- ❌ Cubrir todos los sectores listados en el ICP (5-6 con buen mix está bien)
- ❌ 1 plantilla para todos los sectores

---

**Vuelve al microsite:** https://labs.loggro.com/growth-engineer
**Carpeta de datos:** [`./`](./)
