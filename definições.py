# Dicionário com as definições da máquina de estados do jogo.
# As opções dos jogadores são definidas como expressões regulares.
estados = {
    0: {
        'frases': ['Seja bem-vindo(a) ao jogo cuidado onde pisa, para poder jogar digite “iniciar”.'],
        'proximos_estados': {
            '[iI]niciar?': 1
        },
        'tempo_limite': -1
    },
    1: {
        'frases': ['Você acorda, de repente, ao nascer do sol em uma canoa em mar aberto, dentro de um saco de lixo preto com algumas regiões rasgadas, sem lembrar do que lhe ocorreu e de qual é a sua identidade. Você está sozinho, sem ao menos com a presença de um pássaro, somente ouve o som de piavas pulando do mar.\nAo se levantar, sente uma dor forte atrás da cabeça, perto da nuca. Você analisa a parte interna da embarcação e apenas encontra uma bússola, interage com ela e chega a conclusão de que sempre aponta para a mesma direção, independente da sua movimentação.\nVocê vasculha uma parte do barco coberta de uma lona e encontra um pedaço de madeira semelhante a um remo, tendo apenas ele e a bússola em mãos, por enquanto.\n\nDigite "1" para Pegar a madeira e remar em direção à ponta da bússola'],
        'proximos_estados': {
            '1|"1"': 2,
        },
        'tempo_limite': -1
    },
    2: {
        'frases': ['Você seguiu em direção ao norte por 30 minutos e escuta um nítido som, uma canção, de uma voz feminina, doce, aguda e encantadora ao leste do seu caminho.\n\nDigite "1" para Seguir o som para descobrir do que se trata ou digite "2" para Ignorar o som e seguir em frente'],
        'proximos_estados': {
            '1|"1"': 3,
            '2|"2"': 4,
        },
        'tempo_limite': -1
    },
    3: {
        'frases': ['Você rema a leste e avista, na linha do horizonte, uma ilha. E à medida que você se aproxima do lugar, o som vai aumentando, até que você chega à ilha e atraca na parte rasa, ainda do mar, sua canoa para analisar a ilha…\nA ilha, com um ar de vazio e sensação de solidão, nada tem, além de alguns coqueiros bem altos com cocos para se alimentar. Você olha para sua esquerda e se depara com um ser de corpo metade peixe e metade humano, deitada sobre uma rocha bem próxima à margem do mar e de repente ouve o som novamente com um pouco mais de altura e nota que é de lá que vem a canção…\nAo se aproximar do ser estranho, a música cessa e a sereia inicia um diálogo com você. Questiona quem é você e de onde vem, mas a sua resposta nada mais é do que incerteza e ausência de alguma lembrança. A sereia o desmente, pois pensa que você é um pescador querendo se aproveitar. Você conta a real história de que não sabe quem realmente é você e que está perdido, o que faz com que a sereia se solidarize com você…\nAo anoitecer, depois de uma longa conversa, você nada pensa, além de querer se relacionar com o ser. A sereia compreende que conseguiu te enfeitiçar e tenta lhe atrair para o fundo do mar, com a premissa de que lá há comida para lhe alimentar. Porém, com 3 segundos sem resposta da proposta da sereia, você percebe que está sendo enfeitiçado pela sereia\n\nDigite "1" para Ignorar o pedido da sereia ou digite "2" para Seguir a sereia para se livrar da fome e tentar um romance'],
        'proximos_estados': {
            '1|"1"': 4
        },
        'tempo_limite': -1
    },
    4: {
        'frases': ['A sereia se dá conta de que seu encanto não lhe afeta mais, se irrita, e pula para o mar, nadando em direção à sua canoa e fura o fundo do barco com a intenção de lhe deixar preso na ilha para sempre e morrer de fome ou até mesmo enlouquecer…\nPassam-se horas, dias, semanas e você acabou com os cocos da ilha, ficando sem mais nada para se alimentar. O calor da ilha o afeta e lhe deixa maluco, você decide, então, acabar com essa desgraça, se jogando no mar, em direção ao fundo para se afogar…\n\nVocê falhou na missão :cry:;\nDigite “reiniciar” para jogar novamente :smiley:'],
        'proximos_estados':{
            '[Rr]einiciar|"[Rr]einiciar': 1
        }
    }
}

# Dicionário com os estados correntes de cada jogador.
partidas = {}