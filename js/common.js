document.addEventListener("DOMContentLoaded", function() {
  'use strict';

  var html = document.querySelector('html'),
    menuOpenIcon = document.querySelector(".nav__icon-menu"),
    menuCloseIcon = document.querySelector(".nav__icon-close"),
    menuList = document.querySelector(".main-nav"),
    toggleTheme = document.querySelector(".toggle-theme"),
    portfolioViewButton = document.querySelector('.portfolio__toggle'),
    btnScrollToTop = document.querySelector(".top");


  /* =======================================================
  // Menu + Theme Switcher + Toggle list view
  ======================================================= */
  menuOpenIcon.addEventListener("click", () => {
    menuOpen();
  });

  menuCloseIcon.addEventListener("click", () => {
    menuClose();
  });

  var togglePet = document.querySelector(".toggle-pet");

  toggleTheme.addEventListener("click", () => {
    darkMode();
  });

  togglePet.addEventListener("click", () => {
    catMode();
  });

  if (portfolioViewButton) {
    portfolioViewButton.addEventListener("click", () => {
      viewToggle();
    });
  }

  function menuOpen() {
    menuList.classList.add("is-open");
  }

  function menuClose() {
    menuList.classList.remove("is-open");
  }


  // Theme Switcher
  function darkMode() {
    if (html.classList.contains('dark-mode')) {
      html.classList.remove('dark-mode');
      localStorage.removeItem("theme");
      document.documentElement.removeAttribute("dark");
    } else {
      html.classList.add('dark-mode');
      localStorage.setItem("theme", "dark");
      document.documentElement.setAttribute("dark", "");
    }
  }


  // Cat Mode
  function catMode() {
    if (html.classList.contains('cat-mode')) {
      html.classList.remove('cat-mode');
      localStorage.removeItem("petMode");
      swapPortfolioImages('cat', 'lab');
    } else {
      html.classList.add('cat-mode');
      localStorage.setItem("petMode", "cat");
      swapPortfolioImages('lab', 'cat');
    }
  }

  function swapPortfolioImages(from, to) {
    var images = document.querySelectorAll('.portfolio__image');
    images.forEach(function(img) {
      var src = img.getAttribute('src');
      var dataSrc = img.getAttribute('data-src');
      if (src) {
        img.setAttribute('src', swapPetPath(src, from, to));
      }
      if (dataSrc) {
        img.setAttribute('data-src', swapPetPath(dataSrc, from, to));
      }
    });
  }

  function swapPetPath(path, from, to) {
    var fromDir = from === 'lab' ? 'Black and White Labs' : 'Black and White Cats';
    var toDir = to === 'lab' ? 'Black and White Labs' : 'Black and White Cats';
    return path
      .replace(fromDir, toDir)
      .replace('/' + from + '-', '/' + to + '-');
  }

  // Apply cat mode to portfolio images on page load
  if (localStorage.getItem("petMode") === "cat") {
    swapPortfolioImages('lab', 'cat');
  }


  // Toggle list view
  function viewToggle() {
    if (html.classList.contains('view-list')) {
      html.classList.remove('view-list');
      localStorage.removeItem("classView");
      document.documentElement.removeAttribute("list");
    } else {
      html.classList.add('view-list');
      localStorage.setItem("classView", "list");
      document.documentElement.setAttribute("list", "");
    }
  }


  /* =======================
  // Responsive Videos
  ======================= */
  reframe(".post__content iframe:not(.reframe-off), .page__content iframe:not(.reframe-off)");


  /* =======================
  // Zoom Image
  ======================= */
  const lightense = document.querySelector(".page__content img, .post__content img"),
  imageLink = document.querySelectorAll(".page__content a img, .post__content a img");

  if (imageLink) {
    for (var i = 0; i < imageLink.length; i++) imageLink[i].parentNode.classList.add("image-link");
    for (var i = 0; i < imageLink.length; i++) imageLink[i].classList.add("no-lightense");
  }

  if (lightense) {
    Lightense(".page__content img:not(.no-lightense), .post__content img:not(.no-lightense)", {
    padding: 60,
    offset: 30
    });
  }


  /* =======================
  // LazyLoad Images
  ======================= */
  var lazyLoadInstance = new LazyLoad({
    elements_selector: ".lazy"
  })


  /* ==========================
  // Lightbox Gallery
  ========================== */
  const lightbox = GLightbox({
    touchNavigation: true,
    loop: true,
    moreLength: 0,
    autoplayVideos: true
  });


  /* =================================
  // Smooth scroll to the tags page
  ================================= */
  document.querySelectorAll(".tag__link").forEach(anchor => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();

      document.querySelector(this.getAttribute("href")).scrollIntoView({
        behavior: "smooth"
      });
    });
  });


  /* =======================
  // Scroll Top Button
  ======================= */
  window.addEventListener("scroll", function () {
    window.scrollY > window.innerHeight ? btnScrollToTop.classList.add("is-active") : btnScrollToTop.classList.remove("is-active");
  });

  btnScrollToTop.addEventListener("click", function () {
    if (window.scrollY != 0) {
      window.scrollTo({
        top: 0,
        left: 0,
        behavior: "smooth"
      })
    }
  });

});