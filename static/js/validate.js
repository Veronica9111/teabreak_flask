$(function(){
	var password = null;

	$("#register-email").blur(function(){
		var email = $(this).val();
		var re = new RegExp("[a-zA-Z0-9-\.]{1,}@([a-zA-Z\.])?[a-zA-Z0-9]{1,}\.[a-zA-Z]{1,4}", "gi");
		if (!re.test(email)) {
			$(this).css("border", "red 1px solid");
		}
		else {
			$(this).css("border", "#ccc 1px solid");
		}
	});

	$("#register-nickname").blur(function(){
		var nickname = $(this).val();
		if (nickname.length < 4 || nickname.length > 12) {
			$(this).css("border", "red 1px solid");
			//TODO Check if the nickname is existed
		}
		else {
			$(this).css("border", "#ccc 1px solid");
		}
	});

	$("#register-password").blur(function(){
		password = $(this).val();
		if (password < 6) {
			$(this).css("border", "red 1px solid");
		}
		else {
			$(this).css("border", "#ccc 1px solid");
		}
	});

	$("#register-confirm-password").blur(function(){
		var confirm_password = $(this).val();
		if (confirm_password != password) {
			$(this).css("border", "red 1px solid");
		}
		else {
			$(this).css("border", "#ccc 1px solid");
		}
	});
});
