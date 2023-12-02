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

def sintomas():
    #Usuário irá marcar quais sintomas está sentindo para que o médico possa analizar previamente.
    
    sintomas = ["Tontura", "Náusea", "Vômitos", "Resfriado", "Indisposição", "Dores no corpo", "Febre", "Diarréia", "Dor de cabeça",
    "Gases", "Desmaio", "Tosse", "Dor ocular", "Dor de garganta"]

    print("Selecione os sintomas que está sentindo (digite os números separados por espaço):")
    for i, sintoma in enumerate(sintomas, 1):
        print(f"{i}. {sintoma}")

    numeros_sintomas = input().split()
    sintomas_selecionados = [sintomas[int(numero) - 1] for numero in numeros_sintomas]

    return sintomas_selecionados

def exibir_relatorio_paciente(info_paciente, sintomas_selecionados):
    #Parte que irá mostrar tudo que foi feito pelo usuário.
    
    print("\nRelatório do Paciente:")
    print(f"Nome: {info_paciente['Nome']}")
    print(f"Data de Nascimento: {info_paciente['Data de Nascimento']}")
    print(f"Peso: {info_paciente['Peso']} kg")
    print(f"Altura: {info_paciente['Altura']} metros")
    print(f"Gênero Biológico: {info_paciente['Gênero Biológico']}")
    print(f"Identificação de Gênero: {info_paciente['Identificação de Gênero']}")
    print("Sintomas:")
    for sintoma in sintomas_selecionados:
        print(f"- {sintoma}")
    print("Seus dados serão encaminhados para um de nossos médicos! Por favor aguarde.")
