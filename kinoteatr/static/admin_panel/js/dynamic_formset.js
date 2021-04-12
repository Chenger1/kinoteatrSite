function cloneRow(selector, prefix, form_class, image_prefix){
	let newElement = $(selector).clone(true); // copy element with his event handlers
	let total = $('#id_'+prefix+'-TOTAL_FORMS').val(); // get total number if forms

	newElement.find(':input:not([type=button]):not([type=submit]):not([type=reset])').each(function(){ 
	// find all inputs which are no 'button, submit, reset'
	// replace the name and id of this inputs with new one to fit in to current forms row
		let name = $(this).attr('name').replace('-'+(total-1)+'-', '-'+total +'-');
		let id = 'id_' + name;
		$(this).attr({'name': name, 'id': id}).val('').removeAttr('checked'); 
	});

	//find input with type 'file'. This input gets uploaded image in have 'onchange' attr to dynamic update image
	// in template. On change functiion requires current form`s id. So it needs to update it
	newElement.find("input[type='file']").each(function(){
		let onchange_attr = $(this).attr('onchange').replace((total-1), total);
		$(this).attr({'onchange': onchange_attr});
	})

	newElement.find('label').each(function(){
	// find label of the current form and repalce it 'for' attr
	// to fit in with new form id
		let forValue = $(this).attr('for');
		if (forValue){
			forValue = forValue.replace('-' + (total-1)+'-', '-'+ total + '-');
			$(this).attr({'for': forValue});
		};
	});

	// preview img has special name to identify it from other form in formset. 
	// after created new form, we have to update image name too. 
	newElement.find('img').each(function(){
		let nameValue = $(this).attr('name');
		if (nameValue){
			nameValue = nameValue.replace('_' + (total-1), '_'+ total)
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
	let id_regex = new RegExp('(' + prefix + '-\\d+)'); // set Regular Expression
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

	let total = parseInt($('#id_'+prefix+'-TOTAL_FORMS').val()); // get integer(value) from given formset input - TOTAL FORMS
	if(total >1){
		btn.closest(form_class).remove(); // finds nearest form to delete
		let forms = $(form_class);
		$('#id_'+prefix+'-TOTAL_FORMS').val(forms.length); // update TOTAL_FORMS count according to new value

		for(i=0; i<forms.length; i++){
			$(forms.get(i)).find(':input').each(function(){ // Update All forms according to new value
				updateElementIndex(this, prefix, i);
			});
		}
	}
	return false;
}
