
setInterval(function(){

    if ($("#username").val().length >= 5 && $("#password").val().length >= 8){
        $("#sbmt_btn").prop("disabled", false);
    } else {
        $("#sbmt_btn").prop("disabled", true);
    }
    console.log($("#username").length)
}, 100)

