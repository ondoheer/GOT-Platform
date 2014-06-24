$(document).ready(function() {



    $('#submitHouses').on('click', function() {
        var selectedRealm = $('#selectRealm').val();
        var houseName = $('#houseName').val();
        var houseSize = $('#houseSize').val();
        var houseFoundation = $('#houseFoundation').val();

        /****
       	BORRAMOS EL CONTENIDO PREVIO
       	****/
        /*
        $('#houseStats').empty();
        $('#houseEvents').empty();
        $('#defenseHoldings').empty();
        */
        $('.houseDataSection').each(function() {
            $(this).empty();
        });


        houseData = {
            'name': houseName,
            'realm': selectedRealm,
            'size': houseSize,
            'foundation': houseFoundation
        }
        console.log('envio');
        console.log(houseData);

        /****************
        FUNCION QUE SOLICITA E IMPRIME LA DATA
        ****************/
        $.getJSON('/houseGenerator', houseData, function(receivedData) {
            console.log('recibí:');
            console.log(receivedData);

            $('#houseStats').append('<span class="houseStat houseDefense"> Defense: ' + receivedData.defense + '</span><span class="">Remaining Points:' + receivedData.remainingDefense + '</span><br>');
            $('#houseStats').append('<span class="houseStat houseDefense"> Influence: ' + receivedData.influence + '</span><span class="">Remaining Points:' + receivedData.remainingInfluence + '</span><br>');
            $('#houseStats').append('<span class="houseStat houseDefense"> Lands: ' + receivedData.lands + '</span><br>');
            $('#houseStats').append('<span class="houseStat houseDefense"> Law: ' + receivedData.law + '</span><br>');
            $('#houseStats').append('<span class="houseStat houseDefense"> Population: ' + receivedData.population + '</span><br>');
            $('#houseStats').append('<span class="houseStat houseDefense"> Power: ' + receivedData.power + '</span><br>');
            $('#houseStats').append('<span class="houseStat houseDefense"> Wealth: ' + receivedData.wealth + '</span><br>');


            for (var i = 0; i < receivedData.events.length; i++) {
                $('#houseEvents').append('<span class="houseStat houseEvent"> Event: ' + receivedData.events[i] + '</span><br>');
            }

            for (var j = 0; j < receivedData.defenseHoldings.length; j++) {
                $('#defenseHoldings').append('<span class="defenseHoldings">' + receivedData.defenseHoldings[j] + '</span><br>');
            }
            $('#influenceHoldings').append('<span>Max Head of the House Status: ' + receivedData.maxStatus + '</span><br>');
            for (var i = 0; i < receivedData.influenceHoldings.length; i++) {
                $('#influenceHoldings').append('<span class="influenceHoldings">' + receivedData.influenceHoldings[i] + '</span><br>');
            }





        });
    });

});