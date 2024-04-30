from django.db import models


class NedAssessment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
    question_01 = models.CharField(
        verbose_name='Eu sou...',
        choices=(
            ('I', 'I - Idealista, criativo e visionário'),
            ('C', 'C - Divertido, espiritual e benéfico'),
            ('O', 'O - Confiável, meticuloso e previsível'),
            ('A', 'A - Focado, determinado e persistente'),
        ),
        max_length=1,
        default='',
    )
    question_02 = models.CharField(
        'Eu gosto de...',
        choices=(
            ('A', 'A - Ser piloto'),
            ('C', 'C - Conversar com os passageiros'),
            ('O', 'O - Planejar a viagem'),
            ('I', 'I - Explorar novas rotas'),
        ),
        max_length=1,
        default='',
    )
    question_03 = models.CharField(
        'Se você quiser se dar bem comigo...',
        choices=(
            ('I', 'I - Me dê liberdade'),
            ('O', 'O - Me deixe saber sua expectativa'),
            ('A', 'A - Lidere, siga ou saia do caminho'),
            ('C', 'C - Seja amigável, carinhoso e compreensivo'),
        ),
        max_length=1,
        default='',
    )
    question_04 = models.CharField(
        'Para conseguir obter bons resultados é preciso...',
        choices=(
            ('I', 'I - Ter incertezas'),
            ('O', 'O - Controlar o essencial'),
            ('C', 'C - Diversão e celebração'),
            ('A', 'A - Planejar e obter recursos'),
        ),
        max_length=1,
        default='',
    )
    question_05 = models.CharField(
        'Eu me divirto quando...',
        choices=(
            ('A', 'A - Estou me exercitando'),
            ('I', 'I - Tenho novidades '),
            ('C', 'C - Estou com os outros'),
            ('O', 'O - Determino as regras'),
        ),
        max_length=1,
        default='',
    )
    question_06 = models.CharField(
        'Eu penso que...',
        choices=(
            ('C', 'C - Unidos venceremos, divididos perderemos'),
                ('A', 'A - O ataque é melhor que a defesa'),
            ('I', 'I - E bom ser manso, mas andar com um porrete'),
            ('O', 'O - Um homem prevenido vale por dois'),
        ),
        max_length=1,
        default='',
    )
    question_07 = models.CharField(
        'Minha preocupação é...',
        choices=(
            ('I', 'I - Gerar a ideia global'),
            ('C', 'C - Fazer com que as pessoas gostem'),
            ('O', 'O - Fazer com que funcione'),
            ('A', 'A - Fazer com que aconteça'),
        ),
        max_length=1,
        default='',
    )
    question_08 = models.CharField(
        'Eu prefiro...',
        choices=(
            ('I', 'I - questions e respostas'),
            ('O', 'O - Ter todos os detalhes'),
            ('A', 'A - Vantages a meu favor'),
            ('C', 'C - Que todos tenham a chance de serem ouvidos')
        ),
        max_length=1,
        default='',
    )
    question_09 = models.CharField(
        'Eu gosto de...',
        choices=(
            ('A', 'A - Fazer progresso'),
            ('I', 'I - Construir memórias'),
            ('O', 'O - Fazer sentido'),
            ('C', 'C - Tornar as pessoas confortáveis'),
        ),
        max_length=1,
        default='',
    )
    question_10 = models.CharField(
        'Eu gosto de chegar...',
        choices=(
            ('A', 'A - Na frente'),
            ('C', 'C - Junto'),
            ('O', 'O - Na hora'),
            ('I', 'I - Em outro lugar'),
        ),
        max_length=1,
        default='',
    )
    question_11 = models.CharField(
        'Um ótimo dia para mim é quando...',
        choices=(
            ('A', 'A - Consigo fazer muitas coisas'),
            ('C', 'C - Me divirto com meus amigos'),
            ('O', 'O - Tudo segue conforme planejado'),
            ('I', 'I - Desfruto de coisas novas e estimulantes'),
        ),
        max_length=1,
        default='',
    )
    question_12 = models.CharField(
        'Eu vejo a morte como...',
        choices=(
            ('I', 'I - Uma grande aventura misteriosa'),
            ('C', 'C - Oportunidade para rever os falecidos'),
            ('O', 'O - Um modo de receber recompensas'),
            ('A', 'A - Algo que sempre chega muito cedo'),
        ),
        max_length=1,
        default='',
    )
    question_13 = models.CharField(
        'Minha filosofia a de vida é...',
        choices=(
            ('A', 'A - Há ganhadores e perdedores, e eu acredito ser um ganhador'),
            ('C', 'C - Para eu ganhar, ninguém precisa perder'),
            ('O', 'O - Para ganhar é preciso seguir as regras'),
            ('I', 'I - Para ganhar, é necessário inventar novas regras'),
        ),
        max_length=1,
        default='',
    )
    question_14 = models.CharField(
        'Eu sempre gostei de...',
        choices=(
            ('I', 'I - Explorar'),
            ('O', 'O - Evitar surpresas'),
            ('A', 'A - Focalizar a meta'),
            ('C', 'C - Realizar uma abordagem natural'),
        ),
        max_length=1,
        default='',
        )
    question_15 = models.CharField(
        'Eu gosto de mudanças se...',
        choices=(
            ('A', 'A - Me der uma vantagem competitiva'),
            ('C', 'C - For divertido e puder ser compartilhado'),
            ('I', 'I - Me der mais liberdade e variedade'),
            ('O', 'O - Melhorar ou me der mais controle'),
        ),
        max_length=1,
        default='',
    )
    question_16 = models.CharField(
        'Não existe nada de errado em...',
        choices=(
            ('A', 'A - Se colocar na frente'),
            ('C', 'C - Colocar os outros na frente'),
            ('I', 'I - Mudar de ideia'),
            ('O', 'O - Ser consistente'),
        ),
        max_length=1,
        default='',
    )
    question_17 = models.CharField(
        'Eu gosto de buscar conselhos de...',
        choices=(
            ('A', 'A - Pessoas bem-sucedidas'),
            ('C', 'C - Anciões e conselheiros'),
            ('O', 'O - Autoridades no assunto'),
            ('I', 'I - Lugares, os mais estranhos'),
        ),
        max_length=1,
        default='',
    )
    question_18 = models.CharField(
        'Meu lema é...',
        choices=(
            ('I', 'I - Fazer o que precisa ser feito'),
            ('O', 'O - Fazer bem feito'),
            ('C', 'C - Fazer junto com o grupo'),
            ('A', 'A - Simplesmente fazer'),
        ),
        max_length=1,
        default='',
    )
    question_19 = models.CharField(
        'Eu gosto de...',
        choices=(
            ('I', 'I - Complexidade, mesmo se confuso'),
            ('O', 'O - Ordem e sistematização'),
            ('C', 'C - Calor humano e animação'),
            ('A', 'A - Coisas claras e simples'),
        ),
        max_length=1,
        default='',
    )
    question_20 = models.CharField(
        'Tempo para mim é...',
        choices=(
            ('A', 'A - Algo que detesto desperdiçar'),
            ('C', 'C - Um grande ciclo'),
            ('O', 'O - Uma flecha que leva ao inevitável'),
            ('I', 'I - Irrelevante'),
        ),
        max_length=1,
        default='',
    )
    question_21 = models.CharField(
        'Se eu fosse bilionário...',
        choices=(
            ('C', 'C - Faria doações para muitas entidades'),
            ('O', 'O - Criaria uma poupança avantajada'),
            ('I', 'I - Faria o que desse na cabeça'),
            ('A', 'A - Me exibiria bastante para algumas pessoas'),
        ),
        max_length=1,
        default='',
    )
    question_22 = models.CharField(
        'Eu acredito que...',
        choices=(
            ('A', 'A - O destino é mais importante que a jornada'),
            ('C', 'C - A jornada é mais importante que o destino'),
            ('O', 'O - Um centavo economizado é um centavo ganho'),
            ('I', 'I - Bastam um navio e uma estrela para navegar'),
        ),
        max_length=1,
        default='',
    )
    question_23 = models.CharField(
        'Eu acredito também que...',
        choices=(
            ('A', 'A - Aquele que hesita está perdido'),
            ('O', 'O - De grão em grão a galinha enche o papo'),
            ('C', 'C - O que vai, volta'),
            ('I', 'I - Um sorriso ou uma careta é o mesmo para quem é cego'),
        ),
        max_length=1,
        default='',
    )
    question_24 = models.CharField(
        'Eu acredito ainda que...',
        choices=(
            ('O', 'O - E melhor prudência do que arrependimento'),
            ('I', 'I - A autoridade deve ser desafiada'),
            ('A', 'A - Ganhar é fundamental'),
            ('C', 'C - O coletivo é mais importante do que o individual'),
        ),
        max_length=1,
        default='',
    )
    question_25 = models.CharField(
        'Eu penso que...',
        choices=(
            ('I', 'I - Não é fácil ficar encurralado'),
            ('O', 'O - É preferível olhar, antes de pular'),
            ('C', 'C - Duas cabeças pensam melhor do que uma'),
            ('A', 'A - Se você não tem condições de competir, não compita'),
        ),
        max_length=1,
        default='',
    )
    
    def __str__(self):
        return f"Avaliação Ned – {self.created_at.strftime('%d/%m/%Y %H:%M')}"
    
    def resultado_aguia(self):
        pontos = 0
        for number in range(1, 26):
            question = f'question_{number:02d}'
            if self.__dict__[question] == 'I':
                pontos += 1
        return pontos * 4
    
    def resultado_gato(self):
        pontos = 0
        for number in range(1, 26):
            question = f'question_{number:02d}'
            if self.__dict__[question] == 'C':
                pontos += 1
        return pontos * 4
    
    def resultado_tubarao(self):
        pontos = 0
        for number in range(1, 26):
            question = f'question_{number:02d}'
            if self.__dict__[question] == 'A':
                pontos += 1
        return pontos * 4
    
    def resultado_lobo(self):
        pontos = 0
        for number in range(1, 26):
            question = f'question_{number:02d}'
            if self.__dict__[question] == 'O':
                pontos += 1
        return pontos * 4
