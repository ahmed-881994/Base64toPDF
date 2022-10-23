
// run on ducument read
// $('document').ready(function () {

// });

// Text input and GET request
function loading(enabled) {
    if (enabled) {
        $('#loader').removeClass('gone');
        $("input[type=button]").attr("disabled", "disabled");
    } else {
        $('#loader').addClass('gone');
        $("input[type=button]").removeAttr("disabled");
    }
}

$('#text-submit').click(function (e) {
    loading(true)
    var data = $('#text-input').val();
    if (data.length > 0) {
        sendPostRequest(data);
    };
});

function sendPostRequest(request) {

    $('#error').html("");
    //console.log(request);
    request = JSON.stringify(request);

    $.ajax({
        method: "POST",
        url: "./local/decode",
        data: { "request": request }
    }).done(function (response) {

        if (response.hasOwnProperty('error')) {
            $('#error').html(response['error']);
            console.log(response['error']);
        }
        else {
            console.log('entered else')
            var path = "../static/result/document.pdf#toolbar=1&navpanes=0&scrollbar=0";
            $("#file-display").attr("src", path);
            $("#file-display-container").removeClass('gone');
            
        }
        loading(false);
    });
}