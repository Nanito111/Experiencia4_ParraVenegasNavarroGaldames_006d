$(window).on('load', function() {
  // Validación del nombre de usuario
  $("#username").blur(function() {
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

    // Validar si el nombre de usuario ya está en uso
    
    
    else {
      $("#username").addClass('is-valid');
    }
  });

  // Validación de la contraseña
  $("#password").blur(function() {
    $("#password").removeClass('is-valid');
    $("#password").removeClass('is-invalid');

    if ( $("#password").val().match(/^$/g)) {
      $("#password").addClass('is-invalid');
      $(".password.invalid-feedback").text("Debes completar este campo");
    }

    else if ($("#password").val().match(/^.{8,}$/g) == null) {
      $("#password").addClass('is-invalid');
      $(".password.invalid-feedback").text("La contraseña debe tener al menos 8 caracteres");
    }
    else if ($("#password").val().match(/^.{50,}$/g) != null) {
      $("#password").addClass('is-invalid');
      $(".password.invalid-feedback").text("La contraseña no puede tener más de 50 caracteres");
    }
    else {
      $("#password").addClass('is-valid');
    }
  });
});

