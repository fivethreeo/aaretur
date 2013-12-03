$(function(){
    
    var AppView = Backbone.View.extend({
        el: 'body',
    
        template: _.template($('#app-template').html()),
    
        render: function() {
            this.$el.html(this.template({}));
            return this;
        },
        
        initialize: function() {
            this.render()
        }      
    })
    
    var App = new AppView;
  
});