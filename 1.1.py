# F = C × 9/5 + 32
# K = C + 273.15
# Use functions for each conversion
# Validate user input
def convert_ctof(degreeC):
    degreeF= degreeC * 9/3 +32

    return degreeF
def convert_ctok(degreeC):
    degreeK= degreeC +273.15
    
    return degreeK
def convert_ftoc(degreeF):
    degreeC =(degreeF-32)*3/9

    return degreeC
def convert_ktoc(degreeK):
    degreeC = degreeK-273.15
    
    return degreeC

while True:
    try:
        inpu= float(input("enter the degree"))
        print("choose num to convert to ")
        print ("1. Celsius to Fahrenheit \n2. Fahrenheit to Celsius \n3. Celsius to Kelvin \n4. Kelvin to Celsius")
        ch= input()
        match ch :
            case "1":
                print (convert_ctof(inpu))
                break
            case "2":
                print (convert_ftoc(inpu))
                break
            case "3":
                print (convert_ctok(inpu))
                break
            case "4":
                print (convert_ktoc(inpu))
                break
            case _:
                print ("choose valid num")
                break
    except ValueError:
        print ("enter valid degree")

        

