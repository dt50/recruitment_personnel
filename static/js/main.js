$(document).ready(function() {
  (function initAos() {
    AOS.init();
  })();

  (function init_gallery_pane() {
    var gallery = document.querySelector("#gallery-pane");
    if (gallery == null) return;
    var galleryTns = tns({
      container: "#gallery-pane",
      items: 4,
      slideBy: 1,
      gutter: 15,
      nav: false,
      mouseDrag: true,
      prevButton: ".gallery .prev-button",
      nextButton: ".gallery .next-button",
    });
  })();
  (function init_new_arrivals_gallery() {
    var gallery = document.querySelector("#new-arrivals-gallery");
    if (gallery == null) return;
    var galleryTns = tns({
      container: "#new-arrivals-gallery",
      items: 4,
      slideBy: 1,
      gutter: 15,
      nav: false,
      mouseDrag: true,
      prevButton: "#new-arrivals-container .prev-button",
      nextButton: "#new-arrivals-container .next-button",
    });
  })();
  (function init_recomended_gallery() {
    var gallery = document.querySelector("#recomended-gallery");
    if (gallery == null) return;
    var galleryTns = tns({
      container: "#recomended-gallery",
      items: 4,
      slideBy: 1,
      gutter: 15,
      nav: false,
      mouseDrag: true,
      prevButton: "#recomended-container .prev-button",
      nextButton: "#recomended-container .next-button",
    });
  })();
  (function init_from_blogs_gallery() {
    var gallery = document.querySelector("#from-blogs-gallery");
    if (gallery == null) return;
    var galleryTns = tns({
      container: "#from-blogs-gallery",
      items: 3,
      slideBy: 1,
      gutter: 25,
      nav: false,
      mouseDrag: true,
      edgePadding: 5,
      prevButton: ".from-blogs-gallery .prev-button",
      nextButton: ".from-blogs-gallery .next-button",
    });
  })();
  (function updateStickyTopMenu() {
    var topMenu = $(".header");
    sticky = false;
    $(window).scroll(function(event) {
      var st = $(this).scrollTop()
      if (st > 25) {
        if (!sticky) {
          topMenu.addClass("sticky");
          sticky = true;
        }
      }
      else {
        if (sticky) {
          topMenu.removeClass("sticky");
          sticky = false;
        }
      }
    });
  })();
});
