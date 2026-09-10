/* Delt skriptlag for instituttets sider.
   Alt er valgfritt pynt: sidene virker fullt ut uten dette. */

/* ------------------------------------------------------------------
   1. Åpningstid
   Instituttet holder åpent 06:00-07:00, altså i det eneste tidsrommet
   som i seg selv utgjør en godkjent utløser. Sidene oppgir tidsrommet
   statisk; her legges leserens egen klokke til.
   ------------------------------------------------------------------ */
(function () {
  var ut = document.getElementById('apningsstatus');
  if (!ut) return;

  var UKEDAGER = ['søndag', 'mandag', 'tirsdag', 'onsdag', 'torsdag',
                  'fredag', 'lørdag'];

  function ukedag(d) { return d.getDay() >= 1 && d.getDay() <= 5; }

  /* Neste virkedag klokka 06:00, regnet med Date og ikke med timearitmetikk.
     Hopper over helg, siden seksjonen ikke er bemannet da. */
  function nesteApning(na) {
    var k = new Date(na.getFullYear(), na.getMonth(), na.getDate(), 6, 0, 0, 0);
    if (k <= na) { k.setDate(k.getDate() + 1); }
    while (!ukedag(k)) { k.setDate(k.getDate() + 1); }
    return k;
  }

  function tekst() {
    var na = new Date();
    if (ukedag(na) && na.getHours() === 6) {
      return 'Åpent nå. Stenger om ' + (60 - na.getMinutes()) + ' min.';
    }
    var k = nesteApning(na);
    var minutter = Math.round((k - na) / 60000);
    if (minutter >= 24 * 60) {
      return 'Stengt. Åpner ' + UKEDAGER[k.getDay()] + ' 06:00.';
    }
    return 'Stengt. Åpner om ' + Math.floor(minutter / 60) + ' t '
         + (minutter % 60) + ' min.';
  }

  function vis() { ut.textContent = tekst(); }
  vis();
  setInterval(vis, 30000);
})();

/* ------------------------------------------------------------------
   2. Utløser
   Tallet 67 er en godkjent utløser. Skrives det inn, registrerer
   instituttet ytringen og utsteder klasse A.
   ------------------------------------------------------------------ */
(function () {
  var buffer = '';
  var seddel = null;
  var timer = null;

  function utsted() {
    if (seddel) { return; }
    seddel = document.createElement('div');
    seddel.className = 'kvittering';
    seddel.setAttribute('role', 'status');
    seddel.innerHTML =
      '<span class="k1">Ytring registrert</span>' +
      '<span class="k2">6 7</span>' +
      '<span class="k3">Klasse A &#183; ingen merknad</span>';
    document.body.appendChild(seddel);

    timer = setTimeout(function () {
      seddel.classList.add('bort');
      setTimeout(function () {
        if (seddel && seddel.parentNode) { seddel.parentNode.removeChild(seddel); }
        seddel = null;
      }, 400);
    }, 4200);
  }

  document.addEventListener('keydown', function (e) {
    var t = e.target;
    if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.isContentEditable)) {
      return;
    }
    if (e.key === '6' || e.key === '7') {
      buffer = (buffer + e.key).slice(-2);
      if (buffer === '67') { buffer = ''; utsted(); }
    } else {
      buffer = '';
    }
  });
})();
