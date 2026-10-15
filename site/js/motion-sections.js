/**
 * motion-sections.js — Animações por Seção da Tropical Pet Shop
 * Regras: Apenas transform/opacity em nós folha.
 * Respeita TropicalMotion.mode ('full', 'reduced', 'paused') e TropicalMotion.quality ('high', 'low').
 */

(function () {
  'use strict';

  function initSectionHero() {
    const hero = document.getElementById('hero');
    if (!hero || typeof gsap === 'undefined') return;

    const M = window.TropicalMotion || { mode: 'full', quality: 'high' };

    // Se preferência for reduced motion: apenas garantir visibilidade limpa imediata
    if (M.mode === 'reduced') {
      gsap.set(['#hero .hero-heading span', '#hero .hero-subtext', '#hero .hero-dog-jumping', '#hero .badge-delivery'], {
        opacity: 1,
        y: 0,
        scale: 1,
        clearProps: 'all'
      });
      return;
    }

    // 1. Entrance Timeline do Hero (dispara logo na carga)
    const tl = gsap.timeline({
      defaults: { ease: 'power2.out' }
    });

    const headingLines = hero.querySelectorAll('.hero-heading span');
    const subtext = hero.querySelector('.hero-subtext');
    const dog = hero.querySelector('.hero-dog-jumping');
    const badge = hero.querySelector('.badge-delivery');

    // Começar a partir de offsets suaves sem esconder nada permanentemente
    tl.from(headingLines, {
      y: 28,
      opacity: 0,
      duration: 0.75,
      stagger: 0.12,
      clearProps: 'transform,opacity'
    }, 0.1);

    if (subtext) {
      tl.from(subtext, {
        y: 20,
        opacity: 0,
        duration: 0.65,
        clearProps: 'transform,opacity'
      }, 0.35);
    }

    if (dog) {
      tl.from(dog, {
        y: 42,
        scale: 0.94,
        opacity: 0,
        duration: 0.85,
        ease: 'back.out(1.15)',
        clearProps: 'transform,opacity'
      }, 0.2);
    }

    if (badge) {
      tl.from(badge, {
        scale: 0.7,
        opacity: 0,
        duration: 0.6,
        ease: 'back.out(1.35)',
        clearProps: 'transform,opacity'
      }, 0.45);
    }

    // 2. Flutuação Contínua (Somente em Quality HIGH e enquanto na tela)
    if (M.quality === 'high' && M.mode === 'full') {
      if (badge) {
        const badgeFloat = gsap.to(badge, {
          y: -7,
          duration: 2.6,
          ease: 'sine.inOut',
          yoyo: true,
          repeat: -1,
          paused: false
        });
        badge._motionLoopTween = badgeFloat;
        if (M.registerLoop) M.registerLoop(badge, { type: 'float' });
      }

      if (dog) {
        const dogFloat = gsap.to(dog, {
          y: -5,
          duration: 3.4,
          ease: 'sine.inOut',
          yoyo: true,
          repeat: -1,
          paused: false
        });
        dog._motionLoopTween = dogFloat;
        if (M.registerLoop) M.registerLoop(dog, { type: 'float' });
      }
    }

    // 3. Parallax Sutil de Rolagem (0.05 a 0.08)
    if (typeof ScrollTrigger !== 'undefined' && M.quality === 'high' && M.mode === 'full') {
      if (dog) {
        gsap.to(dog, {
          yPercent: 12,
          ease: 'none',
          scrollTrigger: {
            trigger: hero,
            start: 'top top',
            end: 'bottom top',
            scrub: true
          }
        });
      }

      if (badge) {
        gsap.to(badge, {
          yPercent: -15,
          ease: 'none',
          scrollTrigger: {
            trigger: hero,
            start: 'top top',
            end: 'bottom top',
            scrub: true
          }
        });
      }
    }

    console.log('[Motion] Seção 01: Hero inicializada com sucesso.');
  }

  // Inicializar quando o DOM e Motion Core estiverem prontos
  function init() {
    initSectionHero();
  }

  window.TropicalSectionsMotion = {
    initHero: initSectionHero,
    init: init
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
