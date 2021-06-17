let transition = document.getElementById('transacao');

transition.addEventListener('change', () => {

    switch(transition.value) {

        case 'pagamento':

            $('#transition-div-row').empty();

            var rowNode = document.getElementById('transition-div-row');
            
            var colNode = document.createElement('div');
            colNode.setAttribute('class', 'col-md-6');
            rowNode.append(colNode)

            var valorLabel = document.createElement('label');
            valorLabel.innerHTML = 'Valor da Fatura';
            colNode.append(valorLabel);

            var valor = document.createElement('input');
            valor.setAttribute('class', 'form-control');
            valor.setAttribute('value', 'R$ 500,00');
            colNode.append(valor)
            
            var col2Node = document.createElement('div');
            col2Node.setAttribute('class', 'col-md-6');
            col2Node.setAttribute('style', 'padding-top:15px');
            rowNode.append(col2Node);

            var formPagar = document.createElement('form');
            formPagar.setAttribute('style','margin-top:10px');
            formPagar.setAttribute('method', 'POST');
            col2Node.append(formPagar);

            var formRow = document.createElement('div');
            formRow.setAttribute('class', 'row');
            formPagar.append(formRow);

            var colInput = document.createElement('div');
            colInput.setAttribute('class', 'col-md-5');
            formRow.append(colInput);

            var inputpagar = document.createElement('input');
            inputpagar.setAttribute('class', 'form-control');
            inputpagar.setAttribute('type', 'number');
            colInput.append(inputpagar);

            var colButton = document.createElement('div');
            colButton.setAttribute('class','col-md-5');
            formRow.append(colButton);

            var btnpagar = document.createElement('button');
            btnpagar.setAttribute('class', 'btn-fibo-1');
            btnpagar.setAttribute('style', 'width: 100px')
            btnpagar.innerHTML = 'Pagar'
            colButton.append(btnpagar);

            document.getElementById('transition-div').append(rowNode);

            break;

        case 'deposito':

            $('#transition-div-row').empty();

            break;
        
        case 'transferencias':

            $('#transition-div-row').empty();

            break;
    
        default:
            break;
    }
});


