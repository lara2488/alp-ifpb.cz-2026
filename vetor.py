estojo = []
print ("olá usuario, oque deseja adicionar ao estojo?")
objeto = ""
while objeto != 0:
    objeto = int(input('deseja colocar algo no seu estojo? digite 0 para não e 1 para sim e 2 para surpresa'))
    if objeto == 1:
       item = input('digite qual objeto você quer adicionar ao seu estojo')
       estojo.append(item)
       for item in estojo:
        print(item)
    else:
        print ("olá!! aqui está os seus itens no estojo")
        for item in estojo:
            print(item)
    if objeto == 2:
                print("VOCÊ GANHOU UM VÁ TRABALHAR 😜😜😜!!!!!!!")

