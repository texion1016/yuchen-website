# -*- coding: utf-8 -*-
# fix12.py - 密碼欄位加眼睛圖示

with open('C:/Users/ROG/yuchen-website/index.html', encoding='utf-8') as f:
    html = f.read()

# 1. 加 CSS
EYE_CSS = """
/* 密碼眼睛 */
.pwd-wrap { position: relative; }
.pwd-wrap input { padding-right: 2.8rem !important; }
.pwd-eye {
  position: absolute; right: .8rem; top: 50%; transform: translateY(-50%);
  cursor: pointer; color: var(--ink-dim); font-size: 1.1rem;
  user-select: none; transition: color .2s;
}
.pwd-eye:hover { color: var(--cyan); }
"""
html = html.replace('</style>', EYE_CSS + '\n</style>', 1)

# 2. 包裝登入密碼欄
html = html.replace(
    '<div class="bov-field"><label>密碼</label><input type="password" id="loginPwd" placeholder="••••••••" /></div>',
    '''<div class="bov-field"><label>密碼</label><div class="pwd-wrap">
      <input type="password" id="loginPwd" placeholder="••••••••" />
      <span class="pwd-eye" onclick="togglePwd('loginPwd',this)">👁</span>
    </div></div>''',
    1
)

# 3. 包裝申請密碼欄
html = html.replace(
    '<div class="bov-field"><label>設定密碼 *</label><input type="password" id="regPwd" placeholder="至少 8 個字元" /></div>',
    '''<div class="bov-field"><label>設定密碼 *</label><div class="pwd-wrap">
      <input type="password" id="regPwd" placeholder="至少 8 個字元" />
      <span class="pwd-eye" onclick="togglePwd(\'regPwd\',this)">👁</span>
    </div></div>''',
    1
)

# 4. 加 togglePwd JS（插在 </script> 前，bov script 區塊內）
TOGGLE_JS = """
function togglePwd(id, el) {
  const inp = document.getElementById(id);
  if (inp.type === 'password') { inp.type = 'text'; el.textContent = '🙈'; }
  else { inp.type = 'password'; el.textContent = '👁'; }
}
"""
# 插在第一個 </script> 之前（bov script 裡）
html = html.replace('</script>', TOGGLE_JS + '</script>', 1)

with open('C:/Users/ROG/yuchen-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("done.")
