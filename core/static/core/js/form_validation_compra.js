$(document).ready(function() {
  const subtotal = parseInt($("#subtotal").text());
  const stock = parseInt($("#stock").text());
  let newSubtotal;
  console.log(subtotal)
  $("#codeInput").keyup(function() {
    codeValidation("#codeInput", ".code");
  });

  $("#unitInput").keyup(function() {
    newSubtotal = subtotal * $("#unitInput").val();
    $("#subtotal").text(parseInt(newSubtotal));
    unitValidation("#unitInput", ".unit");
  });

  function codeValidation(idElement, classElement) {
    $(idElement).removeClass('is-valid');
    $(idElement).removeClass('is-invalid');
    if ($(idElement).val() == 'MACETITAS') {
      $(idElement).addClass('is-valid');
      $("#descuento").text((10 / 100) * newSubtotal);
      $(idElement).attr("disabled", 'disabled');
      totalValidation();
    }
    else {
      $(idElement).addClass('is-invalid');
      $(classElement+".invalid-feedback").text("Código inválido");
    }
  }

  function unitValidation(idElement, classElement) {
    totalValidation();
    $(idElement).removeClass('is-valid');
    $(idElement).removeClass('is-invalid');

    if ($(idElement).val() <= 0) {
      $(idElement).addClass('is-invalid');
      $(classElement+".invalid-feedback").text("La cantidad no puede ser cero o negativa");

    }
    else if ($(idElement).val() > stock) {
      $(idElement).addClass('is-invalid');
      $(classElement+".invalid-feedback").text("La cantidad no puede ser mayor al stock disponible");
    }
    else {
      $(idElement).addClass('is-valid');
    }
  }

  function totalValidation() {
    if (newSubtotal == NULL) {
      let descuento = $("#descuento").text((10 / 100) * subtotal);
      let newTotal = parseInt(subtotal - descuento);
      $("#total").text(newTotal);
    } else {
      let descuento = $("#descuento").text((10 / 100) * newSubtotal);
      let newTotal = parseInt(newSubtotal - descuento);
      $("#total").text(newTotal);
    }

  }
});