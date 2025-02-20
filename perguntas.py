import PySimpleGUI as sg
import random

# Definindo as perguntas e respostas
perguntas_de_ciencia = [ #Perguntas de ciências
    {
        "pergunta": "Qual é o maior órgão do corpo humano?",
        "alternativas": ["Fígado", " Cérebro", "Pele", "Estômago", "Pulmão"],
        "resposta_correta": "Pele",
        "explicacao": "A pele é o maior órgão do corpo humano, cobrindo toda a superfície externa e atuando como uma barreira protetora.'."
    },
    {
        "pergunta": "Qual é o processo pelo qual as plantas produzem seu próprio alimento?",
        "alternativas": ["Respiração", "Fotossíntese", "Fermentação", "Digestão", "Transpiração"],
        "resposta_correta": "Fotossíntese",
        "explicacao": "A fotossíntese é o processo em que as plantas convertem luz solar, água e gás carbônico em glicose e oxigênio."
    },
    {
        "pergunta": "Qual é o elemento químico mais abundante no universo?",
        "alternativas": [ "Hélio", "Oxigênio", "Carbono", "Hidrogênio", "Nitrogênio"],
        "resposta_correta": "Hidrogênio",
        "explicacao": "O hidrogênio é o elemento mais abundante, constituindo cerca de 75% da massa elementar do universo."
    },
    {
        "pergunta": "Qual planeta é conhecido como o planeta vermelho?",
        "alternativas": ["Marte", "Vênus", "Júpiter", "Saturno", "Urano"],
        "resposta_correta": "Marte",
        "explicacao": "Marte é chamado de 'planeta vermelho' devido à presença de óxido de ferro em sua superfície, que lhe dá uma coloração avermelhada."
    },
    {
        "pergunta": "Qual é o maior osso do corpo humano?",
        "alternativas": ["Costela", "Fêmur", "Tíbia", "Fíbula", "Úmero"],
        "resposta_correta": "Fêmur",
        "explicacao": "O fêmur, localizado na coxa, é o maior e mais forte osso do corpo humano."
    }
]

perguntas_de_humanas = [ #Perguntas de humanas
 {
        "pergunta": "Quem foi o principal líder da Revolução Russa de 1917?",
        "alternativas": ["Vladimir Lenin", "Joseph Stalin", "Leon Trotsky", "Mikhail Gorbachev", "Nikita Khrushchev"],
        "resposta_correta": "Vladimir Lenin",
        "explicacao": "Lenin foi o líder do Partido Bolchevique e principal figura da Revolução Russa, que estabeleceu o primeiro Estado socialista."
    },
    {
        "pergunta": "Qual foi o evento que marcou o início da Idade Contemporânea?",
        "alternativas": ["Revolução Francesa", "Revolução Industrial", "Descobrimento da América", "Reforma Protestante", "Independência dos EUA"],
        "resposta_correta": "Revolução Francesa",
        "explicacao": "A Revolução Francesa (1789) é considerada o marco inicial da Idade Contemporânea, trazendo ideias de liberdade, igualdade e fraternidade.."
    },
    {
        "pergunta": "Qual foi o principal motivo da Guerra Fria?",
        "alternativas": ["Disputa por territórios na África", "Conflitos religiosos no Oriente Médio", "Disputa ideológica entre EUA e URSS", "Conflitos étnicos na Europa", "Disputa por recursos naturais na América Latina"],
        "resposta_correta": "Disputa ideológica entre EUA e URSS",
        "explicacao": "A Guerra Fria foi um conflito ideológico e político entre os EUA (capitalismo) e a União Soviética (socialismo)."
    },
    {
        "pergunta": "Quem foi o primeiro presidente do Brasil?",
        "alternativas": ["Getúlio Vargas", "Juscelino Kubitschek", "Deodoro da Fonseca", "Tancredo Neves", "José Sarney"],
        "resposta_correta": "Deodoro da Fonseca",
        "explicacao": "Deodoro da Fonseca foi o primeiro presidente do Brasil, após a proclamação da República em 1889."
    },
    {
        "pergunta": "Qual foi o principal movimento de resistência à ditadura militar no Brasil?",
        "alternativas": ["Movimento dos Caras-Pintadas", "Diretas Já", "Levante dos 18 do Forte", "Ação Libertadora Nacional", "Luta Armada"],
        "resposta_correta": "Diretas Já",
        "explicacao": "O movimento 'Diretas Já' foi uma campanha pela realização de eleições diretas para presidente do Brasil, durante a ditadura militar."
    }]

quiz_data = perguntas_de_ciencia + perguntas_de_humanas

random.shuffle(quiz_data) #Embaralha as perguntas
