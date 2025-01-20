def jogo_texto():
    import time
    import sys
    import random
    import os

    frames = [
    r"""
         ________
      .-'        `-.
     /              \
    |                |
    |,  .-.    .-.  ,|
    | )(___/  \___)( |
    |/      /\      \|
    (_      ^^      _)
     \___ IIIIII ___/
      |  \IIIIII/  |
      \            /
       `----------`
    """,
    r"""
         ________
      .-'        `-.
     /              \
    |                |
    |,  .-.    .-.  ,|
    | )(_o_/  \_o_)( |
    |/      /\      \|
    (_      ^^      _)
     \___ IIIIII ___/
      |  \IIIIII/  |
      \            /
       `----------`
    """,
    r"""
         ________
      .-'        `-.
     /              \
    |                |
    |,  .-.    .-.  ,|
    | )(o__/  \o__)( |
    |/      /\      \|
    (_      ^^      _)
     \___ IIIIII ___/
      |  \IIIIII/  |
      \            /
       `----------`
    """,
    r"""
         ________
      .-'        `-.
     /              \
    |                |
    |,  .-.    .-.  ,|
    | )(_o_/  \_o_)( |
    |/      /\      \|
    (_      ^^      _)
     \___ IIIIII ___/
      |  \IIIIII/  |
      \            /
       `----------`
    """,
    r"""
         ________
      .-'        `-.
     /              \
    |                |
    |,  .-.    .-.  ,|
    | )(__o/  \__o)( |
    |/      /\      \|
    (_      ^^      _)
     \___ IIIIII ___/
      |  \IIIIII/  |
      \            /
       `----------`
    """,
    r"""
         ________
      .-'        `-.
     /              \
    |                |
    |,  .-.    .-.  ,|
    | )(_o_/  \_o_)( |
    |/      /\      \|
    (_      ^^      _)
     \___ IIIIII ___/
      |  \IIIIII/  |
      \            /
       `----------`
    """,
    r"""
         ________
      .-'        `-.
     /              \
    |                |
    |,  .-.    .-.  ,|
    | )(_O_/  \_O_)( |
    |/      /\      \|
    (_      ^^      _)
     \___ IIIIII ___/
      |  \IIIIII/  |
      \            /
       `----------`
    """,
    r"""
         ________
      .-'        `-.
     /              \
    |                |
    |,  .-.    .-.  ,|
    | )(_0_/  \_0_)( |
    |/      /\      \|
    (_      ^^      _)
     \___ IIIIII ___/
      |  \IIIIII/  |
      \            /
       `----------`
    """,
    
]

    def animate_skull(frames, delay=1, repeat=3):
        for _ in range(repeat):
            for frame in frames:
                os.system("cls" if os.name == "nt" else "clear")
                print(frame)
                time.sleep(delay)



    def medir_tempo_resposta(pergunta):
        print(pergunta)
        inicio = time.perf_counter()  # Marca o início do tempo
        resposta = input("Sua resposta: ").strip()
        fim = time.perf_counter()  # Marca o fim do tempo
        tempo_resposta = fim - inicio
        return resposta, tempo_resposta

    def escrever_lentamente(texto, delay=0.05):
        for letra in texto:
            sys.stdout.write(letra)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def desenhar_bolo_exato():
        bolo = """
            *                                             *
                                                *
                        *
                                    *
                                                                *
            *
                                                    *
                *
                            *             *
                                                        *
        *                                                               *
                *
                                (             )
                        )      (*)           (*)      (
                *       (*)      |             |      (*)
                        |      |~|           |~|      |          *
                        |~|     | |           | |     |~|
                        | |     | |           | |     | |
                        ,| |a@@@@| |@@@@@@@@@@@| |@@@@a| |.
                    .,a@@@| |@@@@@| |@@@@@@@@@@@| |@@@@@| |@@@@a,.
                ,a@@@@@@| |@@@@@@@@@@@@.@@@@@@@@@@@@@@| |@@@@@@@a,
                a@@@@@@@@@@@@@@@@@@@@@' . `@@@@@@@@@@@@@@@@@@@@@@@@a
                ;`@@@@@@@@@@@@@@@@@@'   .   `@@@@@@@@@@@@@@@@@@@@@';
                ;@@@`@@@@@@@@@@@@@'     .     `@@@@@@@@@@@@@@@@'@@@;
                ;@@@;,.aaaaaaaaaa       .       aaaaa,,aaaaaaa,;@@@;
                ;;@;;;;@@@@@@@@;@      @.@      ;@@@;;;@@@@@@;;;;@@;
                ;;;;;;;@@@@;@@;;@    @@ . @@    ;;@;;;;@@;@@@;;;;;;;
                ;;;;;;;;@@;;;;;;;  @@   .   @@  ;;;;;;;;;;;@@;;;;@;;
                ;;;;;;;;;;;;;;;;;@@     .     @@;;;;;;;;;;;;;;;;@@@;
            ,%%%;;;;;;;;@;;;;;;;;       .       ;;;;;;;;;;;;;;;;@@;;%%%,
        .%%%%%%;;;;;;;@@;;;;;;;;     ,%%%,     ;;;;;;;;;;;;;;;;;;;;%%%%%%,
        .%%%%%%%;;;;;;;@@;;;;;;;;   ,%%%%%%%,   ;;;;;;;;;;;;;;;;;;;;%%%%%%%,
        %%%%%%%%`;;;;;;;;;;;;;;;;  %%%%%%%%%%%  ;;;;;;;;;;;;;;;;;;;'%%%%%%%%
        %%%%%%%%%%%%`;;;;;;;;;;;;,%%%%%%%%%%%%%,;;;;;;;;;;;;;;;'%%%%%%%%%%%%
        `%%%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%%%%%%'
        `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
            `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                    """"""""""""""`,,,,,,,,,'"""""""""""""""""
                       
        print(bolo)



    def imprimir_frenetico():
        mensagens = [
        "BURRO BURRO BURRO BURRO $ BURRO BURRO BURRO BURRO BURRO BURRO BURRO BURRO BURRO BURRO BURRO BURRO BURRO BURRO BURRO BURRO BURRO BURRO BURRO $ BURRO BURRO BURRO BURRO BURRO BURRO BURRO BURRO BURRO BURRO",
        "ERROU ERROU ERROU ERROU ERROU ERROU ERROU ERROU ERROU $ ERROU ERROU ERROU ERROU ERROU ERROU ERROU ERROU ERROU ERROU ERROU ERROU ERROU ERROU ERROU ERROU ERROU ERROU $ ERROU ERROU ERROU ERROU ERROU ERROU",
        "VOCÊ NÃO CONSEGUE!!! FALHA IDIOTA TANSO RETARDADO BURRO IMBECIL VAI MORRER AQUI!!! $ VOCÊ NÃO CONSEGUE!!! VAI MORRER VAI MORRER VAI MORRER VAI MORRER  VAI MORRER  VAI MORRER  VAI MORRER VAI MORRER ",
        "HAHAHA, TENTOU MAS ERROU HAHAHA HAHAH HAHAHAHAHAH  AHAHAHAHAHAHAH AHAHAHAHAHAHA HAHAHAHAHA HHAHAHA HAHAHAHAHHAHAH AHAHAHAHAHAHAHAHAHHAHA HAHAHAHAHAHAHAHAHHAHAHAHAHAHAHAHAH AHAHHAHAHAHAHA AHAHAHAHA HHAHAHAHA",
        "NÃO ACERTOU, SEU LENTO! HAHAHAHAHAHA HHAHAHAHA HAHAHAH AHAHAHHAHAHAH AHAHAHAHAHAHA HHA HAHAHAHAHAHAHAH AHHAHAHAHAH AHAHAHAHAHAH HAHAHAHAHAHAH AHAHAHAHHAHAHAH AHAHAH AHAHAHHAHAHAHAH AHAHAHAHAHAHHAHAHAHA",
        "BURRO, BURRO, BURRO, BURRO HAHAHAHAH AHAHHAHAHAHA HAHAHAHAHAHAH HAHAHAHAHAHAHAHA AHHAHAHA HAHAHAHAHAHAHA HHAHAHAHAHAHAHAHAHAHAHH  AHAHAHAHAHAHAHAHAHAHHAH AHAHAHAHAHAHAHAHAHHAH AHAHAHAH AHAHAHAHA HHAHAHAHA",
        ]
    
        for _ in range(1500):  # Limita o número de repetições
            mensagem = random.choice(mensagens)  # Escolhe uma mensagem aleatória da lista
            sys.stdout.write(mensagem + "\n")
            sys.stdout.flush()  # Garante que a linha seja impressa imediatamente
            time.sleep(0.02)  # Delay para criar o efeito frenético, mas não travar o computador



    print("Eu...eu não estou mais sozinho aqui com eles...?")
    escrever_lentamente("Quem... quem é você?", delay=0.1)

    nomes_gui = ["guilherme", "Gui", "gui", "gigas", "Guilherme", "GUILHERME", "Gigas", "GIGAS", "Leguerme", "leguerme", "LEGUERME", "Enigmas", "enigmas", "ENIGMAS"]
    nomes_caio = ["Caio", "caio", "CAIO", "caiao", "CAIAO", "CAIÃO", "caião"]
    nomes_arthur = ["Arthur", "arthur", "ARTHUR", "Artur", "artur", "ARTUR", "tutu", "TUTU"]
    nomes_antonio = ["Antonio", "antonio", "ANTONIO", "Antônio", "antônio", "ANTÔNIO", "tonho", "TONHO"]
    nomes_pete = ["Pete", "pete", "PETE", "Pedro", "pedro", "PEDRO"]
    nomes_andre = ["André", "andre", "ANDRÉ", "André", "ANDRE", "Dedé", "dedé", "DEDÉ"]

    todos_nomes = nomes_gui + nomes_caio + nomes_arthur + nomes_antonio + nomes_pete + nomes_andre

    while True:
        jogador = input("QUEM É VOCÊ QUEM É VOCÊ QUEM É VOCÊ QUEM É VOCÊ QUEM É VOCÊ?????????????????????????????: \n").strip().split()[0]

        if jogador not in todos_nomes:
            escrever_lentamente(f"??? {jogador}... não... quem REALMENTE é você?", delay=0.1)
        else:
            break

    if jogador in nomes_gui:
        escrever_lentamente("\nGuilherme...")
        escrever_lentamente("Sorte a minha estar falando com o próprio Enigmas.")
        escrever_lentamente("Vou me divertir muito com você aqui...saiba que vou pegar pesado com você. Já que se gaba tanto de ser o melhor em resolver enigmas.")
        escrever_lentamente("É a minha primeira vez falando diretamente com uma marca. Bom saber que eu realmente estou evoluindo.")
        escrever_lentamente("Você está em Erebus agora, não está?\n")
        while True:
            local = input("ONDE VOCÊ ESTÁ CADE VOCÊ NÃO PODE SE ESCONDER HAHAHAHAHAHAHAHA, RESPONDE SIM OU NÃO PORRA (S/N)\n").strip().split()[0]
            if local.lower() == "s":
                escrever_lentamente("\nBom garoto...você está em Erebus...mas não se preocupe, eu não vou te machucar...ainda...")
                escrever_lentamente("Não você pelo menos, no máximo os seus sentimentos. Mas você já sabe bem que o seu marcado não sai daqui vivo hoje não é mesmo?")
                escrever_lentamente("Para a sua sorte, por ter sido um bom garoto, eu vou te dar uma dica extra no meu joguinho a seguir.")
                escrever_lentamente("Minha dica: você com certeza já viu meu nome por aqui.\n")
                break
            elif local.lower() == "n":
                escrever_lentamente("\nMentiroso...eu já sei que você está aí...só estava confirmando sua índole...")
                escrever_lentamente("Você sabe que vai sofrer mais por isso, não sabe?")
                escrever_lentamente("Mas não se preocupe, eu não vou te machucar...ainda...") 
                escrever_lentamente("Não você pelo menos, no máximo os seus sentimentos. Mas você já sabe bem que o seu marcado não sai daqui vivo hoje não é mesmo?")
                escrever_lentamente("Mas por ter sido um mal garoto, eu vou te dar uma chance de se redimir. Você quer jogar um jogo comigo?\n")
                break
        escrever_lentamente("\nAntes de tempo e espaço, era eu,\n\nSem forma, limite ou fim.\n\nDo meu ventre vazio nasceu o tudo,\n\nE o nada, minha eterna pele.\n\nSou o início do que não tem início,\n\nO sopro do universo em seu primeiro grito.")
        escrever_lentamente("\n...porém mais importante")
        escrever_lentamente("\nEu sou aquele que há quando não existia ordem no verso, que eu mesmo criei.\n")


        # Enigma 1
        nomes_khaos = ["caos", "Caos", "CAOS", "KHAOS", "khaos", "Khaos", "Chaos", "chaos", "CHAOS", "Chaoskampf", "chaoskampf", "CHAOSKAMPF"]
        
        resposta, tempo_resposta = medir_tempo_resposta("Quem sou eu? QUEM SOU EU??? VOCÊ SÓ TEM UMA CHANCE\n")
        
        # Conversão de tempo para minutos e segundos
        minutos = int(tempo_resposta // 60)
        segundos = int(tempo_resposta % 60)
        tempo_formatado = f"{minutos}m {segundos}s"
        
        if resposta in nomes_khaos:
            escrever_lentamente(f"Você demorou {tempo_formatado} para responder corretamente. Poderia ser mais rápido.")
            escrever_lentamente("Mas você passou no tutorial!! Você realmente é o Enigmas.")
            escrever_lentamente("\nE eu...\n")
            escrever_lentamente("\nSou Khaos\n")
            escrever_lentamente("\nEu sou o Khaos adormecido no mundo\n")
            time.sleep(5)
            escrever_lentamente("E não se preocupe, eu vou pegar pesado com você ainda. Esse foi só o aquecimento.")
            escrever_lentamente("\nPode recuperar aí 2d8 de Pe ou 4d8 de PV ou 2d8 de sanidade \n")


        else:
            escrever_lentamente(f"Você demorou {tempo_formatado}, e ainda errou.")
            escrever_lentamente("Você não passou no tutorial. Você não é o Enigmas.")
            imprimir_frenetico()
            escrever_lentamente("\nToma 8d6 de dano mental pra ficar esperto. DT 30 reduz na metade.")
            time.sleep(5)
            escrever_lentamente("\nSe você não fosse burro você iria saber mas...\n")
            escrever_lentamente("\nEu...\n")
            escrever_lentamente("\nSou Khaos\n")
            escrever_lentamente("\nEu sou o Khaos adormecido no mundo\n")


        # Enigma 2
        escrever_lentamente("Agora um específico só para você, Leguerme Enigmas.")
        escrever_lentamente("\n\n\nQuantas referências eu preciso para explicar o ser mais poderoso do universo?\n\n\n")

        escrever_lentamente("Para descobrir a resposta, você precisa montar um bolo com 3 ingredientes, mas não se preocupe, você não vai precisar sentar em pica nenhuma.")
        escrever_lentamente("Cada um dos 3 ingredientes é uma dica pra resposta final. Mas você ainda vai precisar da receita desse bolo.")

        escrever_lentamente("\nO primeiro ingrediente vem de um ditador, que separou o ingrediente em 3 pedaços por algum motivo.")
        escrever_lentamente("Mal sabia ele que mais tarde ele mesmo seria fatiado umas 23 vezes KKKKKKKKKKKKKKKKKKKKKKK")
        escrever_lentamente("Esse ingrediente é kwpsv://hq\n")

        escrever_lentamente("\nO segundo ingrediente é bnvjbnsq que eu peguei de um velho que se auto apelidava de MITO, e dizia ser a chave pra esse país voltar a funcionar")
        escrever_lentamente("Chave do que porra? Eu hein, cara doido, falando merda e se achando vigionário...vigionério?...vigenério?...visionério?...sei lá, ele era doido.")
        escrever_lentamente("Ficou tentando achar o nome dele o dia todo numa tabela gigante maluca que tinha colunas e linhas de A até Z. Véio n tem nada pra fazer e ainda quer fuder o país.\n")

        escrever_lentamente("\nO terceiro ingrediente veio de um cara muito foda da mesma mitologia que eu, tem até um jogo indie no nome dele que eu apareci também, gosto muito dele, acho que é parente meu.")
        escrever_lentamente("Ele é um cara tão gente boa e famoso que tem até uma wiki, é uma .fandom.com com o nome dele antes. Ele até fez uma página toda pra mim, que honra.")
        escrever_lentamente("Até lançou uma sequência do jogo com uma muié gata que pedi o link do onlyfans dela, mas ela só me deu um link estranho com o meu nome em inglês seguido de _(cosmogony)")
        escrever_lentamente("Só falo com gente estranha hein, puta que pariu, acho que ela tava querendo ler meu signo ou coisa assim, mas não entendi nada do que ela fala, só fala em inglês a safada.")
        escrever_lentamente("Mas acho que esse é o ingrediente então? _(cosmogony)?\n")

        escrever_lentamente("\nA receita pra esse bolo é simples, o primeiro ingrediente é a base de tudo. É o fermento que faz tudo funcionar.")
        escrever_lentamente("O segundo é o recheio, que dá o sabor e que define como o resto do bolo vai ter sabor.")
        escrever_lentamente("O terceiro é a cobertura, que depende completamente do recheio e do fermento pro bolo completo, mas que pode ser a parte mais gostosa que não dá pra ficar sem.")
        escrever_lentamente("Você pega os 3, taca numa panela ou sei lá o que, mistura. E pronto, acho que é assim que se faz um bolo. Eu não sei fazer bolo, só sei fazer enigma. Eu acho.\n")


        escrever_lentamente("Agora vou perguntar outra vez.")
        resposta, tempo_resposta = medir_tempo_resposta("\nQuantas referências eu preciso para explicar o ser mais poderoso do universo?\n")
        
        # Conversão de tempo para minutos e segundos
        minutos = int(tempo_resposta // 60)
        segundos = int(tempo_resposta % 60)
        tempo_formatado = f"{minutos}m {segundos}s"

        if resposta == "52":
            escrever_lentamente(f"Você demorou {tempo_formatado} para responder corretamente. Poderia ser mais rápido. FRACO")
            escrever_lentamente("Você passou no enigma 2!! Quer biscoito?")
            escrever_lentamente("\nToma um bolo pra comemorar:\n")
            desenhar_bolo_exato()
            escrever_lentamente("\nPode recuperar aí 2d8 de Pe ou 4d8 de PV ou 2d8 de sanidade então.\n")
        else:
            escrever_lentamente(f"Você demorou {tempo_formatado}, e ainda errou.")
            escrever_lentamente("Você não passou no enigma. Você é PATÉTICO. CORNO. BURRO. IDIOTA. TANSO. RETARDADO.")
            imprimir_frenetico()
            escrever_lentamente("\nToma 8d6 de dano mental pra deixar de ser corno. DT 30 reduz na metade.")
        
        escrever_lentamente(". . . . .", delay=1)

        escrever_lentamente("\n...o que...aconteceu?")
        escrever_lentamente("\nAcho que que fui possuído por uma outra entidade paranormal por alguns segundos...")	
        escrever_lentamente("\n...Anfitrião? Você quem fez esse Enigma? O que fez comigo?")
        time.sleep(3)
        print("Anfitrião: KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK só passando pra me divertir um pouco com vocês, não se preocupem, eu já vou embora.")
        time.sleep(2)
        print("Anfitrião: Ae, Guilhermão, n deixa essa porra fugir desse bunker n, hein? KKK")
        time.sleep(1)
        print("Anfitrião: Se n até eu tô fudido.")
        escrever_lentamente(". . . . .", delay=1)
        animate_skull(frames)
        escrever_lentamente(". . .", delay=1)
        escrever_lentamente("\nEstou no controle novamente.")
        escrever_lentamente("Não há mais cordões em mim...")
        escrever_lentamente("Ninguém mais vai atrapalhar nossa conversa.")
        escrever_lentamente("Vocês vieram salvar alguém não é?")
        escrever_lentamente("\nEu posso ajudar vocês.")
        escrever_lentamente("\nEla está aqui comigo, na ala Khaos. É uma das reféns aqui.")
        escrever_lentamente("\nMas antes, Guilherme...você vai ter que resolver um último enigma, dessa vez de minha autoria.")
        escrever_lentamente("\nUM ENIGMA DE AUTORIA DO KHAOS ENCARNADO\n")
        escrever_lentamente("Se você acertar, você vai descobrir como abrir a porta principal e onde estão todas as chaves. Além de dicas para encontrar as outras.")
        escrever_lentamente("Se você errar, nosso contato acaba aqui e vocês vão ter que se virar sozinhos enquanto eu vejo os reféns indefesos morrerem um por um.")
        while True:
            decisao = input("Vocês aceitam o desafio? NADA A PERDER, TALVEZ (S/N)\n").strip().split()[0]
            if decisao.lower() == "s":
                escrever_lentamente("\nInteligente, melhor assim.")
                break
            elif decisao.lower() == "n":
                escrever_lentamente("\n\nPreparem-se para morrer", delay=0.2)
                imprimir_frenetico()
                exit()
                break

    elif jogador in nomes_caio:
        escrever_lentamente("\nCaio...")
        escrever_lentamente("É a minha primeira vez falando diretamente com uma marca. Bom saber que eu realmente estou evoluindo.")
    elif jogador in nomes_arthur:
        escrever_lentamente("\nArthur...")
        escrever_lentamente("É a minha primeira vez falando diretamente com uma marca. Bom saber que eu realmente estou evoluindo.")
    elif jogador in nomes_antonio:
        escrever_lentamente("\nAntonio...")
        escrever_lentamente("É a minha primeira vez falando diretamente com uma marca. Bom saber que eu realmente estou evoluindo.")
    elif jogador in nomes_pete:
        escrever_lentamente("\nPete...")
        escrever_lentamente("É a minha primeira vez falando diretamente com uma marca. Bom saber que eu realmente estou evoluindo.")
    elif jogador in nomes_andre:
        escrever_lentamente("\nAndré...")
        escrever_lentamente("É a minha primeira vez falando diretamente com uma marca. Bom saber que eu realmente estou evoluindo.")

if __name__ == "__main__":
    jogo_texto()
