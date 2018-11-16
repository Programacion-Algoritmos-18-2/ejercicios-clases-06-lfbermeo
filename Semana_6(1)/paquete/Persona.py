#Importo abc para la clase padre sea abstracta
import abc
#Super calse padre
class PersonaEquipo(metaclass=abc.ABCMeta):
	#Declaro la variable nombre 
	def __init__(self,nom):
		self.nombre= nom
	#Creó está función para obtener los nombres de cada una de las clases hijo
	def getNombre(self):
		return self.nombre		
	#Este es el método abstracto que debo tener en cada una de las sub clases
	@abc.abstractmethod
	def entrenar():
		pass
#subclase
class Entrenador(PersonaEquipo):
	#hago referencia con el super  ala calse padre y n son los atributos d ela clase padre para heredarlos
	def __init__(self,n):
		super(Entrenador,self).__init__(n)
		#Creó mi atributo solamnete de está clase
		self.codigo_entrenador = " "	 
		#Creo mi función abstracta que obligadamente debo hacerlo o si no dará un error
	def entrenar(self):
		#Imprimo en pantalla con la concatenación del nombre de cada uns de las clases
		print("Yo %s ,entrenador, soy el director del entrenamiento" % self.getNombre())	

#subclase
class Futbolista(PersonaEquipo):
	def __init__(self,n):
		super(Futbolista,self).__init__(n)
		self.posicion_campo=""	

	def entrenar(self):
		#imprimo en pantalla
		print("Yo %s, futbolista, hago prática en el entrenamiento" % self.getNombre())


#subclase
class MedicoEquipo(PersonaEquipo):
	def __init__(self,n):
		super(MedicoEquipo,self).__init__(n)
		self.titulo=""				
	#imprimo en pantalla
	def entrenar(self):
		print("Yo %s, medico, atiendo a los jugadores en el entrenamiento" % self.getNombre())	

#subclase que herada de la calse padre
class PresidenteEquipo(PersonaEquipo):
	def __init__(self,n):
		super(PresidenteEquipo,self).__init__(n)
		self.numero_propiedades=""				
	
	def entrenar(self):
		#imprimo en pantalla
		print("Yo %s, presidente, pongo dinero para el entrenamiento" % self.getNombre())								