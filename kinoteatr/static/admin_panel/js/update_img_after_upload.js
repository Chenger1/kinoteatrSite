function setPreview(input, form_id, prefix){
  if(input.files && input.files[0]){ // check if input widget uploads any files
    let reader = new FileReader(); // create new instance of FileReader object

    reader.onload = function(e){ // set function to onload handler to set new image preview
      $('img[name="'+ prefix + '_image_preview_' + form_id+'"]').attr('src', e.target.result);
      // build image name using formset prefix in form_id. It needs to have unique name for every image and its input
    };

    reader.readAsDataURL(input.files[0]); 
    // read data as a base64 coded url. It needs to put src to image element
  };
};
