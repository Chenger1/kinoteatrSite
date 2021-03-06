function SearchEvent(url){
	let search_url = url;

	this.set_focus_event = function(){
		let field = $('#myInput')[0]; 
		$(field).on('keyup', function(){
			let value = $(this).val()
			if(value == ''){
				$('#myDropdown').find('a').remove();
			}else{
				send_request(value);
			}	
		});
		$(field).focusout(function(event) {
			if(!$(event.relatedTarget).hasClass('dropdown_a')){
				$('#myDropdown').find('a').remove();
				$(field).val('');
			}
		});
	};

	function send_request(value){
		$.ajax({
			method: 'GET',
			url: search_url,
			data: {'value': value},
			success: function(response){
				update_search_box(response['result'])
			}
		})

	}

	function update_search_box(response){
		$('#myDropdown').find('a').remove();
		for(index in response){
			$('#myDropdown').append('<a href="'+ response[index]['url'] +'" class="dropdown_a">'+ response[index]['name'] +'</a>')
		}
	}
}