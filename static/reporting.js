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

	$('#id_report_type').change(function(e) {
		$('#report-type').submit();
	});

	var entries = $('.req-entry');
	$.each(entries, function(index, entry) {
		$(entry).click(function (event) {
			var value = entry.innerText;
			entry.innerText = '';
			$(entry).append('<input class="wat" type="text" value="' + value + '"/>');
			$(entry).children()[0].focus();
		});
	});

	$('input.wat').live("blur", function() {
		// submit something
		var node = $(this)[0];
		var value = node.value;
		var parent_node = $(this).parent()[0];

		var postData = {
			'status_id': parent_node.getAttribute('status_id'),
			'req_id': parent_node.getAttribute('req_id'),
			'value': value
		}
		$.ajax({
		    'url': '/reporting/ajax_status_value',
			'type': 'POST',
			'data': postData,
			'success': function(response) {
				parent_node.innerHTML = response;
			}
		});
	});

	$('input.wat').live("keypress", function(e) {
		if (e.keyCode == 13 ) {
		var node = $(this)[0];
		var value = node.value;
		var parent_node = $(this).parent()[0];

		var postData = {
			'status_id': parent_node.getAttribute('status_id'),
			'req_id': parent_node.getAttribute('req_id'),
			'value': value
		};
		$.ajax({
		    'url': '/reporting/ajax_status_value',
			'type': 'POST',
			'data': postData,
			'success': function(response) {
				parent_node.innerHTML = response;
			}
		});
		}
	});
});