document.getElementById('year') && (document.getElementById('year').textContent = new Date().getFullYear());

const navToggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');
if (navToggle && navLinks) {
  navToggle.addEventListener('click', () => navLinks.classList.toggle('open'));
  navLinks.querySelectorAll('a').forEach(a =>
    a.addEventListener('click', () => navLinks.classList.remove('open'))
  );
}

// Terminal typing effect
const text = 'introduce("Abdul Rehman")';
const typedEl = document.getElementById('typedLine');
const outBlock = document.getElementById('outBlock');
const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

function typeIt() {
  if (!typedEl) return;
  if (prefersReduced) {
    typedEl.textContent = text;
    outBlock && outBlock.classList.add('visible');
    return;
  }
  let i = 0;
  const iv = setInterval(() => {
    typedEl.textContent = text.slice(0, i + 1);
    i++;
    if (i >= text.length) {
      clearInterval(iv);
      setTimeout(() => outBlock && outBlock.classList.add('visible'), 300);
    }
  }, 55);
}
window.addEventListener('load', typeIt);
