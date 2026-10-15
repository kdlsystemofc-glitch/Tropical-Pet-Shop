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

    const pillBadge = hero.querySelector('.hero-pill-badge');
    const headingLines = hero.querySelectorAll('.hero-heading span');
    const pawIcon = hero.querySelector('.hero-paw-icon');
    const subtext = hero.querySelector('.hero-subtext');
    const actionsRow = hero.querySelector('.hero-actions-row');
    const dog = hero.querySelector('.hero-dog-jumping');
    const badge = hero.querySelector('.badge-delivery');
    const ambientGlow = hero.querySelector('.hero-ambient-glow');
    const particles = hero.querySelectorAll('.particle');
    const blobWrapper = hero.querySelector('.hero-blob-wrapper');
    const textCol = hero.querySelector('.hero-text-col');

    // Se preferência for reduced motion: apenas garantir visibilidade limpa imediata
    if (M.mode === 'reduced') {
      gsap.set([pillBadge, headingLines, subtext, actionsRow, dog, badge, ambientGlow, particles, blobWrapper, textCol], {
        opacity: 1,
        x: 0,
        y: 0,
        scale: 1,
        rotate: 0,
        clearProps: 'all'
      });
      return;
    }

    // 1. Cinematic Staggered Entrance Timeline
    const tl = gsap.timeline({
      defaults: { ease: 'power3.out' }
    });

    if (pillBadge) {
      tl.from(pillBadge, {
        y: -18,
        scale: 0.88,
        opacity: 0,
        duration: 0.65,
        ease: 'back.out(1.4)'
      }, 0.05);
    }

    if (headingLines.length > 0) {
      tl.from(headingLines, {
        y: 42,
        opacity: 0,
        duration: 0.85,
        stagger: 0.12,
        ease: 'power3.out'
      }, 0.15);
    }

    if (subtext) {
      tl.from(subtext, {
        y: 24,
        opacity: 0,
        duration: 0.7,
        ease: 'power2.out'
      }, 0.38);
    }

    if (actionsRow) {
      tl.from(actionsRow, {
        y: 20,
        opacity: 0,
        duration: 0.7,
        ease: 'power2.out'
      }, 0.48);
    }

    if (ambientGlow) {
      tl.from(ambientGlow, {
        scale: 0.65,
        opacity: 0,
        duration: 1.1,
        ease: 'power2.out'
      }, 0.2);
    }

    if (dog) {
      tl.from(dog, {
        y: 60,
        scale: 1.12,
        rotate: -5,
        opacity: 0,
        duration: 1.05,
        ease: 'power3.out',
        clearProps: 'transform,opacity'
      }, 0.25);
    }

    if (badge) {
      tl.from(badge, {
        scale: 0,
        rotate: -35,
        opacity: 0,
        duration: 0.8,
        ease: 'back.out(1.6)',
        clearProps: 'transform,opacity'
      }, 0.5);
    }

    if (particles.length > 0) {
      tl.from(particles, {
        scale: 0,
        opacity: 0,
        stagger: 0.1,
        duration: 0.6,
        ease: 'back.out(2.0)'
      }, 0.6);
    }

    // 2. Flutuação Orgânica em Camadas (High Quality & Full Mode)
    if (M.quality === 'high' && M.mode === 'full') {
      if (badge) {
        const badgeFloat = gsap.to(badge, {
          y: -8,
          rotate: 2.5,
          duration: 2.7,
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
          y: -6,
          rotate: -0.5,
          duration: 3.5,
          ease: 'sine.inOut',
          yoyo: true,
          repeat: -1,
          paused: false
        });
        dog._motionLoopTween = dogFloat;
        if (M.registerLoop) M.registerLoop(dog, { type: 'float' });
      }

      if (ambientGlow) {
        gsap.to(ambientGlow, {
          scale: 1.08,
          opacity: 0.85,
          duration: 3.2,
          ease: 'sine.inOut',
          yoyo: true,
          repeat: -1
        });
      }

      particles.forEach((part, idx) => {
        gsap.to(part, {
          y: (idx % 2 === 0 ? -12 : -8),
          rotate: (idx % 2 === 0 ? 15 : -15),
          duration: 2.4 + idx * 0.4,
          ease: 'sine.inOut',
          yoyo: true,
          repeat: -1
        });
      });
    }

    // 3. Interactive 3D Mouse Parallax & Cinematic Tilt (Desktop & Fine Pointer)
    const isFinePointer = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
    if (isFinePointer && M.quality === 'high' && M.mode === 'full') {
      let mouseX = 0;
      let mouseY = 0;

      hero.addEventListener('mousemove', (e) => {
        if (M.mode === 'paused') return;
        const rect = hero.getBoundingClientRect();
        mouseX = (e.clientX - rect.left) / rect.width - 0.5;
        mouseY = (e.clientY - rect.top) / rect.height - 0.5;

        if (dog) {
          gsap.to(dog, {
            x: mouseX * 28,
            y: mouseY * 18,
            rotate: -1.5 + mouseX * 3.5,
            duration: 0.9,
            ease: 'power2.out',
            overwrite: 'auto'
          });
        }

        if (badge) {
          gsap.to(badge, {
            x: -mouseX * 42,
            y: -mouseY * 28,
            rotate: -mouseX * 8,
            duration: 0.8,
            ease: 'power2.out',
            overwrite: 'auto'
          });
        }

        if (ambientGlow) {
          gsap.to(ambientGlow, {
            x: mouseX * 32,
            y: mouseY * 22,
            duration: 1.0,
            ease: 'power2.out',
            overwrite: 'auto'
          });
        }

        particles.forEach((part, idx) => {
          const factor = (idx === 0 ? 46 : (idx === 1 ? -32 : 38));
          gsap.to(part, {
            x: mouseX * factor,
            y: mouseY * factor * 0.7,
            duration: 0.8 + idx * 0.1,
            ease: 'power2.out',
            overwrite: 'auto'
          });
        });

        if (blobWrapper) {
          gsap.to(blobWrapper, {
            x: -mouseX * 15,
            y: -mouseY * 10,
            duration: 1.2,
            ease: 'power2.out',
            overwrite: 'auto'
          });
        }
      });

      hero.addEventListener('mouseleave', () => {
        if (dog) gsap.to(dog, { x: 0, y: 0, rotate: -1.5, duration: 1.2, ease: 'power2.out' });
        if (badge) gsap.to(badge, { x: 0, y: 0, rotate: 0, duration: 1.2, ease: 'power2.out' });
        if (ambientGlow) gsap.to(ambientGlow, { x: 0, y: 0, duration: 1.2, ease: 'power2.out' });
        particles.forEach(part => gsap.to(part, { x: 0, y: 0, duration: 1.2, ease: 'power2.out' }));
        if (blobWrapper) gsap.to(blobWrapper, { x: 0, y: 0, duration: 1.4, ease: 'power2.out' });
      });

      // Magnetic Hover Physics no Badge
      if (badge) {
        badge.addEventListener('mousemove', (e) => {
          const bRect = badge.getBoundingClientRect();
          const bX = (e.clientX - bRect.left) - bRect.width / 2;
          const bY = (e.clientY - bRect.top) - bRect.height / 2;
          gsap.to(badge, {
            x: bX * 0.35,
            y: bY * 0.35,
            scale: 1.06,
            duration: 0.3,
            ease: 'power2.out',
            overwrite: 'auto'
          });
        });
        badge.addEventListener('mouseleave', () => {
          gsap.to(badge, {
            x: 0,
            y: 0,
            scale: 1,
            duration: 0.6,
            ease: 'elastic.out(1, 0.4)',
            overwrite: 'auto'
          });
        });
      }

      // Design Spell: Energetic Paw Wiggle on Click/Hover
      if (pawIcon) {
        pawIcon.addEventListener('mouseenter', () => {
          gsap.to(pawIcon, {
            scale: 1.4,
            rotate: 20,
            duration: 0.25,
            ease: 'back.out(2)'
          });
        });
        pawIcon.addEventListener('mouseleave', () => {
          gsap.to(pawIcon, {
            scale: 1,
            rotate: 0,
            duration: 0.4,
            ease: 'elastic.out(1, 0.4)'
          });
        });
      }
    }

    // 4. Multi-Plane Cinematic Scroll Parallax (Scrubbing Depth)
    if (typeof ScrollTrigger !== 'undefined' && M.quality === 'high' && M.mode === 'full') {
      const scrollTl = gsap.timeline({
        scrollTrigger: {
          trigger: hero,
          start: 'top top',
          end: 'bottom top',
          scrub: 0.5
        }
      });

      if (textCol) {
        scrollTl.to(textCol, {
          yPercent: -28,
          opacity: 0.18,
          ease: 'none'
        }, 0);
      }

      if (dog) {
        scrollTl.to(dog, {
          yPercent: 24,
          scale: 1.05,
          ease: 'none'
        }, 0);
      }

      if (badge) {
        scrollTl.to(badge, {
          yPercent: -42,
          rotate: 20,
          opacity: 0.25,
          ease: 'none'
        }, 0);
      }

      if (ambientGlow) {
        scrollTl.to(ambientGlow, {
          yPercent: 18,
          scale: 1.25,
          opacity: 0,
          ease: 'none'
        }, 0);
      }

      if (blobWrapper) {
        scrollTl.to(blobWrapper, {
          yPercent: 14,
          scale: 1.08,
          ease: 'none'
        }, 0);
      }

      if (particles.length > 0) {
        scrollTl.to(particles, {
          yPercent: -65,
          opacity: 0,
          ease: 'none'
        }, 0);
      }
    }

    console.log('[Motion] Seção 01: Hero cinematográfico inicializado com sucesso.');
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

  // --------------------------------------------------------------------------
  // 05. CTA WhatsApp & Rodapé Section (#cta-footer)
  // --------------------------------------------------------------------------
  function initSectionFooter() {
    const footer = document.getElementById('cta-footer');
    if (!footer || typeof gsap === 'undefined') return;

    const M = window.TropicalMotion || { mode: 'full', quality: 'high' };
    const heading = footer.querySelector('.footer-heading');
    const ctaBtn = footer.querySelector('.btn-whatsapp-pill');
    const metaItems = footer.querySelectorAll('.meta-item');
    const bottomCopy = footer.querySelector('.footer-bottom-copy');

    if (M.mode === 'reduced') {
      gsap.set([heading, ctaBtn, ...metaItems, bottomCopy], {
        opacity: 1,
        y: 0,
        scale: 1,
        clearProps: 'all'
      });
      return;
    }

    if (typeof ScrollTrigger === 'undefined') {
      gsap.from([heading, ctaBtn, ...metaItems, bottomCopy], {
        opacity: 0,
        y: 20,
        duration: 0.6,
        stagger: 0.1,
        clearProps: 'all'
      });
      return;
    }

    // Timeline disparada a 35% de visibilidade (start: 'top 75%')
    const tl = gsap.timeline({
      scrollTrigger: {
        trigger: footer,
        start: 'top 75%',
        toggleActions: 'play none none none',
        once: true
      },
      defaults: { ease: 'power2.out' }
    });

    if (heading) {
      tl.from(heading, {
        y: 24,
        opacity: 0,
        duration: 0.65,
        clearProps: 'transform,opacity'
      }, 0);
    }

    if (ctaBtn) {
      tl.from(ctaBtn, {
        scale: 0.88,
        y: 20,
        opacity: 0,
        duration: 0.7,
        ease: 'back.out(1.25)',
        clearProps: 'transform,opacity'
      }, 0.15);
    }

    if (metaItems.length > 0) {
      tl.from(metaItems, {
        y: 16,
        opacity: 0,
        duration: 0.6,
        stagger: 0.1,
        clearProps: 'transform,opacity'
      }, 0.3);
    }

    if (bottomCopy) {
      tl.from(bottomCopy, {
        opacity: 0,
        duration: 0.7,
        clearProps: 'opacity'
      }, 0.45);
    }

    // Respiração suave do botão de WhatsApp para guiar a conversão final (quality HIGH)
    if (ctaBtn && M.quality === 'high' && M.mode === 'full') {
      const ctaPulse = gsap.to(ctaBtn, {
        scale: 1.025,
        duration: 2.4,
        ease: 'sine.inOut',
        yoyo: true,
        repeat: -1,
        paused: false
      });
      ctaBtn._motionLoopTween = ctaPulse;
      if (M.registerLoop) M.registerLoop(ctaBtn, { type: 'pulse' });
    }

    console.log('[Motion] Seção 05: CTA WhatsApp & Rodapé inicializada com sucesso.');
  }

  // Inicializar quando o DOM e Motion Core estiverem prontos
  function init() {
    initSectionHero();
    initSectionServices();
    initSectionProducts();
    initSectionReviews();
    initSectionFooter();
  }

  window.TropicalSectionsMotion = {
    initHero: initSectionHero,
    initServices: initSectionServices,
    initProducts: initSectionProducts,
    initReviews: initSectionReviews,
    initFooter: initSectionFooter,
    init: init
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
