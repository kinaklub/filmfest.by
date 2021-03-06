# -*- coding: utf-8 -*-
from collections import namedtuple
from datetime import datetime


Program = namedtuple('Program', 'title description parts')


def _get_program_animation():
    title = 'Анимация. Внеконкурсная программа.'
    description = 'В программе анимации представлены короткометражные фильмы о зомби, Франкенштейне, черепахах, белке и осьминоге, также не обойдены вниманием проблемы экологии и смысла жизни. Половина из работ входит в конкурсную программу — а это значит, что они получили самые высокие зрительские оценки.'
    parts = [
        (
            [
                (
                    datetime(2013, 1, 14, 19, 0),
                    'Дом Фишера,\nпр-т Независимости, 84а',
                    '300 руб/минуту'
                ),
                (
                    datetime(2013, 1, 15, 18, 40),
                    'Фойе кинотеатра «Центральный»,\nпр-т Независимости, 13',
                    '15000'
                ),
            ],
            '''Томатная история, реж. Ольга и Татьяна Полиектовы (Россия, 2010)
Комедия/ 4 минуты

Junky Food, реж. Юрий Твердин (Беларусь, 2011)
Экспериментальный видео-арт/ 1 минута

Sponge ideas, реж. Катажына Наливайка, Павлина Жевчик (Польша, 2011)
Музыкальное видео/ 5 минут

Чертовщина 6: ремейк «Франкенштейна» 1910 года, реж. Денис Кант (Украина, 2012)
Экспериментальное кино/ 4 минуты

Климат и ты, реж. Марианна Леонард (Беларусь, 2012)
Социальный ролик/ 4 минуты

Добро, красота и правда, реж. Бальбина Буршевска (Польша, 2011)
Драма/ 6 минут

Horad, реж. Андрей Баджи Токинданг (Беларусь, 2012)
Пародия/ 4 минуты

Шум, реж. Татьяна и Ольга Полиектовы (Россия, 2012)
Драма/ 10 минут

Если может кот..., реж. Марианна Леонард (Беларусь, 2012)
Социальный ролик/ 1 минута

Краткая история климатических изменений, реж. Жори Клерте (Франция, 2012)
Социальный ролик/ 1 минута

Охота, реж. Урал (Россия, 2012)
Первобытная драма в стиле экшн/ 8 минут

Пир зверей, реж. Эзра Вубе (США, 2012)
Народная сказка/ 10 минут

Нить сновидения, реж. Марта Пайек (Польша, 2011)
Драма/ 14 минут '''
        ),
    ]

    return Program(title, description, parts)
# -*- coding: utf-8 -*-

def _get_program_bel():
    title = 'Белорусские фильмы. Внеконкурсная программа.'
    description = 'На фестиваль Cinema Perpetuum Mobile было подано 75 заявок от участников из Беларуси. Во внеконкурсной программе собраны фильмы белорусских участников – в ней можно найти и анимацию, и документальные, и игровые фильмы. Бюджет белорусского кино - «нервы-нервы», «море пота и усилий», «питание актеров» и редко измеряется в денежном эквиваленте. Тем не менее, есть и полуполнометражная драма, и мистика со спецэффектами. Задумываются молодые и начинающие режиссёры и о социальных проблемах – не потому ли, что короткий метр позволяет быть независимым?'
    parts = [
        (
            [
                (
                    datetime(2013, 1, 16, 21, 10),
                    'Фойе кинотеатра «Центральный»,\nпр-т Независимости, 13',
                    15000
                ),
            ],
            '''Танцуем чарльстон в Минске, Надежда Клементенок (Беларусь, 2012)
Лирический танцевальный клип/4 минуты

Если может кот..., Марианна Леонард (Беларусь, 2012)
Социальный ролик/ 1 минута

Письмо Карла Маркса, реж. Дмитрий Сорока (Беларусь, 2012)
Социальное эссе/ 3 минуты

Социальная смерть, реж. Марина Лепешко (Беларусь, 2012)
Интервью/ 3 минуты

Тележизнь, реж. Светлана Колодкина (Беларусь, 2011)
Драма/ 3 минуты

Конкордия, реж. Михаил Умпирович (Беларусь, 2012)
Драма, мистика/ 13 минут

Человек-вещь, реж. Дарья Ефимова (Беларусь, 2012)
Философский дневник/ 11 минут

Ambitious Untitled Project, реж. Катя Дорожкина (Беларусь, 2012)
Черная комедия/ 5 минут

Солигорские терриконы, реж. Виталий Наркевич (Беларусь, 2012)
Документальный фильм/ 2 минуты

Климат и ты, реж. Марианна Леонард (Беларусь, 2012)
Социальный ролик/ 4 минуты

Песочница, реж. Олеся Погорелова (Беларусь, 2012)
Мелодрама/ 8 минут

Junky Food, реж. Юрий Твердин (Беларусь, 2011)
Экспериментальный видео-арт/ 1 минута

Проникновение, реж. Александр Касперович (Беларусь, 2012)
Мистическая драма, 19 минут

Horad, реж. Андрей Баджи Токинданг (Беларусь, 2012)
Боевик, пародия, триллер, ужасы/ 4 минуты

Кирляндия, реж. Илья Божко (Беларусь, 2012)
Сатира, фантастическая антутопия/7 минут

Простые вещи, реж. Артем Лобач (Беларусь, 2012)
Документальный фильм/ 11 минут'''
        ),
    ]

    return Program(title, description, parts)

def _get_program_gender():
    title = '«Женская роль»,\nГендерное кино. Внеконкурсная программа'
    description = 'Правила «нормального» поведения для женщины отличаются от тех, что предписываются в обществе мужчинам. Готовые шаблоны могут позволить человеку бесконфликтно проживать  жизнь, но помешают стать самим собой. Выйти за рамки «нормального», шаблонов и приличий – не это ли нам нужно, чтобы спасти своё «я» от растворения в серости вечного повторения одного и того же? Режиссёры рассказывают истории о том, как женщины являются женщинами в разных, сложных, комичных и трагичных ситуациях.\n\nПрограмма подготовлена совместно с инициативой ["Гендерный маршрут"](http://gender-route.org)'
    parts = [
        (
            [
                (
                    datetime(2013, 1, 18, 21, 10),
                    'Фойе кинотеатра «Центральный»,\nпр-т Независимости, 13',
                    '15000'
                ),
            ],
            '''Одень меня, реж. Малгожата Голишевска (Польша, 2011)
Документальный фильм/ 16 минут

Свободное падение, реж. Карин Брэк (Швеция, 2010)
Драма, 14 минут

Песочница, реж. Олеся Погорелова (Беларусь, 2012)
Мелодрама/ 8 минут

Исчезновение, реж. Бартош Круглик (Польша, 2011)
Психологическая драма/ 20 минут

Мама, реж. Дмитрий Суржиков (Украина, 2011)
Драма, триллер/ 15 минут

Революция в Рейкьявике, реж. Изольд Уггадоттир (Исландия, 2012)
Драма/ 19 минут'''
        ),
        (
            [
                (
                    datetime(2013, 1, 12, 19, 0),
                    'Молодежный обазовательный центр «Фиальта»,\n'\
                    'ул. Мясникова, 35',
                    None
                )
            ],
            '''Не по-детски. История о выборах, реж. Татьяна Элькина, Ксения Граушкина (Россия, 2012)
Документальный фильм/ 19 минут

Женщины. Площадь, реж. Светлана Алексиевич (Беларусь, 2012)
Документальный фильм/ 33 минуты

Легко ли быть активистом?, реж. Наталья Простякова (Россия, 2012)
Документальный фильм/ 21 минута'''
        ),
        (
            [
                (
                    datetime(2013, 1, 13, 19, 0),
                    'Молодежный обазовательный центр «Фиальта»,\n'\
                    'ул. Мясникова, 35',
                    None
                )
            ],
            '''Станция «Бесконечная», реж. Майя Ветрова (Россия, 2012)
Игровой/ 20 минут

Мама, реж. Дмитрий Суржиков (Украина, 2011)
Драма, триллер/ 15 минут

Одень меня, реж. Малгожата Голишевска (Польша, 2011)
Документальный фильм/ 16 минут'''
        ),
    ]
    return Program(title, description, parts)

def _get_program_docs():
    title = 'Документальное кино. Внеконкурсная программа.'
    description = 'Иногда жизнь похожа на кино, а иногда кино похоже на жизнь. В документальном кино, конечно, важнее быть реалистичным. Но доля поэтичности не мешает приблизиться к реальности, а, возможно, даже способствует чёткости в её выражении. К белорусской, российской, украинской, польской и интернациональной реальности можно будет стать ближе в документальной программе Cinema Perpetuum Mobile.'
    parts = [
        (
            [
                (
                    datetime(2013, 1, 14, 21, 10),
                    'Фойе кинотеатра «Центральный»,\nпр-т Независимости, 13',
                    '15000'
                )
            ],
            '''Солигорские терриконы, реж. Виталий Наркевич (Беларусь, 2012)
Документальный фильм/ 2 минуты

Такой вид птиц, реж. Малгожата Голишевска (Польша, 2012)
Документальный фильм/ 12 минут

Хождение по муХам, реж. Алексей Захарченко (Россия, 2011)
Неигровой фильм/ 6 минут 

Я это я, реж. Карин Брэк (Швеция, 2012)
Документально-поэтический эксперимент/  6 минут
10 минут, реж. Ростислав Смирнягин (Россия, 2012)
Коллективный портрет/ 7 минут

Социальная смерть, реж. Марина Лепешко (Беларусь, 2012)
Интервью/ 3 минуты

Проект ПодКожный, реж. Андрада Попан Дорка (Великобритания, 2012)
Документальный фильм/ 12 минут

Весь мир Гани и Стася, реж. Томаш Юркевич (Польша, 2011) 
Документальный фильм/  58 минут

Испорченный телефон, реж. Антон Жадько (Украина, 2012)
Социальная драма/ 8 минут

Простые вещи, реж. Артем Лобач (Беларусь, 2012)
Документальный фильм/ 11 минут'''
        ),
    ]
    return Program(title, description, parts)

def _get_program_good():
    title = 'Ещё одна программа хорошего кино. Внеконкурсная.'
    description = 'По регламенту фестиваля в конкурсе не могли участвовать фильмы, хронометраж которых больше 20 минут. Тем не менее, в числе заявок оказались такие, которые из-за этого ограничения не смогли участвовать в конкурсе. Но оргкомитет внимательно рассмотрел все заявки и все фильмы, в результате чего появилась ещё одна внеконкурсная программа. Про что может быть хорошее кино? Конечно, про гуманизм и высшие человеческие ценности, про вечную любовь, которая заставляет круговорот действительности не стоять на месте и про волшебство в праздники и будни. Два часа на всё это – много или мало? В самый раз!'
    parts = [
        (
            [
                (
                    datetime(2013, 1, 12, 21, 10),
                    'Фойе кинотеатра «Центральный»,\nпр-т Независимости, 13',
                    15000
                ),
                (
                    datetime(2013, 1, 19, 21, 10),
                    'Фойе кинотеатра «Центральный»,\nпр-т Независимости, 13',
                    15000
                ),
            ],
            '''Человеческий фактор, реж. Тибо ЛеТексье (Франция, 2011)
Эксперементальный документальный фильм/ 28 минут

Санта, кто?, реж. Димитрис Мутсякас (Греция, 2011)
Игровой фильм/ 24 минуты 

Нолия, реж. Цем Озгуфекчи (Турция, 2011)
Драма/ 26 минут

Twist & Blood, реж. Куба Чекай (Польша, 2010)
Драма/ 30 минут'''
        ),
    ]
    return Program(title, description, parts)

def _get_program_competition():
    title = 'Конкурсная программа'
    description = 'Отбор фильмов, присыланных на фестиваль, в конкурсную программу осуществлялся на основании зрительских оценок. Киноманы и заинтересованные в кино люди посещали открытые предпросмотры, которые проходили в течение месяца (шесть выходных дней, 10 часов каждый день) и оцениивали фильмы, которые увидели. Всего в качестве зрителей предпросмотры посетило 83 человека, из 328 заявленных фильмов в конкурсную программу было отобрано 25. Их можно будет увидеть как на специальных конкурсных показах. Также, большинство из них входит в различные внеконкурсные тематические программы. '
    parts = [
        (
            [
                (
                    datetime(2013, 1, 12, 18, 40),
                    'Фойе кинотеатра «Центральный»,\nпр-т Независимости, 13',
                    '15000'
                )
            ],
            '''Пляска смерти, реж. Юлия Новичева (Россия, 2012)
Трагедия/ 3 минуты

Голубой вагон, реж. Стефани Ассимакопоуло (Франция, 2012)
Фантастика, сказка, мистика/ 18 минут 

Висельник, Бартош Круглик (Польша, 2012)
Фантастика, черная комедия/ 15 минут

Кирляндия, реж. Илья Божко (Беларусь, 2012), 
Сатира, фантастическая антутопия/7 минут

Если может кот..., Марианна Леонард (Беларусь, 2012)
Социальный ролик/ 1 минута

Эскимосский поцелуй, реж. Карин Брэк (Швеция, 2012) 
Драма/ 13 минут

Шум, реж. Татьяна и Ольга Полиектовы (Россия, 2012)
Драма/ 10 минут

Фейерферки, реж. Джакомо Аббруццезе (Франция, 2011)
Экшн, приключения, политический боевик / 21 минута'''
        ),
        (
            [
                (
                    datetime(2013, 1, 13, 18, 40),
                    'Фойе кинотеатра «Центральный»,\nпр-т Независимости, 13',
                    '15000'
                )
            ],
            '''Танцуем чарльстон в Минске, Надежда Клементенок (Беларусь, 2012)
Лирический танцевальный клип/4 минуты

Прощай, жестокий мир!, реж. Андриус Паскевичус (Литва, 2012),
Драма/ 8 минут

82, реж. Калум Макдиармид (Великобритания, 2012)
Драма, триллер / 6 минут

Мама, реж. Дмитрий Суржиков (Украина, 2011)
Драма, триллер/ 15 минут

Краткая история климатических изменений, реж. Жори Клерте (Франция, 2012),
Социальный ролик / 1 минута

Испорченный телефон, реж. Антон Жадько (Украина, 2012)
Социальная драма/ 8 минут

Нить сновидения, реж. Марта Пайек (Польша, 2011)
Драма /14 минут 

Второе дыхание, реж. Сергей Цысс (Россия, 2012)
Научная фантастика/ 7 минут

Соляной камень, реж. Элиза Мурсан (Франция, 2012)
Драма/ 21 минута'''
        ),
        (
            [
                (
                    datetime(2013, 1, 13, 21, 10),
                    'Фойе кинотеатра «Центральный»,\nпр-т Независимости, 13',
                    '15000'
                )
            ],
            '''Horad, реж. Андрей Баджи Токинданг (Беларусь, 2012)
Боевик, пародия, триллер, ужасы/ 4 минуты

Охота, реж. Урал (Россия, 2012)
Первобытная драма в стиле экшн/ 8 минут

Очарование Рук, реж. Юрий Титов (США, 2012)
Абсурдная комедия/ 18 минут

Deadline, реж. Анастасия Гавинская (Украина, 2012)
Драма/ 11 минут

Цирк, реж. Пабло Ремон (Испания, 2011)
Комедия/ 8 минут

Ваня, реж. Оксана Артеменко (Украина, 2012)
Драма/10 минут

Простые вещи, реж. Артем Лобач (Беларусь, 2012)
Документальный фильм/ 11 минут

Революция в Рейкьявике, реж. Изольд Уггадоттир (Исландия, 2012)
Драма/ 19 минут'''
        ),
    ]
    return Program(title, description, parts)

def _get_program_youth():
    title = '3+ 12+ 16+ 18+,\nМолодежное кино. Внеконкурсная программа.'
    description = 'Справедливо ли выделять среди хорошего кино молодежную, программу? Да! Если это означает, что фильмы в ней пропитаны энергией, зарядом молодой дерзости и юношеским максимализмом! Именно в молодости люди серьёзно думают о смысле жизни, для них жизненно важно найти свое место в своем мире, они не боятся бороться и добиваться правды, брать неизведанные рубежи. А ещё громко петь, смеяться и делать глупости. Специально для тех, кто пока ещё молод, два показа хорошего кино от фестиваля Cinema Perpetuum Mobile.'
    parts = [
        (
            [
                (
                    datetime(2013, 1, 12, 17, 0),
                    'Минский государственный Дворец детей и молодежи,\n'\
                    'Старовиленский тракт, 41',
                    None,
                ),
                (
                    datetime(2013, 1, 14, 18, 40),
                    'Фойе кинотеатра «Центральный»,\nпр-т Независимости, 13',
                    '15000',
                ),
            ],
            '''Добро, красота и правда, реж. Бальбина Буршевска (Польша, 2011)
Драма/ 6 минут

Шум, реж. Татьяна и Ольга Полиектовы (Россия, 2012)
Драма/ 10 минут

Краткая история климатических изменений, реж. Жори Клерте (Франция, 2012)
Социальный ролик/ 1 минута

Песочница, реж. Олеся Погорелова (Беларусь, 2012)
Мелодрама/ 8 минут

Twist & Blood, реж. Куба Чекай (Польша, 2010)
Драма/ 30 минут

Испорченный телефон, реж. Антон Жадько (Украина, 2012)
Социальная драма/ 8 минут

Мама, реж. Дмитрий Суржиков (Украина, 2011)
Драма, триллер/ 15 минут'''
        ),
        (
            [
                (
                    datetime(2013, 1, 15, 21, 10),
                    'Фойе кинотеатра «Центральный»,\nпр-т Независимости, 13',
                    '15000',
                ),
                (
                    datetime(2013, 1, 16, 18, 40),
                    'Фойе кинотеатра «Центральный»,\nпр-т Независимости, 13',
                    '15000',
                ),
                (
                    datetime(2013, 1, 19, 17, 0),
                    'Минский государственный Дворец детей и молодежи,\n'\
                    'Старовиленский тракт, 41',
                    None,
                ),
            ],
            '''100!, реж. Карин Брэк (Швеция, 2011)
Экспериментальное кино/ 4 минуты

Ваня, реж. Оксана Артеменко (Украина, 2012)
Драма/10 минут

Исчезновение, реж. Бартош Круглик (Польша, 2011)
Психологическая драма/ 20 минут

Стрельба в школе, реж. Стефан Грубер (США, 2012)
Мюзикл, 10 минут

Если может кот..., Марианна Леонард (Беларусь, 2012)
Социальный ролик/ 1 минута

Одень меня, реж. Малгожата Голишевска (Польша, 2011)
Документальный фильм/ 16 минут
10 минут, реж. Ростислав Смирнягин (Россия, 2012)
Коллективный портрет/ 7 минут

Эскимосский поцелуй, реж. Карин Брэк (Швеция, 2012) 
Драма/ 13 минут

Революция в Рейкьявике, реж. Изольд Уггадоттир (Исландия, 2012)
Драма/ 19 минут'''
        ),
    ]
    return Program(title, description, parts)

def _get_program_pierre_luc():
    title = 'Программа экспериментальных фильмов\nот Пьера-Люка Вайянкура\n(Институт экспериментального кино, Канада)'
    description = 'Как призма оживления света и звука, эта программа короткометражек отражает органические и трансцендентальные возможности кино. Конструктивистские симфонии, микрокосмическое оживление и эксцентричные перспективы – всё сходится в киноизобретениях визуальной и звуковой динамики. Программа представляет экспериментальные фильмы канадских режиссеров с 1950 до наших дней, специально отобранные для того, чтобы совершить радостное и возбуждающее путешествие по магическим образам такого искусства как кино.\n\nВ программе фильмы [Стивена Волошена](http://en.wikipedia.org/wiki/Steven_Woloshen), [Карла Брауна](http://making-light-of-it.blogspot.com/2010/09/carl-brown-interview.html), [Нормана МакЛарена](http://en.wikipedia.org/wiki/Norman_McLaren), [Теодора Ушева](http://en.wikipedia.org/wiki/Theodore_Ushev), [Карла Лемьё](http://www.incite-online.net/lemieuxone.html), [Даичи Саито](http://lumenjournal.org/i-forests/saito/), Пьера-Люка Вайянкура.'
    parts = [
        (
            [
                (
                    datetime(2012, 1, 17, 19, 0),
                    'Музей Современного Искусства,\n'\
                    'Минск, пр. Независимости, 47',
                    'уточняется'
                )
            ],
            None
        )
    ]
    return Program(title, description, parts)

def _get_program_experimental():
    title = 'Экспериментальные фильмы. Внеконкурсный показ.'
    description = 'Для экспериментального кино нет никаких рамок и правил – эксперимент в фильмах секции экспериментального кино каждый режиссер понимает по-своему. Есть фильмы, эксплуатирующие жесткость визуального и вписывающиеся в рамки сложившихся экспериментальных школ - из Германии и Австралии. Есть поэтические, ностальгические фильмы из Швеции и Франции. Авторы из России и Украины представляют себе эксперимент скорее как деформацию традиционной наррации. Тем не менее, всех объединяет стремление уйти от привычного и создать нечто новое, показать нечто таинственное и необычное.'
    parts = [
        (
            [
                (
                    datetime(2012, 1, 18, 19, 0),
                    'Музей Современного Искусства,\n'\
                    'Минск, пр. Независимости, 47',
                    'уточняется'
                )
            ],
            '''Стакан молока, реж. Егор Чичканов (Россия, 2012),
Драма, мистика/ 6 мин.

Я это я, реж. Карин Брэк (Швеция, 2012)
Документально-поэтический эксперимент/ 6 мин.

Страшный шок, реж. Аня Дорниден, Хуан Давид Гонсалес Монро (Германия, 2011)
Экспериментальный фильм/ 3 мин.

Ожидание, реж. Алексей Захарченко (Россия, 2011)
Экспериментальное видео/ 4 мин.

I see you, реж. Татьяна и Ольга Полиектовы (Россия, 2012)
Арт/ 2 мин.

Oro Parece, реж. Аня Дорниден, Хуан Давид Гонсалес Монро (Германия, 2011)
Экспериментальный фильм/ 6 мин.

Дым и зеркала, реж. Ник Мур (Австралия, 2012)
Экспериментальный/ 6 мин.

Visitors, реж. Дмитро Бондарчук (Украина, 2012)
Драма, триллер/ 8 мин.

Чертовщина 6, реж. Денис Кант (Украина, 2012)
Хоррор/ 4 мин.

Любовники, реж. Лопе Сериз (Франция, 2011)
Экспериментальный фильм/ 30 мин.'''
        )
    ]
    return Program(title, description, parts)

def _get_program_urban():
    title = 'Кино о городе и его политике. Внеконкурсная программа'

    description = '''Город — место жительства большинства населения Земли и отправной пункт для многих дискуссий. Так, без урбанизации невозможно представить разговор об экономическом кризисе и неолиберальной политике. Смещение ракурса обсуждения с национального на городской уровень дает нам возможность говорить о вопросах сообществ, собственности и землепользования, городского управления и культурных индустрий. Когда мы рассуждаем о современном социальном движении, то признаем: в его авангарде нынче стоят низовые жилищные инициативы и городские активисты, которых можно объединить идеей «права на город».
    
Лейтмотивом программы “Mundo Urbano” является оккупация - однако это не просто рассказы о социальных центрах и сквотах как об автономных оазисах альтернативного образа жизни. Эти повествования затрагивают широкие и общие проблемы - несправедливую жилищную политику, последствия деиндустрилизации и глобального соревнования городов в креативности - например, история барселонского движения “1000 домов” (“Squat – La ville est a nous” Кристофа Коэльо), анализ борьбы за доступные культурные и жилищные пространства в Амстердаме (“Creative Capitalist City” Тино Буххольца), рассказ о захватывающих дома матерях из польского Вальбжиха (“Strajk matek” Магды Малиновской). С городской политикой переплетаются и другие нарративы: например, квартирный вопрос как причина отсутствия личной жизни (нелегкую долю румынских архитекторов описывает в “La Pierre de sel” Элиза Муресан); а темы взросления и старения находят отражение в очень личной истории о вынужденном переселении в фильме “Resettlement” Филиппа Антони Малиновского.
    
Введением в белорусскую проблематику станет фильм “Новый свет” Артема Лобача о разрушении одноименного района в Гродно. После этого состоится панельная дискуссия, в рамках которой мы вместе с экспертами попытаемся разобраться, что же такое «право на город» по-белорусски.'''
    parts = [
        (
            [
                (
                    datetime(2013, 1, 17, 19, 0),
                    'Молодежный обазовательный центр «Фиальта»,\n'\
                    'ул. Мясникова, 35',
                    None
                )
            ],
            '''Сквот — город принадлежит нам, реж. Кристоф Коэльо (Франция, 2011)
Документальный фильм/ 94 минуты

Страйк матерей, реж. Малгожата Мацевска, Магда Малиновска (Польша, 2010)
Документальный фильм/ 22 минуты'''
        ),
        (
            [
                (
                    datetime(2013, 1, 19, 17, 0),
                    'Молодежный обазовательный центр «Фиальта»,\n'\
                    'ул. Мясникова, 35',
                    None
                )
            ],
            '''Соляной камень, реж. Элиза Муресан  (Румыния, 2012)
Игровой фильм/ 21 минута

(Ex)terrados, реж. Алекс Лора (Испания, 2008)
Игровой фильм/ 11 минут

Переселение, реж. Филип Антони Малиновски (Австрия/Польша, 2012)
Документальный фильм/ 56 минут'''
        ),
        (
            [
                (
                    datetime(2013, 1, 20, 15, 0),
                    'Молодежный обазовательный центр «Фиальта»,\n'\
                    'ул. Мясникова, 35',
                    None
                )
            ],
            '''Креативный капиталистический город, реж. Тино Буххольц (Нидерланды, 2011)
Документальный фильм/ 55 минут

Новый Свет, реж. Артем Лобач (Беларусь, 2012)
Документальный фильм/ 14 минут

* Дискуссия: «Право на город по-белорусски»'''
        ),
    ]
    return Program(title, description, parts)


def _get_program_bvc():
    title = 'Программа фильмов БелВидеоЦентра'

    description = ''
    parts = [
        (
            [
                (
                    datetime(2013, 1, 17, 21, 10),
                    'Фойе кинотеатра «Центральный»,\nпр-т Независимости, 13',
                    '15000',
                )
            ],
            '''«Тепло» ( Виктор Аслюк, Беларусь, 2012, документальный , 21 мин )
Это немного странное место, где зимой, среди сугробов и замерзших ледяных водопадов, очень тепло. Мужчины и женщины полуодетые, разгоряченные. Их движения у станков совершенны – быстрые, ритмичные, точные, будто танец. Люди на этой фабрике в поселке Смиловичи недалеко от Минска делают валенки, которые потом продаются по всему миру.

«День Трубача» ( Никита Пинигин, Сергей Макаров , Беларусь, 2012, документальный, 26 мин  )
Мало кто знает, что в Беларуси живет и работает человек, имеющий профессию, которой нет больше ни у кого во всей стране. Ежедневно, преодолев 120 ступенек, на пожарную каланчу города Гродно взбирается трубач-сигналист, чтобы протрубить полдень. Прежде чем стрелки покажут полдень и начнут бить колокола башенных часов, со своим соло вступает трубач.

«Туфельки» (Константин Фам , Беларусь –Чехия–Россия–США, 2012, драма, 20 мин  )
История начинается в витрине модного магазина  и заканчивается в братской могиле обуви в концлагере Освенцим. Главная героиня фильма – еврейская девушка из провинциального европейского городка. История ее юности, романтической любви, счастливой семейной жизни и трагической гибели под каблуком фашизма – является сюжетом фильма. '''
        ),
    ]
    return Program(title, description, parts)



_programs = {
    'animation': _get_program_animation(),
    'bel': _get_program_bel(),
    'gender': _get_program_gender(),
    'docs': _get_program_docs(),
    'good': _get_program_good(),
    'competition': _get_program_competition(),
    'youth': _get_program_youth(),
    'pierre_luc': _get_program_pierre_luc(),
    'experimental': _get_program_experimental(),
    'urban': _get_program_urban(),
    'bvc': _get_program_bvc(),
}
programs = sorted(_programs.iteritems(), key=lambda x: x[1][0])

get_program = lambda program_id: _programs.get(program_id)


