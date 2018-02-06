var currentSurveyIndex = 0;

$(document).ready(function() {
    $('html, body').hide();
    for (var i = 1; i <= 3; i++) {
        $('div[data-survey-pane' + '*="' + i + '"]').hide();
    }
    $('div[data-survey-pane="0"').show();
    $('html, body').show();

    $('#prev').on('click', function() {
        if ($(this).hasClass('disabled')) {
            return;
        }
        $('div[data-survey-pane="' + currentSurveyIndex + '"]').hide();
        currentSurveyIndex--;
        $('div[data-survey-pane="' + currentSurveyIndex + '"]').show();
        if (currentSurveyIndex == 0) {
            $('#prev').addClass('disabled');
        }
        $('#next').text('Next');
    });

    $('#next').on('click', function() {
        $('div[data-survey-pane="' + currentSurveyIndex + '"]').hide();
        currentSurveyIndex++;
        $('div[data-survey-pane="' + currentSurveyIndex + '"]').show();
        if (currentSurveyIndex > 0) {
            $('#prev').removeClass('disabled');
        }
        if (currentSurveyIndex == 2) {
            $('#next').text('Submit');
        }
        if (currentSurveyIndex == 3) {
            window.setTimeout(function() {
                $('.circle-loader').toggleClass('load-complete');
                $('.checkmark').toggle();
                
                $('.load-complete').show();
            }, 2000);
            $('#next').hide();
            $('#prev').hide();
        }
    })
});