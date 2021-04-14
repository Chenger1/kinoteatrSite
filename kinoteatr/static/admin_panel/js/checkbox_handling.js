jQuery(document).ready(function($) { // waiting for document to be loaded
	let radio1 = $('.radio1') // get elements with selected classes
	let radio2 = $('.radio2')
	radio1.click(function(){ // set click handler for all elements
		radio2.checked = false; // if element clicked, change 'checked' status of another to false
	})
	radio2.click(function(){
		radio1.checked = false;
	})
});