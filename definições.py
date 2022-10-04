frases = {
    'inventario_insuficiente': 'Sem os recursos necessários para avançar.',
    'erro': 'I\'m sorry Dave, I\'m afraid I can\'t do that.'
}

# Dicionário com as definições da máquina de estados do jogo.
# As opções dos jogadores são definidas como expressões regulares.
estados = {
    0: {
        'frases': ['Seja bem-vindo(a) ao jogo cuidado onde pisa, para poder jogar digite “iniciar”.'],
        'proximos_estados': {
            '[iI]niciar+?': 1
        },
        'inventario': set()
    },
    1: {
        'frases': ['Você acorda, de repente, ao nascer do sol em uma canoa em mar aberto, dentro de um saco de lixo preto com algumas regiões rasgadas, sem lembrar do que lhe ocorreu e de qual é a sua identidade. Você está sozinho, sem ao menos com a presença de um pássaro, somente ouve o som de piavas pulando do mar.\nAo se levantar, sente uma dor forte atrás da cabeça, perto da nuca. Você analisa a parte interna da embarcação e apenas encontra uma bússola, interage com ela e chega a conclusão de que sempre aponta para a mesma direção, independente da sua movimentação.\n\nVocê vasculha uma parte do barco coberta de uma lona e encontra um pedaço de madeira semelhante a um remo, tendo apenas ele e a bússola em mãos, por enquanto.\nNesse momento, você tem apenas uma opção: **Pegar a madeira e remar em direção à ponta da bússola.**\n\n**Digite "1" para selecioná-la.**'],
        'proximos_estados': {
        '1|"1"': 2,
        },
        'inventario':set()
    },
    2: {
        'frases': ['Você seguiu em direção ao norte por 30 minutos e escuta um nítido som, uma canção, de uma voz feminina, doce, aguda e encantadora ao leste do seu caminho\n\nDiante dessa situação, você tem duas escolhas para tomar: Seguir o som para descobrir do que se trata (1) ou Ignorar o som e seguir em frente (2)\n\nDigite "1" para escolher a primeira opção\nDigite "2" para escolher a segunda opção'],
        'proximos_estados': {
            '1|"1"': 3,
            '2|"2"': 6,
        },
        'inventario':set()
    },
    3: {
        'frases': ['Você rema a leste e avista, na linha do horizonte, uma ilha. E à medida que você se aproxima do lugar, o som vai aumentando, até que você chega à ilha e atraca na parte rasa, ainda do mar, sua canoa para analisar a ilha…\nA ilha, com um ar de vazio e sensação de solidão, nada tem, além de alguns coqueiros bem altos com cocos para se alimentar. Você olha para sua esquerda e se depara com um ser de corpo metade peixe e metade humano, deitada sobre uma rocha bem próxima à margem do mar e de repente ouve o som novamente com um pouco mais de altura e nota que é de lá que vem a canção…\nAo se aproximar do ser estranho, a música cessa e a sereia inicia um diálogo com você. Questiona quem é você e de onde vem, mas a sua resposta nada mais é do que incerteza e ausência de alguma lembrança. A sereia o desmente, pois pensa que você é um pescador querendo se aproveitar. Você conta a real história de que não sabe quem realmente é você e que está perdido, o que faz com que a sereia se solidarize com você…\nAo anoitecer, depois de uma longa conversa, você nada pensa, além de querer se relacionar com o ser. A sereia compreende que conseguiu te enfeitiçar e tenta lhe atrair para o fundo do mar, com a premissa de que lá há comida para lhe alimentar. Porém, com 3 segundos sem resposta da proposta da sereia, você percebe que está sendo enfeitiçado pela sereia\n\nDigite "1" para Ignorar o pedido da sereia ou digite "2" para Seguir a sereia para se livrar da fome e tentar um romance'],
        'proximos_estados': {
            '1|"1"': 4,
            '2|"2"': 5,
        },
        'inventario':set()
    },
    4: {
        'frases': ['A sereia se dá conta de que seu encanto não lhe afeta mais, se irrita, e pula para o mar, nadando em direção à sua canoa e fura o fundo do barco com a intenção de lhe deixar preso na ilha para sempre e morrer de fome ou até mesmo enlouquecer…\nPassam-se horas, dias, semanas e você acabou com os cocos da ilha, ficando sem mais nada para se alimentar. O calor da ilha o afeta e lhe deixa maluco, você decide, então, acabar com essa desgraça, se jogando no mar, em direção ao fundo para se afogar…\n\nVocê falhou na missão :cry:;\nDigite “reiniciar” para jogar novamente :smiley:'],
        'proximos_estados':{
            '[Rr]einiciar|"[Rr]einiciar': 1
        },
        'inventario':set()
    },
    5: {
        'frases': ['Você ignora o encanto da sereia, pois sente uma extrema paixão por ela, além de querer comer algo…\nA sereia inicia, com sua voz doce e hipnotizante, uma canção muito boa de se ouvir e você a segue em direção ao oceano…\nDe repente, a sereia pausa a música e o agarra, levando-o embora, em direção ao fundo do mar e você se afoga e fica preso lá, dentro de uma espécie de reino subaquático e vira comida de tubarão…\n\nDigite “reiniciar” para jogar novamente :smiley:'],
        'proximos_estados':{
            '[Rr]einiciar|"[Rr]einiciar"': 1
        },
        'inventario':set()
    },
    6: {
        'frases': ['Você analisa e vê que não é normal alguém estar cantando no meio de um mar aberto e decide não dar ouvidos à canção e opta por continuar o seu rumo…\nQuando alcançou a metade do dia, com o Sol no centro do céu, sente fome e vasculha a canoa, mais especificamente a lona em que encontrou o pedaço de madeira. Você encontra uma longa vara com uma pedra afiada na ponta do objeto e uma âncora de ferro.\n\n*Digite "1" para Pular ao mar para caçar um peixe;\nDigite "2" para Você pensa que ainda é cedo para se alimentar e decide continuar remando com a esperança de encontrar ajuda.'],
        'proximos_estados':{
            '1|"1"': 7,
            '2|"2"': 12,
        },
        'inventario':set()
    },
    7: {
        'frases': ['Você aguarda dentro do barco na expectativa de avistar um cardume para tentar atacar e conseguir vários de uma vez…\nPassados 22 minutos, as ondas começaram a surgir e várias tilápias pequenas e piavas começaram a pular. Você coloca a âncora abaixo ao mar para prender o barco e espera alguns peixes chegarem perto da sua canoa para ter mais facilidade. E isto  aconteceu, você pula sobre a lateral do barco e cai de barriga sobre a água e utiliza sua espécie de lança para pegar os animais marinhos. Conforme pega os peixes, os joga para dentro do barco…\nAté que avista uma barbatana azul nadando em torno do barco e vai se aproximando conforme você fica parado.\n\nDigite "1" para Tentar combater o animal que está o rodeando para tentar um banquete maior ou "2" para Voltar ao barco imediatamente'],
        'proximos_estados':{
            '1|"1"': 8,
            '2|"2"': 9,
        },
        'inventario':set()
    },
    8: {
        'frases': ['Você foi estúpido demais para achar que teria alguma chance contra o tubarão e acaba sendo comido por ele.\n\nVocê falhou na missão :cry:;\nDigite “reiniciar” para jogar novamente :smiley:'],
        'proximos_estados':{
            '[Rr]einiciar|"[Rr]einiciar"': 1
        },
        'inventario':set()
    },
    9: {
        'frases': ['Você nada rapidamente para a sua canoa, puxa sua âncora de volta para o barco e se livra do tubarão…\nFicou parado por um tempo, sem remar, apenas comendo os peixes crus, comeu 3 e guardou 4 debaixo da lona…\nCom o sol quase se pondo, você pegou a lona e a utilizou como cobertor para se proteger do frio que estava chegando. Anoiteceu e você não enxergou nada, a não ser as estrelas e a lua no céu. Com a brisa do mar e o som calmo das ondas, caiu em um sono profundo, mas sem sonhos…\nVocê acorda com os gritos dos pelicanos que voam próximo a você por sentirem o mau cheiro dos peixes mortos que estavam dentro da sua canoa.\n\nDigite "1" para Jogar os peixes para água, para que as aves possam se alimentar, assim, evitando com elas cheguem mais perto de você para tentar lhe atacar ou "2" para Você se acha o Pescador e provoca os pelicanos comendo os peixes crus na frente deles'],
        'proximos_estados':{
            '1|"1"': 10,
            '2|"2"': 11,
        },
        'inventario':set()
    },
    10: {
        'frases': ['Você devolve os peixes para o mar e, já que eles boiam por estar mortos, os pelicanos conseguiram se alimentar. Você, muito esperto, manteve uma piava dentro da lona para come-la, posteriormente.\nCom medo de que os pássaros descubram a sua piava, você rema em direção contrária aos pelicanos. Passados 10 minutos de remada, a fome começa a lhe afetar e você não pode deixar para comer depois. Por isso, você pega sua lança e faz fatias dessa piava para tentar evitar as espinhas. Após saborear uma terrível carne crua de peixe podre com lodo, o mar começa a rodopiar e você cai de costas à lona por conta de sentir enorme enjoo. Seu estômago começa a vibrar e suas mãos sujas de lodo a tremer. Você se levanta um pouco e sente um desconforto abdominal intenso. Porém a tontura piora e você, não conseguindo enxergar com o Sol apontando para seus olhos, tropeça em uma madeira solta na lateral do barco e cai novamente, dessa vez, batendo a cabeça direto no chão do barco, tendo a cabeça aberta, além de uma morte um pouco desconfortante, porém rápida.\n\nVocê falhou na missão :cry:;\nDigite “reiniciar” para jogar novamente :smiley:'],
        'proximos_estados':{
            '[Rr]einiciar|"[Rr]einiciar"': 1
        },
        'inventario':set()
    },
    11: {
        'frases': ['Os pelicanos se sentiram intimidados por verem você com os peixes e voam em sua direção. Com um exército de pássaros sobrevoando seu barco, você corre para debaixo da sua lona, no entanto, os pelicanos furam a sua cobertura, fazendo você ficar a vista e é bicado pelo arsenal.\nPara tentar fugir, você se atira em direção ao mar, mas se esquece que no dia anterior estava fugindo de um tubarão. Os pelicanos demoram a se retirar da sua canoa, com 21 minutos observando as aves, você avista uma outra barbatana a 30 metros de distância, porém uma barbatana maior e cinza. O animal vai se aproximando com uma velocidade constante e morde a sua perna. Em 2 segundos, você estava dentro de um círculo de um líquido vermelho. A água salgada começa a causar um ardor no ferimento e você perde o controle do nado e começa a afundar, acabando se afogando, tendo uma morte lenta e torturante.\n\nVocê falhou na missão :cry:;\nDigite “reiniciar” para jogar novamente :smiley:'],
        'proximos_estados':{
            '[Rr]einiciar|"[Rr]einiciar"': 1
        },
        'inventario':set()
    },
    12: {
        'frases': ['A fome não tem vitória sobre você. Você não mexe na vara com uma pedra na ponta, muito menos na âncora de ferro e continua a remar sob um céu azul com um Sol no centro…\nDe repente, com o Sol se direcionando ao Oeste, algo surge no horizonte, em que coincidentemente, fica em direção aonde a bússola aponta. Você, cansado de estar nesse mar que parece ser infinito, rema como um louco para verificar o local, até, talvez encontrar ajuda sem medo de falhar, pois sente uma espécie de chama verde acender no seu interior, a esperança…\nA sensação é que você parece não conseguir alcançar essa linha, mas sem pensar em desistir, você acelera o ritmo e rema mais depressa, tendo o barco mais rápido que o normal, superando o vento gelado soprando contra você…|Quase lá, com os ombros pesados, as mãos machucadas, todas picadas por causa das farpas da madeira utilizada como remo, você enxerga uma superfície amarelada, com alguns pontos no mar. Árvores cheias de vida, com folhas verdes, são incluídas na imagem da linha do horizonte, e você percebe que é dali que está vindo toda a ventania…\nFinalmente, você se dá conta do local: uma praia, com muitas pessoas se banhando no mar, crianças e adolescentes, brincando na areia, correndo e construindo castelos de areia, com os vendedores de picolé ambulantes carregando um carrinho sinalizando os deliciosos gelados para a criançada. Os salva-vidas sentados em suas torres de vigias.\nAo se aproximar da areia, aumentam os olhos que miram você. Alguns se assustam com a embarcação chegando mais perto, pois surgiu do nada. Seus berros de pedidos de ajuda não alcançam os ouvidos das pessoas, pois o vento soprando em direção oposta a você faz sua voz se propagar na contra-mão. Por isso, você começa a gesticular com os braços, juntos, para a direita e para esquerda com a ideia de chamar a atenção dos socorristas, que depois de 26 segundos de gestos, percebem que isto se tratava de um pedido de socorro e correm em direção a você para lhe ajudar, chegam à beira da água e aguardam o seu barco atracar, pois sua canoa estava em uma distância consideravelmente difícil de ser enxergada…|Depois de 10 minutos explicando para os salva-vidas o que lhe aconteceu e que não se lembra de nada, nem de quem é, você descobre o país em que veio parar: Ilha da Madeira, Portugal.\nOs salva vidas oferecem ajuda a você, a fim de levar você a um hospital para se tratar.\n\nDigite "1" para Aceitar o convite, pois lá você poderia descansar, ser alimentado para depois continuar sua jornada ou "2" para Recusa a ideia e continua o seu caminho sozinho, pois pensa que não é uma boa ideia ir para um local como este.'],
        'promixos_estados':{
            '1|"1"': 13,
            '2|"2"': 16
        },
        'inventario':set()
    },
    13: {
        'frases': ['Ao aceitar a ajuda dos socorristas, os mesmos chamam uma ambulância para lhe levar a um hospital para tratar você. 8 minutos de espera passados, você percebe um carro com o capô quadrado seguido de um parabrisa retangular de vidro um pouco embaçado, a lataria de cores vermelho e branco com luzes também vermelhas bem chamativas piscando longe da sua direção. A van dos médicos tinha pneus extremamente espessos, com as rodas cinzentas com algumas regiões enferrujadas. A lateral das portas possui adesivos de cruzes vermelhas e a porta de trás tinha um vidro com uma película um pouco escura.\nOs salva vidas o conduzem à ambulância e lhe deixam dentro dela sentado sobre uma maca bem macia com uma capa branca que cobre um colchão. Após 14 minutos de trânsito, a ambulância finalmente estaciona no hospital, em que se encontrava no centro de um parque com um grande lago com patos nadando e comendo pedaços de pães jogados por pedestres nas redondezas.\nVocê explica à enfermeira o porquê de estar ali. A mulher tinha um rosto liso como uma boneca, olhos puxados como os dos asiáticos, cabelos pretos liso e longo e com muitas espinhas no rosto.\nO quarto em que você foi levado era pequeno, de formato retangular com uma janela defronte à porta de entrada com uma vista diretamente para o estacionamento, as paredes eram de cor verde claro e havia uma espécie de criado mudo ao lado da maca com alguns doces em cima.\nConforme anoitecia, você repousava sobre a maca e se energizava com a janta servida pelo hospital e com os doces como sobremesa. Antes de adormecer, você foi informado que um detetive iria vir ao local para lhe fazer algumas perguntas e você aceitou numa boa…|No dia seguinte, um céu nublado apresentava uma alta chance de chuva, às 8:30h da manhã. Você acorda com a enfermeira trazendo ao seu lado o detetive prometido.\nO diálogo fluiu, você deixou o detetive ciente de tudo que lhe aconteceu. Ele tira um diagnóstico da conversa e lhe explica que, cerca de dois dias atrás, recebeu ligações a respeito de um desaparecimento de um jovem com características físicas semelhantes a sua. O detetive mostra o telefone que recebeu a chamada e lhe pergunta se desejaria tentar retornar o telefone.\n\nDigite "1" para Aceitar a proposta e entrar em contato com esse telefoneou "2" para Ignorar a ligação pois seria muita coincidência de esse telefone ter contatado o detetive relatando o seu desaparecimento'],
        'proximos_estados': {
            '1|"1"': 14,
            '2|"2"': 15
        },
        'inventario':set()
    },
    14: {
        'frases': ['O detetive lhe empresta seu celular e disca para o número do telefone. De repente, ou por coincidência, um telefone começa a tocar próximo ao seu quarto. Você desconfia mas ignora, cancela a chamada e tenta mais uma vez, e novamente, o outro aparelho começou a tocar. Você e o detetive trocam olhares curiosos e decidem seguir o telefone barulhento…\nAo entrar no quarto, se deparam com uma senhora muito idosa adormecida em um quarto igual ao seu. A mulher tinha uma aparência semelhante à sua e o cabelo de cor igual ao seu também. Ao lado da maca em que estava a senhora, havia uma enfermeira arrumando os remédios da paciente, que lhe contou que a senhora surgiu um dia antes de você aparecer, diagnosticada com perda de memória depois de ter sido atropelada por um carro em uma rodovia da região. Você questiona a doutora da identidade da senhora e descobre que seu nome é Lilian Weasley de 67 anos, mãe de um rapaz desaparecido, chamado Tom Weasley…|O quarto começa a clarear, mas depois se apaga e você apenas enxerga as estrelas da sua imaginação, pois sua pressão cai rapidamente, por conta de, finalmente, lembrar de quem você é: Tom Weasley, filho único de um casal de costureira e artesão,  22 anos, de nacionalidade portuguesa, que estava comemorando a sua formação em medicina. Nesta noite, um sábado com um céu bem estrelado e de lua crescente, você estava no salão da festa comemorando sua conquista, mas de tanto beber, foi para a rua respirar um pouco. Porém, a embriaguês tomou conta do seu controle que o fez andar para longe do salão, indo parar em um bar da pesada, em que havia muitas pessoas não confiáveis na região. Você entra no bar e encontra essas pessoas apostando no jogo de sinuca, aquilo lhe atiça e você mostrou interesse em participar, entretanto nem se tocou que não possuía um euro em seu bolso. Por tudo isso, perdeu a partida e, como não tinha o que pagar, os vencedores o agarram, batem com os tacos de sinuca na cabeça, próximo da nuca, em que você adormece e lhe levam para próximo a um lugar parecido com um porto e lhe colocam dentro do barco que você acordou, posteriormente.\nFeliz e um pouco desesperado de ter se lembrado do que lhe aconteceu, você percebe que teria que enfrentar um outro problema: a memória de sua mãe que se encontrava adormecida…|Passados 2 dias sendo paciente do hospital, a enfermeira que lhe recebeu quando você entrou, pela primeira vez no local, vem ao seu encontro com pressa, em que lhe conta que sua mãe, Lilian Weasley, acordou perguntando sobre um tal de Tom. A enfermeira lhe conduziu ao quarto, lá estava a sua querida mãe: deitada sobre uma maca igual a sua, com a janela aberta com alguns vasos de flores posicionados para dentro do quarto, na frente da abertura...\nAo encostar sua mão na de sua mãe, um choque percorre sobre seu peito. Você profere, suavemente, a palavra "mãe", chamando-a... E acordando aos poucos, abre seus olhos bem devagar e lhe responde com "Olá, meu filho! Senti tanto sua falta"...|Um sentimento de felicidade faz seu coração bater aceleradamente. Você e sua mãe colocam as conversas em dia, ela fica ciente de que lhe ocorreu e diz sobre o seu pai: continuou com o seu serviço de artesão para manter a casa. O doutor entra no quarto da sua mãe para verificar seu estado e tirar um diagnóstico...\nPoucas horas depois, você retorna, finalmente, para sua casa: uma cabana de madeira, de espaço para três pessoas. A cozinha possuía apenas uma geladeira e um fogão de duas bocas, com uma mesa de pedra posicionada no meio da área. As lâmpadas se acendem com uma fraca luz amarela.\nSentado em uma das três cadeiras da mesa da cozinha, estava seu pai. Um homem alto, com um chapéu de palha usando uma camisa de manga curta cor xadrez verde e preta. Ele se levantou com pressa e lhe abraçou ("que saudades de você, meu filho").\nPor fim, seus pais ficaram cientes do que aconteceu com você: o que lhe aconteceu na noite da formatura e o motivo de ter ido parar dentro de um barco. O seu objetivo foi concluído, você conseguiu se lembrar de quem é você e o que lhe aconteceu!!\n\nParabéns, missão cumprida!! :first_place: :call_me:'],
        "inventario": set()
    },
    15: {
        'frases': ['Você, sem curiosidade, afirma que não quer retornar a ligação. Porém, o telefone vibra e começa a tocar. O celular apresentava a mensagem de “número desconhecido”. Você, um pouco assustado, diz ao detetive para atender a chamada. O detetive atende e coloca no viva-voz e uma voz fria e rouca pronuncia uma frase tremendamente assustadora e arrepiante: “7 dias…”. Então, um completo silêncio toma conta de todo o telefonema, após a mensagem se encerrar, a chamada cai. A sua reação é de dúvida e desentendimento, por não saber o que essa frase poderia significar, 7 dias poderia ser o tempo total do seu desaparecimento, poderia ser a quantidade de dias até o seu aniversário, o prazo de pagamento de uma aposta do jogo do bicho ou que daqui a 7 dias algo estaria te esperando…|E, realmente, algo estava à sua espera: Passada uma semana depois do telefonema, você, ainda no hospital, se encontrava sozinho sentado em um sofá, numa espécie de sala de descanso, assistindo um jogo da sua seleção (Portugal VS Camarões) e de repente a televisão de 28 polegadas se desliga, ficando com a tela toda escurecida. Um frio toca a sua pele e uma névoa surge do chão, tapando um pouco a sua visão, tendo, para você, agora, uma sala bem embaciada e pouco nítida. A tela se racha e uma mão mais pálida que um palmito se arrasta sobre o piso da sala. Depois surge uma cabeça olhando em direção ao solo, com seus cabelos pretos longos e quebradiços caídos, um vestido branco como sua pele, bem rasgado. Os braços da criatura estavam com marcas pretas, parecidas com sujeiras. A criatura se posiciona a 5 metros de você, em pé descalço encarando-o. Ela volta para o chão, e engatinha rapidamente atrás de você gritando “Tom” com sua voz fria. Você grita por ajuda, mas parece que sua voz não existe. A criatura lhe puxa para o chão e o arrasta para dentro da televisão, trancando-o no aparelho para sempre, desaparecendo, para os outros, de forma misteriosa. Após o sequestro sobrenatural, a tela da TV volta ao normal e o jogo retorna à transmissão.\n\nVocê falhou na missão :cry:;\nDigite “reiniciar” para jogar novamente :smiley:'],
        'proximos_estados':{
            '[Rr]einiciar|"[Rr]einiciar"': 1
        },
        'inventario':set()
    },
    16: {
        'frases': ['Você pensa que não é uma boa ideia ir para um local como este, pois pode retardar a sua missão e decide seguir em frente, sozinho, porém num local mais povoado…\nAo sair da praia, pensando no que fazer, você avista um prédio, com várias antenas no topo, com uma identificação de Rádio, que ficava do outro lado da rua. Com a ideia de tentar transmitir a sua situação para mais pessoas, você decide seguir até esse prédio, porém esqueceu de olhar para os dois lados antes de atravessar e é atropelado por um caminhão de gás, e acaba tendo uma morte rápida e nem um pouco dolorosa.\n\nVocê falhou na missão :cry:;\nDigite “reiniciar” para jogar novamente :smiley:'],
        'proximos_estados':{
            '[Rr]einiciar|"[Rr]einiciar"': 1
        },
        'inventario':set()
    }
}

# Dicionário com os estados correntes de cada jogador.
partidas = {}                                                                           