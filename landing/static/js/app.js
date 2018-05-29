$(document).foundation()

$(".newsletter_scroll").click(function() {
    $('html, body').animate({
        scrollTop: $("#bg3").offset().top
    }, 2000);
});

