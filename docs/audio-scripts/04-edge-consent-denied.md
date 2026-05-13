# 04. Edge case: consentimiento de grabacion negado

**Duracion target:** 2 minutos (~280-320 palabras)

**Voces:**
- `speaker_0` (Andres, vendedor Loggro, masculino, 30s, paisa Medellin): voz tipo `Mateo`, stability 0.45
- `speaker_1` (Marcos Beltran, prospecto, masculino, 40s, acento neutro): voz tipo `Brian` o `Josh`, stability 0.55

**Contexto:** Primera llamada. Andres marca a Marcos, director financiero de una pyme de servicios profesionales. Es discovery inicial. A los 30 segundos Andres da el aviso de grabacion y Marcos pide no ser grabado. Andres acepta de inmediato, detiene la grabacion, y la conversacion sigue brevemente sin contenido procesable.

**Tono:** respeto, cumplimiento Habeas Data. Andres profesional, sin friccion. Marcos firme pero amable.

**Comportamiento esperado del pipeline:** detectar el instante exacto en que Marcos niega consentimiento. Todo lo anterior es procesable. Todo lo posterior se marca `consent_denied=true` y NO se procesa para extraccion de insights ni transcripcion completa. Solo metadata (duracion, participantes, timestamp de denegacion).

**Directivas de voz globales:** ritmo natural, pausa marcada de 2 segundos despues de la denegacion (Andres procesa y responde).

---

[speaker_0] Hola Marcos, buenos dias, soy Andres de Loggro. ¿Me escucha bien?

[speaker_1] Buenos dias Andres, si lo escucho.

[speaker_0] Perfecto Marcos. Gracias por sacar el espacio. Como hablamos por correo, la idea es que tengamos una conversacion corta para entender un poco el contexto de su empresa, los retos que tienen en el area administrativa y financiera, y ver si lo que ofrecemos en Loggro hace sentido para ustedes. ¿Le funciona el tiempo de los treinta minutos que agendamos?

[speaker_1] Si, treinta minutos esta bien.

[speaker_0] Listo. Antes de entrar en materia, le informo Marcos que esta llamada se esta grabando para fines de calidad y mejora del servicio. La grabacion se guarda con todas las garantias de habeas data y usted puede solicitar acceso o eliminacion en cualquier momento. [pausa 1s]

[speaker_1] Ah, mira Andres, te voy a pedir el favor. Yo preferiria que no la graben. ¿Podemos seguir sin grabacion?

[pausa 2s]

[speaker_0] Por supuesto Marcos, lo entiendo perfecto. Detengo la grabacion en este momento. [pausa 1s] Listo, ya quedo detenida. Si le sirve, podemos hacer la siguiente cosa: yo despues de la llamada le mando un correo con el resumen de lo que conversemos y los siguientes pasos. Asi queda registro escrito de lo acordado pero sin grabacion de audio. ¿Le parece?

[speaker_1] Si, eso me parece bien. Gracias por la flexibilidad.

[speaker_0] Con gusto Marcos. Es completamente su derecho y para nosotros es lo normal. Bueno, entonces sigamos. Cuenteme un poco del momento de la empresa, ¿en que rubro estan, mas o menos cuantos empleados manejan?

[speaker_1] Somos firma de consultoria, llevamos doce anos. Hoy somos cuarenta y cinco personas, oficinas en Bogota y Medellin.

[speaker_0] Excelente. Marcos, antes de que sigamos en detalle, quiero confirmar la agenda de la llamada de hoy con usted. ¿Le parece si arrancamos por entender que sistemas usan hoy y de ahi vamos a los dolores?

[speaker_1] Perfecto, dale.
