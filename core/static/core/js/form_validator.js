$(window).on('load', function() {
    var inputs = document.getElementsByClassName('form-control'); 
    var validation = Array.prototype.filter.call(inputs, function(input) {
      $(input).blur(function() {
        input.classList.remove('is-invalid')
        input.classList.remove('is-valid')

        if (input.checkValidity() == false || input.value.trim() == "") {
          input.classList.add('is-invalid');
        } else {
          input.classList.add('is-valid')
        }
      });
    });
});