/* Must run in <head> BEFORE any Supabase client can consume the callback URL. */
(function () {
  'use strict';
  var query = new URLSearchParams(location.search);
  var hash = new URLSearchParams(location.hash.slice(1));
  var type = hash.get('type') || query.get('type');
  var pending = '';
  try { pending = sessionStorage.getItem('flw-password-pending') || ''; } catch (_) {}
  var isCallback = type === 'invite' || type === 'recovery';
  var hasError = hash.has('error') || query.has('error');
  if (isCallback || hasError || pending) {
    window.flwAuthRedirecting = true;
    if (isCallback) {
      try {
        sessionStorage.setItem('flw-password-pending', type);
        sessionStorage.removeItem('flw-password-user');
      } catch (_) {}
    }
    location.replace('/password-setup.html' + location.search + location.hash);
  }
})();
