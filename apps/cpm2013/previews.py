# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _


class GENDER:
    MALE = 1
    FEMALE = 2
    OTHER = 3

    CHOICES = (
        (MALE, _(u'мужской')),
        (FEMALE, _(u'женский')),
        (OTHER, _(u'другой')),    
    )

    DEFAULT = OTHER


class EDUCATION:
    SECONDARY = 1
    INCOMPLETE_HIGHER = 2
    HIGHER = 3
    
    CHOICES = (
        (SECONDARY, _(u'среднее')),
        (INCOMPLETE_HIGHER, _(u'незаконченное высшее')),
        (HIGHER, _(u'высшее')),
    )

    DEFAULT = SECONDARY


class YESNO:
    NO = 1
    YES = 2

    CHOICES =(
        (NO, _(u'нет')),
        (YES, _(u'да')),
    )

    DEFAULT = NO

class WORKING(YESNO):
    CHOICES =(
        (YESNO.NO, _(u'не работаю')),
        (YESNO.YES, _(u'работаю')),
    )

class PARTICIPATION_IN_FILM_CREATION:
    NO = 1
    YES_BY_CHANCE = 2
    YES = 3
    YES_OFTEN = 4

    CHOICES = (
        (NO, _(u'нет')),
        (YES_BY_CHANCE, _(u'да, случайно участвовал(а)')),
        (YES, _(u'да, время от времени участвую')),
        (YES_OFTEN, _(u'да, постоянно участвую')),
    )

    DEFAULT = NO

class HOW_OFTEN:
    WEEK = 1
    MONTH = 2
    HALF_A_YEAR = 3
    YEAR = 4
    
    CHOICES = [
        (WEEK, _(u'несколько раз в неделю')),
        (MONTH, _(u'несколько раз в месяц')),
        (HALF_A_YEAR, _(u'несколько раз в полгода')),
        (YEAR, _(u'несколько раз в год и реже')),
    ]

    DEFAULT = YEAR

class HOW_OFTEN_SCREENINGS(HOW_OFTEN):
    NEVER = 5

    CHOICES = HOW_OFTEN.CHOICES + [(NEVER, _(u'ни разу не посещал'))]

class CINEPHILIA_STAGE:
    CINEMALOVER = 1
    CINEMALOVER_ADVANCED = 2
    CINEMAN_NOVICE = 3
    CINEMAM_ADVANCED = 4
    CINEPHIL = 5
    
    CHOICES = (
        (CINEMALOVER, _(u'Кинолюбитель')),
        (CINEMALOVER_ADVANCED, _(u'Продвинутый кинолюбитель')),
        (CINEMAN_NOVICE, _(u'Киноман-новичок')),
        (CINEMAM_ADVANCED, _(u'Киноман с опытом')),
        (CINEPHIL, _(u'Синефил')),
    )

    DEFAULT = CINEMALOVER
