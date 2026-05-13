# Track B - Marketing Insights Dataset

Dataset sintetico para el reto tecnico VE-1770 (Growth Engineer - Automatizacion y IA). El candidato construye un sistema que analiza este snapshot de campanas y produce 3 insights priorizados con accion concreta y deteccion de anomalias.

## Periodo cubierto
Enero a Mayo de 2026 (Q1 + parte de Q2).

## Moneda
Todos los montos en COP. No hay tasas de cambio que convertir.

## Archivo principal

```
track-b-insights/
  campaigns.json                       30 campanas activas Q1-Q2 2026
  README.md                            este archivo
```

## Schema breve

### campaigns.json
Array de 30 objetos con: `id`, `name`, `channel` (linkedin_ads / meta_ads / google_ads / email / whatsapp / organic_seo), `product_line` (8 productos Loggro), `objective`, fechas, presupuesto, gasto, funnel completo (impressions -> clicks -> leads -> mql -> sql -> opportunities -> customers), CAC, audiencia, brief creativo, `landing_page_url`, `lessons_learned` (algunas campanas lo tienen, otras no).

## Anomalias plantadas

Hay anomalias plantadas, encontralas. Las que esperamos que el candidato detecte:

1. **Fatiga creativa con saturacion de audiencia** en una campana POS de Meta (alta frecuencia, CTR cayo significativamente en ultimas semanas).
2. **Audiencia ancha que no convierte** en una campana de awareness LIA donde el CTR luce decente pero la conversion lead-MQL es la mitad del benchmark Meta interno; landing page con bounce rate alto.
3. **Audiencia LinkedIn mal segmentada** en una campana Restobar donde el CTR es bueno pero los leads no son decisores.

## Campanas enganosas (a primera vista lucen bien)

1. **Una campana Meta con CTR alto pero conversion downstream pesima** (bounce rate landing > 80%, casi cero clientes a pesar del trafico).
2. **Una campana awareness Google Display con CTR aparentemente normal pero cero cierre**: 2M impressions, casi 13k clicks, cero customers. El candidato debe notar que es awareness y el funnel no estaba conectado a conversion.

## Consideraciones para el analista

- Los presupuestos no son lineales. Una campana con 65M no necesariamente debe rendir 3x mas que una de 20M; el segmento (Enterprise vs Pymes) cambia el LTV y por tanto el CAC tolerable.
- El CAC solo se calcula cuando hay customers; campanas con `customers = 0` tienen `cac_estimated_cop = null`.
- Los lessons_learned son pistas explicitas que el equipo ya documento, pero faltan en muchas: parte del trabajo es generarlos.

## Stack que se asume (contexto del equipo)
HubSpot + n8n + Meta Ads + Google Ads + LinkedIn Ads + WhatsApp Business + GA4. KPIs principales: MQL, SQL, CPL, CPA, CAC, ROAS, ROI, CTR, conversion por etapa del funnel.

## Estado del dataset

El `campaigns.json` actual es placeholder con 2 entradas para validar el schema. El dataset completo de 30 campanas se sube antes del lanzamiento del reto.
