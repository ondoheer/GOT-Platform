$(document).ready(function() {

    // Función que ata la funcion de click con los elementos aún no creados.
    //para lograrlo llamamos el .on a un elemento ya existente, pero lo atamos a uno
    //que aparecerá después
    $('.dataContainer').on('click', '.removeElement', function() {

        $(this).parent('.toRemove').remove();
    });
    $('.button').on('click', function() {


        /*********
        BORRAMOS TODO EL CONTENIDO DEL GENERADO ANTERIOR
        *********/
        $('.traitsContainer').empty();
        $('.eventsContainer').empty();
        $('.religionContainer').empty();
        $('.spouseContainer').empty();
        $('.descendantsContainer').empty();
        $('.siblingsContainer').empty();
        $('.relativesContainer').empty();
        $('.loverContainer').empty();

        npcCharacter.age = $('#age').val();
        if ($('#male').is(':checked')) {
            npcCharacter.gender = 'male'
        } else if ($('#female').is(':checked')) {
            npcCharacter.gender = 'female'
        } else {
            alert('Please select a gender');
        }

        if ($('#age').val() < 13) {
            alert('minimum age is 13');
        }

        // solo si se han cumplido los requicitos envía la data.
        if (npcCharacter.gender != null && $('#age').val() > 12) {


            /********
             Enviamos el objeto generado en functions.js
            ********/
            $.getJSON('/NPCgenerator', npcCharacter, function(npcReceived) {
                console.log(npcReceived.family);


                /***************
                AGREGAMOS DATOS A LA WEB
                ***************/
                var religion = npcReceived.religion
                var events = npcReceived.events
                var traits = npcReceived.traits
                var family = npcReceived.family


                // Religion
                if (religion.believe != false) {
                    $('.religionContainer').append('<div class="toRemove"><span class="nameTrait"> Faith: </span><span>' + religion.believe + '</span></div>');
                }
                if (religion.level != false) {
                    $('.religionContainer').append('<div class="toRemove"><span class="nameTrait"> Commitment: </span><span>' + religion.level + '</span></div>');
                }

                // traits
                if (traits.special != false) {
                    $('.traitsContainer').append('<div class="toRemove"><span class="nameTrait"> special: </span><span>' + traits.special + '</span></div>');
                }
                if (traits.psychological != false) {
                    $('.traitsContainer').append('<div class="toRemove"><span class="nameTrait"> Pyschological: </span><span>' + traits.psychological + '</span></div>');
                }
                if (traits.physical != false) {
                    $('.traitsContainer').append('<div class="toRemove"><span class="nameTrait"> Physical: </span><span>' + traits.physical + '</span></div>');
                }
                if (traits.motivational != false) {
                    $('.traitsContainer').append('<div class="toRemove"><span class="nameTrait"> motivational: </span><span>' + traits.motivational + '</span></div>');
                }

                // events
                if (events.personal != false) {
                    $('.eventsContainer').append('<div class="toRemove"><span class="nameTrait"> Personal: </span><span>' + events.personal + '</span></div>');
                }
                if (events.family != false) {
                    $('.eventsContainer').append('<div class="toRemove"><span class="nameTrait"> Family: </span><span>' + events.family + '</span></div>');
                }
                if (events.social != false) {
                    $('.eventsContainer').append('<div class="toRemove"><span class="nameTrait"> Social: </span><span>' + events.social + '</span></div>');
                }
                if (events.war != false) {
                    $('.eventsContainer').append('<div class="toRemove"><span class="nameTrait"> At war: </span><span>' + events.war + '</span></div>');
                }
                if (events.money != false) {
                    $('.eventsContainer').append('<div class="toRemove"><span class="nameTrait"> Money: </span><span>' + events.money + '</span></div>');
                }
                if (events.physical != false) {
                    $('.eventsContainer').append('<div class="toRemove"><span class="nameTrait"> Physical: </span><span>' + events.physical + '</span></div>');
                }

                // family
                // siblings
                if (family.siblings != false || family.siblings != 0) {
                    $('.siblingsContainer').append('<div class="toRemove"><span class="nameTrait"> siblings: </span><span>' + family.siblings + '</span></div>');
                    printSibling('sibling 1 ', family.sibling1, $('.siblingsContainer'));
                    printSibling('sibling 2 ', family.sibling2, $('.siblingsContainer'));
                    printSibling('sibling 3 ', family.sibling3, $('.siblingsContainer'));
                    printSibling('sibling 4 ', family.sibling4, $('.siblingsContainer'));
                    printSibling('sibling 5 ', family.sibling5, $('.siblingsContainer'));
                    printSibling('sibling 6 ', family.sibling6, $('.siblingsContainer'));
                    printSibling('sibling 7 ', family.sibling7, $('.siblingsContainer'));
                    printSibling('sibling 8 ', family.sibling8, $('.siblingsContainer'));
                    printSibling('sibling 9 ', family.sibling9, $('.siblingsContainer'));
                    printSibling('sibling 10 ', family.sibling10, $('.siblingsContainer'));

                }
                // spouse
                if (family.spouse != false) {
                    $('.spouseContainer').append('<div class="toRemove"><span class="nameTrait"> spouse: </span><span>' + family.spouse + '</span></div>');
                }
                if (family.spouse2 != false) {
                    $('.spouseContainer').append('<div class="toRemove"><span class="nameTrait"> spouse 2: </span><span>' + family.spouse2 + '</span></div>');
                }
                if (family.spouse3 != false) {
                    $('.spouseContainer').append('<div class="toRemove"><span class="nameTrait"> spouse 3: </span><span>' + family.spouse3 + '</span></div>');
                }
                if (family.spouse4 != false) {
                    $('.spouseContainer').append('<div class="toRemove"><span class="nameTrait"> spouse 4: </span><span>' + family.spouse4 + '</span></div>');
                }
                if (family.spouse5 != false) {
                    $('.spouseContainer').append('<div class="toRemove"><span class="nameTrait"> spouse 5: </span><span>' + family.spouse5 + '</span></div>');
                }
                if (family.spouse6 != false) {
                    $('.spouseContainer').append('<div class="toRemove"><span class="nameTrait"> spouse 6: </span><span>' + family.spouse6 + '</span></div>');
                }
                // lover
                if (family.lover != false) {
                    $('.loverContainer').append('<div class="toRemove"><span class="nameTrait"> lover: </span><span>' + family.lover + '</span></div>');
                }


                // descendants
                if (family.descendants != false || family.descendants != 0) {
                    $('.descendantsContainer').append('<div class="toRemove"><span class="nameTrait"> descendants: </span><span>' + family.descendants + '</span></div>');
                    printSibling('descendant 1 ', family.descendant1, $('.descendantsContainer'));
                    printSibling('descendant 2 ', family.descendant2, $('.descendantsContainer'));
                    printSibling('descendant 3 ', family.descendant3, $('.descendantsContainer'));
                    printSibling('descendant 4 ', family.descendant4, $('.descendantsContainer'));
                    printSibling('descendant 5 ', family.descendant5, $('.descendantsContainer'));
                    printSibling('descendant 6 ', family.descendant6, $('.descendantsContainer'));
                    printSibling('descendant 7 ', family.descendant7, $('.descendantsContainer'));
                    printSibling('descendant 8 ', family.descendant8, $('.descendantsContainer'));
                    printSibling('descendant 9 ', family.descendant9, $('.descendantsContainer'));
                    printSibling('descendant 10 ', family.descendant10, $('.descendantsContainer'));
                }

                // Parientes relatives
                if (family.relatives != false) {
                    $('.relativesContainer').append('<div class="toRemove"><span class="nameTrait"> Ralationship: </span><span>' + family.relatives + '</span></div>');
                }

                $('.nameTrait + span').each(function() {
                    $(this).after('<button class="removeElement">Remove</button>');

                });


            });
        }

    });




});