    $(document).ready(function(){
        $('.desc').each(function(){
            $(this).children().each(function(){
                recursiveIteration(this);
            })
        })
    })

    function recursiveIteration(elem){
        if($(elem).children().length <1){
            setColor(elem);
        }else{
            for(child of $(elem).children()){
                recursiveIteration(child);
            }
        }
    }

    function setColor(elem){
        $(elem).css('color', 'white');
    }