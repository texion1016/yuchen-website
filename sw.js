/* 房聯網 PWA：提供安裝資格；不攔截內容，避免快取舊版網站。 */
self.addEventListener('install', function () {
  self.skipWaiting();
});

self.addEventListener('activate', function (event) {
  event.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', function () {
  // 保持網路優先：網站每次開啟都使用最新內容。
});
