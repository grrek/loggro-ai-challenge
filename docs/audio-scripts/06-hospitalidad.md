# 06. Demo Loggro Alojamientos a hotel boutique Cartagena

**Duracion target:** 6 minutos (~900-1.100 palabras)

**Voces:**
- `speaker_0` (Andres, vendedor Loggro Alojamientos, masculino, 30s, paisa Medellin): voz tipo `Mateo`, stability 0.45
- `speaker_1` (Diego Polo, gerente hotel boutique, masculino, 35s, costeno Cartagena): voz tipo `Antoni` o `Sam`, ritmo mas rapido, stability 0.40

**Contexto:** Segunda llamada. Diego gerencia un hotel boutique de 18 habitaciones en el centro historico de Cartagena, con restaurante de 40 cubiertos. Hoy usa un PMS basico que no se integra con OTAs ni con su contable. Andres demuestra Loggro Alojamientos (PMS + integracion OTAs + POS restaurante + factura electronica turistica). Diego pregunta especificamente por IVA turistico (huesped nacional vs extranjero) y soporte en temporada alta.

**Tono:** comercial alegre, cliente abierto. Diego conversador, paisa-costeno. Andres conecta facil, ritmo mas rapido. Algunas "mi llave", "primo" del lado costeno permitido.

**Directivas de voz globales:** pausas breves, ritmo mas vivo que las otras demos, energia positiva.

---

[speaker_0] Diego, ¿como esta primo? Soy Andres.

[speaker_1] Hola Andres, todo bien mi llave, ¿como esta el paisa? Aca dandole, esta semana arrancando ya con reservas para mitad de ano.

[speaker_0] Que bueno oirlo. Mira, hoy te tengo lista la demo de Loggro Alojamientos como quedamos. Te voy a mostrar el PMS, la integracion con OTAs, el POS del restaurante y la parte de facturacion electronica turistica. Quiero que veas como queda todo integrado. ¿Listo?

[speaker_1] Listo, dale.

[speaker_0] Voy compartiendo pantalla. ¿Ya la ves?

[speaker_1] Si, ya la veo.

[speaker_0] Esto es el calendario de ocupacion de un hotel demo que monte parecido al tuyo, dieciocho habitaciones boutique en zona historica. Aqui veo el grid de habitacion por noche. Esto en verde son ocupadas, amarillo en check-in pendiente, rojo bloqueadas. La gracia es que esta informacion esta sincronizada con tus canales: Booking, Expedia, Airbnb, Despegar, los tienes conectados via channel manager. Cuando un huesped reserva en Booking, la habitacion se bloquea automaticamente en los demas canales, evitando overbooking.

[speaker_1] Eso ya lo escuche en la primera llamada. Lo que me interesa hoy es lo siguiente. Yo manejo huespedes nacionales y extranjeros. Los extranjeros, segun ley de turismo, si pagan en divisas y se demuestra que vienen del exterior, estan exentos de IVA. Los nacionales pagan IVA del diecinueve. Mi pregunta es: ¿el sistema discrimina eso automatico o me toca andar cuadrandolo a mano? Porque hoy lo hago a mano y es un dolor de cabeza al cierre de mes.

[speaker_0] Excelente pregunta Diego, esa es la pregunta que separa los sistemas. Te muestro. Aqui en el modulo de check-in, cuando registras al huesped, el sistema te pide nacionalidad y el medio de pago. Si la nacionalidad es no colombiana y el pago se hace con tarjeta internacional o divisas, el sistema automaticamente aplica la exencion de IVA segun la regulacion de turismo. La factura electronica que se emite respeta esa categoria fiscal y la reporta correctamente a la DIAN.

[speaker_1] ¿Y eso me lo deja registrado para auditoria? Porque la DIAN cuando le da la gana audita esos beneficios.

[speaker_0] Si Diego, queda toda la trazabilidad: nacionalidad, pasaporte cargado, medio de pago, fecha de hospedaje. El sistema genera un reporte mensual de huespedes con exencion para que tu contadora lo tenga listo para la DIAN si lo pide. Ese reporte se descarga del modulo de cumplimiento, con un clic.

[speaker_1] Eso suena bien. Ah, y al cierre del dia o del mes, ¿como se cuadra eso contra el contable? Porque ahi es donde generalmente se desordena el asunto.

[speaker_0] Mira, ahi viene la gracia de que sea Loggro completo. El cierre diario del hotel cierra automaticamente contra el contable: ingresos por hospedaje, ingresos por restaurante, propinas, anticipos, todo separado por cuenta contable y por centro de costo. Tu contadora abre el balance de prueba y ya esta cuadrado, no hay que digitar nada manual.

[speaker_1] Ok eso me gusta. Hablemos del restaurante. Tenemos cuarenta cubiertos, el restaurante atiende tanto huespedes (con cargo a habitacion) como walk-in. ¿Como manejan eso?

[speaker_0] Aqui te muestro el POS del restaurante. Es modulo Loggro Restobar, integrado nativamente. Cuando viene un walk-in, el mesero abre cuenta nueva y se factura en el momento. Cuando es huesped, el mesero busca la habitacion y carga la cuenta al folio del huesped. El huesped al hacer check-out paga todo junto, hospedaje mas consumos del restaurante, y la factura electronica se genera unificada.

[speaker_1] ¿Y las propinas?

[speaker_0] Las propinas se manejan aparte, en un fondo de propinas que se reparte segun la regla que tu definas. El sistema soporta voluntarias y sugeridas, y las reporta separadas del ingreso del hotel.

[speaker_1] Listo, otra cosa Andres y te suelto. Yo en diciembre y en enero llego al cien por ciento de ocupacion, mas las cenas del restaurante con reserva. En esos picos he tenido problemas con sistemas que se ponen lentos. ¿Como aguanta Loggro?

[speaker_0] La arquitectura es cloud, AWS region Brasil con replica para Colombia. Soporta sin problema concurrencia mucho mayor a la tuya. Pero mas importante que la pura arquitectura: en temporada alta de turismo, octubre a febrero, nosotros activamos un equipo de soporte veinticuatro siete dedicado al sector hotelero. Para tu plan, esta incluido. Cualquier evento critico tiene respuesta en menos de quince minutos.

[speaker_1] Ah eso si me gusta. Porque uno en plena fiesta de Ano Nuevo no quiere estar peleando con un chatbot.

[speaker_0] [risa breve] Exacto Diego. Soporte humano, en castellano, con conocimiento del sector. ¿Como cerramos?

[speaker_1] Pasame propuesta y vamos a hacer lo siguiente. Yo arranco con prueba de treinta dias gratis para ver el sistema en mi operacion. Si me funciona, firmamos antes de octubre para entrar a temporada con el sistema andando, ya no en pruebas. ¿Te parece?

[speaker_0] Me parece perfecto Diego. Eso justo iba a proponerte. Si firmamos antes de octubre, alcanzamos a implementar en septiembre y arrancas temporada alta con todo cuadrado. Te mando esta misma tarde el acuerdo de prueba, el cronograma de implementacion y el contacto del especialista hotelero que te va a acompanar. ¿Algo mas?

[speaker_1] Eso es todo mi llave. Hablamos cuando reciba el correo.

[speaker_0] Excelente Diego, te cuento esta tarde. Buen dia.

[speaker_1] Igual primo, chao.
