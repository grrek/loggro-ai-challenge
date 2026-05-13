# Sessions — transcripts y exports de tus sesiones con IA

Aca subes 2 a 3 sesiones representativas de tu trabajo con un agente / chat IA. La idea NO es vaciar todo el log de tu Claude Code, ni que mandes 50 screenshots. Queremos ver **como trabajaste cuando estabas resolviendo algo no trivial**.

## Que sirve

- **Claude Code:** corre `/export` despues de una sesion productiva, sube el `.md` resultante a este directorio
- **Cursor:** copia el panel de chat (o usa `Cursor: Export Chat`) a un `.md`
- **ChatGPT / Claude.ai:** usa el boton "Share" para link publico, o copia/pega la conversacion a un `.md`
- **Screenshots:** si el flujo fue muy visual (ej: te trabaste con un error y la IA te ayudo a leerlo), 2-3 imagenes vale

## Que NO sirve

- "Le pedi a Claude que me formateara este JSON" — trivial, sin signal
- Sesiones donde la IA hizo todo bien al primer intento (improbable, y si pasa, no nos enteramos de nada)
- Logs de 20.000 tokens con todo el setup — preferimos 1 sesion concentrada de 200 lineas con friccion

## Plantilla por sesion

Sugerido `docs/sessions/session-01.md`:

```markdown
# Sesion 01 — Debuggeando el classifier con doble negacion

**Cuando:** Q2 de tus 48h, hora ~12 del run
**Agente:** Claude Code (Opus 4.7) + 1 subagente
**Duracion:** ~45 min
**Resultado:** subi accuracy de 6/10 a 9/10 cambiando prompt + agregando few-shot

## Por que la elegi

Esta es la sesion donde tuve que parar y pensar. Claude default proponia regex. Lo descartamos y diseñamos few-shot prompt. Aca se ve el ida y vuelta real.

## Transcript (relevante)

[pega aca el export, o link si es muy largo]
```

## Privacidad

No subas keys, tokens, o info sensible de Loggro. Si el agente te ayudo con la virtual key, redacta `LLM_BROKER_KEY=***`.
