$(function() {
    $('form#htmlForm').on('submit', function(e) {
        e.preventDefault();
        var htmlString = $('textarea#htmlString').val();
        $.ajax({
        type: 'POST',
        url: '/',
        data: {'html_string': htmlString},
        success: function(response) {
            $('textarea#markdownString').val(response.markdown_string);
        },
        dataType: 'json'
        });
    });
});
