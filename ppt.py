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
	jugaras contra mi humano. 

	Para poder jugar debes introducir las siguientes letras

		- (S) Para elegir piedra
		- (T) Para elegir tijeras
		- (P) Para elegir papel

	Preparate para jugar pero primero dime tu nombre: 
	"""

	print(mensaje)

def generar_turno(nombre_usuario):
	turno = random.randint(1,2)

	if turno == 1:
		print(f'Te toca a ti {nombre_usuario}')
		return turno
	else:
		print(f'Me toca a mi {nombre_usuario}')
		return turno


def jugada_computadora():
	jugadas = ['S','P','T']
	jugada_computadora = random.choice(jugadas)

	if jugada_computadora == 'S':
		print('Elijo piedra!')
		jugada_computadora = piedra()
		print(jugada_computadora)
	elif jugada_computadora == 'P':
		print('Elijo papel!')
		jugada_computadora = papel()
		print(jugada_computadora)
	else:
		print('Eligo tiejeras!')
		jugada_computadora = tijera()
		print(jugada_computadora)


def jugada_usuario():
	jugada_usuario = input('Ingresa tu jugada (S) para pieda, (T) para tijera o (P) para papel: ').upper()

	if jugada_usuario == 'S':
		jugada_usuario = piedra()
		print(jugada_usuario)
	elif jugada_usuario == 'T':
		jugada_usuario = tijera()
		print(jugada_usuario)
	elif jugada_usuario == 'P':
		jugada_usuario = papel()
		print(jugada_usuario)
	else:
		print('La opcion ingresada no existe')
		jugada_usuario()

def main():
	bienvenida()
	nombre_usuario = input('Introduce tu nombre: ').upper()
	turno_jugador = generar_turno(nombre_usuario)

	if turno_jugador == 1:
		jugada_usuario()
	if turno_jugador == 2:
		jugada_computadora()



if __name__ == '__main__':
	main()