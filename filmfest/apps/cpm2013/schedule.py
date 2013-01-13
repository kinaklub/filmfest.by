# -*- coding: utf-8 -*-
from datetime import date, time

from django.utils.translation import ugettext_lazy as _


class PROGRAMS:
    OPENING = (None, _(u'открытие фестиваля'))
    CLOSING = (None, _(u'закрытие фестиваля'))
    AWARDS = (None, _(u'награждение победителей'))
    
    ANIMATION = ('animation', _(u'программа анимации'))
    GOOD = ('good', _(u'хорошее кино'))
    DOCUM = ('docs', _(u'документальное кино'))
    DOCUM_INCONV = (None, _(u'неудобная документалистика'))
    BELARUS = ('bel', _(u'беларусское кино'))
    BVC = (None, _(u'фильмы БелВидеоЦентра'))
    MUSIC = (None, _(u'клипы'))
    KINOLIFE = (None, _(u'презентация Международной интерактивной платформы для кинематографистов KINOLIFE.eu'))
    URBAN = ('urban', _(u'программа урбанистики'))
    INT = (None, _(u'международная программа'))
    ECOLOGICAL = (None, _(u'экологическая программа'))
    REGIONAL = (None, _(u'региональная программа'))
    UZV = (None, _(u'программа для университета золотого века'))

    GENDER1 = ('gender', _(u'гендерная программа 1'))
    GENDER2 = ('gender', _(u'гендерная программа 2'))
    GENDER3 = ('gender', _(u'гендерная программа 3'))
    
    YOUNG1 = ('youth', _(u'молодежная программа 1'))
    YOUNG2 = ('youth', _(u'молодежная программа 2'))

    COMPET1 = ('competition', _(u'конкурсная программа 1'))
    COMPET2 = ('competition', _(u'конкурсная программа 2'))
    COMPET3 = ('competition', _(u'конкурсная программа 3'))

    KARIN = (None, _(u'ретроспектива Карин Брэк'))
    PIERRE_LUC = (
        'pierre_luc',
        _(u'программа экспериментального кино от Пьер-Люка Вайянкура')
    )
    EXPERIMENTAL = ('experimental', _(u'экспериментальное кино'))

    CONCERT = (None, _(u'концерт бардов и рок-групп'))

class PLACES_MINSK:
    LAMORA = _(u'ДК La мора\n2-ая ул. Щорса, 7а')
    DDM = _(u'Минский государственный Дворец детей и молодежи\n'\
            u'Старовиленский тракт, 41')
    CENTER = _(u'кинотеатр Центральный\nпр-т Независимости, 13')
    FIALTA = _(u'Молодежный образовательный центр "Фиальта"\n'\
               u'ул. Мясникова, 35 (вход со двора)')
    FISHER = _(u'Дом Фишера\nпр-т Независимости, 84А')
    MUSEUM_CIN = _(u'Музей кино\nул. Свердлова, 4')
    MUSEUM_MODERN = _(u'Музей современного искусства\nпр-т Независимости, 47')
    MUSEUM_ARTS = _(u'Национальный музей\nул. Ленина 20')

MINSK = [
    (
        date(2013, 1, 12),
        [
            (time(12, 00), [PROGRAMS.ANIMATION], PLACES_MINSK.DDM),
            (time(17, 00), [PROGRAMS.YOUNG1], PLACES_MINSK.DDM),
            (time(18, 40), [PROGRAMS.COMPET1], PLACES_MINSK.CENTER),
            (time(19, 00), [PROGRAMS.GENDER1], PLACES_MINSK.FIALTA),
            (time(21, 10), [PROGRAMS.GOOD], PLACES_MINSK.CENTER),
        ]
    ),
    (
        date(2013, 1, 13),
        [
            (time(18, 40), [PROGRAMS.COMPET2], PLACES_MINSK.CENTER),
            (time(19, 00), [PROGRAMS.GENDER2], PLACES_MINSK.FIALTA),
            (time(21, 10), [PROGRAMS.COMPET3], PLACES_MINSK.CENTER),
        ]
    ),
    (
        date(2013, 1, 14),
        [
            (time(18, 40), [PROGRAMS.YOUNG1], PLACES_MINSK.CENTER),
            (time(19, 00), [PROGRAMS.ANIMATION], PLACES_MINSK.FISHER),
            (time(21, 10), [PROGRAMS.DOCUM], PLACES_MINSK.CENTER),
        ]
    ),
    (
        date(2013, 1, 15),
        [
            (time(18, 40), [PROGRAMS.ANIMATION], PLACES_MINSK.CENTER),
            (time(21, 10), [PROGRAMS.YOUNG2], PLACES_MINSK.CENTER),
        ]
    ),
    (
        date(2013, 1, 16),
        [
            (time(18, 40), [PROGRAMS.YOUNG2], PLACES_MINSK.CENTER),
            (time(21, 10), [PROGRAMS.BELARUS], PLACES_MINSK.CENTER),
        ]
    ),
    (
        date(2013, 1, 17),
        [
            (time(18, 00), [PROGRAMS.KARIN], PLACES_MINSK.MUSEUM_CIN),
            (time(19, 00), [PROGRAMS.PIERRE_LUC], PLACES_MINSK.MUSEUM_MODERN),
            (time(19, 00), [PROGRAMS.MUSIC, PROGRAMS.KINOLIFE], PLACES_MINSK.FISHER),
            (time(19, 00), [PROGRAMS.URBAN], PLACES_MINSK.FIALTA),
            (time(21, 10), [PROGRAMS.BVC], PLACES_MINSK.CENTER),
        ]
    ),
    (
        date(2013, 1, 18),
        [
            (time(19, 00), [PROGRAMS.INT], PLACES_MINSK.MUSEUM_ARTS),
            (time(19, 00), [PROGRAMS.EXPERIMENTAL], PLACES_MINSK.MUSEUM_MODERN),
            (time(21, 10), [PROGRAMS.GENDER3], PLACES_MINSK.CENTER),
        ]
    ),
    (
        date(2013, 1, 19),
        [
            (time(12, 00), [PROGRAMS.ANIMATION], PLACES_MINSK.DDM),
            (time(17, 00), [PROGRAMS.URBAN], PLACES_MINSK.FIALTA),
            (time(17, 00), [PROGRAMS.YOUNG2], PLACES_MINSK.DDM),
            (time(21, 10), [PROGRAMS.GOOD], PLACES_MINSK.CENTER),
        ]
    ),
    (
        date(2013, 1, 20),
        [
            (time(15, 00), [PROGRAMS.URBAN], PLACES_MINSK.FIALTA),
            (time(19, 00), [PROGRAMS.AWARDS], PLACES_MINSK.MUSEUM_ARTS),
            (time(21, 10), [PROGRAMS.DOCUM_INCONV], PLACES_MINSK.LAMORA),
        ]
    ),
]


class PLACES_HRODNA:
    KALYAN = _(u'Кальянная №4\nул. К.Марска, 10')
    SEKTOR3 = _(u'Центр "Третий Сектор"')
    KR_ZVEZDA = _(u'Кинотеатр "Красная звезда"\nул. Социалистическая, 4')
    BIOFAK = _(u'Биофак ГрГУ')

HRODNA = [
    (
        date(2013, 1, 13),
        [
            (time(13, 00), [PROGRAMS.OPENING, PROGRAMS.YOUNG1], PLACES_HRODNA.KALYAN),
            (time(17, 00), [PROGRAMS.GENDER1], PLACES_HRODNA.SEKTOR3),
        ]
    ),
    (
        date(2013, 1, 14),
        [
            (time(18, 00), [PROGRAMS.DOCUM], PLACES_HRODNA.KALYAN),
        ]
    ),
    (
        date(2013, 1, 15),
        [
            (time(18, 00), [PROGRAMS.MUSIC, PROGRAMS.ANIMATION], PLACES_HRODNA.KALYAN),
        ]
    ),
    (
        date(2013, 1, 16),
        [
            (time(11, 30), [PROGRAMS.ECOLOGICAL], PLACES_HRODNA.BIOFAK),
        ]
    ),
    (
        date(2013, 1, 16),
        [
            (time(19, 00), [PROGRAMS.REGIONAL], PLACES_HRODNA.KR_ZVEZDA),
        ]
    ),
    (
        date(2013, 1, 17),
        [
            (time(18, 00), [PROGRAMS.BELARUS], PLACES_HRODNA.KALYAN),
        ]
    ),
    (
        date(2013, 1, 18),
        [
            (time(18, 00), [PROGRAMS.GOOD, PROGRAMS.KARIN], PLACES_HRODNA.SEKTOR3),
        ]
    ),
    (
        date(2013, 1, 19),
        [
            (time(14, 00), [PROGRAMS.UZV], PLACES_HRODNA.SEKTOR3),
            (time(16, 00), [PROGRAMS.CLOSING, PROGRAMS.YOUNG2], PLACES_HRODNA.KALYAN),
        ]
    ),
]


PLACES_LIDA_MUSEUM = _(u'Лидский государственный историко-художественный '\
                       u'музей\nул. Победы, З7а, Лида')

LIDA = [
    (
        date(2013, 1, 12),
        [
            (time(18, 00), [PROGRAMS.OPENING, PROGRAMS.CONCERT], PLACES_LIDA_MUSEUM),
        ]
    ),
    (
        date(2013, 1, 14),
        [
            (time(18, 00), [PROGRAMS.COMPET1], PLACES_LIDA_MUSEUM),
        ]
    ),
    (
        date(2013, 1, 15),
        [
            (time(18, 00), [PROGRAMS.COMPET2], PLACES_LIDA_MUSEUM),
        ]
    ),
    (
        date(2013, 1, 16),
        [
            (time(18, 00), [PROGRAMS.COMPET3], PLACES_LIDA_MUSEUM),
        ]
    ),
    (
        date(2013, 1, 17),
        [
            (time(18, 00), [PROGRAMS.ANIMATION], PLACES_LIDA_MUSEUM),
        ]
    ),
    (
        date(2013, 1, 18),
        [
            (time(18, 00), [PROGRAMS.YOUNG1], PLACES_LIDA_MUSEUM),
        ]
    ),
    (
        date(2013, 1, 19),
        [
            (time(18, 00), [PROGRAMS.CLOSING], PLACES_LIDA_MUSEUM),
        ]
    ),
]


def get_upcoming_events(city):
    today = date.today()
    for date_, places in city:
        if date_ >= today:
            yield date_, places


SCHEDULES = [
    (_(u'Minsk'), 'minsk', list(get_upcoming_events(MINSK))),
    (_(u'Hrodna'), 'hrodna', list(get_upcoming_events(HRODNA))),
    (_(u'Lida'), 'lida', list(get_upcoming_events(LIDA))),
]
