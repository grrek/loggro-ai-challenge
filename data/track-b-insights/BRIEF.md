# Escenario B — Insights de Campañas de Marketing

> Brief técnico del Escenario B del reto VE-1770. Léelo después de decidir que B es tu track.

## Brief

Construye un sistema que analiza el **portafolio real de campañas de marketing digital de Loggro** (Q1-Q2 2026) y genera:

1. **3 hallazgos priorizados** con hipótesis + métrica + acción concreta + impacto esperado
2. **Detección de anomalías** (encontrar las 3 plantadas)
3. **Flag de campañas engañosas** (vanity metrics que parecen anomalía pero no lo son)

Es trabajo de marketing analytics aplicado: cruzar el funnel completo, identificar patrones, escribir conclusiones que un CMO pueda accionar el lunes.

## Inputs entregados

| Archivo | Qué es |
|---|---|
| [`campaigns.json`](./campaigns.json) | **124 campañas reales** Q1-Q2 2026 anonimizadas |
| Schema enriquecido | Funnel (impressions → clicks → leads → MQL → SQL → customers) + CAC + audiencia + brief + landing + lessons_learned (en ~15 campañas) |
| Cobertura | 7 productos (Pymes, POS, Restobar, Nómina, Enterprise, Alojamientos, Contadores) · 3 canales (Google Ads, Meta Ads, LinkedIn Ads) |
| Estados | `active` y `paused` ambos en el dataset (el candidato decide cómo tratarlos) |
| Virtual key del LLM Broker | En tu `.env` |

**Información clave que NO te decimos:** cuáles son los `campaign_id` de las 3 anomalías ni de las 2 engañosas. Esa es la parte del ejercicio.

## Anomalías plantadas en el dataset

Hay **3 anomalías reales** que tu pipeline debe detectar:

1. **Fatiga creativa con saturación de audiencia** — campaña Meta lead_gen con alta frecuencia (>2.5), CTR cayó significativamente, sin refresh de creative
2. **Audiencia ancha que no convierte** — CTR luce decente pero la conversión lead→MQL es la mitad del benchmark Meta interno (~2% vs 4-6% esperado)
3. **Audiencia LinkedIn mal segmentada** — campaña Restobar donde el CTR es bueno (1.85%) pero los leads NO son decisores; CAC tiende a infinito

## Campañas engañosas (a primera vista lucen bien)

Hay **2 campañas que parecen anomalía pero NO son las que pedimos**. Si tu pipeline las flagea como las 3 anomalías, **resta puntos**. Las identificarás bien si entendés vanity metrics:

1. **CTR alto + conversion downstream cero** — bounce rate alto en landing → leads abundantes sin closure (la métrica vanity)
2. **Awareness con tráfico decente pero cero customers** — era awareness no conectada a pipeline → no es anomalía, es decisión de diseño

## Outputs esperados

Tu pipeline debe producir un JSON con esta forma:

```jsonc
{
  "anomalies_detected": [
    {
      "campaign_id": "CAMP-XXX",
      "anomaly_type": "audience_fatigue_creative_burnout",
      "signals": ["frequency > 2.8", "ctr decay > 50%", "..."],
      "confidence": 0.85,
      "recommended_action": "rotar creative + reducir frecuencia con freq cap"
    }
    // ... otras 2
  ],
  "insights_prioritized": [
    {
      "rank": 1,
      "title": "Re-asignar 30% del budget de Google Search Genérico a Meta Lookalike Pymes",
      "hypothesis": "Meta Lookalike tiene CPL 40% menor que Google Genérico para Pymes",
      "metric_evidence": "CPL Meta LAL: $40K vs Google Genérico: $67K (12 campañas analizadas)",
      "action": "Pausar 2 campañas Google Genérico, redirigir $5M COP/mes a Meta LAL existente",
      "expected_impact": "+~50 MQLs/mes con mismo budget"
    }
    // ... otros 2
  ],
  "vanity_metrics_flagged": [
    {
      "campaign_id": "CAMP-XXX",
      "reason": "CTR alto pero cero customers; bounce 80%+"
    }
  ]
}
```

Más:

1. **Tablero agregado** (markdown, Streamlit, Next.js, libre)
2. **README con arquitectura + 1 hallazgo personal** del conjunto de datos (algo no obvio que descubriste vos)

## Sub-agentes esperados (mínimo 3)

| Sub-agente | Qué hace |
|---|---|
| `DataIngestor` | Ingesta + normaliza JSON, maneja `active` vs `paused`, MQL=0 en awareness, CAC=null cuando customers=0 |
| `CampaignAnalyzer` | Clasifica + compara, detecta anomalías, separa vanity de señal real |
| `InsightPrioritizer` | Genera 3 hallazgos priorizados con acción accionable + número, no 20 hallazgos genéricos |

## Consideraciones para el analista

- **Presupuestos no lineales:** una campaña con 65M no necesariamente rinde 3x más que una de 20M; el segmento (Enterprise vs Pymes) cambia el LTV y por tanto el CAC tolerable
- **CAC solo si hay customers:** campañas con `customers = 0` tienen `cac_cop = null`. No las descartes, mirá el funnel completo
- **MQL = 0 en muchas:** Google Ads y awareness Meta no producen MQL directo (solo lead). No es bug, es diseño del funnel
- **Lessons_learned dispersas:** algunas campañas (~15) tienen aprendizajes documentados; el resto no. Parte del trabajo es identificar patrones que ya están escritos vs los que tenés que inferir vos
- **Status (active/paused):** la campaña pausada puede tener señal útil (alguien la pausó por algo). No la ignores automáticamente

## Stack del equipo Loggro (contexto)

HubSpot + n8n + Meta Ads + Google Ads + LinkedIn Ads + WhatsApp Business + GA4. KPIs principales: MQL, SQL, CPL, CPA, CAC, ROAS, CTR, conversión por etapa del funnel.

## Cómo evaluamos este track

| Dimensión | Qué miramos |
|---|---|
| **Detección de anomalías** | ¿Encontraste las 3? ¿No flageaste las 2 engañosas? |
| **Insights priorizados** | ¿Tienen hipótesis + métrica + acción + número? ¿O son genéricos tipo "subir presupuesto"? |
| **Vanity metrics flagged** | ¿Detectaste las 2 campañas que parecen pero no son? |
| **Razonamiento sobre el funnel** | ¿Cruzaste impressions → MQL → customer? ¿O te quedaste en CTR? |
| **Reasoning quality** | ¿Tu output tiene "porque" claros o son afirmaciones huecas? |
| **Manejo de edge cases** | Campañas paused, MQL=0, CAC=null — ¿las trataste con criterio? |

## ¿A quién atrae este track?

Analytics, data-oriented, candidatos cómodos cruzando fuentes JSON, separando vanity metrics de señal real, y escribiendo conclusiones para un CMO. Si vienes de marketing técnico te sentís en casa. Si vienes de pura programación, te falta el lente de negocio. Si vienes de marketing puro sin datos, te ahogás en el funnel.

---

**Vuelve al microsite:** https://labs.loggro.com/growth-engineer
**Carpeta de datos:** [`./`](./)
