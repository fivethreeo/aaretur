$(function(){
    
    var Deltager = Backbone.Model.extend({
        defaults: function() {
            return {
                navn: 'Navn',
                fodselsdato: new Date()
            };
        }
    });
        
    var DeltagerList = Backbone.Collection.extend({
        model: Deltager
    });
    
    var Deltagere = new DeltagerList;
       
    var DeltagerForm = Backbone.Form.extend({
        schema: {
            navn:       'Text',
            fodselsdato:   'Date'
        }     
    });
    
    var DeltagerView = Backbone.View.extend({
        
        tagName: 'tr',
        
        template: _.template($('#deltager-template').html()),
            
        initialize: function() {
    
            this.listenTo(this.model, 'change', this.render);
            this.listenTo(this.model, 'destroy', this.remove);

        },
        
        render: function() {
            this.$el.html(this.template(this.model.toJSON()));
            return this;
        }
    });      
    
    var DeltagerListView = Backbone.View.extend({
        
        template: _.template($('#deltager-list-template').html()),
            
        initialize: function() {
            this.render()
    
            this.listenTo(Deltagere, 'add', this.addOne);
            this.listenTo(Deltagere, 'reset', this.addAll);

            Deltagere.add(new Deltager)
            Deltagere.add(new Deltager)
            Deltagere.add(new Deltager)

        },
    
        addOne: function(deltager) {
          var view = new DeltagerView({model: deltager});
          this.$('.deltagere-list').append(view.render().el);
        },
        
        addAll: function() {
          Deltagere.each(this.addOne, this);
        },
        
        render: function() {
            this.$el.html(this.template({}));
            return this;
        }
    });  
       
    var AppView = Backbone.View.extend({
        el: 'body',
    
        template: _.template($('#app-template').html()),
    
        render: function() {
            this.$el.html(this.template({}));
            return this;
        },
        
        initialize: function() {
            this.render()
            var self = this
            new DeltagerListView({el:self.$(".deltagere")})
        }      
    })
    
    var App = new AppView;
  
});