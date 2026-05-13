# 01. Demo a contadora de pyme (DIAN, factura electronica)

**Duracion target:** 7 minutos (~1.000-1.200 palabras)

**Voces:**
- `speaker_0` (Andres, vendedor Loggro Pymes, masculino, 30s, acento paisa Medellin): voz tipo `Mateo` o `Adam`, stability 0.45
- `speaker_1` (Marcela Henao, contadora general, femenina, 40s, acento bogotano): voz tipo `Bella` o `Sarah`, stability 0.50

**Contexto:** Segunda llamada. Ya hubo discovery la semana pasada. Andres llama a Marcela, contadora general de una pyme manufacturera de 80 empleados en Bogota (productos plasticos para hogar). Demo del modulo de Facturacion Electronica DIAN integrado a Loggro Pymes.

**Tono:** profesional informativo. Andres usa "usted" todo el rato (cliente nueva). Marcela tambien lo trata de usted. Ritmo pausado, ella toma notas mientras habla.

**Directivas de voz globales:** ritmo natural conversacional, pausas de 0.3-0.5s entre turnos, sin interrupciones, sin overlapping.

---

[speaker_0] Hola Marcela, buenos dias, soy Andres de Loggro. ¿Me escucha bien? [pausa 1s]

[speaker_1] Hola Andres, si si, te escucho perfecto.

[speaker_0] Listo, muchas gracias por hacer el espacio. Como quedamos la semana pasada, hoy le quiero mostrar en vivo el modulo de facturacion electronica integrado a Loggro Pymes. La idea es que vea como se comporta con casos reales y que aprovechemos para responder lo que le quede en el tintero. ¿Le parece?

[speaker_1] Si perfecto. Mira, te cuento que yo ya he visto otras herramientas. Lo que mas me interesa es entender que pasa cuando la cosa se complica, no cuando todo sale bonito.

[speaker_0] [risa breve] Eso me gusta Marcela, vamos al grano entonces. Le voy compartiendo pantalla. ¿Ya la ve?

[speaker_1] Si, ya veo el dashboard.

[speaker_0] Bueno, esto que esta viendo es el panel de emision. Aqui salen los documentos del dia, con sus estados: emitido, aprobado por la DIAN, rechazado, pendiente de transmision. La empresa que tenemos cargada es una empresa demo del sector manufactura, similar a la suya. Lo primero que quiero que veamos es el flujo normal: yo genero una factura desde Loggro Pymes y ese documento se transmite a la DIAN automaticamente, sin que el usuario tenga que hacer nada distinto.

[speaker_1] Ok. Esa parte la entiendo. Mi pregunta es otra Andres. ¿Que pasa cuando la DIAN cambia el formato XML? Porque a mi me paso lo del cambio de resolucion en el veintitres y nos toco quedarnos dos semanas sin facturar electronicamente, mas o menos.

[speaker_0] Esa pregunta es clave y me da gusto que la haga de una vez. Mire, nosotros tenemos un equipo legal y de producto dedicado solo a normatividad DIAN. Cuando la DIAN saca una nueva resolucion o un cambio de version, ese equipo trabaja contra el cronograma de implementacion oficial. La meta interna que manejamos es tener el modulo actualizado en menos de setenta y dos horas despues de que la DIAN publique los anexos tecnicos finales.

[speaker_1] Setenta y dos horas suena bien, pero ¿como sabe el cliente cuando ya esta listo? ¿Le toca actualizar algo?

[speaker_0] No, esa es la gracia de que sea SaaS. La actualizacion se hace del lado nuestro y los clientes lo reciben sin tocar nada. Lo unico que les llega es un correo del area de servicio diciendo "actualizamos al esquema nuevo, sigan facturando normal". El cambio de la resolucion del veintitres que usted menciona, por darle un dato real, lo soportamos sin que ninguno de nuestros clientes parara facturacion.

[speaker_1] Ok, eso me gustaria validarlo con un cliente referencia. ¿Es posible?

[speaker_0] Claro que si, eso lo coordinamos esta misma semana. Le mando un par de contactos del sector manufactura para que hable directo con ellos. Sigamos. La segunda pregunta es ¿como manejan errores de transmision? Yo le mostre el flujo bonito, pero ¿que pasa cuando la DIAN se cae o cuando hay un rechazo por validacion?

[speaker_1] Exacto, eso era lo siguiente.

[speaker_0] Listo. Aqui en el dashboard, si yo filtro por estado "fallo de transmision", me salen los documentos que no pudieron llegar. El sistema tiene retry exponencial automatico: a los cinco minutos vuelve a intentar, despues a los diez, despues a los treinta, despues a los sesenta. Si pasan las cuatro horas y sigue sin pasar, escala como alerta critica al contacto tecnico que ustedes designen.

[speaker_1] ¿Y como me entero? ¿Me llega correo?

[speaker_0] Correo y notificacion en el panel, las dos cosas. Adicional, hay un endpoint de webhook por si ustedes quieren recibir las alertas en su propio sistema, pero eso es opcional, la mayoria de pymes usa el correo.

[speaker_1] Mmm ok. Y los errores de validacion, los de logica, esos que la DIAN devuelve porque uno se equivoco en una retencion o en el codigo de producto, ¿como los manejan?

[speaker_0] Buena pregunta. Ahi el sistema le marca el documento en rojo con el codigo de error exacto que devolvio la DIAN, traducido a lenguaje claro. Por ejemplo, si fue un error en el calculo de retencion en la fuente, le dice "retencion mal calculada, revise el porcentaje del proveedor". Usted corrige desde el mismo documento, vuelve a emitir y reintenta transmision con un clic. No tiene que regenerar la factura desde cero.

[speaker_1] Ok eso suena razonable. Tercera pregunta, y con esta cierro por hoy. Suponga que la DIAN si recibio el documento, todo bien. ¿Quien valida que efectivamente quedo aprobado? ¿Hay como un acuse de recibo formal o uno se queda con la duda?

[speaker_0] Si, hay acuse formal. La DIAN devuelve un CUFE que es el codigo unico de la factura electronica, y un mensaje de aceptacion. Eso queda guardado en el documento, usted lo puede consultar en cualquier momento. Tambien hay un dashboard de cumplimiento donde, mes a mes, le sale el porcentaje de documentos transmitidos exitosamente, los rechazados, los pendientes. Si necesita auditoria, descarga el reporte en Excel y listo.

[speaker_1] Ah ok, eso me sirve para entregarle al revisor fiscal.

[speaker_0] Exacto. Y para que esto cierre con cositas que en el discovery me menciono: tambien tenemos integracion bancaria con Bancolombia, Davivienda y Banco de Bogota. Eso le ayuda a conciliar los pagos de las facturas electronicas automaticamente, sin doble digitacion. Y todo el manejo de RUT, regimen comun, retencion en la fuente, ReteICA y ReteIVA, esta dentro del mismo modulo, no es un anadido.

[speaker_1] ¿Y la conciliacion bancaria es automatica automatica, o me toca subir el extracto?

[speaker_0] En Bancolombia es directa via API, usted no sube nada. En Davivienda y Banco de Bogota es por archivo plano, lo descarga del portal del banco y lo carga al sistema, el cruce lo hace el motor solo.

[speaker_1] Ok perfecto. Andres, esto me esta haciendo sentido. Yo necesito proponerlo a la gerente y a la junta. ¿Como seguimos?

[speaker_0] Le propongo lo siguiente. Le doy una prueba de siete dias con un ambiente cargado con datos suyos, los que usted quiera. No es una demo generica, son sus facturas, sus proveedores, su plan de cuentas. Asi prueba con sus casos reales y le presenta a la junta algo concreto, no una promesa. ¿Le parece si arrancamos la prueba el lunes?

[speaker_1] Si, dale, lunes me sirve. Te paso hoy mismo la data que necesites para cargarla.

[speaker_0] Perfecto Marcela. Le mando ahora un correo con la lista de archivos que necesito, los contactos de los clientes referencia del sector y el calendario para la sesion de cierre la otra semana. ¿Algo mas que necesite que cubramos hoy?

[speaker_1] No, por ahora con eso quedo bien. Gracias Andres.

[speaker_0] Con gusto Marcela. Que tenga buen dia.

[speaker_1] Igual, chao.
