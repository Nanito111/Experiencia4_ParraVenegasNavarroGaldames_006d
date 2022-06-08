$(document).ready(function() {
    // Validación del nombre
    $("#name").keyup(function() {
      nameValidation();
      submitValidation();
    });

    // Validación del nombre
    $("#asunto").keyup(function() {
        asuntoValidation();
        submitValidation();
    });

    // Validación del mensaje
    $("#message").keyup(function() {
      messageValidation();
      submitValidation();
    });
  
    // Validación del correo electrónico
    $("#email").keyup(function() {
      mailValidation();
      submitValidation();
    });
  
    function nameValidation() {
      $("#name").removeClass('is-valid');
      $("#name").removeClass('is-invalid');
  
      if ( $("#name").val().match(/^$/g)) {
        $("#name").addClass('is-invalid');
      }
      else if ( $("#name").val().match(/^.{64,}$/g)) {
        $("#name").addClass('is-invalid');
      }
      else if ($("#name").val().match(/^\S+(?: \S+)*$/g) == null) {
        $("#name").addClass('is-invalid');
      }
      else if ($("#name").val().match(/\d+/g) != null) {
        $("#name").addClass('is-invalid');
      }
      else {
        $("#name").addClass('is-valid');
      }
    }

    function asuntoValidation() {
        $("#asunto").removeClass('is-valid');
        $("#asunto").removeClass('is-invalid');
    
        if ( $("#asunto").val().match(/^$/g)) {
          $("#asunto").addClass('is-invalid');
        }
        else if ( $("#asunto").val().match(/^.{64,}$/g)) {
          $("#asunto").addClass('is-invalid');
        }
        else if ($("#asunto").val().match(/^\S+(?: \S+)*$/g) == null) {
          $("#asunto").addClass('is-invalid');
        }
        else {
          $("#asunto").addClass('is-valid');
        }
      }
  
    function messageValidation(){
      $("#message").removeClass('is-valid');
      $("#message").removeClass('is-invalid');
  
      if ( $("#message").val().match(/^$/g)) {
        $("#message").addClass('is-invalid');
      }
      else if ( $("#message").val().match(/^.{64,}$/g)) {
        $("#message").addClass('is-invalid');
      }
      else if ($("#message").val().match(/^\S+(?: \S+)*$/g) == null) {
        $("#message").addClass('is-invalid');
      }
      else {
        $("#message").addClass('is-valid');
      }
    }
  
    function mailValidation() {
      $("#email").removeClass('is-valid');
      $("#email").removeClass('is-invalid');
  
      if ( $("#email").val().match(/^$/g)) {
        $("#email").addClass('is-invalid');
        $(".email.invalid-feedback").text("Debes completar este campo");
      }
      else if ($("#email").val().match(/^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])/g) == null) {
        $("#email").addClass('is-invalid');
        $(".email.invalid-feedback").text("El correo electrónico no es válido");
      }
      else if ($("#email").val().match(/^.{100,}$/g) != null) {
        $("#email").addClass('is-invalid');
        $(".email.invalid-feedback").text("El correo no puede tener más de 100 caracteres");
      }
      else if ($("#email").val().match(/^\S+(?: \S+)*$/g) == null) {
        $("#email").addClass('is-invalid');
        $(".email.invalid-feedback").text("El correo no empezar ni terminar con espacios");
      }
      else {
        $("#email").addClass('is-valid');
      }
    }
  
    function submitValidation () {
      if (!$("#name").hasClass('is-valid')) {
        $("#submit").attr("disabled", true);
      }
      else if (!$("#email").hasClass('is-valid')) {
        $("#submit").attr("disabled", true);
      }
      else if (!$("#asunto").hasClass('is-valid')) {
        $("#submit").attr("disabled", true);
      }
      else if (!$("#message").hasClass('is-valid')) {
        $("#submit").attr("disabled", true);
      }
      else{
        $("#submit").removeAttr("disabled");
      }
    }
  });
  
  