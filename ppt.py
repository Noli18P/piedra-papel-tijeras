import random

"""
Piedra = 1 gana a tijera = 2
Tijera gana a papel = 3
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
	jc = 0
	if jugada_computadora == 'S':
		print('Elijo piedra!')
		jugada_computadora = piedra()
		print(jugada_computadora)
		jc = 1
		return jc
	elif jugada_computadora == 'P':
		print('Elijo papel!')
		jugada_computadora = papel()
		print(jugada_computadora)
		jc = 3
		return jc
	else:
		print('Eligo tiejeras!')
		jugada_computadora = tijera()
		print(jugada_computadora)
		jc = 2
		return jc


def jugada_de_usuario():
	jugada_usuario = input('Ingresa tu jugada (S) para pieda, (T) para tijera o (P) para papel: ').upper()
	ju = 0
	if jugada_usuario == 'S':
		jugada_usuario = piedra()
		print(jugada_usuario)
		ju = 1
		return ju
	elif jugada_usuario == 'T':
		jugada_usuario = tijera()
		print(jugada_usuario)
		ju = 2
		return ju
	elif jugada_usuario == 'P':
		jugada_usuario = papel()
		print(jugada_usuario)
		ju = 3
		return ju
	else:
		print('La opcion ingresada no existe')
		jugada_de_usuario()


def comenzar_juego():
	bienvenida()
	nombre_usuario = input('Introduce tu nombre: ').upper()
	turno_jugador = generar_turno(nombre_usuario)
	ju = 0
	jc = 0 

	if turno_jugador == 1:
		ju = jugada_de_usuario()
		jc = jugada_computadora()

	if turno_jugador == 2:
		jc = jugada_computadora()
		ju = jugada_de_usuario()

	return ju,jc,nombre_usuario 


def deternimar_ganador(jugada, jugada_pc,nombre):
	if jugada == jugada_pc:
		print('! E M P A T E !')
	elif jugada == 1 and jugada_pc == 2:
		print(f'! {nombre} G A N A!')
	elif jugada == 2 and jugada_pc == 3:
		print(f'! {nombre} G A N A!')
	elif jugada == 3 and jugada_pc == 1:
		print(f'! {nombre} G A N A!')
	else:
		print('G A N A - C O M P U T A D O R')	


def main():
	ju,jc,nombre = comenzar_juego()
	deternimar_ganador(ju,jc,nombre)


if __name__ == '__main__':
	main()