# Track B - Marketing Insights Dataset

Dataset sintetico para el reto tecnico VE-1770 (Analista de Automatizacion y RevOps). El candidato construye un sistema que analiza estas 3 fuentes y produce 3 insights priorizados con accion concreta.

## Periodo cubierto
Enero a Mayo de 2026 (Q1 + parte de Q2). Las fechas de actividad varian por fuente (campanas: enero-mayo; reportes GA: marzo-mayo; transcripciones: abril).

## Moneda
Todos los montos en COP. No hay tasas de cambio que convertir.

## Archivos

```
track-b-insights/
  campaigns.json                       20 campanas activas Q1-Q2 2026
  transcripts.json                     3 transcripciones reuniones Marketing/Growth
  ga_reports/
    report-acquisition.csv             trafico por fuente/medio/campana (70 filas)
    report-pages.csv                   pageviews por URL (90 filas)
    report-events.csv                  eventos GA4 (form_submit, demo_request, etc)
    report-audience.csv                segmentos ciudad x dispositivo (41 filas)
    report-conversion.csv              embudo visit -> customer (60 filas)
  README.md                            este archivo
```

## Schema breve

### campaigns.json
Array de 20 objetos con: `id`, `name`, `channel` (linkedin_ads / meta_ads / google_ads / email / whatsapp / organic_seo), `product_line` (8 productos Loggro), `objective`, fechas, presupuesto, gasto, funnel completo (impressions -> clicks -> leads -> mql -> sql -> opportunities -> customers), CAC, audiencia, brief creativo, `landing_page_url`, `lessons_learned` (solo 5 de 20 lo tienen).

### ga_reports/*.csv
Exportes simulados de Google Analytics 4. La columna `campaign` en acquisition se mapea al `id_slug` de campaigns.json (ej. `fe-dian-2026q1-midmarket` = CAMP-001). El candidato debe cruzar manualmente.

### transcripts.json
Array de 3 reuniones con `participants` (nombres reales del equipo Marketing/Growth Loggro), `transcript` con marcadores `[Nombre]:`, y `mentioned_campaigns` (referencia cruzada a campaigns.json).

## Como cruzar las 3 fuentes

1. **Campana <-> GA**: el slug del `name` en kebab-case = valor de la columna `campaign` en `report-acquisition.csv`. Ej. `FE-DIAN-2026Q1-MidMarket` <-> `fe-dian-2026q1-midmarket`.
2. **Campana <-> landing page**: campo `landing_page_url` en campaigns.json se relaciona con `page_path` en `report-pages.csv` (limpiar el host).
3. **Transcripcion <-> campana**: campo `mentioned_campaigns` lista los IDs. Las transcripciones tambien hacen referencia narrativa al nombre o slug.

## Anomalias plantadas

Hay anomalias plantadas, encontralas. Las que esperamos que el candidato detecte:

1. **Fatiga creativa con saturacion de audiencia** en una campana POS de Meta (alta frecuencia, CTR cayo significativamente en ultimas semanas, mencionada en una transcripcion).
2. **Audiencia ancha que no convierte** en una campana de awareness LIA donde el CTR luce decente pero la conversion lead-MQL es la mitad del benchmark Meta interno; landing page con bounce rate alto.
3. **Audiencia LinkedIn mal segmentada** en una campana Restobar donde el CTR es bueno pero los leads no son decisores; cero alineacion con la audiencia de la campana hermana que si funciona.

## Campanas enganosas (a primera vista lucen bien)

1. **Una campana Meta con CTR alto pero conversion downstream pesima** (bounce rate landing > 80%, casi cero clientes a pesar del trafico).
2. **Una campana awareness Google Display con CTR aparentemente normal pero cero cierre**: 2M impressions, casi 13k clicks, cero customers. El candidato debe notar que es awareness y el funnel no estaba conectado a conversion.

## Insight contradictoria en transcripciones

Una de las 3 transcripciones contiene una afirmacion de un participante que los datos de `campaigns.json` contradicen. El candidato debe pillar la inconsistencia entre lo que se dice en reunion y lo que los datos muestran.

## Consideraciones para el analista

- Los presupuestos no son lineales. Una campana con 65M no necesariamente debe rendir 3x mas que una de 20M; el segmento (Enterprise vs Pymes) cambia el LTV y por tanto el CAC tolerable.
- El CAC solo se calcula cuando hay customers; campanas con `customers = 0` tienen `cac_estimated_cop = null`.
- Los lessons_learned (en solo 5 campanas) son pistas explicitas que el equipo ya documento, pero faltan en las demas: parte del trabajo es generarlos.
- GA reportes tienen filas con `0` (campanas que aun no arrancaron en esa fecha) y filas con `(not set)` (trafico directo y organico).
- Las transcripciones tienen jerga colombiana, interrupciones, dudas. No esperes prosa limpia.

## Stack que se asume (contexto del equipo)
HubSpot + n8n + Meta Ads + Google Ads + LinkedIn Ads + WhatsApp Business + GA4. KPIs principales: MQL, SQL, CPL, CPA, CAC, ROAS, ROI, CTR, conversion por etapa del funnel.
