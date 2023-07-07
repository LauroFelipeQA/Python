pessoa = {"Nome": "Lauro", "idade": 28}
print(pessoa)

pessoa["telefone"] = 3499999999
print(pessoa)

#dicionaios aninhados
contatos = {
    "lauro1@gmail.com": {"Nome": "Lauro1", "Telefone": 32333330},
    "Lauro2@gmail.com": {"Nome": "Lauro2", "Telefone": 32333331},
    "lauro3@gmail.com": {"Nome": "Lauro2", "Telefone": 32333332}
}

lauro = contatos["lauro1@gmail.com"]["Nome"]
print(lauro)

for nome in contatos:
    print(nome,contatos[nome])

for cha,valor in contatos.items():
    print(cha, valor)

#Metodos
#.clear() limpa o dicionario
#.copy() copia o dicionario
#dict.fromkeys(["NOme", "Tel"]) vai adicionar novas chaves vazias
#dict.fromkeys(["NOme", "Tel"], "Response") vai adicionar novas chaves com a string após a virgura
#.get pegar os dados atravez de uma chave
#.keys, mostra todas as chaves o dicionario
#.pop remove a chave passada
#.setdefault adiociona a chave passada se ela não existir, não sobreescreve
#.update({"sdasda":{"asdasd": "dasdsa"}}) ele atualiza ou criar se não existir
#.values retorna todos os valores após as chaves
#in para validar com retorno boleano de iterar e validar se uma chave esta no dicionario
#.del remove a chave ou valor da chave passado