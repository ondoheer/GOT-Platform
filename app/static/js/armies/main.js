require(['controller',
        'jquery',
        'underscore',
        'backbone'
    ],
    function(Controllers, jquery, underscore, backbone) {
        console.log('cargué con require');
        var view = new Controllers.ArmyView({
            collection: new Controllers.Army()
        });

        Backbone.history.start();

    });