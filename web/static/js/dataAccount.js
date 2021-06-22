$(document).ready(function() {

    $('#extrato-div').on('click', function(){

        $.ajax({

            type: 'GET',
            url: 'ajax/extrato/',
            data: {extrato: $('extrato-id').val()},
            success: function(response){
                console.log(response);
            }
        });
    });
});