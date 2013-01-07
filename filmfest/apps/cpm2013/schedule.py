# -*- coding: utf-8 -*-
from datetime import date, time

from django.utils.translation import ugettext_lazy as _


class PROGRAMS:
    ANIMATION = ('animation', _(u'анимационная программа'))
    GOOD = ('good', _(u'хорошее кино'))
    DOCUM = ('docs', _(u'документальное кино'))
    DOCUM_INCONV = (None, _(u'неудобная документалистика'))
    BELARUS = ('bel', _(u'беларусское кино'))
    BVC = (None, _(u'фильмы БелВидеоЦентра'))
    MUSIC = (None, _(u'клипы, презентация KinoLife.com'))
    URBAN = ('urban', _(u'программа урбанистики'))
    AWARDS = (None, _(u'награждение победителей'))
    INT = (None, _(u'международная программа'))
    
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

class PLACES:
    LAMORA = _(u'ДК La мора')
    DDM = _(u'Минский государственный Дворец детей и молодежи')
    CENTER = _(u'кинотеатр Центральный')
    FIALTA = _(u'Молодежный образовательный центр "Фиальта""')
    FISHER = _(u'Дом Фишера')
    MUSEUM_CIN = _(u'Музей кино')
    MUSEUM_MODERN = _(u'Музей современного искусства')
    MUSEUM_ARTS = _(u'Национальный музей')

SCHEDULE = [
    (
        date(2013, 1, 12),
        [
            (time(12, 00), PROGRAMS.ANIMATION, PLACES.DDM),
            (time(17, 00), PROGRAMS.YOUNG1, PLACES.DDM),
            (time(18, 40), PROGRAMS.COMPET1, PLACES.CENTER),
            (time(19, 00), PROGRAMS.GENDER1, PLACES.FIALTA),
            (time(21, 10), PROGRAMS.GOOD, PLACES.CENTER),
        ]
    ),
    (
        date(2013, 1, 13),
        [
            (time(18, 40), PROGRAMS.COMPET2, PLACES.CENTER),
            (time(19, 00), PROGRAMS.GENDER2, PLACES.FIALTA),
            (time(21, 10), PROGRAMS.COMPET3, PLACES.CENTER),
        ]
    ),
    (
        date(2013, 1, 14),
        [
            (time(18, 40), PROGRAMS.YOUNG1, PLACES.CENTER),
            (time(19, 00), PROGRAMS.ANIMATION, PLACES.FISHER),
            (time(21, 10), PROGRAMS.DOCUM, PLACES.CENTER),
        ]
    ),
    (
        date(2013, 1, 15),
        [
            (time(18, 40), PROGRAMS.ANIMATION, PLACES.CENTER),
            (time(21, 10), PROGRAMS.YOUNG2, PLACES.CENTER),
        ]
    ),
    (
        date(2013, 1, 16),
        [
            (time(18, 40), PROGRAMS.YOUNG2, PLACES.CENTER),
            (time(21, 10), PROGRAMS.BELARUS, PLACES.CENTER),
        ]
    ),
    (
        date(2013, 1, 17),
        [
            (time(18, 40), PROGRAMS.KARIN, PLACES.MUSEUM_CIN),
            (time(19, 00), PROGRAMS.PIERRE_LUC, PLACES.MUSEUM_MODERN),
            (time(19, 00), PROGRAMS.MUSIC, PLACES.FISHER),
            (time(19, 00), PROGRAMS.URBAN, PLACES.FIALTA),
            (time(21, 10), PROGRAMS.BVC, PLACES.CENTER),
        ]
    ),
    (
        date(2013, 1, 18),
        [
            (time(18, 40), PROGRAMS.INT, PLACES.MUSEUM_ARTS),
            (time(19, 00), PROGRAMS.EXPERIMENTAL, PLACES.MUSEUM_MODERN),
            (time(21, 10), PROGRAMS.GOOD, PLACES.CENTER),
        ]
    ),
    (
        date(2013, 1, 19),
        [
            (time(12, 00), PROGRAMS.ANIMATION, PLACES.DDM),
            (time(17, 00), PROGRAMS.URBAN, PLACES.FIALTA),
            (time(17, 00), PROGRAMS.YOUNG2, PLACES.DDM),
            (time(21, 10), PROGRAMS.GENDER3, PLACES.CENTER),
        ]
    ),
    (
        date(2013, 1, 20),
        [
            (time(15, 00), PROGRAMS.URBAN, PLACES.FIALTA),
            (time(18, 40), PROGRAMS.AWARDS, PLACES.MUSEUM_ARTS),
            (time(21, 10), PROGRAMS.DOCUM_INCONV, PLACES.LAMORA),
        ]
    ),
]
