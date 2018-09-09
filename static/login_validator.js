// Defining fields
var $password = $("#password");
var $passwordHamburguer = $("#password-hamburguer");
var $username = $("#username");
var $usernameHamburguer = $("#username-hamburguer");

// Defining validity-checker functions
function isUsernameValid() {
    return $username.val().length >= 5;
}
function isUsernameHamburguerValid() {
    return $usernameHamburguer.val().length >= 5;
}
function isPasswordValid() {
    return $password.val().length >= 8;
}
function isPasswordHamburguerValid() {
    return $passwordHamburguer.val().length >= 8;
}

// Defining submit-enabler functions
function canSubmit() {
    return isPasswordValid() && isUsernameValid();
}
function canSubmitHamburguer() {
    return isPasswordHamburguerValid() && isUsernameHamburguerValid();
}

// Defining event functions
function enableSubmitEvent(){
    $("#submit").prop("disabled", !canSubmit());
}

function enableSubmitHamburguerEvent(){
    $("#submit-hamburguer").prop("disabled", !canSubmitHamburguer());
}

$username.focus(enableSubmitEvent).keyup(enableSubmitEvent).change(enableSubmitEvent)
$password.focus(enableSubmitEvent).keyup(enableSubmitEvent).change(enableSubmitEvent)

$usernameHamburguer.focus(enableSubmitHamburguerEvent).keyup(enableSubmitHamburguerEvent).change(enableSubmitHamburguerEvent)
$passwordHamburguer.focus(enableSubmitHamburguerEvent).keyup(enableSubmitHamburguerEvent).change(enableSubmitHamburguerEvent)