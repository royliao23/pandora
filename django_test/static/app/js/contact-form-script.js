(function($) {
  'use strict';

  $(window).on('load', function() {
    $('#contactForm').submit(function (e) {
      e.preventDefault();

      // get msgSubmit container and clear
      var msgSubmit = $('#msgSubmit');
      msgSubmit.attr('class', 'h3 text-center hidden').text('');

      // submit form
      var form = this;
      $.ajax({
        type: 'POST',
        url: this.getAttribute('action'),
        data: $(this).serialize()
      }).done(function (data) {
        // show message
        msgSubmit.attr('class', 'h3 text-center tada animated text-success').text('Message Submitted!');

        // clear any errors
        $(form).find('.help-block').empty();
      }).fail(function (xhr) {
        var errors = xhr.responseJSON ? xhr.responseJSON.errors : {};
        // show message
        msgSubmit.attr('class', 'h3 text-center text-danger').text('Did you fill in the form properly?');

        // show field errors
        for (var i = 0; i < form.length; ++i) {
          var field = form[i];
          var field_errors = errors[field.name];
          var dom = $(field).next('.help-block').empty();
          if (field_errors) {
            var ul = $('<ul class="list-unstyled"></ul>').appendTo(dom);
            field_errors.forEach(function (error) {
              $('<li>', {text: error.message}).appendTo(ul);
            });
          }
        }
      });
    });
  });
}(jQuery));
