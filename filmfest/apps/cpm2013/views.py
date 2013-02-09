# -*- coding: utf-8 -*-
import io
import os
import os.path
from hashlib import md5

from django.http import HttpResponse, Http404
from django.views.generic.create_update import create_object
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import loader, RequestContext
from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.core.mail import mail_managers
from django.conf import settings

from apps.cpm2013.models import Submission, NewsEntry, Page,\
     SubmissionFileUpload
from apps.cpm2013.forms import SubmissionForm, FileUploadForm
from apps.cpm2013.tasks import SendSubmissionEmail

def index(request):
    news = NewsEntry.objects.language().order_by('-added_at')[:10]
    return render_to_response(
        'cpm2013/index.html',
        {'news': news},
        context_instance=RequestContext(request),
    )

def submit(request):
    return render_to_response(
        'cpm2013/submit_closed.html',
        context_instance=RequestContext(request),
    )

    form = SubmissionForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        submission = form.save(commit=False)
        submission.submission_language = translation.get_language()
        submission.save()

        SendSubmissionEmail().apply_async(args=[submission])
        
        return render_to_response(
            'cpm2013/submit_done.html',
            {'email': submission.applicant_email},
            context_instance=RequestContext(request),
        )
        
    return render_to_response(
        'cpm2013/submit.html',
        {'form': form},
        context_instance=RequestContext(request),
    )

def page(request, slug):
    base_page = get_object_or_404(Page, slug=slug)
    pages = base_page._meta.translations_model.objects.filter(master=base_page)
    pages = dict((t.language_code, t) for t in pages)

    current_lang = translation.get_language()
    if current_lang in pages:
        page = pages[current_lang]
    else:
        for lang_code in ['en', 'ru', 'be']:
            if lang_code in pages:
                page = pages[lang_code]
                break

    return render_to_response(
        'cpm2013/page.html',
        {'page': page},
        context_instance=RequestContext(request),
    )

class Rules:
    LANGUAGES = {
        'be': 'rules_ru.md',
        'ru': 'rules_ru.md',
        'en': 'rules_en.md',

        'ar': 'rules_ar.md',
        'cn': 'rules_cn.md',
        'de': 'rules_de.md',
        'es': 'rules_es.md',
        'fr': 'rules_fr.md',
        'it': 'rules_it.md',
        'pl': 'rules_pl.md',
        'pt': 'rules_pt.md',
    }
    RTL = set(('ar',))

    PATH = os.path.join(settings.PROJECT_ROOT, 'apps', 'cpm2013', 'docs')

    @classmethod
    def translation(cls, lang):
        if lang is None:
            lang = translation.get_language()

        lang = lang.lower()
        if lang not in cls.LANGUAGES:
            lang = 'en'

        rules = os.path.join(cls.PATH, cls.LANGUAGES[lang])
        rtl = lang in cls.RTL

        return lang, rules, rtl

    def __call__(self, request, lang=None):
        lang, rules_filename, rtl = self.translation(lang)
        rules = io.open(
            rules_filename,
            'r', encoding='utf-8'
        ).read()
        return render_to_response(
            'cpm2013/rules.html',
            {
                'rules': rules,
                'rtl': rtl,
                'current_lang': lang,
                'languages': sorted(self.LANGUAGES.iterkeys()),
            },
            context_instance=RequestContext(request),
        )
rules = Rules()

def partners(request):
    img_dir = '/static/cpm2013/banners/'
    main_banners = [
        (
            img_dir + 'where450.png',
            'http://www.spn.ru/publishing/whereminsk/',
            'Where Minsk'
        ),
        (
            img_dir + 'relax450.png',
            'http://relax.by/',
            'relax.by - развлечения в Минске, развлекательные центры столицы'
        ),

    ]
    banners = [
        (
            img_dir + 'lamora.png',
            'http://la-mora.info/',
            'Арт-пространство ДК «La мора»'
        ),        (
            img_dir + 'bvc.png',
            'http://www.belvc.by/',
            'Белорусский видеоцентр'
        ),
        (
            img_dir + 'minsk24dok.png',
            'http://mtis.tv/',
            'Минск 24 ДОК'
        ),
        (
            img_dir + 'paramonak.png',
            'http://paramonak.by/',
            'Креативное агенство Парамонак'
        ),
        (
            img_dir + 'kinolife.png',
            'http://kinolife.eu/',
            'Film & TV Online Platform'
        ),
        (
            img_dir + 'iysff.png',
            'http://www.makesilentfilm.com/',
            'International Youth Silent Film Festival'
        ),
        (
            img_dir + 'luma.png',
            'http://luma.net.my/',
            'LUMA – a creative hub for the media arts'
        ),
        (
            img_dir + 'euroradio.png',
            'http://euroradio.fm/',
            'Последние новости политики и культуры Беларуси - Euroradio'
        ),
        (
            img_dir + 'bolshoi.png',
            'http://bolshoi.by/',
            'Журнал "Большой"'
        ),
        (
            img_dir + 'minchanka.png',
            'http://www.minchanka.by/',
            'Минчанка: быть женщиной - это интересно!'
        ),
        (
            img_dir + 'open.png',
            'http://open.by/',
            'Интернет-портал OPEN.BY'
        ),
        (
            img_dir + 'mart.png',
            'http://mart.by/',
            'Современное белорусское искусство'
        ),
        (
            img_dir + 'vgomele.png',
            'http://vgomele.by/',
            'vGomele.by - гомельский информационно-развлекательный портал'
        ),
        (
            img_dir + 'belarusdigest.png',
            'http://belarusdigest.com/',
            'Беларусы за мяжой'
        ),
        (
            img_dir + 'ky.png',
            'http://kyky.org/',
            'KYKY.ORG - Культурный портал'
        ),
        (
            img_dir + 'nomadic.png',
            'http://vagrant.kinaklub.org/',
            'Nomadic Film Club'
        ),
    ]
    return render_to_response(
        'cpm2013/partners.html',
        {'main_banners': main_banners, 'banners': banners},
        context_instance=RequestContext(request),
    )

def submission_info(request, subm_id, subm_hash):
    submission = get_object_or_404(Submission, id=subm_id)

    real_hash = md5('%s%s' % (settings.SECRET_KEY, subm_id)).hexdigest()
    if real_hash != subm_hash:
        return HttpResponse('Forbidden', status=403)

    file_uploads = SubmissionFileUpload.objects.filter(submission=submission)
        
    return render_to_response(
        'cpm2013/submission_info.html',
        {
            'submission': submission,
            'files': list(file_uploads),
            'subm_hash': subm_hash
        },
        context_instance=RequestContext(request),
    )

def submission_info_upload(request, subm_id, subm_hash):
    submission = get_object_or_404(Submission, id=subm_id)

    real_hash = md5('%s%s' % (settings.SECRET_KEY, subm_id)).hexdigest()
    if real_hash != subm_hash:
        return HttpResponse('Forbidden', status=403)

    form = FileUploadForm(request.POST or None, request.FILES or None)
    error = ''
    if request.method == 'POST' and form.is_valid():
        uploaded_file = form.cleaned_data['file']

        name, ext = os.path.splitext(uploaded_file.name)
        real_name = md5(
            '%s%s' % (settings.SECRET_KEY, uploaded_file.name)
        ).hexdigest() + ext
        subm_file_upload = SubmissionFileUpload(
            submission=submission,
            display_name=name + ext,
            real_name=real_name
        )

        real_path = os.path.join(settings.MEDIA_ROOT, real_name)
        if not os.path.exists(real_path):
            with open(real_path, 'w') as f:
                buf = uploaded_file.read(4096)
                while buf:
                    f.write(buf)
                    buf = uploaded_file.read(4096)

            subm_file_upload.save()
            mail_managers(
                'CPM2013: new file upload',
                '%s at %s' % (
                    uploaded_file.name,
                    request.build_absolute_uri(reverse(
                        'cpm2013:submission_info',
                        args=[subm_id, subm_hash]
                    )),
                )
            )

            return redirect('cpm2013:submission_info', subm_id, subm_hash)

        error = _('File with such name exists')

    return render_to_response(
        'cpm2013/submission_info_upload.html',
        {'submission': submission, 'form': form, 'error': error},
        context_instance=RequestContext(request),
    )

def press_kit(request):
    programs
    return render_to_response(
        'cpm2013/press_kit.html', {},
        context_instance=RequestContext(request),
    )

def programs(request):
    from apps.cpm2013.programs import programs

    return render_to_response(
        'cpm2013/programs.html', {'programs': programs},
        context_instance=RequestContext(request),
    )
    
def program(request, program_id):
    from apps.cpm2013.programs import get_program

    program = get_program(program_id)
    if program is None:
        raise Http404
    
    return render_to_response(
        'cpm2013/program.html',
        {
            'title': program.title,
            'description': program.description,
            'parts': program.parts,
        },
        context_instance=RequestContext(request),
    )
