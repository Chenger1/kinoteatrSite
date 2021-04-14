function updateElementAttrForHidden(old_name){
	reg = new RegExp('-[0-9]-'); // create new regular expression

	matching_index = old_name.search(reg) + 1; // search for matching
	new_name = old_name.replace(old_name[matching_index], '0'); 
	// replace old element index with new one
	return new_name;
}

function cloneRow(selector, prefix, form_class, image_prefix){
	let total = $('#id_'+prefix+'-TOTAL_FORMS').val(); // get total number if forms
	let newElement;

	if(total == 0){
		newElement = $('.'+form_class+':first').css('display', 'block'); // show element if it is hide and it is alone
	}else{
		newElement = $(selector).clone(true); // copy element with his event handlers	
	}

	newElement.find(':input:not([type=button]):not([type=submit]):not([type=reset])').each(function(){ 
	// find all inputs which are no 'button, submit, reset'
	// replace the name and id of this inputs with new one to fit in to current forms row
		if(total == 0){
			var name = updateElementAttrForHidden($(this).attr('name')); // update name if last form was hidden
		}else{
			var name = $(this).attr('name').replace('-'+(total-1)+'-', '-'+ total +'-');
		}
		let id = 'id_' + name;
		$(this).attr({'name': name, 'id': id}).val('').removeAttr('checked'); 
		// set new attributtes and remove 'checked' attr to create fresh form
	});

	//find input with type 'file'. This input gets uploaded image in have 'onchange' attr to dynamic update image
	// in template. On change functiion requires current form`s id. So it needs to update it
	newElement.find("input[type='file']").each(function(){
		if(total == 0){
			var onchange_attr = 'setPreview(this, 0, '+ "'"+image_prefix+"'"+')';
			// if this form is alone, set onchange function with 0 index and given image prefix
		}else{
			var onchange_attr = $(this).attr('onchange').replace((total-1), total);	
			// set current index in onchange function 
		}
		
		$(this).attr({'onchange': onchange_attr}); // set new onchange function
	})

	newElement.find('label').each(function(){
	// find label of the current form and repalce it 'for' attr
	// to fit in with new form id
		var forValue = $(this).attr('for');
		if (forValue){
			if(total == 0){
				forValue = forValue.replace('-' + (total-1)+'-', '-'+ '0' + '-');
				// if element is alone, set the label index to 0
			}else{
				forValue = forValue.replace('-' + (total-1)+'-', '-'+ total + '-');
				// update label index for current	
			}
			$(this).attr({'for': forValue}); // set new 'for' attr in label
		};
	});

	// preview img has special name to identify it from other form in formset. 
	// after created new form, we have to update image name too. 
	newElement.find('img').each(function(){
		var nameValue = $(this).attr('name');
		if (nameValue){
			if(total == 0){
				nameValue = image_prefix + '_image_preview_0';
				// if the form is alone, set '0' for its image
			}else{
				nameValue = nameValue.replace('_' + (total-1), '_'+ total);
				// update image name according to new element index	
			}
			
			$(this).attr({'name': nameValue});
		}
		$(this).attr('src', default_image); // set default image from static directory
	})

	// link in block 'btn-tool' can delete existing gallery image if it stores in db
	// if new form has just created, this link has to dynamicly delete new row
	let tool_link = newElement.find('.btn-tool')
	tool_link.attr('href', '')
	tool_link.addClass('delete-' + image_prefix +'-row'); 

	total++;
	$('#id_'+prefix+'-TOTAL_FORMS').val(total); // increment and update TOTAL_FORMS input
	$(selector).after(newElement); // add newElement after last one
	return false;

};


function updateElementIndex(element, prefix, index){
	let id_regex = new RegExp('(' + prefix + '-\\d+)'); // set Regular Expression to find formset inputs
	let replacement = prefix + '-' + index;
	if($(element).attr('for')){ // check 'for' attr and replace it`s value to new one`
		$(element).attr('for', $(element).attr('for').replace(id_regex, replacement));
	}
	if(element.id){
		element.id = element.id.replace(id_regex, replacement); // replace id`s value`
	}
	if (element.name){
		element.name = element.name.replace(id_regex, replacement); // replace element`s name value
	}
}

function deleteForm(prefix, btn, className){
	form_class = '.'+className;

	var total = parseInt($('#id_'+prefix+'-TOTAL_FORMS').val()); // get integer(value) from given formset input - TOTAL FORMS

	if(total == 1){
		btn.closest(form_class).css('display', 'none');
		$('#id_'+prefix+'-TOTAL_FORMS').val(0);
	}else{
		btn.closest(form_class).remove(); // finds nearest form to delete
		var forms = $(form_class);
	    $('#id_'+prefix+'-TOTAL_FORMS').val(forms.length);
	}
	 // update TOTAL_FORMS count according to new value

	for(i=0; i<forms.length; i++){
		$(forms.get(i)).find(':input').each(function(){ // Update All forms according to new value
			updateElementIndex(this, prefix, i);
		});
	};
};

