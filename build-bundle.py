# -*- coding: utf-8 -*-
"""Spleiser de seks sidene til én selvstendig fil med hash-ruter.

Flersidesversjonen i repo-rota er kanonisk: ekte URL-er, virker uten
JavaScript, og hvert dokument kan deles for seg. Denne bundelen er en
komplett kopi i én fil, til bruk der bare én fil kan leveres.

Kjør:  python build-bundle.py
Ut:    dist/sekstisju-protokollen.html   frittstående dokument
       dist/artifact.html                samme innhold uten doctype/head,
                                         for publisering som Artifact
"""
import io, os, re

D = os.path.dirname(os.path.abspath(__file__))
SIDER = [
    ('index.html', 'protokollen', 'Protokollen'),
    ('avvik.html', 'avvik', 'Avviksklasser'),
    ('litteratur.html', 'litteratur', 'Litteratur'),
    ('masteroppgave.html', 'masteroppgave', 'Masteroppgave'),
    ('arkiv.html', 'arkiv', 'Arkiv'),
    ('instituttet.html', 'instituttet', 'Instituttet'),
]
RUTE = {fil: rute for fil, rute, _ in SIDER}

FAVICON = ("<link rel=\"icon\" href=\"data:image/svg+xml,"
           "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Ccircle cx='16' cy='16' r='14.5' fill='none' stroke='%23CF4520' stroke-width='2'/%3E"
           "%3Ctext x='16' y='21.5' font-family='Arial,Helvetica,sans-serif' font-size='13'"
           " font-weight='700' text-anchor='middle' fill='%23CF4520'%3E67%3C/text%3E"
           "%3C/svg%3E\">")


def les(navn):
    return io.open(os.path.join(D, navn), encoding='utf-8').read()


def kropp(s):
    """Innholdet mellom <body> og </body>, uten navigasjon og delt skript."""
    b = re.search(r'<body>(.*)</body>', s, re.S).group(1)
    b = re.sub(r'  <nav class="docnav">.*?  </nav>\n', '', b, count=1, flags=re.S)
    b = re.sub(r'\s*<script src="assets/base\.js"[^>]*></script>', '', b)
    return b.strip('\n')


def lenker_om(b):
    """side.html -> #/rute, og kryssenker til data-anchor."""
    def bytt(m):
        fil, frag = m.group(1), m.group(2)
        if fil not in RUTE:
            return m.group(0)
        h = 'href="#/%s"' % RUTE[fil]
        if frag:
            h += ' data-anchor="%s"' % frag
        return h
    return re.sub(r'href="([a-z-]+\.html)(?:#([^"]+))?"', bytt, b)


seksjoner = []
for fil, rute, _ in SIDER:
    seksjoner.append(
        '<section class="rute" data-rute="%s"%s>\n%s\n</section>'
        % (rute, '' if rute == 'protokollen' else ' hidden',
           lenker_om(kropp(les(fil))))
    )

nav = ['<nav class="docnav bundlenav">']
for _, rute, navn in SIDER:
    cur = ' aria-current="page"' if rute == 'protokollen' else ''
    nav.append('  <a href="#/%s"%s>%s</a>' % (rute, cur, navn))
nav.append('</nav>')
nav = '\n'.join(nav)

css = les(os.path.join('assets', 'base.css'))
delt_js = les(os.path.join('assets', 'base.js'))

RUTER = '''
(function () {
  var ruter = document.querySelectorAll('.rute');
  var lenker = document.querySelectorAll('.bundlenav a');

  function gjeldende() {
    var h = location.hash.replace(/^#\\//, '');
    for (var i = 0; i < ruter.length; i++) {
      if (ruter[i].getAttribute('data-rute') === h) { return h; }
    }
    return 'protokollen';
  }

  function vis(anker) {
    var r = gjeldende();
    for (var i = 0; i < ruter.length; i++) {
      ruter[i].hidden = ruter[i].getAttribute('data-rute') !== r;
    }
    for (var j = 0; j < lenker.length; j++) {
      if (lenker[j].getAttribute('href') === '#/' + r) {
        lenker[j].setAttribute('aria-current', 'page');
      } else {
        lenker[j].removeAttribute('aria-current');
      }
    }
    var mal = anker && document.getElementById(anker);
    if (mal) { mal.scrollIntoView(); } else { window.scrollTo(0, 0); }
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest ? e.target.closest('a[href^="#/"]') : null;
    if (!a) { return; }
    var anker = a.getAttribute('data-anchor');
    if (a.getAttribute('href') === location.hash) {
      e.preventDefault();
      vis(anker);
      return;
    }
    window.__anker = anker;
  });

  window.addEventListener('hashchange', function () {
    var a = window.__anker;
    window.__anker = null;
    vis(a);
  });

  vis(null);
})();
'''

TITTEL = '<title>Sekstisju-protokollen</title>'
BESKR = ('<meta name="description" content="Kalibreringssertifikat for tallet 67, '
         'med avviksklasser, litteraturregister, masteroppgave og arkiv.">')

innhold = (
    '<div class="doc">\n' + nav + '\n</div>\n'
    + '\n'.join(seksjoner) + '\n'
    + '<script>\n' + delt_js.strip() + '\n</script>\n'
    + '<script>' + RUTER + '</script>\n'
)
stil = '<style>\n' + css + '\n.rute[hidden]{display:none !important}\n</style>'

# ---- frittstående dokument ----
standalone = '\n'.join([
    '<!DOCTYPE html>', '<html lang="nb">', '<head>',
    '<meta charset="utf-8">',
    '<meta name="viewport" content="width=device-width, initial-scale=1">',
    FAVICON, TITTEL, BESKR, stil, '</head>', '<body>', '',
]) + innhold + '\n</body>\n</html>\n'

# ---- artifact-variant: innpakningen legger selv på doctype og head ----
artifact = TITTEL + '\n' + stil + '\n' + innhold

os.makedirs(os.path.join(D, 'dist'), exist_ok=True)
for navn, tekst in [('sekstisju-protokollen.html', standalone),
                    ('artifact.html', artifact)]:
    io.open(os.path.join(D, 'dist', navn), 'w',
            encoding='utf-8', newline='\n').write(tekst)
    print('dist/%-28s %.1f KB' % (navn, len(tekst.encode()) / 1024))

# ---- kontroll ----
for tekst, navn in [(standalone, 'standalone'), (artifact, 'artifact')]:
    for _, rute, _ in SIDER:
        assert 'data-rute="%s"' % rute in tekst, '%s mangler rute %s' % (navn, rute)
    assert 'assets/base.css' not in tekst, '%s: ekstern CSS gjenstar' % navn
    assert 'assets/base.js' not in tekst, '%s: eksternt skript gjenstar' % navn
    assert re.search(r'href="[a-z-]+\.html"', tekst) is None, \
        '%s: ubehandlet sidelenke' % navn
    assert tekst.count('<script') == 4, \
        '%s: forventet 4 skript, fant %d' % (navn, tekst.count('<script'))
assert '<!DOCTYPE' not in artifact and '<body>' not in artifact, \
    'artifact-varianten skal ikke ha egen innpakning'
print('ruter: %d   kontroll: OK' % len(seksjoner))
