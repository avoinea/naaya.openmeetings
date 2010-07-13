(function(){

jQuery.fn.openmeetings = function(settings){
  var self = this;
  self.options = {
    initialize: function(){
      var parent = self.parent();
      self.fullscreen = false;

      self.width(parent.width());
      self.height(parent.height() - 20);

      var buttons = jQuery('.buttons', self);
      jQuery('.fullscreen', buttons).click(function(){
        var button = jQuery(this);
        self.options.resize(button);
        return false;
      });
    },

    resize: function(button){
      if(!self.fullscreen){
        self.fullscreen = true;
        self.addClass('meetings-fullscreen');
        self.width(jQuery(window).width());
        self.height(jQuery(window).height() - 20);

        button.addClass('exit-fullscreen');
        button.text('Exit fullscreen');

      }else{
        self.fullscreen = false;
        self.removeClass('meetings-fullscreen');
        self.width(self.parent().width());
        self.height(self.parent().height() - 20);

        button.removeClass('exit-fullscreen');
        button.text('Fullscreen');
      }
    }
  };

  if(settings){
    jQuery.extend(self.options, settings);
  };

  self.options.initialize();
  return this;
};

})();
