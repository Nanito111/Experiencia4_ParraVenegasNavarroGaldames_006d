$(window).on('load', function() {
  // Validación del nombre
  $("#name").keyup(function() {
    nameValidation("#name", ".name");
    submitValidation();
  });
  $("#name").blur(function () {
    submitValidation();
  });

  // Validación del apellido
  $("#surname").keyup(function() {
    nameValidation("#surname", ".surname");
    submitValidation();
  });
  $("#surname").blur(function () {
    submitValidation();
  });
  
  // Validación del nombre de usuario
  $("#username").keyup(function() {
    
    usernameValidation();
    submitValidation();
  });
  $("#username").blur(function () {
    submitValidation();
  });

  // Validación del correo electrónico
  $("#mail").keyup(function() {
    mailValidation();
    submitValidation();
  });
  $("#mail").blur(function () {
    submitValidation();
  });

  // Validación de la contraseña
  $("#password").keyup(function() {
    passwordValidation();
    submitValidation();
  });
  $("#password").blur(function () {
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
    // Validar si el nombre de usuario ya está en uso
    
    else {
      $("#username").addClass('is-valid');
    }
  }

  function mailValidation() {
    $("#mail").removeClass('is-valid');
    $("#mail").removeClass('is-invalid');

    if ( $("#mail").val().match(/^$/g)) {
      $("#mail").addClass('is-invalid');
      $(".mail.invalid-feedback").text("Debes completar este campo");
    }
    else if ($("#mail").val().match(/^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])/g) == null) {
      $("#mail").addClass('is-invalid');
      $(".mail.invalid-feedback").text("El correo electrónico no es válido");
    }
    else if ($("#mail").val().match(/^.{100,}$/g) != null) {
      $("#mail").addClass('is-invalid');
      $(".mail.invalid-feedback").text("El correo no puede tener más de 100 caracteres");
    }
    else {
      $("#mail").addClass('is-valid');
    }
  }

  function passwordValidation() {
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
  }

  function submitValidation () {
    if (!$("#name").hasClass('is-valid')) {
      $("#submit").attr("disabled", true);
    }
    else if (!$("#surname").hasClass('is-valid')) {
      $("#submit").attr("disabled", true);
    }
    else if (!$("#username").hasClass('is-valid')) {
      $("#submit").attr("disabled", true);
    }
    else if (!$("#mail").hasClass('is-valid')) {
      $("#submit").attr("disabled", true);
    }
    else if (!$("#password").hasClass('is-valid')) {
      $("#submit").attr("disabled", true);
    }
    else{
      $("#submit").removeAttr("disabled");
    }
  };
});

