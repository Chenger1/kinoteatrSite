jQuery(document).ready(function($) {
	let radio1 = $('.radio1')
	let radio2 = $('.radio2')
	radio1.click(function(){
		radio2.checked = false;
	})
	radio2.click(function(){
		radio1.checked = false;
	})
});