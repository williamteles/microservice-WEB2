
// mask cpf 
$(document).ready(function(){
    $("#cpf").mask("999.999.999-99");
});

//mask dinero
$(document).ready(function(){
    $(money).mask("#.##0,00", {reverse: true});
})

//maks dinero tag <p>