function buildScheme(scheme, trg){

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
				let button = '<button type="button" style="width: 30px; height: 35px;" id="'+button_id+'" class="scheme_button scheme_button_free"'+
				'>'+ Number(i+1) +'</button>'; // create button tag
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
		$(elem).removeClass('scheme_button_selected')
	}else{
		$(elem).addClass('scheme_button_selected');
	}
};