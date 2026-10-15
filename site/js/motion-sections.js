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

  // --------------------------------------------------------------------------
  // 02. Serviços Section (#servicos)
  // --------------------------------------------------------------------------
  function initSectionServices() {
    const services = document.getElementById('servicos');
    if (!services || typeof gsap === 'undefined') return;

    const M = window.TropicalMotion || { mode: 'full', quality: 'high' };
    const title = services.querySelector('.section-title');
    const cards = services.querySelectorAll('.service-pill-card');

    if (M.mode === 'reduced') {
      gsap.set([title, ...cards], { opacity: 1, y: 0, clearProps: 'all' });
      return;
    }

    if (typeof ScrollTrigger === 'undefined') {
      gsap.from([title, ...cards], { opacity: 0, y: 25, duration: 0.6, stagger: 0.1, clearProps: 'all' });
      return;
    }

    // Timeline disparada a 35% de visibilidade (start: 'top 65%')
    const tl = gsap.timeline({
      scrollTrigger: {
        trigger: services,
        start: 'top 65%',
        toggleActions: 'play none none none',
        once: true
      },
      defaults: { ease: 'power2.out' }
    });

    if (title) {
      tl.from(title, {
        y: 25,
        opacity: 0,
        duration: 0.65,
        clearProps: 'transform,opacity'
      }, 0);
    }

    if (cards.length > 0) {
      tl.from(cards, {
        y: 40,
        opacity: 0,
        duration: 0.75,
        stagger: 0.14,
        clearProps: 'transform,opacity'
      }, 0.15);
    }

    // Parallax suave entre os 3 cards (somente em Quality HIGH e desktop)
    if (M.quality === 'high' && M.mode === 'full' && cards.length === 3 && window.innerWidth >= 820) {
      gsap.to(cards[1], {
        y: -12,
        ease: 'none',
        scrollTrigger: {
          trigger: services,
          start: 'top 70%',
          end: 'bottom 20%',
          scrub: 1
        }
      });
      gsap.to([cards[0], cards[2]], {
        y: 8,
        ease: 'none',
        scrollTrigger: {
          trigger: services,
          start: 'top 70%',
          end: 'bottom 20%',
          scrub: 1
        }
      });
    }

    console.log('[Motion] Seção 02: Serviços inicializada com sucesso.');
  }

  // --------------------------------------------------------------------------
  // 03. Super Mercado Pet Section (#produtos)
  // --------------------------------------------------------------------------
  function initSectionProducts() {
    const products = document.getElementById('produtos');
    if (!products || typeof gsap === 'undefined') return;

    const M = window.TropicalMotion || { mode: 'full', quality: 'high' };
    const title = products.querySelector('.section-title');
    const showcaseMedia = products.querySelector('.showcase-media-side');
    const showcaseContent = products.querySelector('.showcase-content-side');
    const miniCards = products.querySelectorAll('.product-mini-column');

    if (M.mode === 'reduced') {
      gsap.set([title, showcaseMedia, showcaseContent, ...miniCards], {
        opacity: 1,
        x: 0,
        y: 0,
        clearProps: 'all'
      });
      return;
    }

    if (typeof ScrollTrigger === 'undefined') {
      gsap.from([title, showcaseMedia, showcaseContent, ...miniCards], {
        opacity: 0,
        y: 25,
        duration: 0.6,
        stagger: 0.08,
        clearProps: 'all'
      });
      return;
    }

    // Timeline disparada a 35% de visibilidade (start: 'top 65%')
    const tl = gsap.timeline({
      scrollTrigger: {
        trigger: products,
        start: 'top 65%',
        toggleActions: 'play none none none',
        once: true
      },
      defaults: { ease: 'power2.out' }
    });

    if (title) {
      tl.from(title, {
        y: 25,
        opacity: 0,
        duration: 0.65,
        clearProps: 'transform,opacity'
      }, 0);
    }

    if (showcaseMedia) {
      tl.from(showcaseMedia, {
        x: -30,
        opacity: 0,
        duration: 0.75,
        clearProps: 'transform,opacity'
      }, 0.12);
    }

    if (showcaseContent) {
      tl.from(showcaseContent, {
        x: 25,
        opacity: 0,
        duration: 0.75,
        clearProps: 'transform,opacity'
      }, 0.2);
    }

    if (miniCards.length > 0) {
      tl.from(miniCards, {
        y: 35,
        opacity: 0,
        duration: 0.65,
        stagger: 0.1,
        clearProps: 'transform,opacity'
      }, 0.35);
    }

    // Micro-flutuação no showcase principal de rações (quality HIGH)
    const showcaseImg = products.querySelector('.showcase-hero-img');
    if (showcaseImg && M.quality === 'high' && M.mode === 'full') {
      const showcaseFloat = gsap.to(showcaseImg, {
        y: -5,
        duration: 3.2,
        ease: 'sine.inOut',
        yoyo: true,
        repeat: -1,
        paused: false
      });
      showcaseImg._motionLoopTween = showcaseFloat;
      if (M.registerLoop) M.registerLoop(showcaseImg, { type: 'float' });
    }

    // Parallax suave entre os 4 mini produtos (quality HIGH e desktop)
    if (M.quality === 'high' && M.mode === 'full' && miniCards.length === 4 && window.innerWidth >= 768) {
      gsap.to([miniCards[0], miniCards[2]], {
        y: -8,
        ease: 'none',
        scrollTrigger: {
          trigger: products,
          start: 'top 60%',
          end: 'bottom 15%',
          scrub: 1
        }
      });
      gsap.to([miniCards[1], miniCards[3]], {
        y: 8,
        ease: 'none',
        scrollTrigger: {
          trigger: products,
          start: 'top 60%',
          end: 'bottom 15%',
          scrub: 1
        }
      });
    }

    console.log('[Motion] Seção 03: Produtos inicializada com sucesso.');
  }

  // --------------------------------------------------------------------------
  // 04. Avaliações Section (#avaliacoes)
  // --------------------------------------------------------------------------
  function initSectionReviews() {
    const reviews = document.getElementById('avaliacoes');
    if (!reviews || typeof gsap === 'undefined') return;

    const M = window.TropicalMotion || { mode: 'full', quality: 'high' };
    const title = reviews.querySelector('.reviews-main-title');
    const bubbles = reviews.querySelectorAll('.speech-bubble-mock');
    const goldenPhoto = reviews.querySelector('.pet-photo-frame-center');
    const labradorPolaroid = reviews.querySelector('.polaroid-inner');

    if (M.mode === 'reduced') {
      gsap.set([title, ...bubbles, goldenPhoto, labradorPolaroid], {
        opacity: 1,
        y: 0,
        scale: 1,
        clearProps: 'all'
      });
      return;
    }

    if (typeof ScrollTrigger === 'undefined') {
      gsap.from([title, ...bubbles, goldenPhoto, labradorPolaroid], {
        opacity: 0,
        y: 20,
        duration: 0.6,
        stagger: 0.08,
        clearProps: 'all'
      });
      return;
    }

    // Timeline disparada a 35% de visibilidade (start: 'top 65%')
    const tl = gsap.timeline({
      scrollTrigger: {
        trigger: reviews,
        start: 'top 65%',
        toggleActions: 'play none none none',
        once: true
      },
      defaults: { ease: 'power2.out' }
    });

    if (title) {
      tl.from(title, {
        y: 25,
        opacity: 0,
        duration: 0.65,
        clearProps: 'transform,opacity'
      }, 0);
    }

    if (bubbles.length > 0) {
      tl.from(bubbles, {
        scale: 0.88,
        y: 22,
        opacity: 0,
        duration: 0.65,
        stagger: 0.08,
        ease: 'back.out(1.15)',
        clearProps: 'transform,opacity'
      }, 0.15);
    }

    if (goldenPhoto) {
      tl.from(goldenPhoto, {
        scale: 0.82,
        opacity: 0,
        duration: 0.7,
        ease: 'back.out(1.25)',
        clearProps: 'transform,opacity'
      }, 0.3);
    }

    if (labradorPolaroid) {
      tl.from(labradorPolaroid, {
        scale: 0.8,
        rotation: -12,
        opacity: 0,
        duration: 0.75,
        ease: 'back.out(1.3)',
        clearProps: 'opacity'
      }, 0.4);
    }

    // Micro-flutuação e balanço nos retratos dos pets (quality HIGH)
    if (M.quality === 'high' && M.mode === 'full') {
      if (goldenPhoto) {
        const goldenFloat = gsap.to(goldenPhoto, {
          y: -5,
          duration: 3.0,
          ease: 'sine.inOut',
          yoyo: true,
          repeat: -1,
          paused: false
        });
        goldenPhoto._motionLoopTween = goldenFloat;
        if (M.registerLoop) M.registerLoop(goldenPhoto, { type: 'float' });
      }

      if (labradorPolaroid) {
        const polaroidSway = gsap.to(labradorPolaroid, {
          rotation: -2.5,
          y: -4,
          duration: 3.6,
          ease: 'sine.inOut',
          yoyo: true,
          repeat: -1,
          paused: false
        });
        labradorPolaroid._motionLoopTween = polaroidSway;
        if (M.registerLoop) M.registerLoop(labradorPolaroid, { type: 'sway' });
      }
    }

    // Parallax suave entre os balões de fala superiores e inferiores (desktop)
    if (M.quality === 'high' && M.mode === 'full' && bubbles.length >= 6 && window.innerWidth >= 860) {
      const topBubbles = [bubbles[0], bubbles[1], bubbles[2]];
      const bottomBubbles = [bubbles[3], bubbles[4], bubbles[5]];

      gsap.to(topBubbles, {
        y: -10,
        ease: 'none',
        scrollTrigger: {
          trigger: reviews,
          start: 'top 70%',
          end: 'bottom 20%',
          scrub: 1
        }
      });

      gsap.to(bottomBubbles, {
        y: 10,
        ease: 'none',
        scrollTrigger: {
          trigger: reviews,
          start: 'top 70%',
          end: 'bottom 20%',
          scrub: 1
        }
      });
    }

    console.log('[Motion] Seção 04: Avaliações inicializada com sucesso.');
  }

  // Inicializar quando o DOM e Motion Core estiverem prontos
  function init() {
    initSectionHero();
    initSectionServices();
    initSectionProducts();
    initSectionReviews();
  }

  window.TropicalSectionsMotion = {
    initHero: initSectionHero,
    initServices: initSectionServices,
    initProducts: initSectionProducts,
    initReviews: initSectionReviews,
    init: init
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
