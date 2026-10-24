// Offline-Cache: App-Dateien werden beim ersten Besuch gespeichert, danach läuft die App auch ohne Netz.
// Deine Karten liegen nicht hier, sondern in IndexedDB auf dem Gerät.
const CACHE = 'zoes-karten-v3';
const SHELL = ['./', './index.html', './manifest.webmanifest', './vendor/ts-fsrs.umd.js', './icons/icon-192.png', './icons/icon-180.png'];
self.addEventListener('install', e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL))); self.skipWaiting(); });
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))));
  self.clients.claim();
});
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  // Netz zuerst (damit Updates ankommen), sonst Cache. Schriften von Google werden mit gespeichert.
  e.respondWith(
    fetch(e.request).then(res => {
      const copy = res.clone();
      caches.open(CACHE).then(c => c.put(e.request, copy)).catch(() => {});
      return res;
    }).catch(() => caches.match(e.request).then(r => r || (e.request.mode === 'navigate' ? caches.match('./index.html') : undefined)))
  );
});
