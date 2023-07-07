def exibir_poema(data_extenso, *args, **kwargs):
    
    texto = "\n".join(args)

    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])

    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"

    print(mensagem)

exibir_poema("Livreto do Lauro", "Lauro é charmoso e estudioso.","asdasdasd", autor="Lauro", ano = 1994)
