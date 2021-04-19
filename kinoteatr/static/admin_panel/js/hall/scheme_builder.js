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

function buildScheme(scheme){
	if(!scheme){
		scheme = default_scheme;
	}

	let parent_div = $('#scheme_builder');
	let incrementor = 0;

	for(row in scheme){
		let row_id = 'row_' + incrementor;
		let row_div = '<div id="'+row_id+'"></div>';
		parent_div.append(row_div);

		let row_seats = scheme[row];
		for(i=0; i<=row_seats.length-1; i++){
			let button_id = 'button_' + row_id + '_'+ i;
			let button = '<button type="button" style="width: 20px; height: 25px;" id="'+button_id+'" class="scheme_button"'+
			'></button>';
			parent = $('#'+row_id);
			parent.append(button);
			$('#'+button_id).on('click', function(){
				selectedButton(this);
			});
			if(row_seats[i] == 0){
				$('#'+button_id).addClass('scheme_button_selected');
			}

		}

		incrementor++;
	}

}


function selectedButton(elem){
	if($(elem).hasClass('scheme_button_selected')){
		seats_amount.text(Number(seats_amount.text())+1);
		$(elem).removeClass('scheme_button_selected')
	}else{
		$(elem).addClass('scheme_button_selected');
		seats_amount.text(Number(seats_amount.text())-1);
	}
};

function saveScheme(){
	let scheme_input = $('#schema_json');
	let parent_div = $('#scheme_builder');
	let scheme_obj = {};
	let rows = $('div[id*=row_]');
	for(row of rows){
		let seats = [];
		for(child of $(row).children('button')){
			if($(child).hasClass('scheme_button_selected')){
				seats.push(0);
			}else{
				seats.push(1);
			}
		}
		scheme_obj[$(row).attr('id')] = seats;

	}
	json_schema = JSON.stringify(scheme_obj)
	scheme_input.attr('value', json_schema);
	parent_div.append('Схема сохранена!')
}
