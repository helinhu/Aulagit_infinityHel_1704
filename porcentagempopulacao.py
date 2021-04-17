votosBrancos = float(input("Digite o valor total de votos brancos: "))
votosNulos = float(input("Digite o valor total de votos nulos: "))
votosValidos = float(input("Digite o valor total de votos validos: "))

totalEleitores= votosBrancos+votosNulos+votosValidos

print("O numero total de Eleitores é igual a: ",totalEleitores)

porcBrancos = votosBrancos/totalEleitores*100
print("O percentual total de votos Brancos é igual a: ", porcBrancos, "%")


porcNulos = votosNulos/totalEleitores*100
print("O percentual total de votos nulos é igual a: ", porcNulos, "%")

porcValidos = votosValidos/totalEleitores*100
print("O percentual total de votos validos é igual a: ", porcValidos, "%")
