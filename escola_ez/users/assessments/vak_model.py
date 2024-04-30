from django.db import models


YES = 'S'
NO = 'N'
YES_NO = (
    (YES, 'Sim'),
    (NO, 'Não'),
)


class VAKAssessment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
    question_01 = models.CharField(
        verbose_name='Escrevo listas daquilo que tenho de fazer?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_02 = models.CharField(
        verbose_name='Realizo coisas desde que as instruções escritas sejam bem detalhadas?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_03 = models.CharField(
        verbose_name='Gosto de fazer palavras cruzadas?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_04 = models.CharField(
        verbose_name='Gosto de exposições e museus?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_05 = models.CharField(
        verbose_name='Localizo-me com facilidade em uma cidade nova se tiver um mapa?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_06 = models.CharField(
        verbose_name='Todos os meses assisto a vários filmes?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_07 = models.CharField(
        verbose_name='Não tenho boa impressão de alguém se estiver mal vestido?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_08 = models.CharField(
        verbose_name='Gosto de observar as pessoas?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_09 = models.CharField(
        verbose_name='Acho que flores realmente embelezam a casa e o escritório?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_10 = models.CharField(
        verbose_name='Mando consertar os arranhões do meu carro o mais rápido possível?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_11 = models.CharField(
        verbose_name='Gosto de longas conversas?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_12 = models.CharField(
          'Gosto de programas de entrevistas, no rádio e na TV?',
          choices=YES_NO,
          max_length=1,
        default='',
    )
    question_13 = models.CharField(
        verbose_name='Sou bom ouvinte?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_14 = models.CharField(
        verbose_name='Prefiro os noticiários de rádio e TV do que jornais e revistas?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_15 = models.CharField(
        verbose_name='Sinto-me mal quando meu carro faz algum barulho diferente?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_16 = models.CharField(
        verbose_name='Quando ouço música presto muita atenção à letra?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_17 = models.CharField(
        verbose_name='Posso dizer muito sobre alguém somente pelo seu tom de voz?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_18 = models.CharField(
        verbose_name='Prefiro fazer uma palestra a escrever sobre um assunto?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_19 = models.CharField(
        verbose_name='As pessoas dizem que, às vezes, falo demais?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_20 = models.CharField(
        verbose_name='Costumo conversar comigo mesmo ou com meu cão ou gato?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_21 = models.CharField(
        verbose_name='Quando ouço música, não consigo deixar de mexer as mãos e os pés?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_22 = models.CharField(
        verbose_name='Gosto muito de estar ao ar livre?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_23 = models.CharField(
        verbose_name='Tenho boa coordenação motora?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_24 = models.CharField(
        verbose_name='Tenho tendência a ganhar peso?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_25 = models.CharField(
        verbose_name='Gosto de criar animais de estimação?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_26 = models.CharField(
        verbose_name='Toco as pessoas quando converso?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_27 = models.CharField(
        verbose_name='Gosto mais de praticar esportes do que assistir a eles?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_28 = models.CharField(
        verbose_name='Adoro banho, piscina, sauna?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_29 = models.CharField(
        verbose_name='Gosto de levantar-me e espreguiçar-me com frequência?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    question_30 = models.CharField(
        verbose_name='Posso dizer muito sobre uma pessoa através de seu aperto de mão?',
        choices=YES_NO,
        max_length=1,
        default='',
    )
    
    def __str__(self):
        return f"Avaliação ACV – {self.created_at.strftime('%d/%m/%Y %H:%M')}"
    
    def pontos_visual(self):
        pontos = 0
        for number in range(1,11):
            question = f'question_{number:02d}'
            if self.__dict__[question] == 'S':
                pontos += 1
        return pontos
    
    def pontos_auditivo(self):
        pontos = 0
        for number in range(11,21):
            question = f'question_{number:02d}'
            if self.__dict__[question] == 'S':
                pontos += 1
        return pontos
    
    def pontos_cinestesico(self):
        pontos = 0
        for number in range(21,31):
            question = f'question_{number:02d}'
            if self.__dict__[question] == 'S':
                pontos += 1
        return pontos
