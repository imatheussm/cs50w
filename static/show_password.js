$("#show-password").click(function () {
    // get the attribute value
    var type = $("#password").attr("type"); 
    // now test it's value
    if (type === "password") {
        // change icon
        $("#show-password-img").hide();
        $("#hide-password-img").show();
        // toggle field
        $("#password").attr("type", "text");
    } else {
        // change icon
        $("#hide-password-img").hide();
        $("#show-password-img").show();
        // toggle field
        $("#password").attr("type", "password");
    } 
});