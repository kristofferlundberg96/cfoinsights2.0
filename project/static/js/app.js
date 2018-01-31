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

    $(".header").headroom({
        offset: 50,
    });

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
            scrollTop: $(target).offset().top - $('.header').height()
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