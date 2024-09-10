class Curso():
	def __init__(self, id, nombre, descripcion, duracion, cupos):
		self.id_curso = id
		self.nombre_curso = nombre
		self.descripcion_curso = descripcion
		self.duracion_curso = duracion
		self.cupos_disponibles_curso = cupos
	def mostrar_curso(self):
		print("ID",self.id_curso)
		print("Nombre del curso",self.nombre_curso)
		print("Descripcion del curso",self.descripcion_curso)
		print("Duracion del curso",self.duracion_curso)
		print("Cupos diponibles",self.cupos_disponibles_curso)