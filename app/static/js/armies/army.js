define(["backbone", "unit"], function(Backbone, Unit) {
    var Army = Backbone.Collection.extend({
        url: 'units',
        model: Unit,

    });
    return Army;

});