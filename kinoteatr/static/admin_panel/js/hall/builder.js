function set_style(){
	let buttons = $('button[id*="button_row_"]'); // get all buttons whose id contains 'button_row'
	for(button of buttons){
		$(button).addClass('scheme_button_free'); // add css class for each button
	};

};

function Builder(schema, render_obj){
	let event_manager = new EventManager(set_style, set_event); // create new object EventManager
	let render = new render_obj(schema); // create new object - renderSchema
	this.schema = schema; 

	this.render_schema = function(){
		//  Render default schema without any dev tools
		render.render_schema();
		set_style();
		event_manager.set_seats_amount();
	};

	this.render_schema_tools = function(){
		// render remove button s
		let incrementor = 0;
		for(row in schema){
			let row_id = 'row_' + incrementor;
			render.render_remove_button(row_id, event_manager, render);
			incrementor ++;
		}
	};


	this.build_schema_for_interact = function(){
		// render schema for build 
		this.render_schema();
		this.render_schema_tools();
		set_style();
		set_event();
		event_manager.set_seats_amount();
	};

	this.saveSchema = function(){
		let scheme_input = $('#schema_json'); // hidden input for django form to save json in db
		let parent_div = $('#scheme_builder'); // div with all roes
		let scheme_obj = {};
		let rows = $('div[id*=row_]'); // get all wors which contain 'row_' in id field
		for(row of rows){ // iterator over all rows
			let seats = [];
			for(child of $(row).children('button[id*="button_row_"]')){
				if(!$(child).hasClass('scheme_button_selected')){ // if buttons is not selected, add it to list of seats
					seats.push(1);
				}else{
					seats.push(0);
				}
			}
			scheme_obj[$(row).attr('id')] = seats; // set row id as a key for object

		}
		json_schema = JSON.stringify(scheme_obj) // stringify js object to json
		scheme_input.attr('value', json_schema); // set attr for hidden input 
		parent_div.prepend('Схема сохранена!');
	};

	function set_event(){
		let buttons = $('button[id*="button_row_"]');
		$(buttons).each(function(index, item){
			$(item).off('click'); // disable previous event. Otherwise event can`t be raised more than once
			$(item).on('click', function(){
				event_manager.selected_button_event(item);
			});
		});
	};

};


function EventManager(set_style, set_event){
	this.set_style = set_style;
	this.set_event = set_event;

	this.delete_row_event = function(row_id, render){
		$('#'+row_id).remove(); // remove row with specific id 
		this.set_seats_amount(); // update amount of seats

		this.recalculate_rows_id(render); // SEE comment for this function for details

		$('.schema_row_number').remove(); // remove all buttons with numbers
		render.render_row_number(); // render buttons with numbers
		if($('div[id*=row_]').length < 21){
			if(!render.check_if_elem_exists('addRowButton')){ // if this button is already exist, pass. Otherwire - render it
				render.render_add_button(this, render);
			}
		}

 	};

 	this.add_row_event = function(render){
 		try {
			var last_row_id = $('div[id*=row_]').last().attr('id').split('_')[1]; // get id number of last elem. 'row_10' -> '10'
		 } catch (error) { // if there are no any rows
			 var last_row_id = -1; // set id as -1 because next code will increment it by 1
		 }
 		let new_row_id = render.render_row(Number(last_row_id)+1); // render new row

		$('.schema_row_number').remove(); // update buttons with numbers
		render.render_row_number();
 		
 		for(i=0; i<=20; i++){
 			render.render_row_button(new_row_id, i); // render buttons for this row. 
 		};
		this.set_style();
		this.set_event();
		this.set_seats_amount();
		render.render_remove_button(new_row_id, this, render);
	

		$('#addRowButton').remove();
		if($('div[id*=row_]').length < 21){
			render.render_add_button(this, render); // if there are less than 21 buttons, render AddButton
		}
		
 	};

	this.set_seats_amount = function(){
		// there function update amount of seats
		let seats = $('button[id*=button_row_]').length;
		$('#seats_amount').text(seats);
	};

	this.recalculate_rows_id = function(render){
		// after delete row, we have to recalculate id`s of another rows and buttons.
		// If we wont do it, for example, if we delete 'row_12', there will be missing number in row ids
		// If we add new row, we will see wrong numbers 

		let rows = $('div[id*=row_]')

		let incrementor = 0;
		for(row of rows){
			let new_id = 'row_' + incrementor; // set new id
			$(row).attr('id', new_id);
			let button = $(row).find('button[id*=button_row_]'); // find all seat buttons in this row
			for(i=0; i<=20; i++){
				$(button[i]).attr('id', 'button_'+new_id+'_'+i); // update id`s
			}

			$(row).find('button[id*=row_delete_row_]').remove(); // remove current delete button in purposes to set new click event
			render.render_remove_button(new_id, this, render);

			incrementor++;
		};
	};

	this.selected_button_event = function(elem){
		// if button already has class 'scheme_button_selected' - delete it. Otherwire - add it. 
		if($(elem).hasClass('scheme_button_selected')){ 
			$(elem).removeClass('scheme_button_selected');
		}else{
			$(elem).addClass('scheme_button_selected');
		}
	};

}