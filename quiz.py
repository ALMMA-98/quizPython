import random

PERGUNTAS = {
    1: {
        "id": 1,
        "enunciado": "Qual filme de 1984, dirigido por Adélia Sampaio, é considerado o primeiro longa-metragem dirigido por uma mulher negra no Brasil?",
        "alternativas": [
            "a) Amor Maldito",
            "b) Um Dia com Jerusa",
            "c) Abolição",
            "d) Café com Canela"
        ],
        "resposta_correta": 1
    },
    2: {
        "id": 2,
        "enunciado": "Qual curta-metragem de 1973, escrito, dirigido e interpretado por Zózimo Bulbul, é amplamente apontado como um marco fundador do cinema negro brasileiro?",
        "alternativas": [
            "a) O Caso do Homem Errado",
            "b) Alma no Olho",
            "c) Rainha",
            "d) Marte Um"
        ],
        "resposta_correta": 2
    },
    3: {
        "id": 3,
        "enunciado": "Qual documentário de Zózimo Bulbul, lançado em 1988, marca o centenário da abolição da escravidão no Brasil reunindo reflexões históricas, sociais e culturais?",
        "alternativas": [
            "a) A Negação do Brasil",
            "b) Chico Rei Entre Nós",
            "c) Abolição",
            "d) Branco Sai, Preto Fica"
        ],
        "resposta_correta": 3
    },
    4: {
        "id": 4,
        "enunciado": "Qual documentário dirigido por Joel Zito de Araújo analisa a trajetória e a representação de atores e personagens negros nas telenovelas brasileiras?",
        "alternativas": [
            "a) Meu Amigo Fela",
            "b) Temporada",
            "c) Nó do Diabo",
            "d) A Negação do Brasil"
        ],
        "resposta_correta": 4
    },
    5: {
        "id": 5,
        "enunciado": "Em qual ano foi criada a Mostra Competitiva de Cinema Negro Adélia Sampaio, idealizada pela cineasta e pesquisadora Edileuza Penha de Souza?",
        "alternativas": [
            "a) 2016",
            "b) 1998",
            "c) 2005",
            "d) 2022"
        ],
        "resposta_correta": 1
    },
    6: {
        "id": 6,
        "enunciado": "Quem assina a direção do longa-metragem 'Um Dia com Jerusa' (2019), drama que acompanha o encontro entre uma senhora moradora do Bixiga e uma jovem pesquisadora?",
        "alternativas": [
            "a) Sabrina Fidalgo",
            "b) Viviane Ferreira",
            "c) Camila de Moraes",
            "d) Renata Martins"
        ],
        "resposta_correta": 2
    },
    7: {
        "id": 7,
        "enunciado": "Qual filme dirigido por Gabriel Martins acompanha o cotidiano de uma família negra em Contagem (MG) e aborda sonhos, afetos e desafios econômicos?",
        "alternativas": [
            "a) Sem Asas",
            "b) Alma no Olho",
            "c) Marte Um",
            "d) Amor Maldito"
        ],
        "resposta_correta": 3
    },
    8: {
        "id": 8,
        "enunciado": "Qual curta-metragem de Sabrina Fidalgo acompanha a trajetória de Rita para se tornar rainha de bateria e discute padrões estéticos e elitização do carnaval?",
        "alternativas": [
            "a) Abolição",
            "b) Um Dia com Jerusa",
            "c) Marte Um",
            "d) Rainha"
        ],
        "resposta_correta": 4
    },
    9: {
        "id": 9,
        "enunciado": "Qual documentário dirigido por Camila de Moraes resgata a história de Júlio César e estabelece paralelos com o racismo estrutural e a violência policial?",
        "alternativas": [
            "a) O Caso do Homem Errado",
            "b) Meu Amigo Fela",
            "c) Temporada",
            "d) Chico Rei Entre Nós"
        ],
        "resposta_correta": 1
    },
    10: {
        "id": 10,
        "enunciado": "Qual filme de 2019 dirigido por Renata Martins acompanha Zu, um menino de 12 anos que descobre que pode voar no caminho de volta da mercearia?",
        "alternativas": [
            "a) Nó do Diabo",
            "b) Sem Asas",
            "c) A Negação do Brasil",
            "d) Rainha"
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
    jogar_partida(PERGUNTAS)