senhas_permitidas = ["senha123", "abc456", "qwerty"]


acesso_concedido = False


while not acesso_concedido:
    senha_digitada = input("Digite a senha: ")


    for senha in senhas_permitidas:
        if senha_digitada == senha:
            acesso_concedido = True
            break

    if acesso_concedido:
        print("Acesso concedido.")
    else:
        print("Senha incorreta. Tente novamente.")


print("Está dentro! Bem-vindo!")