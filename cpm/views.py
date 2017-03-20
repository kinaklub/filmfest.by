# -*- coding: utf-8 -*-

from django.http import HttpResponseForbidden, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

from cpm.forms import ScreeningPlaceProposalForm


def angular(request):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    return render_to_response(
        'cpm/angular.html', {}, context_instance=RequestContext(request)
    )


def new_screening_place(request):
    form = ScreeningPlaceProposalForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render_to_response(
            'cpm/new_screening_place_done.html',
            {'form': form},
            context_instance=RequestContext(request)
        )
    return render_to_response(
        'cpm/new_screening_place.html',
        {'form': form},
        context_instance=RequestContext(request)
    )


def partners(request):
    img_dir = '/static/cpm/partners/'
    banners_info = [
        (
            img_dir + 'info/34.jpg',
            'http://34mag.net/',
            '34mag.net – інтэрнэт-часопіс з Беларусі'
        ),
        (
            img_dir + 'info/afishatut.jpg',
            'http://afisha.tut.by',
            'Афиша Минска и Беларуси'
        ),
        (
            img_dir + 'info/belarus2.jpg',
            'http://www.belarus2.by/',
            'Телеканал Беларусь 2'
        ),
        (
            img_dir + 'info/citydog.jpg',
            'http://citydog.by/',
            'citydog.by - журнал о Минске'
        ),
        (
            img_dir + 'info/cultura.jpg',
            'http://www.tvr.by/radio/kanal-kultura/',
            'Канал "Культура" Белорусского радио'
        ),
        (
            img_dir + 'info/festevalibelarusi.jpg',
            'http://vk.com/fest_by',
            'Фестивали Беларуси'
        ),
        (
            img_dir + 'info/generationby.jpg',
            'http://generation.by/',
            'Generation.by'
        ),
        (
            img_dir + 'info/kaktutjit.jpg',
            'http://kaktutzhit.by/',
            'Как тут жить.'
        ),
        (
            img_dir + 'info/kultprosvet.jpg',
            'http://kultprosvet.by/',
            'Культпросвет - интернет-журнал о театре и взаимодействии искусств'
        ),
        (
            img_dir + 'info/logoIP.jpg',
            'http://www.instpol.by/',
            'Польскі Інстытут'
        ),
        (
            img_dir + 'info/metalscript.jpg',
            'http://metalscript.net/',
            'Metalscript.Net'
        ),
        (
            img_dir + 'info/minchane.jpg',
            'http://minchane.by/',
            'Минчане'
        ),
        (
            img_dir + 'info/minsk24dok.jpg',
            'http://mtis.tv/',
            'Минск 24 ДОК'

        ),
        (
            img_dir + 'info/minskwhere.jpg',
            'http://www.spn.ru/publishing/whereminsk/',
            'Where Minsk'
        ),
        (
            img_dir + 'info/radiusfm.jpg',
            'http://www.radiusfm.by/',
            'Радиус-FM'
        ),
        (
            img_dir + 'info/relax.jpg',
            'http://relax.by/',
            'relax.by - развлечения в Минске, развлекательные центры столицы'
        ),
        (
            img_dir + 'info/stolica.jpg',
            'http://radiostalica.by/',
            'Радыё "Сталiца"'
        ),
        (
            img_dir + 'info/talaka.jpg',
            'http://talaka.by/',
            'Talaka.by – некоммерческая платформа, которая помогает активным людям в Беларуси реализовывать значимые для общества проекты'  # noqa
        ),
        (
            img_dir + 'info/vestnikcentralnogo.jpg',
            'http://vk.com/vestnik_centralnogo',
            'Вестник Центрального'
        ),
        (
            img_dir + 'placesinfo/balki.jpg',
            'http://loftbalki.by/',
            'Лофт Проект БАЛКИ'
        ),
        (
            img_dir + 'placesinfo/beetlejuice.jpg',
            '',
            'Кафе Битлджус'
        ),
        (
            img_dir + 'placesinfo/buffet.jpg',
            '',
            ''
        ),
        (
            img_dir + 'placesinfo/graffiti.jpg',
            '',
            ''
        ),
        (
            img_dir + 'placesinfo/graffiti.jpg',
            '',
            ''
        ),
        (
            img_dir + 'placesinfo/guru.jpg',
            '',
            ''
        ),
        (
            img_dir + 'placesinfo/hosteltrinity.jpg',
            '',
            ''
        ),
        (
            img_dir + 'placesinfo/imaguru.jpg',
            '',
            ''
        ),
        (
            img_dir + 'placesinfo/ktotakoyjongolt.jpg',
            '',
            ''
        ),
        (
            img_dir + 'placesinfo/logvinay.jpg',
            '',
            ''
        ),
        (
            img_dir + 'placesinfo/pen.jpg',
            '',
            ''
        ),
        (
            img_dir + 'placesinfo/polygon.jpg',
            '',
            ''
        ),
        (
            img_dir + 'placesinfo/tnt.jpg',
            '',
            ''
        ),
        (
            img_dir + 'placesinfo/ybar.jpg',
            '',
            ''
        ),
        (
            img_dir + 'placesinfo/zerno.jpg',
            '',
            ''
        ),
    ]
    banners_places = [
        (
            img_dir + 'places/artcorporation.jpg',
            '',
            ''
        ),
        (
            img_dir + 'places/fialta.jpg',
            '',
            ''
        ),
        (
            img_dir + 'places/kinovideoprokat.jpg',
            '',
            ''
        ),
        (
            img_dir + 'places/korpus8.jpg',
            '',
            ''
        ),
        (
            img_dir + 'places/museibelkino.jpg',
            '',
            ''
        ),
    ]
    banners_fests = [
        (
            img_dir + 'fests/docufest.jpg',
            '',
            ''
        ),
        (
            img_dir + 'fests/dotyk.jpg',
            '',
            ''
        ),
        (
            img_dir + 'fests/nomadic.jpg',
            '',
            ''
        ),
        (
            img_dir + 'fests/opla.jpg',
            '',
            ''
        ),
        (
            img_dir + 'fests/selb.jpg',
            '',
            ''
        ),
        (
            img_dir + 'fests/shortmovieclub.jpg',
            '',
            ''
        ),
        (
            img_dir + 'fests/stoptrik.jpg',
            '',
            ''
        ),
        (
            img_dir + 'fests/zubroffka.jpg',
            '',
            ''
        ),
    ]
    return render_to_response(
        'cpm/partners.html',
        {
            'banners_info': banners_info,
            'banners_places': banners_places,
            'banners_fests': banners_fests,
        },
        context_instance=RequestContext(request),
    )


def news_entry(request, news_id):
    from apps.cpm2014.models import NewsEntry
    try:
        news_entry = NewsEntry.objects.language().get(id=int(news_id))
    except NewsEntry.DoesNotExist:
        raise Http404

    return render_to_response(
        'cpm/news_entry.html',
        {'news_entry': news_entry},
        context_instance=RequestContext(request),
    )
