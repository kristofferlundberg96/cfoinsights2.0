$(function() {
    $('.register-button').click(function(e) {
        $('#tickets').append('<img height="1" width="1" style="display:none;" alt="" src="https://dc.ads.linkedin.com/collect/?pid=157308&conversionId=210212&fmt=gif" />');
        $('#tickets').append("<script>fbq('track', 'Lead');</script>");
        return true;
    })
});