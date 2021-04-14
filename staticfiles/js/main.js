/* login form validation */
function validateLogin() {
var userName, passWord;

userName = $("#username").val();
passWord = $("#password").val();

if(userName == null || userName == '') {
$("#unError").text("User name do not empty!");
$("#unError").addClass("show");
$("input#username").focus();
setTimeout(function() {
$("#unError").removeClass("show");
}, 1000);

return false;
}

if(userName.length < 6) {
$("#unError").text("User do not exit!");
$("#unError").addClass("show");
$("input#username").focus();
setTimeout(function() {
$("#unError").removeClass("show");
}, 1000);

return false;
}

if(passWord == null || passWord == '') {
$("#pwError").text("Password do not empty!");
$("#pwError").addClass("show");
$("input#password").focus();
setTimeout(function() {
$("#pwError").removeClass("show");
}, 1000);

return false;
}

if(passWord.length < 6 ) {
$("#pwError").text("Password wrong!");
$("#pwError").addClass("show");
$("input#password").focus();
setTimeout(function() {
$("#pwError").removeClass("show");
}, 1000);

return false;
}
}
/* register form validation */
function validateRegister() {
var userName, passWord, cpassWord, emaidid, atpos, dotpos;

userName = $("#regusername").val();
passWord = $("#regpassword").val();
cpassWord = $("#regcpassword").val();
emailid = document.registerform.regemail.value;
atpos = emailid.indexOf('@');
dotpos = emailid.lastIndexOf('.');

if(userName == null || userName == '') {
$("#reguserError").text("User name do not empty!");
$("#reguserError").addClass("show");
$("input#regusername").focus();
setTimeout(function() {
$("#reguserError").removeClass("show");
}, 1000);

return false;
}

if(userName.length < 6) {
$("#reguserError").text("User short! min 6 char!");
$("#reguserError").addClass("show");
$("input#regusername").focus();
setTimeout(function() {
$("#reguserError").removeClass("show");
}, 1000);

return false;
}

if(passWord == null || passWord == '') {
$("#regpwError").text("Password do not empty!");
$("#regpwError").addClass("show");
$("input#regpassword").focus();
setTimeout(function() {
$("#regpwError").removeClass("show");
}, 1000);

return false;
}

if(passWord.length < 6 ) {
$("#regpwError").text("Password weak!");
$("#regpwError").addClass("show");
$("input#regpassword").focus();
setTimeout(function() {
$("#regpwError").removeClass("show");
}, 1000);

return false;
}

if(passWord.length != cpassWord.length ) {
$("#regcpwError").text("Password does not match!");
$("#regcpwError").addClass("show");
$("input#regcpassword").focus();
setTimeout(function() {
$("#regcpwError").removeClass("show");
}, 1000);

return false;
}

if(emailid == null || emailid == '') {
$("#regemailError").text("Email do not empty!");
$("#regemailError").addClass("show");
$("input#regemail").focus();
setTimeout(function() {
$("#regemailError").removeClass("show");
}, 1000);

return false;
}

if(atpos < 1 || dotpos < atpos+2 || dotpos+2 >= emailid.length) {
$("#regemailError").text("Invalid email id!");
$("#regemailError").addClass("show");
$("input#regemail").focus();
setTimeout(function() {
$("#regemailError").removeClass("show");
}, 1000);

return false;
}
}

$(document).ready(function(){

var dynHeight;

/* tab code */
$(".formCtlBlock a").click(function() {
var tabId = $(this).attr('data-tab');
$(".formCtlBlock a").removeClass("active");
$(".formBlock").removeClass("active");
$(this).addClass("active");
$("#"+tabId).addClass("active");

dynHeight = $(".formBlock.active").height() + 39;
$(".formPage").animate({"min-height": dynHeight}, 300);

});

});