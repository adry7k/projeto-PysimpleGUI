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
    },
    {
        "pergunta": "Qual gás é essencial para a respiração humana?",
        "alternativas": ["Dióxido de carbono", "Nitrogênio", "Oxigênio", "Hidrogênio", "Metano"],
        "resposta_correta": "Oxigênio",
        "explicacao": "O oxigênio é essencial para a respiração humana, sendo utilizado pelas células para produzir energia."
    },
    {
        "pergunta": "Qual é o principal gás responsável pelo efeito estufa?",
        "alternativas": ["Oxigênio", "Dióxido de carbono", "Metano", "Ozônio", "Nitrogênio"],
        "resposta_correta": "Dióxido de carbono",
        "explicacao": "O dióxido de carbono é o principal gás responsável pelo efeito estufa, contribuindo para o aquecimento global."
    },
    {
        "pergunta": "Qual é a unidade básica da hereditariedade?",
        "alternativas": ["Cromossomo", "Gene", "DNA", "RNA", "Proteína"],
        "resposta_correta": "Gene",
        "explicacao": "O gene é a unidade básica da hereditariedade, sendo responsável pela transmissão de características genéticas de uma geração para outra."
    },
    {
        "pergunta": "Qual é a função do sistema nervoso central?",
        "alternativas": ["Controlar a respiração", "Regular a temperatura corporal", "Coordenar os movimentos", "Processar informações", "Digestão dos alimentos"],
        "resposta_correta": "Processar informações",
        "explicacao": "O sistema nervoso central é responsável por processar informações sensoriais, coordenar movimentos e regular funções vitais do corpo."
    },
    {
        "pergunta": "Qual é a principal função do sistema circulatório?",
        "alternativas": ["Respiração", "Digestão", "Circulação de sangue", "Excreção", "Regulação da temperatura"],
        "resposta_correta": "Circulação de sangue", 
        "explicacao": "O sistema circulatório é responsável pela circulação de sangue, transportando oxigênio, nutrientes e hormônios para as células do corpo."
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
    },
    {
        "pergunta": "Qual é o país mais populoso do mundo?",
        "alternativas": ["Índia", "Estados Unidos", "Brasil", "China", "Rússia"],
        "resposta_correta": "China",
        "explicacao": "A China é o país mais populoso do mundo, com mais de 1,4 bilhão de habitantes."
    },
    {
        "pergunta": "Qual foi o evento que marcou o início da Idade Média?",
        "alternativas": ["Queda do Império Romano", "Revolução Industrial", "Descobrimento da América", "Reforma Protestante", "Independência dos EUA"],
        "resposta_correta": "Queda do Império Romano",
        "explicacao": "A queda do Império Romano do Ocidente (476 d.C.) é considerada o marco inicial da Idade Média na Europa."
    },
    {
        "pergunta": "Qual foi o principal motivo da Primeira Guerra Mundial?",
        "alternativas": ["Disputa por territórios na África", "Assassinato do arquiduque Francisco Ferdinando", "Conflitos religiosos no Oriente Médio", "Disputa ideológica entre EUA e URSS", "Disputa por recursos naturais na América Latina"],
        "resposta_correta": "Assassinato do arquiduque Francisco Ferdinando",
        "explicacao": "O assassinato do arquiduque Francisco Ferdinando, herdeiro do trono austro-húngaro, foi o estopim da Primeira Guerra Mundial."
    },
    {
        "pergunta": "Qual é o maior oceano do mundo?",
        "alternativas": ["Oceano Atlântico", "Oceano Índico", "Oceano Pacífico", "Oceano Ártico", "Oceano Antártico"],
        "resposta_correta": "Oceano Pacífico",
        "explicacao": "O Oceano Pacífico é o maior oceano do mundo, cobrindo aproximadamente um terço da superfície terrestre"
    },
    {
        "pergunta": "Qual foi o principal líder do movimento pela independência do Brasil?",
        "alternativas": ["Dom Pedro I", "José Bonifácio", "Tiradentes", "Dom Pedro II", "Leopoldina"],
        "resposta_correta": "Dom Pedro I",
        "explicacao": "Dom Pedro I foi o principal líder do movimento pela independência do Brasil, proclamando a separação de Portugal em 1822."
    }
    ]

perguntas_de_mat = [ #Perguntas de matemática
                    {
        "pergunta": "Qual é o resultado da expressão 2 + 2 * 2?",
        "alternativas": ["4", "6", "8", "10", "12"],
        "resposta_correta": "6",
        "explicacao": "A expressão 2 + 2 * 2 é resolvida seguindo a ordem das operações matemáticas, resultando em 6."
    },
    {
        "pergunta": "Qual é a raiz quadrada de 144?",
        "alternativas": ["8", "10", "12", "14", "16"],
        "resposta_correta": "12",
        "explicacao": "A raiz quadrada de 144 é 12, pois 12 * 12 = 144."
    },
    {
        "pergunta": "Qual é o resultado da expressão 3² + 4²?",
        "alternativas": ["25", "17", "9", "11", "13"],
        "resposta_correta": "25",
        "explicacao": "A expressão 3² + 4² é resolvida elevando cada número ao quadrado e somando os resultados, resultando em 25."
    },
    {
        "pergunta": "Qual é o resultado da expressão (8 - 2) ÷ 2?",
        "alternativas": ["2", "3", "4", "5", "6"],
        "resposta_correta": "3",
        "explicacao": "A expressão (8 - 2) ÷ 2 é resolvida primeiro a subtração e depois a divisão, resultando em 3."
    },
    {
        "pergunta": "Qual é o resultado de 45 - 18?",
        "alternativas": ["15", "20", "25", "30", "35"],
        "resposta_correta": "27",
        "explicacao": "A subtração de 45 - 18 resulta em 27."
    },
    {
        "pergunta": "Qual é o resultado da expressão 2⁴?",
        "alternativas": ["4", "8", "16", "32", "64"],
        "resposta_correta": "16",
        "explicacao": "A expressão 2⁴ é resolvida elevando 2 à quarta potência, resultando em 16."
    },
    {
        "pergunta": "Qual é o resultado da expressão √(25 + 9)?",
        "alternativas": ["4", "5", "6", "7", "8"],
        "resposta_correta": "4",
        "explicacao": "A expressão √(25 + 9) é resolvida primeiro a soma e depois a raiz quadrada, resultando em 4."
    },
    {
        "pergunta": "Qual é o resultado da expressão 3/4 + 1/2?",
        "alternativas": ["1/4", "1/2", "3/4", "1", "2"],
        "resposta_correta": "5/4",
        "explicacao": "A expressão 3/4 + 1/2 é resolvida somando as frações, resultando em 5/4."
    },
    {
        "pergunta": "Qual é o resultado de 100 ÷ 5?",
        "alternativas": ["15", "20", "25", "30", "35"],
        "resposta_correta": "20",
        "explicacao": "A divisão de 100 por 5 resulta em 20."
    },
    {
        "pergunta": "Qual é o resultado da expressão 10% de 200?",
        "alternativas": ["10", "20", "30", "40", "50"],
        "resposta_correta": "20",
        "explicacao": "Para calcular 10% de 200, basta multiplicar 200 por 0,10, resultando em 20."
    },
    
]


quiz_data = perguntas_de_ciencia + perguntas_de_humanas + perguntas_de_mat #Juntando todas as perguntas em uma lista

random.shuffle(quiz_data) #Embaralha as perguntas
