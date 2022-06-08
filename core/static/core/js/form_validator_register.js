$(document).ready(function() {
  // Validación del nombre
  $("#first_name").keyup(function() {
    nameValidation("#first_name", ".first_name");
    submitValidation();
  });

  // Validación del apellido
  $("#last_name").keyup(function() {
    nameValidation("#last_name", ".last_name");
    submitValidation();
  });
  
  // Validación del nombre de usuario
  $("#username").keyup(function() {
    usernameValidation();
    submitValidation();
  });

  // Validación del correo electrónico
  $("#email").keyup(function() {
    mailValidation();
    submitValidation();
  });

  // Validación de la contraseña
  $("#password1").keyup(function() {
    password1Validation();
    submitValidation();
  });

   // Validación confirmacion de la contraseña
   $("#password2").keyup(function() {
    password2Validation();
    submitValidation();
  });

  function nameValidation(idElement, classElement) {
    $(idElement).removeClass('is-valid');
    $(idElement).removeClass('is-invalid');

    if ( $(idElement).val().match(/^$/g)) {
      $(idElement).addClass('is-invalid');
      $(classElement+".invalid-feedback").text("Debes completar este campo");
    }
    else if ( $(idElement).val().match(/^.{64,}$/g)) {
      $(idElement).addClass('is-invalid');
      $(classElement+".invalid-feedback").text("El nombre no puede tener más de 64 caracteres");
    }
    else if ($(idElement).val().match(/^\S+(?: \S+)*$/g) == null) {
      $(idElement).addClass('is-invalid');
      $(classElement+".invalid-feedback").text("El nombre no puede empezar ni terminar con espacios");
    }
    else if ($(idElement).val().match(/\d+/g) != null) {
      $(idElement).addClass('is-invalid');
      $(classElement+".invalid-feedback").text("El nombre no puede contener números");
    }
    else {
      $(idElement).addClass('is-valid');
    }
  }

  function usernameValidation() {
    $("#username").removeClass('is-valid');
    $("#username").removeClass('is-invalid');

    if ( $("#username").val().match(/^$/g)) {
      $("#username").addClass('is-invalid');
      $(".username.invalid-feedback").text("Debes completar este campo");
    }
    else if ( $("#username").val().match(/^[a-zA-Z0-9]+$/g) == null) {
      $("#username").addClass('is-invalid');
      $(".username.invalid-feedback").text("El nombre de usuario solo puede contener caracteres alfanuméricos");
    } 
    else if ( $("#username").val().match(/^(\w{3,20})$/g) == null) {
      $("#username").addClass('is-invalid');
      $(".username.invalid-feedback").text("El nombre de usuario debe contener entre 3 a 20 caracteres");
    }
    else {
      $("#username").addClass('is-valid');
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
    else {
      $("#email").addClass('is-valid');
    }
  }

  function password1Validation() {
    $("#password1").removeClass('is-valid');
    $("#password1").removeClass('is-invalid');

    if ( $("#password1").val().match(/^$/g)) {
      $("#password1").addClass('is-invalid');
      $(".password1.invalid-feedback").text("Debes completar este campo");
    }

    else if ($("#password1").val().match(/^.{8,}$/g) == null) {
      $("#password1").addClass('is-invalid');
      $(".password1.invalid-feedback").text("La contraseña debe tener al menos 8 caracteres");
    }
    else if ($("#password1").val().match(/^.{50,}$/g) != null) {
      $("#password1").addClass('is-invalid');
      $(".password1.invalid-feedback").text("La contraseña no puede tener más de 50 caracteres");
    }
    else {
      $("#password1").addClass('is-valid');
    }
  }
  
  function password2Validation() {
    $("#password2").removeClass('is-valid');
    $("#password2").removeClass('is-invalid');

    if ( $("#password2").val() != $("#password1").val()) {
      $("#password2").addClass('is-invalid');
      $(".password2.invalid-feedback").text("La contraseña no es la misma");
    }
    else {
      $("#password2").addClass('is-valid');
    }
  }

  function submitValidation () {
    if (!$("#first_name").hasClass('is-valid')) {
      $("#submit").attr("disabled", true);
    }
    else if (!$("#last_name").hasClass('is-valid')) {
      $("#submit").attr("disabled", true);
    }
    else if (!$("#username").hasClass('is-valid')) {
      $("#submit").attr("disabled", true);
    }
    else if (!$("#email").hasClass('is-valid')) {
      $("#submit").attr("disabled", true);
    }
    else if (!$("#password1").hasClass('is-valid')) {
      $("#submit").attr("disabled", true);
    }
    else if (!$("#password2").hasClass('is-valid')) {
      $("#submit").attr("disabled", true);
    }
    else{
      $("#submit").removeAttr("disabled");
    }
  }
});

