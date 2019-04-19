$(document).ready(function() {
	$("#button").click(function(event){											//On clicking button id submit
			$.ajax({
				data :  {
					ans1 : $('#ans1').val(),							//POST data through ajax to URL quiz which will be taken in app.py
					ans2 : $('#ans2').val(),
					ans3 : $('#ans3').val(),
					ans4 : $('#ans4').val()				
				},	
				type : 'POST',
				url : '/quiz'
			})
			.done(function(data) {

			if (data.error) {																//Receiving data back ,,if all fields are empty print error
																							//Else print confirmation of push
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#successAlert').text(data.sucess).show();
				$('#errorAlert').hide();											//.hide() to hide one and show case another
				} 

		});
		event.preventDefault();
	}); 
});
