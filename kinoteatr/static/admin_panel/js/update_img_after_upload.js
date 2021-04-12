function setPreview(input, form_id, prefix){
  if(input.files && input.files[0]){
    let reader = new FileReader();

    reader.onload = function(e){
      $('img[name="'+ prefix + '_image_preview_' + form_id+'"]').attr('src', e.target.result);
    };

    reader.readAsDataURL(input.files[0]);
  };
};
