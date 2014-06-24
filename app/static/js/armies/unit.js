define(["backbone"], function(Backbone) {
    var Unit = Backbone.Model.extend({
        urlRoot: '/units',
        defaults: {
            unitName: '',
            type: '',
            cost: {},
            training: '',
            experience: 0,
            discipline: undefined,
            skills: {},
            weapons: ''

        },
        validate: function(attrs, options) {
            var validationErrors = [];
            if (attrs.unitName.length > 0) {
                validationErrors.push("No name Entered");
                alert("No name entered");
            }
            if (attrs.type.length || attrs.training.length < 1) {
                validationErrors.push("You haven't selected type or training");

            }

            if (validate.length > 0) {
                return validationErrors;
            }

        },

    });
    return Unit;
});