function handleMovie(pk, name, img_path){
    let my_modal = $('#movieModal'); 
    let chosen_movie = $('#chose_movie');
    let selected_movie = $('#selected_movie')
    let movie_image = $('#show_main_image');
    // get block and elements


    $(chosen_movie).text(name); // set text for this element
    $(selected_movie).attr('value', pk); // set value
    $(movie_image).attr('src', img_path); // set image path
}


function buildSessionTickets(tickets){ // tickets is a js object in format {'row_0': [{'seats_number': 1, 'ticker_state': 0, 'ticket_pk': 1}]
	for(row in tickets){ // iterate over keys in object
		let row_div = $('#'+row); // find row by id

		for(seat of tickets[row]){ // iterate over values of a given key
			let button = $(row_div).find('#button_'+row+'_'+seat['seat_number']); // find specific button 
			button.removeClass('scheme_button_free'); // remove an extra class
			button.off(); // disable an extra event listener
			if(seat['ticket_state'] == 0){ // if state == 0 -> ticket is reserved
				button.addClass('reserved_button'); // add css class
				button.on('click', function(){
					addButtonClass(this); // add exent for manage reverting option
				})
			}else if(seat['ticket_state'] == 1){ // if ticket state = 1 -> ticket has been bought
				button.addClass('bought_button'); // add css class
			}

			button.attr('value', seat['ticket_pk']); // for every button add ticket pk 

		};
	};
};

function addButtonClass(button){
	if($(button).hasClass('to_revert')){ // add or remove class for manage reverting ticket option 
		$(button).removeClass('to_revert');
	}else{
		$(button).addClass('to_revert');
	}
}