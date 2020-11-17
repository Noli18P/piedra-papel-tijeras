import random

"""
Piedra gana a tijera
Tijera gana a papel
Papel gana a piedra
"""
def papel():
	imagen_papel = """
	    ______
	   |      \      
	   |  \/  |
	   |  /\  |
	   |______|
	"""
	return imagen_papel


def piedra():
	imagen_piedra = """
	    ____
	   /    \ 
	   \____/
	"""
	return imagen_piedra


def tijera():
	imagen_tijera = """
	   	\  _
	 	 \/
	 	 /\_
	    	/ 
	"""
	return imagen_tijera

def bienvenida():
	mensaje = """
	Bienvenido a piedra papel o tijeras, en este juego
	jugaras contra mi humano. Preparate para jugar pero 
	primero dime tu nombre: 
	"""

	print(mensaje)

def generar_turno(nombre_usuario):
	turno = random.randint(1,2)

	if turno == 1:
		return turno
	else:
		print(f'Me toca a mi {nombre_usuario}')

	
def main():
	bienvenida()
	nombre_usuario = input('Introduce tu nombre: ').upper()
	generar_turno()


if __name__ == '__main__':
	main()