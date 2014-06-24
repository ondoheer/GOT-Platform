define(["backbone"], function(Backbone) {
    var ArmyView = Backbone.View.extend({
        el: '#main-app',
        
        events: {
            'click #createButton': 'newUnit',
            'change #power': 'updatePower',
            'change #population': 'updatePopulation',
            'change #wealth': 'updateWealth'
        },
        firstTime: true,
        powerMoney: 0,
        populationMoney: 0,
        wealthMoney: 0,
        initialize: function() {
            this.listenTo(this.collection, 'add', this.addNewUnit);
        },
        updatePower: function() {
            if (this.firstTime) {
                this.powerMoney = $('#power').val();
            }

        },
        updatePopulation: function() {
            if (this.firstTime) {
                this.populationMoney = $("#population").val();
            }
        },
        updateWealth: function() {
            if (this.firstTime) {
                this.wealthMoney = $('#wealth').val();
            }
        },
        newUnit: function(e) {
            e.preventDefault;
            var name = $("#create").val();
            var unitType = $('#unit-type').val();
            var training = $('#training').val();
            var discipline = 0,
                experience = 0,
                power = 0,
                population = 0,
                wealth = 0,
                skills;
            switch (training) {
                case 'green':
                    discipline = 1;
                    experience = 20;
                    break;
                case 'trained':
                    discipline = 3;
                    experience = 60;
                    break;
                case 'veteran':
                    discipline = 5;
                    experience = 100;
                    break;
                case 'elite':
                    discipline = 7;
                    experience = 140;
                    break;
                default:
                    discipline = 0;
                    experience = 0;
            }
            switch (unitType) {
                case 'archers':
                    power = 3;
                    population = 0;
                    wealth = 0;
                    discipline += 3;
                    skills = {
                        1: 'Agility',
                        2: 'Awareness',
                        3: 'Marksmanship'
                    };
                    break;
                case 'cavalry':
                    power = 5;
                    population = 0;
                    wealth = 0;
                    discipline -= 3;
                    skills = {
                        1: 'Agility',
                        2: 'Animal Handling',
                        3: 'Fighting'
                    };
                    break;
                case 'criminals':
                    power = 1;
                    population = 0;
                    wealth = 0;
                    discipline += 6;
                    skills = {
                        1: 'Endurance',
                        2: 'Stealth',
                        3: 'Fighting'
                    };
                    break;
                case 'crusaders':
                    power = 4;
                    population = 0;
                    wealth = 0;
                    skills = {
                        1: 'Athletics',
                        2: 'Endurance',
                        3: 'Fighting'
                    };
                    discipline += 0;
                    break;
                case 'engineers':
                    power = 2;
                    population = 0;
                    wealth = 0;
                    skills = {
                        1: 'Warfare',
                        2: 'Endurance',
                        3: 'Fighting'
                    };
                    discipline += 3;
                    break;
                case 'garrison':
                    power = 2;
                    population = 0;
                    wealth = 0;
                    skills = {
                        1: 'Awareness',
                        2: 'Endurance',
                        3: 'Fighting'
                    };
                    discipline += 3;
                    break;
                case 'guerrillas':
                    power = 2;
                    population = 0;
                    wealth = 0;
                    skills = {
                        1: 'Athletics',
                        2: 'Marksmanship',
                        3: 'Stealth'
                    };
                    discipline += 3;
                    break;
                case 'infantry':
                    power = 4;
                    population = 0;
                    wealth = 0;
                    skills = {
                        1: 'Athletics',
                        2: 'Endurance',
                        3: 'Fighting'
                    };
                    discipline += 0;
                    break;
                case 'mercenaries':
                    var mercTraining = {
                        green: 1,
                        trained: 3,
                        veteran: 6,
                        elite: 9
                    }
                    power = 1;
                    population = 0;
                    wealth = mercTraining[training];
                    skills = {
                        1: 'Athletics',
                        2: 'Endurance',
                        3: 'Fighting'
                    };
                    discipline += 3;
                    break;
                case 'peasants':
                    power = 0;
                    population += 2;
                    wealth = 0;
                    skills = {
                        1: 'Animal Handling',
                        2: 'Awareness',
                        3: 'Survival'
                    };
                    discipline += 6;
                    break;
                case 'personal':
                    power = 6;
                    population = 0;
                    wealth = 0;
                    skills = {
                        1: 'Athletics',
                        2: 'Endurance',
                        3: 'Fighting'
                    };
                    discipline -= 6;
                    break;
                case 'raiders':
                    power = 3;
                    population = 0;
                    wealth = 0;
                    skills = {
                        1: 'Agility',
                        2: 'Endurance',
                        3: 'Fighting'
                    };
                    discipline += 3;
                    break;
                case 'sailors':
                    power = 4;
                    population = 0;
                    wealth = 0;
                    skills = {
                        1: 'Agility',
                        2: 'Awareness',
                        3: 'Fighting'
                    };
                    discipline += 0;
                    break;
                case 'scouts':
                    power = 2;
                    population = 0;
                    wealth = 0;
                    skills = {
                        1: 'Awareness',
                        2: 'Endurance',
                        3: 'Stealth'
                    };
                    discipline += 3;
                    break;
                case 'special':
                    power = 4;
                    population = 0;
                    wealth = 0;
                    skills = {
                        1: '',
                        2: '',
                        3: ''
                    };
                    discipline += 0;
                    break;
                case 'support':
                    power = 2;
                    population = 0;
                    wealth = 0;
                    skills = {
                        1: 'Animal Handling',
                        2: 'Endurance',
                        3: 'Healing'
                    };
                    discipline += 3;
                    break;
                case 'warships':
                    power = 7;
                    population = 0;
                    wealth = 0;
                    skills = {
                        1: 'Awareness',
                        2: 'Fighting',
                        3: 'Marksmanship'
                    };
                    discipline += 0;
                    break;
                default:
                    power = 0;
                    population = 0;
                    wealth = 0;
                    discipline = 0;
            }
            this.collection.add({
                unitName: name,
                type: unitType,
                training: training,
                discipline: discipline,
                experience: experience,
                cost: {
                    power: power,
                    wealth: wealth,
                    population: population
                },
                skills: skills
            });
        },
        addNewUnit: function(model, collection) {
            if (this.firstTime) {

                this.firstTime = false;
            }

            if (this.powerMoney < model.get('cost').power) {
                alert('it seems you ran out of Power...');
                return;
            }
            if (this.populationMoney < model.get('cost').population) {
                alert("You don't seemt o have enough peasants to sacrifice!");
                return;
            }
            if (this.wealthMoney < model.get('cost').wealth) {
                alert("Your house has run out of money...maybe it's time to collect some more taxes!");
                return;
            }

            console.log(this.powerMoney, this.populationMoney, this.wealthMoney);
            console.log(this.populationMoney, model.get('cost').population, this.wealthMoney, model.get('cost').wealth);
            this.powerMoney -= model.get('cost').power;
            this.populationMoney -= model.get('cost').population;
            this.wealthMoney -= model.get('cost').wealth;




            this.$el.find('#costs').html('<h4>Remaining</h4><span><strong>Power: </strong></span>' +
                '<span>' + this.powerMoney + ' </span>' +
                '<span><strong>Population: </strong></span>' +
                '<span>' + this.populationMoney + ' </span>' +
                '<span><strong>Wealth: </strong></span>' +
                '<span>' + this.wealthMoney + ' </span>');

            // }

            this.$el.find('#army').append('<div class="unit">' +
                '<li><strong>Name: </strong>' + model.get('unitName') +
                '</li><li><strong>type: </strong>' + model.get('type') +
                '</li><li><strong>training: </strong>' + model.get('training') +
                '</li><li><strong>discipline: </strong>' + model.get('discipline') +
                '</li><li><strong>experience: </strong>' + model.get('experience') +
                '</li><li><strong>cost:</li><li></strong> power: ' + model.get('cost').power +
                '</li><li> wealth: ' + model.get('cost').wealth +
                '</li><li> population: ' + model.get('cost').population +
                '</li><li> <strong>skills:</li><li></strong>' + model.get('skills')['1'] +
                '</li><li>' + model.get('skills')['2'] +
                '</li><li>' + model.get('skills')['3'] +
                '</div>');

        },


    });
    return ArmyView;
});