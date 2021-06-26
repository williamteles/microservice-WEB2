
// mask cpf 
$(document).ready(function(){
    $("#cpf").mask("999.999.999-99");
});

//mask dinero
$(document).ready(function(){
    $(money).mask("#.##0,00", {reverse: true});
})

//maks dinero tag <p>
var tag_numero = document.querySelectorAll('.money');

for (var i = 0; i < tag_numero.length; i++){
    var numero = parseFloat(tag_numero[i].innerText);
    var moneyBRL = numero.toLocaleString('pt-br',{style: 'currency', currency: 'BRL'});
    tag_numero[i].innerText = moneyBRL;
}
