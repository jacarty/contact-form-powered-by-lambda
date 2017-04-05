// Contact form submission
    (function($){
		function processForm(e){
			{
			$.ajax({
                url: 'https://API-NAME.execute-api.REGION.amazonaws.com/Prod/myform',
			    dataType: 'json',
			    type: 'post',
			    contentType: 'application/json',
			    data: JSON.stringify( { "name": $('#name').val(), "email": $('#email').val(), "subject": $('#subject').val(), "message": $('#message').val(), "g-recaptcha": $('#g-recaptcha-response').val() } ),
			    processData: false,
			    success: function( data, textStatus, jQxhr ){
			        $('#response').html( JSON.stringify(data) );
			    	$('#myform')[0].reset();
			    },
			    error: function( jqXhr, textStatus, errorThrown ){
			        console.log(errorThrown);
			    }
			});
            e.preventDefault();
			grecaptcha.reset()
			}
        }
			$('#myform').submit(processForm);
})(jQuery);
