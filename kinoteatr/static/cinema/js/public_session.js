function publicSession(schema, renderSchema, style, 
	reserved_tickets, ticket_price, session, cinema_hall_pk){
	let schema_render = new renderSchema(schema);
	let price = Number(ticket_price);
	let session_pk = session;
	let reserved_tickets_list = reserved_tickets;
	this.schema = schema;
	this.style = style;


	this.send_request = function(url, tickets){
		callback = this;

		$.ajax({
			method: 'GET', 
			url: url,
			data: { 'tickets': JSON.stringify(tickets),
					'session': session,
					'cinema_hall_pk': cinema_hall_pk},
			success: function(response){
				$('#scheme_builder').text('');
				$('#tickets').text('0');
				$('#total').text('0');
				schema_render = new renderSchema(response['schema']);
				reserved_tickets_list = response['reserved_tickets'];
				callback.render_schema();
			}
		})
	}
	

	this.render_schema = function(){
		schema_render.render_schema();
		this.set_events();
		this.style();
		this.build_session_tickets();
	}

	this.set_events = function(){
		let buttons = $('button[id*="button_row_"]');
		$(buttons).each(function(index, item){
			$(this).off('click'); // disable previous event. Otherwise event can`t be raised more than once
			$(this).on('click', function(){
				selected_button_event(this)

			});
		});
	}

	this.set_button_event = function(url){
		tickets = this.collect_selected_tickets();
		if(jQuery.isEmptyObject(tickets)){
			return;
		}
		this.send_request(url, tickets);

	}

	this.collect_selected_tickets = function(){
		let result = {};
		$('.scheme_button_selected').each(function(){
			row = $(this).parent()

			if($(row).attr('value') in result){
				result[$(row).attr('value')].push($(this).val());
			}else{
				result[$(row).attr('value')] = [];
				result[$(row).attr('value')].push($(this).val());
			}
		});
		return result;
	}

	function selected_button_event(item){
		let tickets =  $('#tickets');
		let total =  $('#total');
		// if button already has class 'scheme_button_selected' - delete it. Otherwire - add it. 
		if($(item).hasClass('scheme_button_selected')){ 
			tickets.text(Number(tickets.text()) - 1);
			total.text(Number(total.text()) - price);
			$(item).removeClass('scheme_button_selected');
		}else{
			tickets.text(Number(tickets.text()) + 1);
			total.text(Number(total.text()) + price);
			$(item).addClass('scheme_button_selected');
		}
	}

	this.build_session_tickets = function(){
		for(row in reserved_tickets_list){ // iterate over keys in object
			let row_div = $('#'+row); // find row by id

			for(seat of reserved_tickets_list[row]){ // iterate over values of a given key
				let button = $(row_div).find('#button_'+row+'_'+seat['seat_number']); // find specific button 
				button.removeClass('scheme_button_free'); // remove an extra class
				button.off(); // disable an extra event listener
				button.addClass('reserved_button'); // add css class
			};
		};
	}

}