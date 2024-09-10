from os import system
from curso import Curso
from biblioteca import Biblioteca
import datetime

class Menu():
	def __init__(self):
		self.biblioteca = Biblioteca()
	def agregar_curso(self):
		try:
			system("cls")
			print("--------------")
			print("Crear un curso")
			print("--------------")
			id = int(input("ingrese el id del curso "))
			nombre_curso = input("ingrese el nombre del curso ")
			descripcion_curso = input("ingrese una descripcion de este curso ")
			duracion_curso = int(input("ingrese la duracion del curso en horas "))
			cupos_disponibles = int(input("ingrese la cantidad de cupos disponibles para este curso "))
			curso = Curso(id, nombre_curso, descripcion_curso, duracion_curso, cupos_disponibles)
			if self.biblioteca.agregar_curso(curso):
				print("Info - Curso agregado Correctamente")
				input()
			else:
				print("Error - el curso no pudo ser agregado")
				input()
		except ValueError:
			print("Error - datos invalidos(agregar curso)")
			input()

	def listar_cursos(self):
		system("cls")
		print("Listado de Cursos")
		print("+++++++++++++++++")
		self.biblioteca.listar_cursos()

	def modificar_curso(self):
		system("cls")
		print("----------------")
		print("Modificar curso")
		print("----------------")
		id_curso = int(input("ingrese el id del curso que desea modificar "))
		if self.biblioteca.buscar_curso(id_curso) != -1:
			if self.biblioteca.modificar_curso(id_curso):
				print("Info - El curso fue modificado correctamente")
			else:
				print("Error - El curso no se pudo modificar")
		else:
			print("Error - no se encontro nigun curso con este id")

	def eliminar_curso(self):
		system("cls")
		print("--------------")
		print("Eliminar Curso")
		print("--------------")
		id_curso = int(input("ingrese el id del curso que desea eliminar "))
		if self.biblioteca.buscar_curso(id_curso) != -1:
			if self.biblioteca.eliminar_curso(id_curso):
				print("Info - Curso eliminado correctamente")
				input()
			else:
				print("Error - El curso no se pudo eliminar")
				input()
		else:
			print("Error - no se encontro ningun curso con este id")

	def mostrar_menu_principal(self):
		while True:
			system("cls")
			print("Menu")
			print("----")
			print("1. Registrar curso")
			print("2. Listar cursos")
			print("3. Modificar curso")
			print("4. Eliminar curso")
			try:
				op = int(input("ingrese una de las opciones que se muestra en el menu"))
				if op == 1:
					self.agregar_curso()
				elif op == 2:
					self.listar_cursos()
				elif op == 3:
					self.modificar_curso()
				elif op == 4:
					self.eliminar_curso()
				elif op == 0:
					break
				else:
					print("Dato Invalido en el menu")
			except ValueError:
				print("ERROR - dato invalido (opcion de menu)")
if __name__ == "__main__":
	menu = Menu()
	menu.mostrar_menu_principal()