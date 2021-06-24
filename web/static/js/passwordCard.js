document.getElementById('password_1').addEventListener('input', () => {
    var password = parseInt(document.getElementById('password_1').value);
    const div = document.getElementById('error');
    
    if (Object.is(password,NaN)) {
        
        $(div).empty();
        
        var erroTag = document.createElement('p');
        erroTag.setAttribute('class', 'messages');
        erroTag.innerText = 'Senha do cartão só pode conter números.';
        div.append(erroTag);
        
        document.getElementById('btn-register').disabled = true;

    } else {
        $(div).empty();
        document.getElementById('btn-register').disabled = false;
    }

} )
