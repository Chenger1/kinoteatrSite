function setPreview(input, form_id, prefix){
  if(input.files && input.files[0]){ // check if input widget uploads any files
    let reader = new FileReader(); // create new instance of FileReader object

    let file_name_length = input.files[0]['name'].length
    if(file_name_length >= 100){
    	 $(document).Toasts('create', {
                class: 'bg-danger',
                title: 'Слишком длинное имя файла',
                body: 'Максимально допустимое имя файла - 100 символов. Сейчас: ' + file_name_length + ' символов'
            })
    	 $(input).val('');
    }else{
    	    reader.onload = function(e){ // set function to onload handler to set new image preview
      		$('img[name="'+ prefix + '_image_preview_' + form_id+'"]').attr('src', e.target.result);
      			// build image name using formset prefix in form_id. It needs to have unique name for every image and its input
    };

	    reader.readAsDataURL(input.files[0]); 
	    // read data as a base64 coded url. It needs to put src to image element
    }


  };
};
