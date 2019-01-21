jQuery(function ($) {

    'use strict';

    // -------------------------------------------------------------
    // News Slider
    // -------------------------------------------------------------

    (function(){
        $('.ticker-flexslider').flexslider({ 
            prevText: "", 
            nextText: "", 
            controlNav: false, 
            directionNav: false,
            smoothHeight: false, 
            touch: true,
            animation: "slide"
        });  
    })(); 
    

    // -------------------------------------------------------------
    //  Magnific Popup
    // -------------------------------------------------------------

    (function() {

        $('.image-link').magnificPopup({
          type: 'image',
          gallery:{
            enabled:true,
          }
        });

    }()); 

    // -------------------------------------------------------------
    //  Sticky Nav
    // -------------------------------------------------------------


    (function () {

        $(window).scroll(function() {
            var nav = $('.navbar');
            var $this = $(this);

            if($this.scrollTop() > 220) {
                nav.addClass('fixed-top animated fadeInDown');
            }
            else {
                nav.removeClass('fixed-top animated fadeInDown');
            }
        });

    }()); 

    /*==============================================================*/
    // TheiaStickySidebar
    /*==============================================================*/
           
   (function() {

        $('.tr-sticky')
            .theiaStickySidebar({
                additionalMarginTop: 0
            });
    }());          

 
});

