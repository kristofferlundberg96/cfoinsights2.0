$(function() {
    var filtered_categories = [];

    function filter_speakers() {
        filtered_categories = [1];
    }

    $('.speaker-category :checkbox').click(function() {
        $('input:checkbox:not(:checked)').each(function() {
            var categories = $(this).val().split(' ');
            $.each(categories, function(index, value) {
                $('div[data-category' + '*="' + value + '"]').hide();
            });
        });
        $('input[type="checkbox"]:checked').each(function() {
            var categories = $(this).val().split(' ');
            $.each(categories, function(index, value) {
                $('div[data-category' + '*="' + value + '"]').show();
            });
        });
    });
});