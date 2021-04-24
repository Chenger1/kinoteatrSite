function renderSchema(schema){
	this.parent_div = $('#scheme_builder'); // parent div for all rows
	this.schema = schema; // schema to render

	this.render_schema = function(){
		let incrementor = 0;
		for(row in this.schema){ // iterate over all keys in schema
			let row_id = this.render_row(incrementor); // render row for each key
			

			let row_seats = schema[row]; // get all seast for each row
			if(!row_seats.find(element => element >0)){ // if list of seats include only '0' - all row has to be empty
				$('#'+row_id).addClass('hiddenRow'); // so, add class to recognise it 
			}else if(row_seats.length < 1){ // if list of seats is empty -> row has to be empty 
				$('#'+row_id).addClass('hiddenRow');
			}

			if(row_seats.length < 1){ // if list of seats is empty - add one hidden button to save hall structure
				let button = '<button type="button" style="opacity: 0" disabled class="scheme_button"></button>';
				$('#'+row_id).append(button);
			}else{
				for(i=0; i <= row_seats.length-1; i++){ // iterate over all seats 
					if(row_seats[i] == 1){
						// '1' - means that seat if available for work with.
						// '0' - means empty space
						this.render_row_button(row_id, i);
					}else{ // render hidden button as empty space
						this.render_hidden_button(row_id);
					};
				}

			}	

			incrementor ++;
		};

		this.render_row_number(incrementor);

	};

	this.render_row = function(inc_value){
		// using value from incrementor, render new row and return its id
		let row_id = 'row_' + inc_value;
		let row_div = '<div id="'+row_id+'"></div>';
		this.parent_div.append(row_div);
		return row_id;
	};

	this.render_row_button = function(row_id, inc_value){
		// using row id and incrementor value, render new button in the given row
		let button_id = 'button_' + row_id + '_'+ inc_value;
		let button = '<button type="button" id="'+ button_id +'" class="scheme_button">'+ Number(inc_value+1) +'</button>'
		parent = $('#' + row_id);
		parent.append(button);
	};

	this.render_hidden_button = function(row_id){
		// hidden button -> empty space for visualise hall 
		let button = '<button type="button" style="opacity: 0" disabled class="scheme_button">x</button>';
		$('#'+row_id).append(button);
	}

	this.render_remove_button = function(row_id, event_manager, render){
		// remove button is used in edit_cinema_hall.html page to remove rows
		let row_div = $('#'+row_id);
		let tool_remove_button = '<button type="button" class="schema_button_remove_tool" id="row_delete_'+row_id+'">X</button>'
		row_div.append(tool_remove_button);
		$('#row_delete_'+row_id).on('click', function(){
			event_manager.delete_row_event(row_id, render);
		});
	};

	this.render_add_button = function(event_manager, render){
		// remove button is used in edit_cinema_hall.html page to add rows
		let tool_add_button = '<button type="button" class="schema_button_add_tool" id="addRowButton">+</button>'
		$('#scheme_builder').append(tool_add_button);
		$('#addRowButton').on('click', function(){
			event_manager.add_row_event(render);
		});
	}

	this.check_if_elem_exists = function(elem_id){
		// if element with given id exists - return true, otherwise - false
		if($('#'+elem_id).length){
			return true;
		}else{
			return false
		}
	};

	this.render_row_number = function(){
		let incrementor = 1;

		for(i=0; i<=$('div[id*=row_]').length; i++){
			if($('#row_'+i).hasClass('hiddenRow')){
				// if row has 'hiddenRow' class - render empty buttons as empty space
				var row_number = '<button type="button" class="schema_row_number" style="opacity:0;" disabled></button>'	
			}else{ // otherwise - render button with row number
				var row_number = '<button type="button" class="schema_row_number" disabled>Ряд ' + Number(incrementor) + '</button>'
				incrementor++;
			}
			$('#row_'+ i).prepend(row_number);
		}

	};

}