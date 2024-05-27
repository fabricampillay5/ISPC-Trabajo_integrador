Algoritmo CreandoMenu
	//Declarar variable donde se guardara la opcion del menu elegido 
	Definir opc Como Caracter
	
	Repetir
		Limpiar Pantalla
		// Mostrar el menu por pantalla
		Escribir "Sistema de Gestion de Stock AI"
		Escribir "MENU"
	    Escribir"****************"
	    Escribir "(1) Ingreso de Productos"
	    Escribir "(2) Egreso de Productos"
	    Escribir "(3) Cierre Mensual de Stock"
	    Escribir "(0) Salir"
	    Escribir "Elige una opcion (0-3)....." Sin Saltar
	    Leer opc
	
	    Segun opc Hacer
		
		'1':
			Limpiar Pantalla
			Escribir ""
			Escribir "Ingreso"
			Escribir "Pulsa una tecla para continuar...."
			Esperar Tecla
		'2':
			Limpiar Pantalla
			Escribir ""
			Escribir "Salida"
			Escribir "Pulsa una tecla para continuar...."
			Esperar Tecla
		'3': 
			Limpiar Pantalla
			Escribir ""
			Escribir "Cierre Mensual"
			Escribir "Pulsa una tecla para continuar...."
			Esperar Tecla
		'0':
			Escribir ""
			Escribir "Gracias por Utilizar AI"
		De Otro Modo:
			Limpiar Pantalla
			Escribir opc, " no es una opcion correcta. Intentalo de nuevo"
			Esperar Tecla
		FinSegun
	Hasta Que (opc == '0')
			
			
FinAlgoritmo
