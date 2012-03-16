$(document).ready(function() {
	$('#see-by-req').click(function(e) {
		e.preventDefault();
		$('#my-board').slideToggle('slow');
	});
});