var _box_question_login = document.getElementsByClassName("box_question_login")[0];
var _box_question_register = document.getElementsByClassName("box_question_register")[0];
var _box__register = document.getElementsByClassName("box__register")[0];
var _box_login = document.getElementsByClassName("box_login")[0];
var _box__register_login = document.getElementsByClassName("box__register_login")[0];
function cambio_a_login() {
    _box_question_login.style.display = "block";
    _box_question_register.style.display = "none";
    _box__register.style.display = "block"
    _box_login.style.display = "none"
    _box__register_login.style.top = "45px"
}
function cambio_a_register() {
    _box_question_login.style.display = "none";
    _box_question_register.style.display = "block";
    _box_login.style.display = "block"
    _box__register.style.display = "none"
    _box__register_login.style.top = "100px"
}