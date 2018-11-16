from paquete.Persona import*
#Creó los objetos para cada una de las clases hijos
futbolista = Futbolista("Antonio")
medico = MedicoEquipo("Ramon")
presidente= PresidenteEquipo("Francisco")
entrenador=Entrenador("José")
#Creó una lista que será un arreglo con cada uno de los métodos 
lista =[futbolista,medico,presidente,entrenador]
#Con ente for puedo hacer la impresión del reporte
for l in lista:
	#del arreglo llamo a la función entrenar
	l.entrenar()
