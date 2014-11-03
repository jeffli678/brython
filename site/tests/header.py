# -*- coding: utf-8 -*-


from browser import document as doc
from browser.html import *


# github.com/simonwhitaker/github-fork-ribbon-css
GITHUB_FORKME_SNIPPET = """<a href="#top"></a>
<div class="github-fork-ribbon-wrapper right-bottom">
<div class="github-fork-ribbon">
<a target=_blank href="//github.com/brython-dev/brython">Fork me on GitHub</a>
</div></div>"""


trans_menu = {
    'menu_console': {
        'en': 'Console',
        'es': 'Consola',
        'fr': 'Console',
        'pt': 'Console'},
    'menu_editor': {
        'en': 'Editor',
        'es': 'Editor',
        'fr': 'Editeur',
        'pt': 'Editor'},
    'menu_gallery': {
        'en': 'Gallery',
        'es': 'Galería',
        'fr': 'Galerie',
        'pt': 'Galeria'},
    'menu_doc': {
        'en': 'Documentation',
        'es': 'Documentación',
        'fr': 'Documentation',
        'pt': 'Documentação'},
    'menu_download': {
        'en': 'Download',
        'es': 'Descargas',
        'fr': 'Téléchargement',
        'pt': 'Download'},
    'menu_dev': {
        'en': 'Development',
        'es': 'Desarrollo',
        'fr': 'Développement',
        'pt': 'Desenvolvimento'},
    'menu_groups': {
        'en': 'Groups',
        'es': 'Grupos',
        'fr': 'Groupes',
        'pt': 'Grupos'}
}


links = {'home': 'index.html',
         'console': 'tests/console.html',
         'editor': 'tests/editor.html',
         'gallery': 'gallery/gallery_%s.html',
         'doc': 'doc/%s/index.html',
         'download': 'https://github.com/brython-dev/brython/releases',
         'dev': 'https://github.com/brython-dev/brython',
         'groups': 'groups.html'
         }


def show(prefix=''):
    # detect language
    language = "en"  # default
    has_req = False

    qs_lang = doc.query.getfirst("lang")
    if qs_lang and qs_lang in ["en", "fr", "es", "pt"]:
        has_req = True
        language = qs_lang
    else:
        import locale
        try:
            lang, enc = locale.getdefaultlocale()
            lang = lang[:2]
            if lang in ("en", "fr", "es", "pt"):
                language = lang
        except:
            pass

    _banner = doc['banner_row']
    _banner.html = GITHUB_FORKME_SNIPPET

    for key in['home', 'console', 'editor', 'gallery',
               'doc', 'download', 'dev', 'groups']:
        if key in ('download', 'dev'):
            href = links[key]
        else:
            href = prefix + links[key]
        if key in ('doc', 'gallery'):
            href = href % language
        if has_req and key not in ('download', 'dev'):
            # add lang to href
            href += '?lang=%s' % language
        if key == 'home':
            img = IMG(src=prefix + "brython_white.png", Class="logo",
                      alt="Brython Logo", title="Brython")
            link = A(img, href=href)
            cell = TD(link, Class="logo")
        else:
            link = A(trans_menu['menu_%s' % key][language],
                     href=href, Class="banner")
            cell = TD(link)
        if key in ('download', 'dev'):
            link.target = "_blank"
        _banner <= cell
    return qs_lang, language

