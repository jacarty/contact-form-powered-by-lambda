// Scroll Reveal
var TopReveal = {
	origin : 'top',
	duration : 400,
};
var LeftReveal = {
	origin : 'left',
	duration : 500,
};
var RightReveal = {
	origin : 'right',
	duration : 500,
};
var BottomReveal = {
	origin : 'right',
	duration : 500,
};
window.sr = ScrollReveal({ reset: false } );
sr.reveal( '.top', TopReveal );
sr.reveal( '.right', RightReveal );
sr.reveal( '.left', LeftReveal );
sr.reveal( '.bottom', BottomReveal );

// Fix Hide Menu on Anchor Click
$(".navbar-nav li a").click(function (event) {
   // check if window is small enough so dropdown is created
   var toggle = $(".navbar-toggle").is(":visible");
   if (toggle) {
     $(".navbar-collapse").collapse('hide');
   }
});

// Contact form submission
    (function($){
        function processForm(e){
            $.ajax({
                url: 'https://API-NAME.execute-api.REGION.amazonaws.com/prod/myform',
			    dataType: 'json',
			    type: 'post',
			    contentType: 'application/json',
			    data: JSON.stringify( { "name": $('#name').val(), "email": $('#email').val(), "subject": $('#subject').val(), "message": $('#message').val() } ),
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
        }
        $('#myform').submit(processForm);
})(jQuery);