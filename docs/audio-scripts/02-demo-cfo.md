# 02. Demo Loggro Enterprise a CFO mid-market (NIIF Plena, multi-compania, migracion desde SAP B1)

**Duracion target:** 8 minutos (~1.200-1.400 palabras)

**Voces:**
- `speaker_0` (Andres, vendedor Loggro Enterprise, masculino, 30s, paisa Medellin): voz tipo `Mateo`, stability 0.45
- `speaker_1` (Carlos Restrepo, CFO mid-market, masculino, 45s, vallecaucano): voz tipo `Antoni` o `Liam`, tono grave, stability 0.55

**Contexto:** Tercera reunion. Carlos es CFO de un grupo manufacturero y de distribucion con tres razones sociales, 350 empleados, sede principal en Cali, con unidad de export en dolares. Hoy tienen SAP Business One desde hace 8 anos, la licencia se renueva en 4 meses, el costo de renovacion subio 30%. Estan migrando de NIIF Pyme a NIIF Plena por tamano. Andres viene de discovery + envio de propuesta tecnica + ahora demo enfocada en consolidacion y migracion.

**Tono:** tecnico de pares, gerencial. Carlos sabe lo que pregunta, Andres no infla. Ritmo medio. Carlos puede sonar escepticismo controlado.

**Directivas de voz globales:** ritmo natural, pausas de 0.5s entre turnos, Carlos pausa mas largo al final de algunas preguntas (procesando).

---

[speaker_0] Carlos, buenos dias. ¿Como esta?

[speaker_1] Hola Andres, bien, bien. Listo para la demo, tengo bloqueada la hora completa.

[speaker_0] Perfecto. Antes de entrar a pantalla, quiero confirmar la agenda. Vamos a cubrir cuatro cosas: primero, como Loggro Enterprise maneja sus tres razones sociales con consolidacion mensual. Segundo, soporte de NIIF Plena que era el dolor que usted me menciono. Tercero, la parte de multi-moneda para la unidad de export. Y cuarto, vamos a hablar de migracion desde SAP B1, que se que es la decision mas grande de esto. ¿Le funciona el orden?

[speaker_1] Funciona. Yo le agrego uno mas: quiero entender que tan modular es el equipo de implementacion que ponen. Eso para mi pesa tanto como el software.

[speaker_0] Excelente, ese lo cubro en el cuarto bloque. Voy compartiendo pantalla. ¿Ya ve el panel principal?

[speaker_1] Si, ya lo veo.

[speaker_0] Esto es el ambiente de Loggro Enterprise con un grupo demo que monte parecido al de ustedes: tres razones sociales, una holding, una operativa de manufactura y una comercial de distribucion. Cada una tiene su propio plan de cuentas pero estan sincronizadas contra un plan corporativo unificado. Cuando yo cierro mes en cada compania, el sistema corre la consolidacion automatica contra el plan corporativo, elimina intercompany y me genera los estados financieros consolidados del grupo.

[speaker_1] Espereme. ¿Eliminacion de intercompany automatica? ¿Como funciona eso? Porque en B1 nosotros tenemos un proceso manual brutal para eso.

[speaker_0] Si senor. Las cuentas que ustedes definan como "intercompany" en el plan corporativo se etiquetan al momento del registro contable. Cuando llega el cierre, el motor de consolidacion identifica los pares (lo que A le debe a B y lo que B le cobro a A) y los cancela automaticamente. Si hay diferencias por tipo de cambio o por timing, el sistema le saca un reporte de partidas no conciliadas para que su equipo revise antes de cerrar.

[speaker_1] Mmm. ¿Y eso lo configura uno o lo configura el equipo de implementacion?

[speaker_0] Lo configura el equipo de implementacion en la fase uno, basado en el mapeo de cuentas suyo. Despues su equipo puede ajustarlo. No es un sistema que usted llega y configura solo, es un sistema que se entrega configurado a su realidad. Sigamos. Aqui esta el reporte consolidado del grupo en NIIF Plena.

[speaker_1] Ah, ahi entra mi siguiente pregunta. ¿Soportan reportes NIIF Plena completos? Nosotros estamos en transicion. Hoy somos NIIF Pyme pero por tamano ya nos toca migrar a Plena este ano. Necesito saber si el sistema me da los reportes correctos: estado de situacion financiera, estado de resultados integral, estado de cambios en el patrimonio, flujo de efectivo metodo directo, todo bajo NIIF Plena.

[speaker_0] Si, los cinco estados financieros bajo NIIF Plena estan soportados. Y mas importante, el sistema maneja los ajustes diferenciales entre NIIF Pyme y NIIF Plena, que es lo que generalmente complica la migracion. Por ejemplo, NIIF Plena le exige a usted reconocer instrumentos financieros a valor razonable con cambios en resultados, mientras que NIIF Pyme le permite costo amortizado. El sistema tiene el modulo de valoracion de instrumentos financieros activable, no es nativo de la version Pyme.

[speaker_1] Ok. ¿Y deterioro de cartera bajo modelo de perdida esperada? Porque eso bajo NIIF Plena es mucho mas riguroso.

[speaker_0] Soportado. El modulo de cartera tiene parametrizacion para modelo de perdida esperada con segmentos de riesgo configurables, historicos de comportamiento y probabilidades. Ahi le doy un dato honesto: la configuracion fina del modelo de perdida esperada la hacemos con su revisor fiscal, no es algo que uno saque de una plantilla generica.

[speaker_1] Eso me parece honesto. Sigamos con la multi-moneda.

[speaker_0] Listo. Aqui le muestro el modulo de la unidad de export. Cada documento se registra en la moneda de la transaccion (en este caso dolares) y el sistema le hace el equivalente automatico al peso colombiano con la TRM oficial del Banco de la Republica del dia, que se descarga automatico. Al cierre de mes, el sistema le corre la revaluacion de saldos en moneda extranjera contra la TRM del ultimo dia del mes y le genera el ajuste por diferencia en cambio, separado por origen (cartera, cuentas por pagar, efectivo en moneda extranjera).

[speaker_1] ¿Eso queda en el estado de resultados o lo segrega como otro resultado integral?

[speaker_0] Por defecto en estado de resultados, pero esta parametrizable. Si tienen operaciones de cobertura o si quieren tratamiento de operacion extranjera con criterios NIIF, eso se configura en la fase de implementacion.

[speaker_1] Ok Andres, me esta haciendo sentido todo. Vamos al cuarto bloque, que es el que me tiene mas pensativo. Migracion desde SAP B1. Tengo ocho anos de historico ahi. Tengo procesos cableados. Tengo gente que aprendio B1 a la fuerza. ¿Como me venden esto y como me lo implementan sin que pare la operacion?

[speaker_0] Voy a serle directo Carlos. Loggro Enterprise no es self-serve. Yo no le voy a decir "compre la licencia y arranque manana", porque no es asi. Loggro Enterprise viene con proyecto de implementacion. Un proyecto serio para su tamano dura entre cuatro y seis meses en paralelo con B1. Le explico la metodologia.

[speaker_1] Dele.

[speaker_0] Fase uno, descubrimiento y diseno. Un mes y medio. Le asignamos un gerente de proyecto dedicado, un consultor funcional senior y un arquitecto. Levantan todos los procesos de B1, los mapean a Loggro y deciden que se migra, que se transforma y que se elimina. Esto es importante: migrar a Loggro no es replicar B1, es mejorar lo que ya tienen. Fase dos, configuracion y carga de datos maestros. Un mes. Plan de cuentas, terceros, productos, centros de costo, todo cargado y validado. Fase tres, paralelo. Dos a tres meses con los dos sistemas corriendo, su gente operando en Loggro pero respaldada en B1. Cierres comparados mes contra mes. Fase cuatro, cutover y estabilizacion. Un mes despues del go-live el equipo nuestro queda dedicado, despues entra a soporte premium.

[speaker_1] ¿Y el equipo de implementacion es de Loggro directo o son partners?

[speaker_0] Para Enterprise siempre es equipo Loggro directo. Partners trabajamos para Pymes. Aqui no porque la complejidad del proyecto requiere consultores que tengan acceso directo a producto y desarrollo para ajustes especificos.

[speaker_1] Ok. Hablemos del costo de la implementacion entonces. Porque la licencia ya la conozco por la propuesta. ¿La implementacion va aparte?

[speaker_0] Si, va aparte. La cifra de implementacion la calculamos contra el alcance del descubrimiento. Lo que esta en la propuesta es un rango estimado para un grupo del tamano suyo. Yo le propongo que despues de esta llamada agendemos una visita tecnica con su equipo de finanzas, dos dias en sitio en Cali con un consultor nuestro, para afinar el alcance y darle una cifra firme. Esa visita no se cobra.

[speaker_1] Eso me sirve. ¿Cuando podrian estar aca?

[speaker_0] Le propongo las dos primeras semanas del mes proximo. Yo le coordino con el equipo y le mando hoy mismo dos posibilidades de agenda.

[speaker_1] Listo Andres. Hagale.

[speaker_0] Excelente Carlos. Una ultima cosa antes de cerrar. Para que la visita sea aprovechable, le voy a mandar un cuestionario corto que su equipo llena antes de la sesion: detalle de volumetria mensual, integraciones criticas con sus otros sistemas, mapa de roles. Para que cuando lleguemos no perdamos el tiempo levantando lo basico.

[speaker_1] Perfecto. Lo paso a contabilidad y operaciones esta semana.

[speaker_0] Excelente. Le mando ahora mismo el correo con todo. Que tenga buen dia Carlos.

[speaker_1] Igual Andres. Hablamos.
