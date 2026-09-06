(function () {
  'use strict';
  var button = document.getElementById('shareWebsite');
  var status = document.getElementById('shareStatus');
  var url = 'https://yuchen-realty.com/';
  button.addEventListener('click', async function () {
    var payload = { title: '房聯網', text: '建商合作・仲介共享案源・成屋聯合銷售', url: url };
    status.textContent = '';
    document.getElementById('shareFallback').hidden = true;
    button.disabled = true;
    try {
      if (navigator.share && (!navigator.canShare || navigator.canShare(payload))) {
        try { await navigator.share(payload); return; }
        catch (error) { if (error.name === 'AbortError') return; }
      }
      if (!navigator.clipboard) throw new Error('clipboard unavailable');
      await navigator.clipboard.writeText(url);
      status.textContent = '網址已複製，可貼到 LINE、訊息或電子郵件分享。';
    } catch (_) {
      document.getElementById('shareFallback').hidden = false;
      var input = document.getElementById('shareUrl');
      input.focus(); input.select();
      status.textContent = '請複製下方網址後分享。';
    } finally { button.disabled = false; }
  });
  // Password setup has already validated the role; portal entry checks it again.
  if (!window.flwAuthRedirecting) {
    var portal = new URLSearchParams(location.search).get('portal');
    if (portal === 'broker' || portal === 'builder') {
      window.addEventListener('load', function () {
        if (portal === 'broker') openBrokerOverlay();
        else openDevOverlay();
      });
    }
  }
})();
