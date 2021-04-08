function readURLSTATIC(input, image_id) {
  if (input.files && input.files[0]) {// check if there are any files in input
    var reader = new FileReader(); // initiate FileReader obj to get info about fle

    reader.onload = function(e) {
      $('#'+image_id).attr('src', e.target.result); // set new image for img tag by changing image src
    }

    reader.readAsDataURL(input.files[0]); // convert to base64 string
  }
}
