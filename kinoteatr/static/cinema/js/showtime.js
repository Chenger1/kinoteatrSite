function showTimeHandler(url){
	this.url = url;
	this.elems = $('.callback');
	this.radio = $('.callback[type=radio]');
	this.checkbox = $('.callback[type=checkbox]');
	this.select = $('.callback[type=select]');


	this.send_request = function(){
		let selected_cinema = $('#cinemas').children(':selected').attr('value');
		let selected_movie = $('#selectMovies').children(':selected').attr('value');
		let selected_period = $('.callback[type=radio]:checked').attr('value');
		let selected_formats = [];
		for(child of $('.callback[type=checkbox]:checked')){
			selected_formats.push($(child).attr('value'))
		}

		let callback = this.render_table;
		let callback_movies = this.render_select_movies;

		$.ajax({
			method: 'GET',
			url: this.url,
			data: {
				'selected_cinema': selected_cinema,
				'selected_movie': selected_movie,
				'selected_period': selected_period,
				'selected_formats': JSON.stringify(selected_formats),
			},
			success: function(response){
				$('#cinemaName').text(response['cinema']);
				callback(response);
				callback_movies(response['select_movies']);
			}
		})

	}


	this.init_handlers = function(elem){
		if($(elem)[0].type == 'radio'){
			this.radio_handler(elem);
		}else if($(elem)[0].type == 'checkbox'){
			this.checkbox_hander(elem);
		}else if($(elem)[0].type == 'select-one'){
			this.select_handler(elem);
		}else{
			console.log('')
		}
	}


	this.radio_handler = function(elem){
		for(child of this.radio){
			$(child).prop('checked', false);
		}

		$(elem).prop('checked', true);

		this.send_request();
	};

	this.checkbox_hander = function(elem){
		this.send_request();
	};

	this.select_handler = function(elem){
		if(elem.attr('id') == 'cinemas'){
			$('#selectMovies').children(':selected').attr('value', 'null');
		}
		this.send_request();
	};

	this.render_table = function(sessions){
		$('#sessionsTable').children('tbody').text('');
		for(session in sessions){
			if(session == 'select_movies' || session == 'cinema'){
				continue;
			}
			let tr = $('<tr></tr>');
			$('#sessionsTable').append(tr);
			tr.append('<td><a href="'+ sessions[session]['movie_url'] +'"><img src="' + sessions[session]['image_url'] + '" width="75" height="75"></a></td>')
			tr.append('<td><a href="'+ sessions[session]['movie_url'] +'">' + sessions[session]['movie'] + '</a></td>');
			tr.append('<td>'+ sessions[session]['age_limit'] +'</td>');
			tr.append('<td>' + sessions[session]['format'] + '</td>');
			tr.append('<td>' + sessions[session]['session_date'] + '</td>');
			tr.append('<td><a href="'+ sessions[session]['session_url'] +'" class="btn btn-outline-success">'+ sessions[session]['start_time'] +'</a></td>');

		}
	};


	this.render_select_movies = function(movies){
		let selected_movie = $('#selectMovies').children(':selected').attr('value');
		$('#selectMovies').children().remove();
		$('#selectMovies').append('<option value="null" selected>Выбрать фильм</option>');
		for(movie of movies){
			if(movie['pk'] == selected_movie){
				$('#selectMovies').append('<option value="'+ movie['pk'] +'" selected>'+ movie['name'] +'</option>');
			}else{
				$('#selectMovies').append('<option value="'+ movie['pk'] +'">'+ movie['name'] +'</option>');
			}
			
		}
	}
};
