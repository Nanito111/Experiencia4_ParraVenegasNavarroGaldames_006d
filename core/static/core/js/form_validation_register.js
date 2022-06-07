$(window).on('load', function() {
  // Validación del nombre
  $("#name").blur(function() {
    $("#name").removeClass('is-valid');
    $("#name").removeClass('is-invalid');
    if ( $("#name").val().match(/^$/g)) {
      $("#name").addClass('is-invalid');
      $(".name.invalid-feedback").text("Debes completar este campo");
    }
    else if ( $("#name").val().match(/^.{64,}$/g)) {
      $("#name").addClass('is-invalid');
      $(".name.invalid-feedback").text("El nombre no puede tener más de 64 caracteres");
    }
    else if ($("#name").val().match(/^\S+(?: \S+)*$/g) == null) {
      $("#name").addClass('is-invalid');
      $(".name.invalid-feedback").text("El nombre no puede empezar ni terminar con espacios");
    }
    else if ($("#name").val().match(/\d+/g) != null) {
      $("#name").addClass('is-invalid');
      $(".name.invalid-feedback").text("El nombre no puede contener números");
    }
    else {
      $("#name").addClass('is-valid');
    }
  });

  // Validación del apellido
  $("#surname").blur(function() {
    $("#surname").removeClass('is-valid');
    $("#surname").removeClass('is-invalid');
    if ( $("#surname").val().match(/^$/g)) {
      $("#surname").addClass('is-invalid');
      $(".surname.invalid-feedback").text("Debes completar este campo");
    }
    else if ( $("#surname").val().match(/^.{64,}$/g)) {
      $("#surname").addClass('is-invalid');
      $(".surname.invalid-feedback").text("El apellido no puede tener más de 64 caracteres");
    }
    else if ($("#surname").val().match(/^\S+(?: \S+)*$/g) == null) {
      $("#surname").addClass('is-invalid');
      $(".surname.invalid-feedback").text("El nombre no puede empezar ni terminar con espacios");
    }
    else if ($("#surname").val().match(/\d+/g) != null) {
      $("#surname").addClass('is-invalid');
      $(".surname.invalid-feedback").text("El apellido no puede contener números");
    }
    else {
      $("#surname").addClass('is-valid');
    }
  });
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
    //TODO: Validar si el nombre de usuario ya está en uso
    else {
      $("#username").addClass('is-valid');
    }
  });

  // Validación del correo electrónico
  $("#mail").blur(function() {
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
  });
});

