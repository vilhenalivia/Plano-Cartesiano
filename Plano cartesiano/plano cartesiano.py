
#Entrada do usuário
num_x = float(input("Digite o valor de X: "))
num_y = float(input("Digite o valor de Y: "))

#Condicional de verificação do valor no plano cartesiano
if num_x > 0 and num_y > 0 :
    print("\nPrimero Quadrante.\n")
elif num_x < 0 and num_y > 0:
    print("\nSegundo Quadrante.\n")
elif num_x < 0 and num_y < 0:
    print("\nTerceiro Quadrante.\n")
elif num_x > 0 and num_y < 0:
    print("\nQuarto Quadrante\n")
else:
    print("\nO ponto está localizado no eixo ou origem.\n")
