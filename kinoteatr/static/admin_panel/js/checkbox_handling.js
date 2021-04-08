const radio1 = document.getElementById('radio1') // get radio buttons
const radio2 = document.getElementById('radio2')

radio1.addEventListener('change', function (){ // set listening for event - 'change'
    if(this.checked){
        radio2.checked = false; // set radio = false if another radio button is checked
    }
});
radio2.addEventListener('change', function (){
    if(this.checked){
        radio1.checked = false;
    }
});