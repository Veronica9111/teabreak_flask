$(function(){


	var password = null;
	var name_valid = false;
	var mail_valid = false;
	var password_valid = false;
	var password_confirm_valid = false;
	function enable_submit_button () {
		if (name_valid && mail_valid && password_valid && password_confirm_valid) {
			$("#register-submit").removeAttr('disabled');
		}
	}
	$("#register-email").blur(function(){
		var email = $(this).val();
		var re = new RegExp("[a-zA-Z0-9-\.]{1,}@([a-zA-Z\.])?[a-zA-Z0-9]{1,}\.[a-zA-Z]{1,4}", "gi");
		if (!re.test(email)) {
			$(this).css("border", "red 1px solid");
			mail_valid = false;
		}
		else {
			$(this).css("border", "#ccc 1px solid");
			mail_valid = true;
		}
		enable_submit_button();
	});

	$("#register-nickname").blur(function(){
		var nickname = $(this).val();
		if (nickname.length < 4 || nickname.length > 12) {
			$(this).css("border", "red 1px solid");
			name_valid = false;
			//TODO Check if the nickname is existed
		}
		else {
			$(this).css("border", "#ccc 1px solid");
			name_valid = true;
		}
		enable_submit_button();
	});

	$("#register-password").blur(function(){
		password = $(this).val();
		if (password < 6) {
			$(this).css("border", "red 1px solid")
			password_valid = false;
		}
		else {
			$(this).css("border", "#ccc 1px solid");
			password_valid = true;
		}
		enable_submit_button();
	});

	$("#register-confirm-password").blur(function(){
		var confirm_password = $(this).val();
		if (confirm_password != password) {
			$(this).css("border", "red 1px solid");
			password_confirm_valid = false;
		}
		else {
			$(this).css("border", "#ccc 1px solid");
			password_confirm_valid = true;
		}
		enable_submit_button();
	});
});
