//designa gender de hijos y hermanos
function designateGender() {
    var chance = Math.floor((Math.random() * 10) + 1);
    var gender;
    if (chance % 2 == 0) {
        gender = 'female';
    } else {
        gender = 'male';
    }
    return gender
}

//imprime hermanos
function printSibling(tag, objectProperty, containerToAppendTo) {
    if (typeof(objectProperty) == 'string') {
        var gender = designateGender();
        containerToAppendTo.append('<div class="toRemove"><span class="nombreRasgo">' + tag + '(' + gender + '): </span><span>' + objectProperty + '</span></div>');
    }
}

/******************
DATOS QUE SE ENVIAN: No es necesario generarlos todos porque solo envío los que python necesita y recibo otros
******************/
var npcCharacter = {
    "age": null,
    "gender": null,

}