# Audio scripts: Track D (VE-1770)

Guiones de llamadas comerciales simuladas en espanol Colombia para montar en ElevenLabs y entregar al candidato como MP3. El candidato construye sobre estos audios un pipeline de inteligencia de conversaciones comerciales (STT + extraccion estructurada + risk score + email).

## Indice

| # | Archivo | Escena | Duracion target | Palabras aprox. |
|---|---------|--------|-----------------|-----------------|
| 1 | `01-demo-contadora.md` | Demo Loggro Pymes + FE-DIAN a contadora pyme Bogota | 7 min | 1.000-1.200 |
| 2 | `02-demo-cfo.md` | Demo Loggro Enterprise a CFO mid-market Cali (migracion desde SAP B1) | 8 min | 1.200-1.400 |
| 3 | `03-negociacion.md` | Negociacion vs Siigo y World Office, retail Medellin | 6 min | 900-1.000 |
| 4 | `04-edge-consent-denied.md` | Consentimiento de grabacion negado a los 30 segundos | 2 min | 280-320 |
| 5 | `05-followup-won.md` | Follow up post-venta + cross-sell POS, distribucion Pereira | 5 min | 700-900 |
| 6 | `06-hospitalidad.md` | Demo Loggro Alojamientos a hotel boutique Cartagena | 6 min | 900-1.100 |
| 7 | `07-nomina.md` | Demo Loggro Nomina a RRHH manufactura Barranquilla | 5 min | 700-900 |
| 8 | `08-deal-estancado.md` | Tercera llamada con prospecto que dilata, Bucaramanga | 4 min | 550-700 |
| 9 | `09-referido.md` | Lead caliente por referido, calificacion MEDDPICC light | 4 min | 550-700 |

Total estimado de audio: ~47 minutos.

## Recomendaciones para montar en ElevenLabs

### Modelo
- **`eleven_multilingual_v2`** para todos los guiones. Es el unico que maneja bien acento neutro latinoamericano + colombianismos sin sonar a doblaje espanol.
- NO usar `eleven_turbo_v2_5` para esto: pierde matices emocionales y suena mas robotico en frases largas.

### Voces sugeridas (catalogo ElevenLabs publico, voice-cloning opcional)

#### Andres (vendedor Loggro, masculino, 30s, paisa Medellin)
Aparece en TODOS los guiones excepto el 04 donde tambien sale como anfitrion.
- Primera opcion: **`Mateo`** (voice ID generica multilingual, suena latino joven profesional)
- Alternativas: **`Adam`** (mas neutro, menos colombiano pero limpio), **`Daniel`** (espanol pero pasable si ajustas stability)
- Settings sugeridos: stability `0.45`, similarity `0.75`, style `0.30`, speaker boost ON

#### Clientes (varian por guion)
- **Marcela** (01, contadora 40s, bogotana): voz `Bella` o `Sarah`, stability `0.50`, style `0.25`
- **Carlos** (02, CFO 45s, vallecaucano): voz `Antoni` o `Liam`, tono mas grave, stability `0.55`
- **Patricia** (03, gerente retail 45s, paisa firme): voz `Rachel` o `Charlotte`, style `0.40` (mas enfasis)
- **Marcos** (04, prospecto, masculino neutro): voz `Brian` o `Josh`, stability `0.55`
- **Liliana** (05, gerente admin 40s, eje cafetero): voz `Bella` con style `0.30` (calidez)
- **Diego** (06, hotelero 35s, costeno Cartagena): voz `Antoni` o `Sam`, ritmo mas rapido, stability `0.40`
- **Tatiana** (07, RRHH 40s, barranquillera): voz `Charlotte` o `Domi`, style `0.35`
- **Mauricio** (08, director admin 45s, santandereano): voz `Liam` o `Brian`, stability `0.55`, ritmo lento
- **Sandra** (09, gerente operaciones 40s, manizalita): voz `Sarah` o `Freya`, style `0.30`

Si Grego quiere ultra-realismo: clonar 2 voces (1 hombre paisa, 1 mujer bogotana) con muestras de 3-5 minutos y usar `voice_clone` con `eleven_multilingual_v2`. Las voces clonadas + colombianismos del script dan resultado indistinguible de llamada real.

### Formato del guion

Cada turno arranca con `[speaker_X]` (X = 0 vendedor, 1 cliente). Directivas inline entre corchetes:

- `[pausa Xs]`: silencio de X segundos. Critico en 04 (consentimiento) y 02 (decision).
- `[risa breve]`, `[suspiro]`, `[tos]`: sonidos no verbales que ElevenLabs interpreta.
- `[enfasis]`: palabra siguiente con mas peso (usar con moderacion).
- Muletillas naturales (`ah`, `ok`, `dale`, `listo`, `mmm`) van en el texto sin corchetes.

### Pipeline de generacion sugerido

1. Crear 2 voces base en el dashboard de ElevenLabs (vendedor + cliente). Para guiones con varios speakers cliente, crear voces adicionales.
2. Usar el modo **Projects** o **Studio** de ElevenLabs (no el TTS basico): permite asignar voces distintas a cada speaker, agregar pausas y exportar como MP3 unico.
3. Exportar como `MP3 44.1 kHz 128 kbps` (suficiente para STT, no inflar tamanos).
4. Renombrar archivos como `loggro-call-01.mp3` ... `loggro-call-09.mp3`.
5. Subir los 9 MP3 a un bucket o ZIP que se entrega al candidato junto con el reto tecnico.

### Tips de post-produccion (opcional)

- Agregar 0.5s de silencio al inicio y al final de cada archivo.
- Normalizar a `-16 LUFS` para que todos suenen al mismo volumen.
- NO agregar ruido de fondo artificial: confunde STT.
- Para realismo extra: pasar por filtro telefonico (band-pass 300Hz-3400Hz) si quieres simular grabacion VOIP. Opcional, el candidato puede asumir audio limpio.

## Convenciones de los guiones

- **Vos consistente**: espanol Colombia. Andres usa "usted" con clientes nuevos (primera llamada) y "tu" con clientes ya conocidos (follow ups). Los clientes generalmente lo tutean de vuelta a partir del segundo turno.
- **Realismo**: muletillas, "ah", "ok", "perfecto", "dale", "listo", pausas naturales.
- **Sin emojis decorativos** (solo directivas tipo `[risa breve]`).
- **Cero em-dashes** ni en-dashes. Usar parentesis, comas, dos puntos o punto seguido.
- **NO se inventan precios**. Andres se refiere a "la cifra que les compartimos en el correo" o "la cotizacion que les enviamos".
- **Nombres**: primeros nombres + apellido plausible, sin coincidir con clientes reales de Loggro.
- **Productos mencionados**: Pymes, POS, Restobar, Nomina, Alojamientos, Enterprise, Facturacion Electronica DIAN, LIA.
- **Competidores que pueden aparecer**: Siigo, World Office, Alegra, ContaPyme, Helisa, SAP Business One, NetSuite.

## Que evalua el candidato con estos audios

Los 9 audios cubren intencionalmente los casos que el pipeline de inteligencia de conversaciones tiene que manejar:

- **Transcripcion limpia** (01, 02): audio claro, lenguaje tecnico contable y financiero.
- **Diarizacion** (todos): 2 speakers definidos.
- **Extraccion estructurada** (01, 02, 06, 07): producto demo, objeciones, proximos pasos, monto si se menciona.
- **Risk scoring** (08): senal de bajo engagement, decision-maker ausente.
- **Sales playbook compliance** (03): el vendedor no denigra competencia, defiende valor, ofrece alternativas a descuento.
- **Compliance edge case** (04): consentimiento de grabacion negado, el pipeline debe respetar y marcar el segmento posterior como no procesable para insights.
- **Upsell / cross-sell detection** (05): cliente actual abre oportunidad de otro modulo.
- **Lead qualification** (09): MEDDPICC light, candidato debe extraer los componentes BANT/MEDDPICC.
- **Negociacion y manejo de objeciones** (03, 06, 07): el modelo debe identificar tactica de cierre y proximos pasos.

## Validacion

Cada guion incluye en su cabecera la duracion target y conteo de palabras (asumiendo 150 palabras/minuto de lectura conversacional). Si al renderizar en ElevenLabs el audio sale fuera del rango por mas de 1 minuto, ajustar pausas o ritmo de voz antes de re-renderizar.
