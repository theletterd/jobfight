$(document).ready(function() {
	$('#see-by-req').click(function(e) {
		e.preventDefault();
		var reqBoard = $('#my-board');
		if(!reqBoard.is(':visible')) {
			$('#req-text').text('hide requisitions');
		} else {
			$('#req-text').text('see by requisition');
		}
		reqBoard.slideToggle('slow');
	});
});