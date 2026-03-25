/* CareerGuide — Main JavaScript */
'use strict';

/* ── Theme toggle ─────────────────────────────────────────── */
function _applyThemeIcon() {
    var icon = document.getElementById('themeIcon');
    if (!icon) return;
    var theme = document.documentElement.getAttribute('data-theme') || 'dark';
    icon.textContent = theme === 'dark' ? '\u2600\uFE0F' : '\uD83C\uDF19';
}

function toggleTheme() {
    var html = document.documentElement;
    var current = html.getAttribute('data-theme') || 'dark';
    var next = current === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', next);
    localStorage.setItem('cg-theme', next);
    _applyThemeIcon();
}

document.addEventListener('DOMContentLoaded', function() {
    _applyThemeIcon();

    // Highlight current nav link
    var currentPath = window.location.pathname;
    document.querySelectorAll('.nav-link').forEach(function(link) {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
});
