function extrato(buttonExtrato) {

    var extratoId = buttonExtrato.id;

    var id = parseInt(extratoId.split('_')[1]);

    $.ajax({

        type: 'GET',
        url: 'ajax/extrato',
        data: {extrato: id},
        success: function(response){
            console.log(response);

            let modalDivNode =  document.getElementById('div-modal-body');

            $(modalDivNode).empty()

            var divRow = document.createElement('div');
            divRow.setAttribute('class','row');
            modalDivNode.append(divRow);

            var divCol = document.createElement('div');
            divCol.setAttribute('class','col-md-6');
            divRow.append(divCol);

            var labelDatetimeNode = document.createElement('label');
            labelDatetimeNode.innerText = 'Data e Hora';
            divCol.append(labelDatetimeNode);

            var dataCompra = document.createElement('p');
            dataCompra.setAttribute('class','form-control');
            dataCompra.innerText = response.date + " - " + response.time;
            divCol.append(dataCompra);


            var divCol2 = document.createElement('div');
            divCol2.setAttribute('class','col-md-6');
            divRow.append(divCol2);

            var labelTypeTransactionNode = document.createElement('label');
            labelTypeTransactionNode.innerText = 'Tipo de transação';
            divCol2.append(labelTypeTransactionNode);

            var typeTransaction = document.createElement('p');
            typeTransaction.setAttribute('class','form-control');
            typeTransaction.innerText = response.type_transaction;
            divCol2.append(typeTransaction);


            if(response.type_transaction === 'Compra') {
                
                var divBuyRow = document.createElement('div');
                divBuyRow.setAttribute('class','row');
                modalDivNode.append(divBuyRow);

                var divCardCol = document.createElement('div');
                divCardCol.setAttribute('class','col-md-8');
                divBuyRow.append(divCardCol);

                var labelCardNode = document.createElement('label');
                labelCardNode.innerText = 'Número do cartão';
                divCardCol.append(labelCardNode);

                var cardNumber = document.createElement('p');
                cardNumber.setAttribute('class','form-control');
                cardNumber.innerText = response.card;
                console.log(response.card)
                divCardCol.append(cardNumber);


                var divCategoryCol = document.createElement('div');
                divCategoryCol.setAttribute('class','col-md-4');
                divBuyRow.append(divCategoryCol);

                var labelCategoryNode = document.createElement('label');
                labelCategoryNode.innerText = 'Tipo de compra';
                divCategoryCol.append(labelCategoryNode);

                var category = document.createElement('p');
                category.setAttribute('class','form-control');
                category.innerText = response.categories;
                divCategoryCol.append(category);
            }
            
            // linha do valor e tipo de pagamento, ou conta transferida
            var divValueRow = document.createElement('div');
            divValueRow.setAttribute('class','row');
            modalDivNode.append(divValueRow)

            if (response.type_transaction === 'Compra') {
                
                var divValeuCol = document.createElement('div');
                divValeuCol.setAttribute('class','col-md-6');
                divValueRow.append(divValeuCol);
    
                var labelValueNode = document.createElement('label');
                labelValueNode.innerText = 'Valor';
                divValeuCol.append(labelValueNode);
    
                var valor = document.createElement('p');
                valor.setAttribute('class','form-control');
                valor.innerText = 'R$ ' + response.value;
                divValeuCol.append(valor);

                var divPaymentTypeCol = document.createElement('div');
                divPaymentTypeCol.setAttribute('class','col-md-6');
                divValueRow.append(divPaymentTypeCol);
    
                var labelPaymentTypeNode = document.createElement('label');
                labelPaymentTypeNode.innerText = 'Tipo de Pagamento';
                divPaymentTypeCol.append(labelPaymentTypeNode);
    
                var paymentType = document.createElement('p');
                paymentType.setAttribute('class','form-control');
                paymentType.innerText = response.payment_type;
                divPaymentTypeCol.append(paymentType);

            } 
            
            else if (response.type_transaction === 'Transferência') {
                divValeuCol = document.createElement('div');
                divValeuCol.setAttribute('class','col-md-6');
                divValueRow.append(divValeuCol);
    
                labelValueNode = document.createElement('label');
                labelValueNode.innerText = 'Valor';
                divValeuCol.append(labelValueNode);
    
                valor = document.createElement('p');
                valor.setAttribute('class','form-control');
                valor.innerText = 'R$ ' + response.value;
                divValeuCol.append(valor);

                var divAccountTransferCol = document.createElement('div');
                divAccountTransferCol.setAttribute('class','col-md-6');
                divValueRow.append(divAccountTransferCol);
    
                var labelAccountTransferNode = document.createElement('label');
                labelAccountTransferNode.innerText = 'Conta de Destino';
                divAccountTransferCol.append(labelAccountTransferNode);
    
                var accountTransfer = document.createElement('p');
                accountTransfer.setAttribute('class','form-control');
                accountTransfer.innerText = response.transfer_account;
                divAccountTransferCol.append(accountTransfer);
            }

           
            else if (response.type_transaction === 'Recebido') {
                
                divValeuCol = document.createElement('div');
                divValeuCol.setAttribute('class','col-md-6');
                divValueRow.append(divValeuCol);
    
                labelValueNode = document.createElement('label');
                labelValueNode.innerText = 'Valor';
                divValeuCol.append(labelValueNode);
    
                valor = document.createElement('p');
                valor.setAttribute('class','form-control');
                valor.innerText = 'R$ ' + response.value;
                divValeuCol.append(valor);

                var divAccountTransferCol = document.createElement('div');
                divAccountTransferCol.setAttribute('class','col-md-6');
                divValueRow.append(divAccountTransferCol);
    
                var labelAccountTransferNode = document.createElement('label');
                labelAccountTransferNode.innerText = 'Conta de Origem';
                divAccountTransferCol.append(labelAccountTransferNode);
    
                var accountTransfer = document.createElement('p');
                accountTransfer.setAttribute('class','form-control');
                accountTransfer.innerText = response.account;
                divAccountTransferCol.append(accountTransfer);
            }

           

            else {
                divValeuCol = document.createElement('div');
                divValeuCol.setAttribute('class','col-md-12');
                divValueRow.append(divValeuCol);

                labelValueNode = document.createElement('label');
                labelValueNode.innerText = 'Valor';
                divValeuCol.append(labelValueNode);

                valor = document.createElement('p');
                valor.setAttribute('class','form-control');
                valor.innerText = 'R$ ' + response.value;
                divValeuCol.append(valor);
            }
           
        }
    });
}