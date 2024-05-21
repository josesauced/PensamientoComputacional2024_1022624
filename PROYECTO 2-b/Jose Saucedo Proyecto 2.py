


Sala=("\n")
Cocina=("\n")
Comedor=("\n")
Sanitario=("\n")
Habitación_Principal =("\n")
Habitación_Visitas=("\n")


print("Bienvenido al Controlador de temperatura")
while True:
    print("Selecciona el numero del menú al que deseas seguir\n")
    print("1. Mostrar temperaturas de las zonas\n" "2. Ajustar temperatura de una zona\n" "3. Programación de horarios\n" "4. Salir\n") 
    opcion = int(input("Seleccione una opción: "))
    if opcion == 4:
        print("Has salido del sistema. \n Gracias por utilizar rl controlador de temperatura")
        break
    match opcion:
        case 1: 
            print("Zonas")
            print("La temperatura de la Sala:" + str(Sala) + "22°C")
            print("La temperatura de la Cocina:" + str(Cocina) + "22°C")
            print("La temperatura del Comedor:" + str(Comedor) + "22°C")
            print("La temperatura del Sanitario:" + str(Sanitario) + "22°C")
            print("La temperatura de la Habitación_Principal:" + str(Habitación_Principal) + "22°C")
            print("La temperatura de la Habitación_Visitas: " + str(Habitación_Visitas) + "22°C")
            print("Presiona Enter para volver al menú y seguir con la operación o salir de ella.")
            input()
            print("\n")
        case 2:
            print("Ajusta la temperatura a como tu quieras (Sabiendo que esta en 22°C)") 
            while True:
                print("Selecciona la zona que quieres\n")
                print("1.Sala\n" "2.Cocina\n" "3.Comedor  \n" "4.Sanitario\n" "5.Habitación_Principal \n" "6.Habitación_Visitas\n") 
                
                opcion = int(input("Seleccione una opción: "))
                if opcion == 1:
                        while True:
                            print("Selecciona Aumentar o Disminuir\n")
                            print("1. Aumentar\n" "2.  Disminuir\n") 
                            opcion = int(input("Seleccione una opción: ")) 
                            
                            if opcion == 1 :  
                                print("Ingrese la temperatura que desea: entre 1°C y 18°C")
                                temperatura = int(input("La temperatura es de:"))
                                print("Sala: " + str(Sala) + str(22 + temperatura ) + "°C")
                                
                            if opcion == 2:
                                print("Ingrese la temperatura que desea: entre 1°C y 18°C")
                                temperatura = int(input("La temperatura es de:"))
                                
                                print("Sala: " + str(Sala) + str(22 - temperatura) + "°C")
                            break 
                        
                if opcion == 2:
                        while True:
                            print("Selecciona Aumentar o Disminuir\n")
                            print("1. Aumentar\n" "2.  Disminuir\n") 
                            opcion = int(input("Seleccione una opción: ")) 
                            if opcion == 1:  
                                print("Ingrese la temperatura que desea: entre 1°C y 18°C")
                                temperatura = int(input("La temperatura es de:"))
                                print("Cocina: " + str(Cocina) + str(22 + temperatura) + "°C") 
                            if opcion == 2:
                                print("Ingrese la temperatura que desea: entre 1°C y 18°C")
                                temperatura = int(input("La temperatura es de:"))
                                print("Cocina: " + str(Cocina) + str(22 - temperatura) + "°C")
                            break 
                if opcion == 3:
                        while True:
                            print("Selecciona Aumentar o Disminuir\n")
                            print("1. Aumentar\n" "2.  Disminuir\n") 
                            opcion = int(input("Seleccione una opción: ")) 
                            if opcion == 1:  
                                print("Ingrese la temperatura que desea: entre 1°C y 18°C")
                                temperatura = int(input("La temperatura es de:"))
                                print("Comedor: " + str(Comedor) + str(22 + temperatura) + "°C") 
                            if opcion == 2:
                                print("Ingrese la temperatura que desea: entre 1°C y 18°C")
                                temperatura = int(input("La temperatura es de:"))
                                print("Comedor: " + str(Comedor) + str(22 - temperatura) + "°C")
                            break
                if opcion == 4:
                    while True:
                        print("Selecciona Aumentar o Disminuir\n")
                        print("1. Aumentar\n" "2.  Disminuir\n") 
                        opcion = int(input("Seleccione una opción: ")) 
                        if opcion == 1:  
                            print("Ingrese la temperatura que desea: entre 1°C y 18°C")
                            temperatura = int(input("La temperatura es de:"))
                            print("Sanitario: " + str(Sanitario) + str(22 + temperatura) + "°C") 
                        if opcion == 2:
                            print("Ingrese la temperatura que desea: entre 1°C y 18°C")
                            temperatura = int(input("La temperatura es de:"))
                            print("Sanitario: " + str(Sanitario) + str(22 - temperatura) + "°C")
                        break
                if opcion == 5:
                    while True:
                        print("Selecciona Aumentar o Disminuir\n")
                        print("1. Aumentar\n" "2.  Disminuir\n") 
                        opcion = int(input("Seleccione una opción: ")) 
                        if opcion == 1:  
                            print("Ingrese la temperatura que desea: entre 1°C y 18°C")
                            temperatura = int(input("La temperatura es de:"))
                            print("Habitación_Principal: " + str(Habitación_Principal) + str(22 + temperatura) + "°C") 
                        if opcion == 2:
                            print("Ingrese la temperatura que desea: entre 1°C y 18°C")
                            temperatura = int(input("La temperatura es de:"))
                            print("Habitación_Principal: " + str(Habitación_Principal) + str(22 - temperatura) + "°C")
                        break 
                if opcion == 6:
                    while True:
                        print("Selecciona Aumentar o Disminuir\n")
                        print("1. Aumentar\n" "2.  Disminuir\n") 
                        opcion = int(input("Seleccione una opción: ")) 
                        if opcion == 1:  
                            print("Ingrese la temperatura que desea: entre 1°C y 18°C")
                            temperatura = int(input("La temperatura es de:"))
                            print("Habitación_Visitas: " + str(Habitación_Visitas) + str(22 + temperatura) + "°C") 
                        if opcion == 2:
                            print("Ingrese la temperatura que desea: entre 1°C y 18°C")
                            temperatura = int(input("La temperatura es de:"))
                            print("Habitación_Visitas: " + str(Habitación_Visitas) + str(22 - temperatura) + "°C")
                        break 
                break 
            print("Presiona Enter para volver al menú y seguir con la operación")
            input()
            print("\n")
   
        case 3:   
            print("Programación de horarios")
            print("1.Sala\n" "2.Cocina\n" "3.Comedor\n" "4.Sanitario\n" "5.Habitación_Principal \n" "6.Habitación_Visitas\n") 
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                print("Sala: " "1. Mañana\n" "2. Tarde\n" "3. Noche\n")
                opcion = int(input("Seleccione una opción: "))
                if opcion == 1:
                    time: str = input("Ingrese la hora que desea: ")
                    print("Sala: " + str(Sala) + str(time) + "A.M") 
                    Temperatura =int(input("Ingrese la temperatura que desea entre 4°C a 40°C : ")) 
                    print("Sala: " + str(Sala) + str(Temperatura) + "°C")   
                if opcion == 2:
                    time: str = input("Ingrese la hora que desea: ")
                    print("Sala: " + str(Sala) + str(time) + "P.M")
                    Temperatura =int(input("Ingrese la temperatura que desea entre 4°C a 40°C : ")) 
                    print("Sala: " + str(Sala) + str(Temperatura) + "°C")
                if opcion == 3:
                    time: str = input("Ingrese la hora que desea: ")
                    print("Sala: " + str(Sala) + str(time) + "P.M")
                    Temperatura =int(input("Ingrese la temperatura que desea entre 4°C a 40°C : ")) 
                    print("Sala: " + str(Sala) + str(Temperatura) + "°C")
            if opcion == 2:
                print("Cocina: " "1. Mañana\n" "2. Tarde\n" "3. Noche\n")
                opcion = int(input("Seleccione una opción: "))
                if opcion == 1:
                    time: str = input("Ingrese la hora que desea: ")
                    print("Cocina: " + str(Cocina) + str(time) + "A.M")
                    Temperatura =int(input("Ingrese la temperatura que desea entre 4°C a 40°C : ")) 
                    print("Cocina: " + str(Cocina) + str(Temperatura) + "°C")
                if opcion == 2:
                    time: str = input("Ingrese la hora que desea: ")
                    print("Cocina: " + str(Cocina) + str(time) + "P.M")
                    Temperatura =int(input("Ingrese la temperatura que desea entre 4°C a 40°C : ")) 
                    print("Cocina: " + str(Cocina) + str(Temperatura) + "°C")
                if opcion == 3:
                    time: str = input("Ingrese la hora que desea: ")
                    print("Cocina: " + str(Cocina) + str(time) + "P.M")
                    Temperatura =int(input("Ingrese la temperatura que desea entre 4°C a 40°C : ")) 
                    print("Cocina: " + str(Cocina) + str(Temperatura) + "°C")
            if opcion == 3:
                print("Comedor: " "1. Mañana\n" "2. Tarde\n" "3. Noche\n")
                opcion = int(input("Seleccione una opción: "))
                if opcion == 1:
                    time: str = input("Ingrese la hora que desea: ")
                    print("Comedor: " + str(Comedor) + str(time) + "A.M")
                    Temperatura =int(input("Ingrese la temperatura que desea entre 4°C a 40°C : ")) 
                    print("Comedor: " + str(Comedor) + str(Temperatura) + "°C")
                if opcion == 2:
                    time: str = input("Ingrese la hora que desea: ")
                    print("Comedor: " + str(Comedor) + str(time) + "P.M")
                    Temperatura =int(input("Ingrese la temperatura que desea entre 4°C a 40°C : ")) 
                    print("Comedor: " + str(Comedor) + str(Temperatura) + "°C")
                if opcion == 3:
                    time: str = input("Ingrese la hora que desea: ")
                    print("Comedor: " + str(Comedor) + str(time) + "P.M")
                    Temperatura =int(input("Ingrese la temperatura que desea entre 4°C a 40°C : ")) 
                    print("Comedor: " + str(Comedor) + str(Temperatura) + "°C")
            if opcion == 4:
                print("Sanitario: " "1. Mañana\n" "2. Tarde\n" "3. Noche\n")
                opcion = int(input("Seleccione una opción: "))
                if opcion == 1:
                    time: str = input("Ingrese la hora que desea: ")
                    print("Sanitario: " + str(Sanitario) + str(time) + "A.M")
                    Temperatura =int(input("Ingrese la temperatura que desea entre 4°C a 40°C : ")) 
                    print("Sanitario: " + str(Sanitario) + str(Temperatura) + "°C")
                if opcion == 2:
                    time: str = input("Ingrese la hora que desea: ")
                    print("Sanitario: " + str(Sanitario) + str(time) + "P.M")
                    Temperatura =int(input("Ingrese la temperatura que desea entre 4°C a 40°C : ")) 
                    print("Sanitario: " + str(Sanitario) + str(Temperatura) + "°C") 
                if opcion == 3:
                    time: str = input("Ingrese la hora que desea: ")
                    print("Sanitario: " + str(Sanitario) + str(time) + "P.M")
                    Temperatura =int(input("Ingrese la temperatura que desea entre 4°C a 40°C : ")) 
                    print("Sanitario: " + str(Sanitario) + str(Temperatura) + "°C")
            if opcion == 5:
                print("Habitación_Principal " "1. Mañana\n" "2. Tarde\n" "3. Noche\n")
                opcion = int(input("Seleccione una opción: "))
                if opcion == 1:
                    time: str = input("Ingrese la hora que desea: ")
                    print("Habitación_Principal: " + str(Habitación_Principal) + str(time) + "A.M")
                    Temperatura =int(input("Ingrese la temperatura que desea entre 4°C a 40°C : ")) 
                    print("Habitación_Principal: " + str(Habitación_Principal) + str(Temperatura) + "°C")
                if opcion == 2:
                    time: str = input("Ingrese la hora que desea: ")
                    print("Habitación_Principal: " + str(Habitación_Principal) + str(time) + "P.M")
                    Temperatura =int(input("Ingrese la temperatura que desea entre 4°C a 40°C : ")) 
                    print("Habitación_Principal: " + str(Habitación_Principal) + str(Temperatura) + "°C")
                if opcion == 3:
                    time: str = input("Ingrese la hora que desea: ")
                    print("Habitación_Principal: " + str(Habitación_Principal) + str(time) + "P.M")
                    Temperatura =int(input("Ingrese la temperatura que desea entre 4°C a 40°C : ")) 
                    print("Habitación_Principal: " + str(Habitación_Principal) + str(Temperatura) + "°C")
            if opcion == 6:
                print("Habitación_Visitas: " "1. Mañana\n" "2. Tarde\n" "3. Noche\n")
                opcion = int(input("Seleccione una opción: "))
                if opcion == 1:
                    time: str = input("Ingrese la hora que desea: ")
                    print("Habitación_Visitas: " + str(Habitación_Visitas) + str(time) + "A.M")
                    Temperatura =int(input("Ingrese la temperatura que desea entre 4°C a 40°C : ")) 
                    print("Habitación_Visitas: " + str(Habitación_Visitas) + str(Temperatura) + "°C")
                if opcion == 2:
                    time: str = input("Ingrese la hora que desea: ")
                    print("Habitación_Visitas: " + str(Habitación_Visitas) + str(time) + "P.M")
                    Temperatura =int(input("Ingrese la temperatura que desea entre 4°C a 40°C : ")) 
                    print("Habitación_Visitas: " + str(Habitación_Visitas) + str(Temperatura) + "°C")
                if opcion == 3:
                    time: str = input("Ingrese la hora que desea: ")
                    print("Habitación_Visitas: " + str(Habitación_Visitas) + str(time) + "P.M")
                    Temperatura =int(input("Ingrese la temperatura que desea entre 4°C a 40°C : ")) 
                    print("Habitación_Visitas: " + str(Habitación_Visitas) + str(Temperatura) + "°C")

            print("Presiona Enter para volver al menú y seguir con la operación")
            input()    
            print("\n")
            
                    
            


                
                
            