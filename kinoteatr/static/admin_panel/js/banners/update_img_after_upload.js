function readURL(input) {
  if (input.files && input.files[0]) { // check if there are any files in input
    var reader = new FileReader(); // initiate FileReader obj to get info about fle

    reader.onload = function(e) {
      // TODO - Jquery or Xpath for more efficient way to find img
      $(input.parentElement.parentElement.parentElement.parentElement.children[0].children[1]).attr('src', e.target.result);
      // set new image for img tag by changing image src. Because of needing to work with dynamic inline form
      // there is no way to set static 'id' or 'class' for concrete img. So it look for it through nodes
    }

    reader.readAsDataURL(input.files[0]); // convert to base64 string
  }
}

function readURLOld(input) {
  if (input.files && input.files[0]) { // check if there are any files in input
    var reader = new FileReader(); // initiate FileReader obj to get info about fle

    reader.onload = function(e) {
      // TODO - Jquery or Xpath for more efficient way to find img
      $(input.parentNode.parentNode.parentNode.children[0].children[1]).attr('src', e.target.result);
      // set new image for img tag by changing image src. Because of needing to work with dynamic inline form
      // there is no way to set static 'id' or 'class' for concrete img. So it look for it through nodes
    }

    reader.readAsDataURL(input.files[0]); // convert to base64 string
  }
}