import random

PERGUNTAS_HISTORIA_GERAL = {
    1: {
        "id": 1,
        "enunciado": "Qual civilização da Antiguidade desenvolveu a escrita cuneiforme em tabuinhas de argila na região da Mesopotâmia?",
        "alternativas": [
            "a) Sumérios",
            "b) Fenícios",
            "c) Hititas",
            "d) Persas"
        ],
        "resposta_correta": 1
    },
    2: {
        "id": 2,
        "enunciado": "Qual evento ocorrido em 1789 marcou o início de um processo de transformação política e social na França, com a queda da Bastilha?",
        "alternativas": [
            "a) Guerra dos Cem Anos",
            "b) Revolução Francesa",
            "c) Comuna de Paris",
            "d) Primavera dos Povos"
        ],
        "resposta_correta": 2
    },
    3: {
        "id": 3,
        "enunciado": "Qual documento inglês de 1215 limitou o poder absoluto do monarca e estabeleceu princípios fundamentais sobre direitos e leis?",
        "alternativas": [
            "a) Bill of Rights",
            "b) Tratado de Westfália",
            "c) Magna Carta",
            "d) Declaração de Independência"
        ],
        "resposta_correta": 3
    },
    4: {
        "id": 4,
        "enunciado": "Qual império pré-colombiano construiu a cidade de Machu Picchu na cordilheira dos Andes?",
        "alternativas": [
            "a) Asteca",
            "b) Maia",
            "c) Olmeca",
            "d) Inca"
        ],
        "resposta_correta": 4
    },
    5: {
        "id": 5,
        "enunciado": "Qual marco da Primeira Revolução Industrial transformou profundamente a produção têxtil e os transportes a partir da segunda metade do século XVIII?",
        "alternativas": [
            "a) A máquina a vapor",
            "b) A linha de montagem elétrica",
            "c) O transistor de silício",
            "d) A prensa tipográfica móvel"
        ],
        "resposta_correta": 1
    },
    6: {
        "id": 6,
        "enunciado": "Qual conflito global ocorreu entre 1939 e 1945 e envolveu as potências do Eixo contra os Aliados?",
        "alternativas": [
            "a) Primeira Guerra Mundial",
            "b) Segunda Guerra Mundial",
            "c) Guerra Fria",
            "d) Guerra da Criméia"
        ],
        "resposta_correta": 2
    },
    7: {
        "id": 7,
        "enunciado": "Qual período histórico, iniciado após a Segunda Guerra Mundial, foi marcado pela rivalidade geopolítica, ideológica e militar entre os Estados Unidos e a União Soviética?",
        "alternativas": [
            "a) Paz Armada",
            "b) Belle Époque",
            "c) Guerra Fria",
            "d) Era Napoleônica"
        ],
        "resposta_correta": 3
    },
    8: {
        "id": 8,
        "enunciado": "Em qual cidade da Grécia Antiga surgiu a democracia direta e floresceram expressões filosóficas e teatrais clássicas no século V a.C.?",
        "alternativas": [
            "a) Esparta",
            "b) Tebas",
            "c) Corinto",
            "d) Atenas"
        ],
        "resposta_correta": 4
    },
    9: {
        "id": 9,
        "enunciado": "Qual movimento cultural e artístico iniciado na Itália entre os séculos XIV e XVI recuperou referências da Antiguidade Clássica e valorizou o humanismo?",
        "alternativas": [
            "a) Renascimento",
            "b) Iluminismo",
            "c) Romantismo",
            "d) Barroco"
        ],
        "resposta_correta": 1
    },
    10: {
        "id": 10,
        "enunciado": "Qual muro construído em 1961 dividiu Berlim durante décadas e se tornou um dos principais símbolos da divisão europeia na Guerra Fria até sua queda em 1989?",
        "alternativas": [
            "a) Muro de Adriano",
            "b) Muro de Berlim",
            "c) Muralha da China",
            "d) Linha Maginot"
        ],
        "resposta_correta": 2
    }
}

MAPA_RESPOSTAS = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}

TOTAL_PERGUNTAS_PARTIDA = 5


def exibir_boas_vindas() -> None:
    """Exibe a mensagem inicial e as regras da partida."""
    print("=" * 60)
    print("QUIZ DE CONHECIMENTOS: CINEMA NEGRO")
    print("=" * 60)
    print("Regras da partida:")
    print(f"- Você responderá a {TOTAL_PERGUNTAS_PARTIDA} perguntas sorteadas sem repetição.")
    print("- Cada pergunta possui 4 alternativas (a, b, c ou d) e vale 1 ponto.")
    print("- Apenas uma alternativa é correta por pergunta.")
    print("- Ao final, você verá seu resumo de acertos, erros e pontuação.")
    print("=" * 60)


def sortear_perguntas(banco: dict, quantidade: int = TOTAL_PERGUNTAS_PARTIDA) -> list[dict]:
    """Sorteia perguntas únicas do dicionário de perguntas."""
    if quantidade > len(banco):
        raise ValueError("A quantidade solicitada é maior que o banco disponível.")
    return random.sample(list(banco.values()), k=quantidade)


def exibir_pergunta(pergunta: dict, numero_atual: int, total: int) -> None:
    """Exibe o enunciado e as alternativas da pergunta atual."""
    print(f"\nPergunta {numero_atual} de {total} (ID #{pergunta['id']}):")
    print(pergunta["enunciado"])
    for alternativa in pergunta["alternativas"]:
        print(f"  {alternativa}")


def obter_resposta_valida() -> int:
    """Solicita e valida a entrada do jogador, retornando o número de 1 a 4."""
    while True:
        entrada = input("Sua resposta (a, b, c ou d): ").strip().lower()
        if entrada in MAPA_RESPOSTAS:
            return MAPA_RESPOSTAS[entrada]
        print("Entrada inválida. Digite apenas 'a', 'b', 'c' ou 'd'.")


def verificar_resposta(escolha_numero: int, resposta_correta: int) -> bool:
    """Compara a escolha convertida (1-4) com o gabarito da pergunta."""
    return escolha_numero == resposta_correta


def exibir_feedback(acertou: bool, pergunta: dict) -> None:
    """Informa se a resposta está correta ou incorreta após cada tentativa."""
    if acertou:
        print("Resposta correta! +1 ponto.")
    else:
        indice_correto = pergunta["resposta_correta"] - 1
        alternativa_certa = pergunta["alternativas"][indice_correto]
        print(f"Resposta incorreta. A alternativa correta era: {alternativa_certa}")


def exibir_resultado_final(acertos: int, total_perguntas: int) -> None:
    """Exibe o resumo final da partida."""
    erros = total_perguntas - acertos
    print("\n" + "=" * 60)
    print("FIM DA PARTIDA - RESUMO FINAL")
    print("=" * 60)
    print(f"Respostas corretas:   {acertos}")
    print(f"Respostas incorretas: {erros}")
    print(f"Pontuação final:      {acertos} de {total_perguntas} pontos")
    print("=" * 60)


def jogar_partida(banco: dict, quantidade: int = TOTAL_PERGUNTAS_PARTIDA) -> None:
    """Controla o fluxo completo de uma partida do quiz."""
    exibir_boas_vindas()
    perguntas_sorteadas = sortear_perguntas(banco, quantidade)
    pontuacao = 0

    for indice, pergunta in enumerate(perguntas_sorteadas, start=1):
        exibir_pergunta(pergunta, indice, quantidade)
        escolha = obter_resposta_valida()
        acertou = verificar_resposta(escolha, pergunta["resposta_correta"])

        if acertou:
            pontuacao += 1

        exibir_feedback(acertou, pergunta)

    exibir_resultado_final(pontuacao, quantidade)


if __name__ == "__main__":
    jogar_partida(PERGUNTAS_HISTORIA_GERAL)