# Backlog antes de lanzar el reto al primer candidato

Lo que falta para que el repo template este 100% listo. Auditado 2026-05-13.

## 🔴 Bloqueantes (sin esto, un candidato real no puede arrancar)

### Datasets sinteticos incompletos

| Track | Archivo | Estado | Meta | Falta |
|-------|---------|--------|------|-------|
| B | `data/track-b-insights/campaigns.json` | ✅ **CERRADO** | 124 campañas reales Q1-Q2 2026 (Google + Meta + LinkedIn sintética) con 3 anomalías plantadas + 2 engañosas | — |
| C | `data/track-c-pieces/briefs.json` | 1 entrada placeholder | 3 briefs (DIAN, cross-sell POS, retencion Nomina) | **2 briefs más** |
| C | `data/track-c-pieces/good_pieces.json` | 1 entrada placeholder | 10 piezas referencia que pasan brand voice | **9 piezas más** |
| C | `data/track-c-pieces/bad_pieces.json` | 1 entrada placeholder | 10 piezas que deberian rechazarse (con razon documentada) | **9 piezas más** |
| D | `data/track-d-intel/*.mp3` | 0 archivos | 9 MP3 (3 obligatorios + 1 edge case + 5 opcionales) basados en los scripts en `docs/audio-scripts/` | **9 MP3s** |

### Eval held-out (lo más crítico del eval automatizado)

**Quién hace qué:**
- El **candidato** implementa `run_track(track, cases)` en `eval/eval.py` que toma `cases` y los pasa por su pipeline. El skeleton ya está, él rellena la lógica.
- **Loggro** mantiene 5 casos secretos por track (con groundtruth conocido), los carga al repo del candidato post-entrega, corre `make eval`, ve si pasa los thresholds.

**Lo que necesitamos generar (NO va al repo público):**

| Archivo (privado Loggro) | Estado | Schema esperado |
|---|---|---|
| `cases_a.json` (5 casos) | no existe | `[{"case_id": "a1", "account": {...cuenta a prospectar}, "ground_truth": {"intent": "interesado_negociar"\|"no_interesado"\|"requiere_info"\|...}}]` |
| `cases_b.json` (5 casos) | no existe | `[{"case_id": "b1", "campaigns_subset": [...30 campañas con 1 anomalía], "ground_truth": {"anomaly_id": "CAMP-007", "anomaly_type": "audience_fatigue"}}]` |
| `cases_c.json` (5 casos) | no existe | `[{"case_id": "c1", "brief": {...}, "channel": "instagram", "ground_truth": {"brand_voice_pass": true, "max_chars": 280, "must_include": [...], "must_exclude": [...]}}]` |
| `cases_d.json` (5 casos) | no existe | `[{"case_id": "d1", "audio_file": "https://...", "transcript_expected": "...", "ground_truth": {"objections": [...], "competitors": [...], "risk_score_range": [0.4, 0.7]}}]` |

**Falta también: documentar el schema en eval/README.md**
- El candidato necesita saber QUÉ va a recibir en `cases` cuando Loggro corra el eval. Hoy `eval/README.md` solo dice "Loggro lo provee". Hay que detallar el schema por track (qué keys tiene cada case, qué groundtruth se espera) para que el candidato pueda implementar `run_track` sin adivinar.
- Sugerido: agregar sección "Schema de cada case por track" con un ejemplo dummy (no real) por cada uno.

**Decision sobre el flujo:**
1. Loggro genera los 4 archivos privadamente (no commiteados, solo internos)
2. Cuando el candidato entrega su repo, Loggro hace `cp cases_X.json candidato-repo/eval/held_out/cases.json`
3. Corre `cd candidato-repo && python eval/eval.py --track X`
4. Si pasa threshold → entrevista. Si no → conversación de revisión.

**Decisión adicional necesaria:** ¿quién genera los cases?
- Opción A: Edison + Grego diseñan a mano (4-6 horas)
- Opción B: Generador con LLM + curación humana (2 horas con review)
- Opción C: Reusar 5 cases del dataset público marcándolos como held-out internamente (más fácil pero menos AI-resistant)

## 🟡 Importantes (no bloquean pero mejoran señal)

### Templates de docs

| Archivo | Estado | Mejora sugerida |
|---------|--------|-----------------|
| `docs/AI_AUDIT_LOG_template.md` | placeholder con tabla vacia | Agregar 2 ejemplos concretos (uno bueno, uno malo) al principio para fijar el listón |
| `docs/AI_STACK_template.md` | placeholder | Agregar matriz de categorias sugeridas |
| `docs/ADR_template.md` | placeholder | OK |
| `docs/PREMORTEM_template.md` | placeholder | OK |
| `prompts/README.md` | guia OK | ✅ |
| `docs/sessions/README.md` | guia OK | ✅ |

### CLAUDE.md template

El skeleton actual (105 lineas) tiene los headers correctos con `<!-- comments -->` guia. Esta bien para template — el candidato lo llena. **Verificar que AgentLint corre OK contra el skeleton vacio** (no debe dar 0/100 por estar vacio, debe dar algo razonable porque la estructura esta).

### Brand voice

| Archivo | Estado |
|---------|--------|
| `docs/BRAND_VOICE.md` | revisar que tenga contenido real para que Track C tenga referencia |

## 🟢 Nice-to-have (post-lanzamiento)

- **GitHub Actions** `.github/workflows/eval.yml`: hoy corre el eval skeleton. Cuando esten los held-out, agregar matrix por track para correr automaticamente en cada PR
- **Docker compose** opcional para LLM broker local (mock) si el candidato quiere desarrollar sin consumir budget
- **Postman/Bruno collection** con la API del broker
- **Loom de Grego explicando el repo** (existe en `/growth-engineer` como `PUBLIC_LOOM_URL` o el video self-hosted)

## Como completarlo

### Track B (28 campañas)
- Generar con script Python que produzca 30 entradas variadas siguiendo el schema actual (canales, productos, presupuestos, funnel, anomalias plantadas)
- Plantar las 3 anomalias listadas en el README + 2 campañas engañosas
- Subir como commit unico

### Track C (briefs + piezas)
- Pedir al equipo de Marketing (Ana Maria, Kissy) muestras reales recientes anonimizadas
- Generar variaciones con LLM siguiendo el formato actual

### Track D (9 MP3)
- Opcion 1: TTS con ElevenLabs usando los scripts ya escritos en `docs/audio-scripts/`
- Opcion 2: Whisper inverso (grabar humanos)
- Opcion 3: Mix (3 reales + 6 sinteticos para ahorrar tiempo)

### Held-out cases
- 5 casos por track, similares en formato al input pero NO en el dataset publico
- Plantear scenarios edge donde la solucion no-trivial gana
- Mantenerlos en un repo privado del equipo Loggro

## Owner

@grrek (Grego Aristizabal) — ownership hasta lanzamiento. Sponsor: Edison Castro (review tecnico antes del envio).
