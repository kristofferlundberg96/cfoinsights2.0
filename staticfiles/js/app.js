$('html, body').hide();

$(document).foundation()

$(function() {
    if($('#scrolling-numbers').visible(true)) {
        $('.count').each(function () {
            $(this).prop('Counter',0).animate({
                Counter: $(this).text()
            }, {
                duration: 2000,
                easing: 'swing',
                step: function (now) {
                    $(this).text(Math.ceil(now));
                }
            });
        });
    }

    var overlayOpen = false;

    var header = $('.header');
    if (!header.hasClass('non-sticky')) {
        $(".header").headroom({
            offset: 50,
        });
    }

    $(".menu-icon").on("click", function(event) {
        if ($("body").hasClass("noscroll")) {
            $("body").removeClass("noscroll");
        } else {
            $("body").addClass("noscroll");
        }
    });
})

function scrollToAnchor(e) {
    if (e) {
        e.preventDefault();
        var target = $(this).attr('href');
    } else {
        var target = location.hash;
    }

    if (document.documentElement.scrollTop > $(target).position().top) {
        $('html, body').animate({
            scrollTop: $(target).offset().top - ($('.header').height() - 1)
        }, 1000);
    } else {
        $('html, body').animate({
            scrollTop: $(target).offset().top
        }, 1000);
    }
}

$(document).ready(function() {
    $("a[href^='#']").bind("click", scrollToAnchor);

    if (window.location.hash) {
        setTimeout(function() {
            $('html, body').scrollTop(0).show();
            scrollToAnchor();
        }, 0);
    } else {
        $('html, body').show();
    }
})

$(document).on('click', '.menu a', function(event) {
    if($(window).width() < 1024) {
        $('#top-menu').css({"display": "none"});
    }
});

var isOpeningMenu = true;

$(document).on('click', 'button.menu-icon', function(event) {
    if (isOpeningMenu) {
        $('.header').css('background-color', 'rgb(0, 49, 65)');
    } else {
        $('.header').removeAttr('style');
    }
    isOpeningMenu = !isOpeningMenu
});