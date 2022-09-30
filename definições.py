# Dicionário com as definições da máquina de estados do jogo.
# As opções dos jogadores são definidas como expressões regulares.
estados = {
    0: {
        'frases': ['Seja bem-vindo(a) ao jogo cuidado onde pisa, para poder jogar digite “iniciar”.'],
        'proximos_estados': {
            '[iI]niciar+?': 1
        },
        'tempo_limite': -1
    },
    1: {
        'frases': ['Você acorda, de repente, ao nascer do sol em uma canoa em mar aberto, dentro de um saco de lixo preto com algumas regiões rasgadas, sem lembrar do que lhe ocorreu e de qual é a sua identidade. Você está sozinho, sem ao menos com a presença de um pássaro, somente ouve o som de piavas pulando do mar.\nAo se levantar, sente uma dor forte atrás da cabeça, perto da nuca. Você analisa a parte interna da embarcação e apenas encontra uma bússola, interage com ela e chega a conclusão de que sempre aponta para a mesma direção, independente da sua movimentação.\n\nVocê vasculha uma parte do barco coberta de uma lona e encontra um pedaço de madeira semelhante a um remo, tendo apenas ele e a bússola em mãos, por enquanto.\nNesse momento, você tem apenas uma opção: **Pegar a madeira e remar em direção à ponta da bússola.**\n\n**Digite "1" para selecioná-la.**'],
        'proximos_estados': {
        '1|"1"': 2,
        },
        'tempo_limite': -1
    },
    2: {
        'frases': ['Você seguiu em direção ao norte por 30 minutos e escuta um nítido som, uma canção, de uma voz feminina, doce, aguda e encantadora ao leste do seu caminho\n\nDiante dessa situação, você tem duas escolhas para tomar: Seguir o som para descobrir do que se trata (1) ou Ignorar o som e seguir em frente (2)\n\nDigite "1" para escolher a primeira opção\nDigite "2" para escolher a segunda opção'],
        'proximos_estados': {
            '[nN][aã]+o': 3
        },
        'tempo_limite': -1
    },
    3: {
        'frases': ['Fim do jogo!', 'Parabéns!'],
        'proximos_estados': {
            '[rR]einicia(r)*': 1
        },
        'tempo_limite': -1
    }
}

# Dicionário com os estados correntes de cada jogador.
partidas = {}