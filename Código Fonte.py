def informacoes_paciente():
    #Usuário irá preencher seus dados que serão armazenados no banco de dados do hospital.
    
    nome = input("Digite seu nome: ")
    idade = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    peso = float(input("Digite seu peso (em kg): "))
    altura = float(input("Digite sua altura (em metros): "))
    genero_biologico = ["Masculino", "Feminino"]
    
    for i, genero in enumerate(genero_biologico, 1):
        print(f"{i}. {genero}")
    
    numero_genero_biologico = int(input("Digite o número correspondente ao seu gênero biológico: "))
    genero_selecionado = genero_biologico[numero_genero_biologico - 1]

    print("Agora, selecione como você se identifica:")
    generos_identificacao = ["Masculino", "Feminino", "Não-Binárie", "Outro"]

    for i, genero_id in enumerate(generos_identificacao, 1):
        print(f"{i}. {genero_id}")

    numero_genero_identificacao = int(input("Digite o número correspondente à sua identificação de gênero: "))
    genero_identificacao_selecionado = generos_identificacao[numero_genero_identificacao - 1]

    return {
        "Nome": nome,
        "Data de Nascimento": idade,
        "Peso": peso,
        "Altura": altura,
        "Gênero Biológico": genero_selecionado,
        "Identificação de Gênero": genero_identificacao_selecionado
        }
