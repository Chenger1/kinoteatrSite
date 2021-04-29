function movieHandler(url){
	this.url = url;

	this.send_request = function(){
		let selected_cinema_id = $('#cinemaDropdown').find('.selected').attr('id');
		let selected_cinema_pk = $('#'+selected_cinema_id+'_hidden').attr('value');

		let selected_format_id = $('.format.active').attr('id');
		let selected_format_value = $('#'+selected_format_id+'_hidden').attr('value');

		let movie_pk = $('#moviePk').attr('value');

		let callback = this.render_table;

		$.ajax({
			method: 'GET',
			url: this.url,
			data: { 'cinema': selected_cinema_pk,
					'format': selected_format_value,
					'movie': movie_pk},
			success: function(response){
				$('#sessionsTable').children('tbody').text('');
				callback(response['sessions']);
			}
		});
	};

	this.cinemaDropdown = function(elem){
		$('#cinemaDropdown').children('.dropdown-item').each(function(){
			if($(this).hasClass('selected')){
				$(this).removeClass('selected');
			}
		})
		$(elem).addClass('selected');
		$('#cinemaName').text($(elem).text());

		this.send_request();
	};

	this.formatOnClick = function(elem){
		$('.format.active').removeClass('active');

		$(elem).addClass('active');

		this.send_request();
	}

	this.render_table = function(sessions){
		for(session in sessions){
			let tr = $('<tr></tr>');
			$('#sessionsTable').append(tr);
			for(key in sessions[session]){
				if(key=='cinema_hall_url'){
					continue;
				}
				if(key=='cinema_hall'){
					tr.append('<td><a href="' + sessions[session]['cinema_hall_url'] + '">'+ sessions[session][key] +'</td>')
				}else if(key == 'detail'){
					tr.append('<td><a href="' + sessions[session][key] + '">Детали</td>')
				}else{
					tr.append($('<td>'+ sessions[session][key] +'</td>'));
				}
			}
		}
	};
};
