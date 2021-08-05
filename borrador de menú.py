import os
from calculadora import Basico, CalEstandar, CalCientifica, Calculadora, Intermedio, Cadena, TratamientoLista


class Menu:
    def __init__(self, titulo, opciones=[]):
        self.titulo = titulo
        self.opciones = opciones

    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc = input("Elija opcion[1...{}]:".format(len(self.opciones)))
        print("")
        return opc


opc = ""
while opc != "5":

    os.system("cls")
    men = Menu("Menu Principal",
               ["1). Calculadora", "2). Operación Numeros", "3). Tratamiento de Listas", "4). Operaciones de  Cadenas",
                "5). Salir"])
    opc = men.menu()

    if opc == "1":
        os.system("cls")
        opc1 = ""
        while opc1 != "10":
            os.system("cls")
            print("Calculadora")
            men1 = Menu("Menu secundario",
                        ["1)Suma ", "2)Resta", "3)Multiplicacion", "4)Division", "5)Exponente", "6)Valor Absoluto",
                         "7)Circunferencia", "8)Area Circulo", "9)Area Cuadrado", "10)Salir"])
            opc1 = men1.menu()
            os.system("cls")
            if opc1 == "1":
                print("Calculadora suma")
                print(" ")
                n1 = int(input("ingrese un numero: "))
                n2 = int(input("ingrese un numero: "))
                cal = CalEstandar(n1, n2)
                print("la suma de los 2 numero es:", cal.suma())
                input("Presionne una tecla para continuar....")



            elif opc1 == "2":
                print("Calculadora Resta")
                print(" ")

                n1 = int(input("ingrese un numero: "))
                n2 = int(input("ingrese un numero: "))
                cal = CalEstandar(n1, n2)
                print("la resta de los 2 numero es:", cal.resta())
                input("Presionne una tecla para continuar....")

            elif opc1 == "3":
                print("Calculadora Multiplicacion")
                print(" ")

                n1 = int(input("ingrese un numero: "))
                n2 = int(input("ingrese un numero: "))
                cal = CalEstandar(n1, n2)
                print("la multiplicacion de los 2 numero es:", "{}*{}={}".format(n1, n2, cal.mutiplicacion()))
                input("Presionne una tecla para continuar....")

            elif opc1 == "4":
                print("Calculadora Division")
                print(" ")
                n1 = int(input("ingrese un numero: "))
                n2 = int(input("ingrese un numero: "))
                cal = CalEstandar(n1, n2)
                print("la división de los 2 numero es:", "{}/{}={}".format(n1, n2, cal.division()))
                input("Presione una tecla para continuar....")


            elif opc1 == "5":
                print("Calculadora Exponente")
                print(" ")
                n1 = int(input("ingrese la base: "))
                n2 = float(input("ingrese el exponente: "))
                cal = CalEstandar(n1, n2)
                print("La multiplicación de potencia es :", "{}**{}={}".format(n1, n2, cal.exponente()))
                input("Presione una tecla para continuar....")


            elif opc1 == "6":
                print("Calculadora Valor Absoluto")
                print(" ")
                n1 = int(input("ingrese un numero: "))
                cal = CalEstandar(n1, 0)
                print("El valor absoluto es de: ", cal.valorAbsoluto(n1))
                input("Presione una tecla para continuar....")


            elif opc1 == "7":
                print("Calculadora Circunferencia")
                print(" ")
                n1 = int(input("ingrese el valor del radio: "))
                cal = CalCientifica(n1, 0)
                print("El perimetro de la circuferencia es: ", cal.circunferencia())
                input("Presione una tecla para continuar....")


            elif opc1 == "8":
                print("Calculadora Area Circulo")
                print(" ")
                n1 = int(input("Ingrese el radio del circulo: "))
                cal = CalCientifica(n1, 0)
                print("El area del circulo es: ", cal.areaCirculo())
                input("Presione una tecla para continuar....")

            elif opc1 == "9":
                print("Calculadora Area Cuadrado")
                print(" ")
                n2 = int(input("ingrese el valor de la radio: "))
                cal = CalCientifica(0, n2)
                print("El area del cuadrado es :", cal.areaCuadrado())
                input("Presione una tecla para continuar....")

    if opc == "2":
        os.system("cls")
        opc1 = ""
        while opc1 != "11":
            os.system("cls")
            print("OPERACIONES CON NUMEROS")
            men1 = Menu("Menu secundario",
                        ["1)Presentar los números de 1 a n ", "2)Sumar los números de 1 a n",
                         "3)Múltiplo de cualquier numero",
                         "4)Presentar los divisores de un numero", "5)Numero Primo", "6)Factorial de cualquier numero",
                         "7)Fibonacci de una serie de n números", "8)Perfecto", "9)Primos gemelos", "10)Números amigos",
                         "11)Salir"])
            opc1 = men1.menu()
            os.system("cls")
            if opc1 == "1":
                print("Presentar los números de 1 a n")
                n1 = int(input("Ingrese un número: "))
                cal = Basico()
                cal.numerosN(n1)
                input("Presione una tecla para continuar....")

            elif opc1 == "2":
                print("Sumar los números de 1 a n")
                n1 = int(input("Ingrese un número: "))
                cal = Basico()
                cal.suma(n1)
                input("Presione una tecla para continuar....")

            elif opc1 == "3":
                print("Múltiplo de cualquier numero")
                print(" ")
                n1 = int(input("Ingrese un numero: "))
                n2 = int(input("Ingrese el segundo numero: "))
                cal = Basico()
                cal.multiplo(n1, n2)
                input("Presione una tecla para continuar....")


            elif opc1 == "4":
                print("Presentar los divisores de un numero")
                print(" ")
                n1 = int(input("Ingrese un numero: "))
                cal = Basico()
                print("los divisores son: ", cal.Divisores(n1))
                input("Presione una tecla para continuar....")

            elif opc1 == "5":
                print("Numero Primo")
                print(" ")
                n1 = int(input(" ingrese un numero: "))
                cal = Basico()
                cal.primo(n1)
                input("Presione una tecla para continuar....")

            elif opc1 == "6":
                print("Factorial de cualquier numero")
                print(" ")
                n1 = int(input(" ingrese un numero: "))
                cal = Intermedio()
                print(cal.factorial(n1))
                input("Presione una tecla para continuar....")

            elif opc1 == "7":
                print("Fibonacci de una serie de n números")
                print(" ")
                n1 = int(input(" ingrese un numero: "))
                cal = Intermedio()
                print(cal.fibonacci(n1))
                input("Presione una tecla para continuar....")

            elif opc1 == "8":
                print("Perfecto")
                print(" ")
                n1 = int(input(" ingrese un numero: "))
                cal = Basico()
                cal.perfecto(n1)
                input("Presione una tecla para continuar....")

            elif opc1 == "9":
                print("Primos gemelos")
                print(" ")
                n1 = int(input(" ingrese un numero: "))
                n2 = int(input(" ingrese un segundo numero: "))
                cal = Intermedio()
                cal.primosGemelos(n1, n2)
                input("Presione una tecla para continuar....")

            elif opc1 == "10":
                print("Números amigos")
                print(" ")
                n1 = int(input(" ingrese un numero: "))
                n2 = int(input(" ingrese un segundo numero: "))
                cal = Intermedio()
                cal.numerosAmigos(n1, n2)
                input("Presione una tecla para continuar....")

            elif opc1 == "11":
                print("Salir")
 if opc == "3":
        os.system("cls")
        opc1 = ""
        while opc1 != "11":
            os.system("cls")
            print("LISTAS")
            men1 = Menu("Menu secundario",
                        ["1)Recorrer y presentar los datos de una lista",
                         "2)Buscar un valor en una lista",
                         "3)Retornar una lista con los factoriales",
                         "4)Retornar una lista de números primos",
                         "5)Recorrer una lista de diccionario con notas de alumnos",
                         "6)Insertar un dato en una Lista dada lo Posición",
                         "7)Eliminar todas las ocurrencias en una Lista",
                         "8)Retornar cualquier valor de una lista eliminándolo ",
                         "9)Copiar cada elemento de una tupla en una lista",
                         "10)Dar el vuelto a varios clientes",
                         "11)Salir"])
            opc1 = men1.menu()
            os.system("cls")
            milista = [5, 4, 7, 8, 6, 9, 7, 3, 11]
            lis = TratamientoLista(milista)

            if opc1 == "1":
                print("Recorrer y presentar los datos de una lista")
                lis.presentarLista()
                input("Presione una tecla para continuar....")

            elif opc1 == "2":
                print("Buscar un valor en una lista")
                num = int(input("Ingrese numero a buscar: "))
                lis.buscarLista(num)
                input("Presione una tecla para continuar....")

            elif opc1 == "3":
                print("Retornar una lista con los factoriales")
                lis.listaFactorial()
                input("Presione una tecla para continuar....")

            elif opc1 == "4":
                print("Retornar una lista de números primos")
                lis.listaPrimo()
                input("Presione una tecla para continuar....")

            elif opc1 == "5":
                print("Recorrer una lista de diccionario con notas de alumnos")
                notas = [{"nombre":"Juan","Nota1":10,"Nota2":7,"Nota3":8},{"nombre":"Patty","Nota1":6,"Nota2":9,"Nota3":9},{"nombre":"Daniela","Nota1":7,"Nota2":7,"Nota3":10}]
                lis.listaNotas(notas)
                input("Presione una tecla para continuar....")

            elif opc1 == "6":
                print("Insertar un dato en una Lista dada lo Posición")
                num = int(input("Ingrese valor a insertar :"))
                pos = int(input("Ingrese posición :"))
                lis.insertarLista(num, pos)
                input("Presione una tecla para continuar....")

            elif opc1 == "7":
                print("Eliminar todas las ocurrencias en una Lista")
                num = int(input("Ingrese valor a eliminar :"))
                lis.eliminarLista(num)
                input("Presione una tecla para continuar....")

            elif opc1 == "8":
                print("Retornar cualquier valor de una lista eliminándolo")
                pos = int(input("Ingrese posicion del elemento :"))
                print("Valor de la posición ",str(pos),": ",lis.retornaValorLista(pos))
                input("Presione una tecla para continuar....")

            elif opc1 == "9":
                print("Copiar cada elemento de una tupla en una lista")
                mitupla = (3, 4, 5, 6, 7, 8)
                print("tupla :",mitupla)
                lis.copiarTuplaLista(mitupla)
                input("Presione una tecla para continuar....")

            elif opc1 == "10":
                print("Dar el vuelto a varios clientes")
                clientes=[{"nombre":"Pedro","Pago":300,"Costo":185},{"nombre":"Mario","Pago":55,"Costo":42},{"nombre":"Layla","Pago":60,"Costo":53}]
                lis.vueltoLista(clientes)
                input("Presione una tecla para continuar....")

            elif opc1 == "11":
                print("Salir")
if opc == "4":
        os.system("cls")
        opc1 = ""
        while opc1 != "10":
            os.system("cls")
            print("CADENAS")
            men1 = Menu("Menu secundario",
                        ["1)Recorrer y presentar los datos de una cadena ",
                         "2)Buscar un carácter en una cadena",
                         "3)Retornar una lista con la posiciones dado un carácter de la cadena",
                         "4)Retornar una lista con todas las palabras de una cadena",
                         "5)Retornar una cadena a partir de una lista",
                         "6)Insertar un dato en una cadena dada lo Posición",
                         "7)Eliminar todas las ocurrencias en una cadena",
                         "8)Retornar cualquier valor de una cadena eliminándolo ",
                         "9)Concatenar cadenas",
                         "10)Salir"])
            opc1 = men1.menu()
            os.system("cls")
            cadena = "Hola mundo magico"
            cad = Cadena(cadena)
            if opc1 == "1":
                print("Recorrer y presentar los datos de una cadena")
                cad.recorrerCadena()
                input("Presione una tecla para continuar....")

            elif opc1 == "2":
                print("Buscar un carácter en una cadena")
                carac = input("Ingrese caracter :")
                cad.buscarCaracter(carac)
                input("Presione una tecla para continuar....")

            elif opc1 == "3":
                print("Retornar una lista con la posiciones dado un carácter de la cadena")
                carac = input("Ingrese caracter :")
                print(cad.listaPosiciones(carac))
                input("Presione una tecla para continuar....")

            elif opc1 == "4":
                print("Retornar una lista con todas las palabras de una cadena")
                print(cad.listaPalabras())
                input("Presione una tecla para continuar....")

            elif opc1 == "5":
                print("Retornar una cadena a partir de una lista")
                print(cad.cadenaLista())
                input("Presione una tecla para continuar....")

            elif opc1 == "6":
                print("Insertar un dato en una cadena dada lo Posición")
                pos = int(input("Ingrese posición a insertar :"))
                print(cad.insertarDato("papa", pos))
                input("Presione una tecla para continuar....")

            elif opc1 == "7":
                print("Eliminar todas las ocurrencias en una cadena")
                cadena2 = input("Ingrese caracter a eliminar :")
                print(cad.eliminarOcurrencias(cadena2))
                input("Presione una tecla para continuar....")

            elif opc1 == "8":
                print("Retornar cualquier valor de una cadena eliminándolo")
                pos = int(input("Ingrese posición :"))
                print(cad.retornaValor(pos))
                input("Presione una tecla para continuar....")

            elif opc1 == "9":
                print("Concatenar cadenas")
                dato = input("Ingrese dato a concatenar :")
                cad.concatenarCadena(dato)
                input("Presione una tecla para continuar....")

            elif opc1 == "10":
                print("Muchas gracias por usar el sistema, vuelva pronto")
