document.getElementById('password_2').addEventListener('input', () => {
    var pass_1 = document.getElementById('password_1').value;
    var pass_2 = document.getElementById('password_2').value;
    var div = document.getElementById('error');
    
    if (pass_1 != pass_2) {
        
        $(div).empty();
        
        var erroTag = document.createElement('p');
        erroTag.setAttribute('class', 'messages');
        erroTag.innerText = 'Senhas não são iguais.'
        div.append(erroTag)
        
        document.getElementById('btn-register').disabled = true;


    } else {
        $(div).empty();
        document.getElementById('btn-register').disabled = false;
    }

} )