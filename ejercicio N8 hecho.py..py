cuanto = float(input( " ¿Cuanto vas a invertir?: "))
interes = float( input( "¿ Cuanto es el interes anual? : " ))
años = int(input ( "¿Por cuantos años? : " ))
print ( " CAPITAL OBTENIDO = " + str(round(cuanto*(interes/100 + 1)**años,2)))

                
