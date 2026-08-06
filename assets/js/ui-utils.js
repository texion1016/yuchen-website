/* Shared, dependency-free UI helpers for public pages. */
(function () {
  'use strict';

  window.togglePwd = function togglePwd(id, trigger) {
    var input = document.getElementById(id);
    if (!input || !trigger) return;

    var isPassword = input.type === 'password';
    input.type = isPassword ? 'text' : 'password';
    trigger.textContent = isPassword ? '🙈' : '👁';
    trigger.setAttribute('aria-label', isPassword ? '隱藏密碼' : '顯示密碼');
  };
}());
