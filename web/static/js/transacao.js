let transition = document.getElementById('transacao');

transition.addEventListener('change', () => {

    switch(transition.value) {

        case 'pagamento':

            document.getElementById('payment').style.display = 'inline';
            document.getElementById('deposit').style.display = 'none';
            document.getElementById('transfer').style.display = 'none';
            document.getElementById('buy').style.display = 'none';
            
            break;
            
        case 'deposito':
                
            document.getElementById('deposit').style.display = 'inline';
            document.getElementById('payment').style.display = 'none';
            document.getElementById('transfer').style.display = 'none';
            document.getElementById('buy').style.display = 'none';

            break;
        
        case 'transferencias':

            document.getElementById('transfer').style.display = 'inline';
            document.getElementById('deposit').style.display = 'none';
            document.getElementById('payment').style.display = 'none';
            document.getElementById('buy').style.display = 'none';

            break;
        
        case 'compra':

            document.getElementById('buy').style.display = 'inline';
            document.getElementById('transfer').style.display = 'none';
            document.getElementById('deposit').style.display = 'none';
            document.getElementById('payment').style.display = 'none';

            break;

        default:
            break;
    }
});


