
// run on ducument read
// $('document').ready(function () {

// });
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
// Text input and POST request
function loading(enabled) {
    if (enabled) {
        $('#loader').removeClass('gone');
        $("input[type=button]").attr("disabled", "disabled");
    } else {
        $('#loader').addClass('gone');
        $("input[type=button]").removeAttr("disabled");
    }
}

function showError(enabled,text='') {
    if (enabled) {
        $('#error').removeClass('gone');
        $('#error').html(text);
    } else {
        $('#error').addClass('gone');
        $('#error').html(text);
    }
}

$('#text-submit').click(function (e) {
    
    showError(false);
    var data = $('#text-input').val();
    if (data.length > 0) {
        loading(true)
        sendPostRequest(data);
    }
    else{
        showError(true, 'No Base64 entered');
    };
});

async function sendPostRequest(request) {

    //console.log(request);
    request = JSON.stringify(request);
    await sleep(1000)
    $.ajax({
        method: "POST",
        url: "./local/decode",
        data: { "request": request }
    }).done(function (response) {

        if (response.hasOwnProperty('error')){
            showError(true,response['error']);
            console.log(response['error']);
        }
        else {
            
            var path = "../static/result/document.pdf#toolbar=1&navpanes=0&scrollbar=0";
            $("#file-display").attr("src", path);
            $("#file-display-container").removeClass('gone');
            
        }
        loading(false);
    });
}