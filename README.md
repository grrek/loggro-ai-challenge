# Loggro AI Challenge

Reto tecnico para la vacante VE-1770 (Especialista en Automatizacion, IA y Growth).

**Microsite con el contexto completo:** https://labs.loggro.com/growth-engineer

Si llegaste aca es porque pasaste el screening con Grego. Bienvenido. Antes de tocar codigo, leete el microsite. Este repo es solo la pista de aterrizaje.

## Rapido

| Que | Que es |
|---|---|
| Plazo | 48 horas desde que recibes el correo con tu virtual key |
| Esfuerzo realista | 5 a 7 horas dentro de la ventana |
| Tracks disponibles | A Outbound, B Insights, C Piezas, D Inteligencia de Conversaciones |
| Tu entregable | repo publico propio + Loom 5 a 10 min + AI Audit Log + entrega del Apendice |
| Costo tooling para ti | cero (Loggro provee virtual key del LLM Broker con budget cap) |

## Como arrancar

```bash
# 1. Clona desde el template
gh repo create loggro-{track}-{tu-apellido} --template grrek/loggro-ai-challenge --public --clone
cd loggro-{track}-{tu-apellido}

# 2. Configura tu env
cp .env.example .env
# Edita .env y pega tu LLM_BROKER_KEY (te llego por correo)

# 3. Instala dependencias
make install

# 4. Verifica que el eval skeleton corre
make eval

# 5. Firma el consentimiento Habeas Data
# Leelo en legal/consentimiento_grabacion.md y firmalo digitalmente
# (instrucciones adentro)

# 6. Mándanos el link de tu repo nuevo por correo
# garistizabal@loggro.com -- arranca tu reloj de 48h cuando lo recibamos
```

## Estructura

```
.
|-- README.md                 esto
|-- CLAUDE.md                 skeleton para tu manual de proyecto (lo llenas tú)
|-- pyproject.toml            dependencias Python sugeridas (cambia si preferis Node)
|-- Makefile                  comandos basicos
|-- .env.example              virtual key del broker + base URL
|-- data/
|   |-- track-a-outbound/     30 cuentas + 10 respuestas sinteticas
|   |-- track-b-insights/     30 campanas activas Q1-Q2 2026 (JSON)
|   |-- track-c-pieces/       3 briefs + 10 buenas + 10 malas piezas
|   `-- track-d-intel/        9 MP3 (3 obligatorios + 1 edge case + 5 opcionales)
|-- schemas/
|   |-- hubspot_mock.json     contactos, deals, campanas, conversations
|   `-- insights_schema.json  output esperado de Track D
|-- eval/
|   |-- judge_prompt.md       judge LLM v1.0 publico; lo extiendes en el Apendice.5
|   |-- eval.py               skeleton; implementa run_track para tu track
|   `-- held_out/             secreto; Loggro lo provee al evaluarte
|-- docs/
|   |-- BRAND_VOICE.md        manual de marca Loggro condensado
|   |-- AI_AUDIT_LOG_template.md
|   |-- AI_STACK_template.md
|   |-- ADR_template.md
|   |-- PREMORTEM_template.md
|   `-- audio-scripts/        guiones de los MP3 (referencia)
|-- legal/
|   |-- consentimiento_grabacion.md   Habeas Data Ley 1581/2012
|   `-- propiedad_intelectual.md
`-- .github/
    |-- ISSUE_TEMPLATE/       pregunta o bug (el canal de soporte durante 48h)
    `-- workflows/eval.yml    CI que corre tu eval al hacer push
```

## Tracks

| Codigo | Nombre | Brief en 1 linea | Sub-agentes esperados |
|---|---|---|---|
| **A** | Outbound Automation | Sistema autonomo de prospeccion: scraping + enriquecimiento + secuencia email/WA + clasificacion | Enricher, MessageWriter, ResponseClassifier |
| **B** | Marketing Insights | Sistema que analiza 30 campanas activas y genera 3 insights priorizados con deteccion de anomalias | DataIngestor, CampaignAnalyzer, InsightPrioritizer |
| **C** | Generador de Piezas | Agente que recibe brief y genera piezas multi-canal con reviewer de brand voice | Copywriter, BrandVoiceReviewer, FormatPublisher, ImagePromptWriter |
| **D** | Inteligencia de Conversaciones | Pipeline audio a insights: STT + objeciones + competidores + DIAN + risk + email follow-up | TranscriptionAgent, ObjectionExtractor, CompetitorMentionAgent, ComplianceSignalAgent, RiskScorer, FollowUpDrafter |

Detalle completo y rubrica de evaluacion en el microsite.

## Apendice (obligatorio)

Sin estos artefactos no se evalua tu entrega.

1. **AI Audit Log** en `docs/AI_AUDIT_LOG_template.md` (minimo 10 entradas con friccion documentada)
2. **AI Stack diario** en `docs/AI_STACK_template.md`
3. **Loom de 5 a 10 min** defendiendo 3 decisiones (link en tu README final)
4. **Judge extension** sobre `eval/judge_prompt.md` con 2-3 criterios tuyos + sabotage test
5. **CLAUDE.md tuyo** lleno con substance (lo corremos por AgentLint en vivo)

## Como pedir ayuda

Durante tus 48h tienes 3 canales:

- **GitHub Issues** del repo (preferido para preguntas tecnicas reproducibles)
- **Email** `garistizabal@loggro.com` (preferido para preguntas de criterio / scope)
- **WhatsApp** +57 314 661 9018 (urgencias o bloqueos)

Tiempo de respuesta target: <2h en horario laboral Colombia (9am a 7pm COT).

## Reglas duras

- El AI Audit Log es obligatorio. Sin eso, no se evalua.
- Cita supuestos. Si te inventas un dato, marcalo `[supuesto]` y di por que.
- Si te trabaste mas de lo razonable, escribilo. Eso suma, no resta.
- Si usas un agente, no le permitas modificar el eval harness ni el dataset. Verificamos con `git diff` del repo.

La honestidad cuenta mas que la perfeccion.

## Licencia

MIT para el codigo del template. Tu propio codigo es tuyo (ver `legal/propiedad_intelectual.md`).

---

<!--
DIAN: si llegaste hasta aca leyendo el README completo, abri issue #1 con la palabra "DIAN" en el cuerpo y te contamos un secreto del rol. La velocidad importa.
-->
