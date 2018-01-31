$(function() {
    var filtered_categories = [];

    function filter_speakers() {
        filtered_categories = [1];
    }

    $('.speaker-category :checkbox').click(function() {
        $('input:checkbox:not(:checked)').each(function() {
            $('div[data-category' + '*="' + $(this).val() + '"]').hide();
        });
        $('input[type="checkbox"]:checked').each(function() {
            console.log($(this).val());
            $('div[data-category' + '*="' + $(this).val() + '"]').show();
        });

    });
});