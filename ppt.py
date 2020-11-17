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
	

def juego(turno):
	jugadas = ['S', 'T', 'P']
	jugada_computadora = random.choices(jugadas) 
	jugada_computadora_imagen = ''
	jugada_usuario_imagen = ''
	jugada_usuario = ''
	if turno == 1:
		jugada_usuario = input('Introduce tu jugada: (S) para tijeras, (P) para papel o (S) para piedra: ').upper()
		if jugada_usuario == 'S':
			jugada_usuario_imagen = piedra()
			return jugada_usuario
		elif jugada_usuario == 'T':
			jugada_usuario_imagen = tijera()
			return jugada_usuario
		elif jugada_usuario == 'P':
			jugada_usuario_imagen = papel()
			return jugada_usuario
		else: 
			print('La opcion que ingresaste no existe')

	else:
		if jugada_computadora == 'S':
			jugada = piedra()
		elif jugada_computadora == 'T':
			jugada = tijera()
		else:
			jugada = papel()
	return jugada_computadora

def main():
	bienvenida()
	nombre_usuario = input('Introduce tu nombre: ').upper()
	turno_jugador = generar_turno(nombre_usuario)

	jugada = juego(turno_jugador)

	i



if __name__ == '__main__':
	main()