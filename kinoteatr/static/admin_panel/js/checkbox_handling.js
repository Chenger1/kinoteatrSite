const radio1 = document.getElementById('radio1')
const radio2 = document.getElementById('radio2')

radio1.addEventListener('change', function (){
    if(this.checked){
        radio2.checked = false;
    }
});
radio2.addEventListener('change', function (){
    if(this.checked){
        radio1.checked = false;
    }
});