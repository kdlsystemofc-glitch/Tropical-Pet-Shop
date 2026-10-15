/**
 * motion-core.js — Arquitetura de Motion para Tropical Pet Shop
 * Modos: full, reduced, paused
 * Qualidade: high, low
 * Integração: GSAP, ScrollTrigger, Lenis
 * Regras: Camadas-folha exclusivas (transform/opacity), pausa em aba oculta/fora de tela
 */

(function () {
  'use strict';

  // Namespace global
  const Motion = {
    mode: 'full',       // 'full' | 'reduced' | 'paused'
    previousMode: 'full',
    quality: 'high',    // 'high' | 'low'
    lenis: null,
    isInitialized: false,
    registeredLoops: [],
    registeredParallaxes: [],
    registeredReveals: []
  };

  window.TropicalMotion = Motion;

  // 1. Detecção de Qualidade de Hardware
  function detectQuality() {
    const isSaveData = navigator.connection && navigator.connection.saveData;
    const lowCores = navigator.hardwareConcurrency && navigator.hardwareConcurrency <= 4;
    const lowMem = navigator.deviceMemory && navigator.deviceMemory <= 4;
    const isSmallScreen = window.innerWidth < 768;

    if (isSaveData || lowCores || lowMem || isSmallScreen) {
      return 'low';
    }
    return 'high';
  }

  // 2. Detecção de Preferência de Movimento
  function detectMotionMode() {
    const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    return prefersReduced ? 'reduced' : 'full';
  }

  // 3. Atualização do DOM com os Modos Atuais
  function applyModeToDOM() {
    document.documentElement.dataset.motionMode = Motion.mode;
    document.documentElement.dataset.motionQuality = Motion.quality;
  }

  // 4. Inicialização do Lenis (Smooth Scroll)
  function initLenis() {
    if (typeof Lenis === 'undefined') return;
    if (Motion.mode === 'reduced' || Motion.quality === 'low') {
      if (Motion.lenis) {
        Motion.lenis.destroy();
        Motion.lenis = null;
      }
      return;
    }

    if (!Motion.lenis) {
      Motion.lenis = new Lenis({
        duration: 1.1,
        easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
        orientation: 'vertical',
        gestureOrientation: 'vertical',
        smoothWheel: true,
        wheelMultiplier: 0.95,
        touchMultiplier: 1.5,
        infinite: false
      });

      if (typeof ScrollTrigger !== 'undefined') {
        Motion.lenis.on('scroll', ScrollTrigger.update);

        gsap.ticker.add((time) => {
          if (Motion.lenis && Motion.mode !== 'paused') {
            Motion.lenis.raf(time * 1000);
          }
        });
        gsap.ticker.lagSmoothing(0);
      }
    }
  }

  // 5. IntersectionObserver para Pausa de Loops Fora da Tela
  const loopObserver = typeof IntersectionObserver !== 'undefined' ? new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      const tween = entry.target._motionLoopTween;
      if (tween) {
        if (entry.isIntersecting && Motion.mode === 'full') {
          tween.play();
        } else {
          tween.pause();
        }
      }
    });
  }, { rootMargin: '50px' }) : null;

  // 6. Registro de Loops Declarativos (data-loop)
  function registerLoop(element, options) {
    if (!element || Motion.mode === 'reduced' || Motion.quality === 'low') return null;

    if (loopObserver) {
      loopObserver.observe(element);
    }
    Motion.registeredLoops.push({ element, options });
    return element._motionLoopTween;
  }

  // 7. Registro de Parallax Declarativo (data-parallax)
  function registerParallax(element, factor) {
    if (!element || Motion.mode === 'reduced' || Motion.quality === 'low') return;
    if (typeof ScrollTrigger === 'undefined') return;

    Motion.registeredParallaxes.push({ element, factor });
  }

  // 8. Registro de Revelação Declarativa (data-reveal)
  function registerReveal(element, config) {
    Motion.registeredReveals.push({ element, config });
  }

  // 9. Controle de Pausa Global (Aba oculta ou Botão de Pausa)
  function setMode(newMode) {
    if (Motion.mode === newMode) return;

    if (newMode === 'paused') {
      Motion.previousMode = Motion.mode;
      Motion.mode = 'paused';
      if (typeof gsap !== 'undefined') gsap.globalTimeline.pause();
      if (Motion.lenis) Motion.lenis.stop();
    } else {
      const wasPaused = Motion.mode === 'paused';
      Motion.mode = newMode;
      if (wasPaused) {
        if (typeof gsap !== 'undefined') gsap.globalTimeline.play();
        if (Motion.lenis && Motion.mode === 'full' && Motion.quality === 'high') {
          Motion.lenis.start();
        }
      }
    }

    applyModeToDOM();
    console.log(`[Motion] Modo alterado para: ${Motion.mode} (Qualidade: ${Motion.quality})`);
  }

  function togglePause() {
    if (Motion.mode === 'paused') {
      setMode(Motion.previousMode || 'full');
    } else {
      setMode('paused');
    }
  }

  // 10. Inicialização do Núcleo
  function init() {
    if (Motion.isInitialized) return;

    Motion.quality = detectQuality();
    Motion.mode = detectMotionMode();
    applyModeToDOM();

    // Registrar plugins GSAP se presentes
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
      gsap.registerPlugin(ScrollTrigger);
    }

    // Inicializar Lenis se aplicável
    initLenis();

    // Listener para preferência do sistema operacional
    window.matchMedia('(prefers-reduced-motion: reduce)').addEventListener('change', (e) => {
      if (Motion.mode !== 'paused') {
        setMode(e.matches ? 'reduced' : 'full');
        initLenis();
      }
    });

    // Pausa automática quando aba fica oculta (Page Visibility API)
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        if (typeof gsap !== 'undefined') gsap.globalTimeline.pause();
        if (Motion.lenis) Motion.lenis.stop();
      } else if (Motion.mode !== 'paused') {
        if (typeof gsap !== 'undefined') gsap.globalTimeline.play();
        if (Motion.lenis && Motion.mode === 'full' && Motion.quality === 'high') Motion.lenis.start();
      }
    });

    // Vincular Botão Acessível de Pausa na UI
    const toggleBtn = document.getElementById('motion-toggle-btn');
    if (toggleBtn) {
      toggleBtn.addEventListener('click', () => {
        togglePause();
        const isPaused = Motion.mode === 'paused';
        toggleBtn.classList.toggle('is-paused', isPaused);
        toggleBtn.setAttribute('aria-label', isPaused ? 'Retomar animações da página' : 'Pausar animações da página');
        const icon = toggleBtn.querySelector('.motion-toggle-icon');
        if (icon) icon.textContent = isPaused ? '▶' : '⏸';
      });
    }

    // Navegação Suave com Lenis para Âncoras do Menu
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function (e) {
        const targetId = this.getAttribute('href');
        if (!targetId || targetId === '#') return;
        const targetEl = document.querySelector(targetId);
        if (targetEl) {
          e.preventDefault();
          if (Motion.lenis && Motion.mode === 'full') {
            Motion.lenis.scrollTo(targetEl, { offset: -20, duration: 1.0 });
          } else {
            targetEl.scrollIntoView({ behavior: 'smooth' });
          }
        }
      });
    });

    Motion.isInitialized = true;
    console.log(`[Motion] Núcleo ativo | Modo: ${Motion.mode} | Qualidade: ${Motion.quality}`);
  }

  // Exportar métodos públicos
  Motion.init = init;
  Motion.setMode = setMode;
  Motion.togglePause = togglePause;
  Motion.registerLoop = registerLoop;
  Motion.registerParallax = registerParallax;
  Motion.registerReveal = registerReveal;

  // Auto-inicializar após DOMContentLoaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
