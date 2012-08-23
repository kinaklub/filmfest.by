from django.http import HttpResponseRedirect, Http404
from django.conf import settings
from django.utils.translation import check_for_language

def set_language(request, lang_code):
    """
    Redirects from /ru/hello/world/?one=two with setting language
    in cookie and session.

    In case language is not registered in settings.LANGUAGES,
    Http404 will be raised.
    """
    allowed_languages = set(lang[0] for lang in settings.LANGUAGES)
    if lang_code not in allowed_languages:# or not check_for_language(lang_code):
        raise Http404
        
    next = request.get_full_path()[len(lang_code) + 1]
    response = HttpResponseRedirect(next)
    
    if hasattr(request, 'session'):
        request.session['django_language'] = lang_code
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)

    return response

