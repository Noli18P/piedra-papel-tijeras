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


def main():
	imagen_tijera = tijera()
	imagen_papel = papel()
	imagen_piedra = piedra()

	print(imagen_piedra)
	print(imagen_papel)
	print(imagen_tijera)


if __name__ == '__main__':
	main()