from curso import Curso
from os import system
class Biblioteca():
	def __init__(self):
		self.curso = Curso
		self.cursos = []
	def agregar_curso(self, curso):
		self.cursos.append(curso)
		return True
	def listar_cursos(self):
		for curso in self.cursos:
			print("")
			print("+++++++++")
			curso.mostrar_curso()
		input()
	def buscar_curso(self, id):
		for i in range(len(self.cursos)):
			if id == self.cursos[i].id_curso:
				return i
		return -1
	def modificar_curso(self, id):
		posicion_curso = self.buscar_curso(id)
		system("cls")
		print("Opciones para modificar")
		print("-----------------------")
		print("1. nombre del curso")
		print("2. descripcion del curso")
		print("3. duracion del curso")
		print("4. cupos disponibles del curso")
		try:
			opcion = int(input("ingrese una opcion del menu "))
			if opcion == 1:
				nuevo_nombre = input("ingrese el nuevo nombre para el curso")
				self.cursos[posicion_curso].nombre_curso = nuevo_nombre
				return True
			elif opcion == 2:
				nueva_descripcion = input("ingrese la nueva descripcion para el curso")
				self.cursos[posicion_curso].descripcion_curso = nueva_descripcion
				return True
			elif opcion == 3:
				nueva_duracion = int(input("Ingrese la nueva duracion en horas para el curso"))
				self.cursos[posicion_curso].duracion_curso = nueva_duracion
				return True
			elif opcion == 4:
				nuevos_cupos = int(input("Ingrese una nueva cantidad de cupos para el curso"))
				self.cursos[posicion_curso].cupos_disponibles_curso = nuevos_cupos
				return True
			else:
				return False
				
		except ValueError:
			print("Error - Datos invalidos (modificar curso)")

	def eliminar_curso(self, id):
		posicion_curso = self.buscar_curso(id)
		if posicion_curso != -1:
			del(self.cursos[posicion_curso])
			return True
		return False