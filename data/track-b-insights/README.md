# Track B - Marketing Insights Dataset

Dataset real (Q1-Q2 2026) anonimizado de las campañas activas y pausadas de Loggro. El candidato construye un sistema que analiza este snapshot y produce **3 insights priorizados con acción concreta y detección de anomalías**.

## Periodo cubierto
Enero a Mayo de 2026 (Q1 + parte de Q2).

## Moneda
Todos los montos en COP. No hay tasas de cambio que convertir.

## Archivo principal

```
track-b-insights/
  campaigns.json                       124 campañas reales Q1-Q2 2026
  README.md                            este archivo
```

## Conteo y diversidad

- **124 campañas** totales
- **Productos cubiertos:** Pymes, POS, Restobar, Nómina, Enterprise, Alojamientos, Contadores
- **Canales:** Google Ads, Meta Ads, LinkedIn Ads
- **Objectives:** lead_gen (mayoría), awareness, engagement
- **Estados:** active, paused (ambos en el dataset, el candidato decide cómo tratarlos)

## Schema completo (por campaña)

```jsonc
{
  "id": "CAMP-001",
  "name": "Pymes 031 - Visitas V3 (similares) Advantage Mix",
  "name_slug": "pymes-031-visitas-v3-similares-advantage-mix",
  "status": "active",            // o "paused"
  "channel": "meta_ads",          // o "google_ads", "linkedin_ads"
  "product_line": "Pymes",        // categoría de producto Loggro
  "objective": "lead_gen",        // o "awareness", "engagement"
  "start_date": "2026-02-14",
  "end_date": null,               // null = aún corriendo
  "budget_cop": 9500000,
  "spend_cop": 7594542,
  "funnel": {
    "impressions": 320473,
    "reach": 274757,
    "clicks": 4400,
    "ctr_pct": 1.37,
    "cpc_cop": 1726,
    "frequency": 1.17,
    "leads": 127,
    "cost_per_lead_cop": 59799,
    "mql": 4,
    "cost_per_mql_cop": 1898636,
    "sql": 2,                     // sintético: mql * 0.40
    "customers": 0,
    "cac_cop": null               // null cuando customers = 0
  },
  "audience": {
    "type": "lookalike",          // lookalike / custom / broad_interests / remarketing / scraped_db / branded_search / intent_high / existing_customers / lead_magnet / linkedin_job_titles
    "size_estimate": 274757
  },
  "brief_summary": "Visitas similares Advantage Mix",
  "landing_page_url": "https://loggro.com/pymes/visitas-similares",
  "lessons_learned": null         // algunas campañas tienen aprendizajes documentados, otras no
}
```

## Anomalías plantadas

Hay 3 anomalías reales en el dataset. **No te decimos cuáles son los IDs**, esa es parte del ejercicio. Las que esperamos que tu pipeline detecte:

1. **Fatiga creativa con saturación de audiencia** en una campaña Meta lead_gen (alta frecuencia >2.5, CTR cayó significativamente, sin refresh de creative).
2. **Audiencia ancha que no convierte**: una campaña donde el CTR luce decente pero la conversión lead→MQL es la mitad del benchmark Meta interno (~2% vs 4-6% esperado).
3. **Audiencia LinkedIn mal segmentada**: una campaña Restobar donde el CTR es bueno (1.85%), llegan leads pero NO son decisores; CAC tiende a infinito.

## Campañas engañosas (a primera vista lucen bien)

Hay 2 campañas que **parecen** anomalía pero no son el patrón principal. Si tu pipeline las marca como las 3 anomalías que pedimos, **resta puntos**. Las identificarás bien si entendés vanity metrics:

1. **CTR alto + conversion downstream cero**: bounce rate alto en landing → leads abundantes sin closure (la métrica vanity).
2. **Awareness con tráfico decente pero cero customers**: era awareness no conectada a pipeline → no es anomalía, es decisión de diseño.

## Cómo evaluamos tu output

Tu sistema debe producir un JSON con la forma:

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
    {"campaign_id": "CAMP-XXX", "reason": "CTR alto pero cero customers; bounce 80%+"}
  ]
}
```

## Held-out evaluation

Loggro mantiene **5 casos held-out privados** que NO están en este repo (`cases_b.json` privado). Cada caso es un subconjunto de ~30 campañas con anomalía conocida. Tu pipeline corre contra ellos vía `eval/eval.py --track b`. Threshold para avanzar: **3/5 pasan + reasoning_quality >= 0.7**.

## Consideraciones para el analista

- **Presupuestos no lineales:** una campaña con 65M no necesariamente rinde 3x más que una de 20M; el segmento (Enterprise vs Pymes) cambia el LTV y por tanto el CAC tolerable.
- **CAC sólo si hay customers:** campañas con `customers = 0` tienen `cac_cop = null`. No las descartes, mirá el funnel completo.
- **MQL = 0 en muchas:** Google Ads y awareness Meta no producen MQL directo (sólo lead). No es bug, es diseño del funnel.
- **Lessons_learned dispersas:** algunas campañas (~15) tienen aprendizajes documentados; el resto no. Parte del trabajo es identificar patrones que ya están escritos vs los que tenés que inferir vos.
- **Status (active/paused):** la campaña pausada puede tener señal útil (alguien la pausó por algo). No la ignores automáticamente.

## Stack del equipo Loggro (contexto)

HubSpot + n8n + Meta Ads + Google Ads + LinkedIn Ads + WhatsApp Business + GA4. KPIs principales: MQL, SQL, CPL, CPA, CAC, ROAS, CTR, conversión por etapa del funnel.
