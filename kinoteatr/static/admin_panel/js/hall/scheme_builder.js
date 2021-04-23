var default_scheme = {  "row_0": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
						"row_1": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
						"row_2": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
						"row_3": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
						"row_4": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
						"row_5": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
						"row_6": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
						"row_7": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
						"row_8": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
						"row_9": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
						"row_10": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
						"row_11": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
						"row_12": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
						"row_13": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
						"row_14": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
						"row_15": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
						"row_16": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
						"row_17": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
						"row_18": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
						"row_19": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
						"row_20": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
					}

function buildScheme(scheme, trg){
	if(!scheme){
		scheme = default_scheme;
	}

	let parent_div = $('#scheme_builder'); // div when row will be created
	let incrementor = 0; // to set unique id for each row

	for(row in scheme){
		let row_id = 'row_' + incrementor;
		let row_div = '<div id="'+row_id+'"></div>';
		parent_div.append(row_div);
		// create new row and append it no scheme_builder div

		let row_seats = scheme[row]; // gets all seats in this row
		if(row_seats.length<1){ // if row is empty, creates empty button with opacity = 0
				let button = '<button type="button" style="opacity: 0" disabled></button>';
				$('#'+row_id).append(button);
		}else{
			for(i=0; i<=row_seats.length-1; i++){
				let button_id = 'button_' + row_id + '_'+ i; // id for button
				let button = '<button type="button" style="width: 20px; height: 25px;" id="'+button_id+'" class="scheme_button scheme_button_free"'+
				'></button>'; // create button tag
				parent = $('#'+row_id); // get parent
				parent.append(button); // add button to parent bloc
				if(!trg){ // if not trg - ad onChange event for eact button
					$('#'+button_id).on('click', function(){
						selectedButton(this);
					});
				}

			}
		}

		incrementor++;
	}

}


function selectedButton(elem){
	// if elemt has 'selected' class - remove it. Another, add it 
	if($(elem).hasClass('scheme_button_selected')){
		seats_amount.text(Number(seats_amount.text())+1); // increase amount of seats
		$(elem).removeClass('scheme_button_selected')
	}else{
		$(elem).addClass('scheme_button_selected');
		seats_amount.text(Number(seats_amount.text())-1); // reduce amount of seats
	}
};

function saveScheme(){
	let scheme_input = $('#schema_json'); // hidden input for django form to save json in db
	let parent_div = $('#scheme_builder'); // div with all roes
	let scheme_obj = {};
	let rows = $('div[id*=row_]'); // get all wors which contain 'row_' in id field
	for(row of rows){ // iterator over all rows
		let seats = [];
		for(child of $(row).children('button')){
			if(!$(child).hasClass('scheme_button_selected')){ // if buttons is not selected, add it to list of seats
				seats.push(1);
			}
		}
		scheme_obj[$(row).attr('id')] = seats; // set row id as a key for object

	}
	json_schema = JSON.stringify(scheme_obj) // stringify js object to json
	scheme_input.attr('value', json_schema); // set attr for hidden input 
	parent_div.append('Схема сохранена!')
}
