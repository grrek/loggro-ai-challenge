# Escenario A — Outbound Automation (Reto VE-1770)

Construyes un sistema de outbound end-to-end: **identificación de cuentas, enrichment, secuencia email + WhatsApp, clasificación de respuestas**.

## Archivos

| Archivo | Que es | Quién lo usa |
|---|---|---|
| **[`ICP.md`](./ICP.md)** | Ideal Customer Profile escrito (criterios, señales, fuentes sugeridas) | Tu input principal. De acá derivas las cuentas a generar |
| `accounts_example.json` | 30 cuentas ya enriquecidas en el formato esperado del output | **Solo referencia**. NO es tu input. Es el formato que tu output debe seguir |
| `responses_sample.json` | 10 respuestas sintéticas (email + WhatsApp) con `groundtruth_intent` | Input para tu clasificador de respuestas + evaluación |
| `README.md` | Este archivo | — |

## Lo que tenés que producir

### 1. Lista de ~100 cuentas nuevas (`accounts.json`)
Cuentas que matchean el ICP, generadas por tu pipeline desde fuentes públicas. Schema en [ICP.md](./ICP.md).

### 2. Secuencia outbound (email + WhatsApp)
Dos versiones por canal mínimo:
- Cold initial (open)
- Bump 1 (follow-up 3-5 días después)

No 1 plantilla para todos. Tiene que adaptarse al sector y rol del destinatario.

### 3. Clasificador de respuestas
Procesa las 10 entradas de `responses_sample.json` y devuelve el `intent` predicho. Compara contra `groundtruth_intent`.

### 4. Pipeline integrado
Los 3 sub-agentes coordinados. Si recibimos una nueva cuenta y una nueva respuesta hipotética, debe correr end-to-end.

## Sub-agentes esperados (sugerido)

| Sub-agente | Qué hace |
|---|---|
| **AccountFinder + Enricher** | Identifica cuentas que matchean el ICP, las enriquece con datos públicos |
| **MessageWriter** | Genera mensajes outbound personalizados por sector + rol |
| **ResponseClassifier** | Clasifica respuestas entrantes en intent (interesado / objecion / pedir_reunion / fuera_de_scope) |

## Schema de `responses_sample.json` (lo que recibe tu clasificador)

| Campo | Tipo | Notas |
|---|---|---|
| `id` | string | `RESP-NNN` (001 a 010) |
| `channel` | string | `email` o `whatsapp` |
| `account_id` | string | FK hacia las cuentas (en `accounts_example.json` y en las tuyas si las generas con esos IDs) |
| `from` | string | Nombre + cargo del que responde (ficticio) |
| `received_at` | string | ISO 8601 con timezone `-05:00` |
| `subject` | string \| null | Solo para email |
| `body` | string | Texto natural en español Colombia |
| `groundtruth_intent` | string | `interesado` / `objecion` / `fuera_de_scope` / `pedir_reunion` |
| `confidence` | string | `high` (6) / `medium` (2) / `low` (2). Los low son ambiguos a propósito |

Distribución:
- 3 `interesado`, 3 `objecion`, 2 `fuera_de_scope`, 2 `pedir_reunion`

## Reglas duras

1. **No hacemos outreach real**. El reto es construir el pipeline, no enviar correos a las cuentas que identifiques.
2. **Cita fuentes** en cada cuenta. Sin fuente verificable → `confidence: low` + justificación.
3. **Respeta TOS** de las plataformas que uses (LinkedIn especialmente — scraping agresivo está prohibido).
4. **Empresas reales en tu output** se tratan como hipotéticas, no como leads. Si querés citarlas en tu demo o Loom, decilo explícito.

## Cómo se evalúa este track

Ver [`eval/judge_prompt.md`](../../eval/judge_prompt.md) para la rúbrica de 5 dimensiones. Lo más específico de Escenario A:

- **Calidad del ICP match**: % de tus 100 cuentas que realmente cumplen el ICP
- **Diversidad sectorial**: balance entre sectores listados
- **Fuentes citadas**: URLs reales o justificación clara cuando no hay
- **Dedupe**: tu pipeline detecta duplicados (mismo dominio, mismo NIT)
- **Secuencia outbound**: adaptada a sector + rol, no template único
- **Clasificador**: precisión contra los 10 cases del `responses_sample.json`

## Estado del dataset

- `accounts_example.json`: 30 cuentas (10 reales verificadas + 20 sintéticas plausibles) en formato canónico. **Solo referencia de formato**.
- `responses_sample.json`: 10 respuestas. Versión final.
