var path = window.location.pathname;
var page = path.split("/").pop();

//#region carrito 
//en esta region hay (añadir producto de tienda a carrito, modificar la cantidad a llevar y quitar productos del carrito)
var updateBtns = document.getElementsByClassName('update-cart')


for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        
        console.log('product: ', productId, 'action: ',action)

        console.log('USER: ', user)
        updateUserOrder(productId, action)
        // if(user == 'AnonymousUser'){
        //     console.log('User is not authenticated')
        // }else{
        // }
    })
}

function updateUserOrder(productId, action) {
    // var btnAgregarRestar = document.getElementsByClassName('aplicar-desc')
    // btnAgregarRestar.addEventListener('click', function() {
    //     var descuento = this.dataset.descuento

        
    // })
    console.log('User is authenticated, sending data...')

    var url = '/update_item/'
    const toastLiveExample = document.getElementById('liveToast')

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    })

    .then((response)=>{
        if(action == 'add'){
            var addToCartBtn = document.getElementById('addToCart_'+productId)
            var displayCartCount = document.getElementById('cart-count')
            console.log('addToCart_'+productId)
            addToCartBtn.disabled = true
            addToCartBtn.innerHTML = 'Añadido <i class="bi bi-bag-check"></i>'

            displayCartCount.innerHTML = Number(displayCartCount.innerHTML)+1

            const toast = new bootstrap.Toast(toastLiveExample)
            toast.show()

        }else if (action == 'aumentar' || action == 'restar') {
            var botonAumentar = document.getElementById('btn_aumentar_'+productId)
            var botonRestar = document.getElementById('btn_restar_'+productId)
            var quantityText = document.getElementById('displayQuantity_'+productId)
            var subtotalText = document.getElementById('display-subtotal')
            var subtotal = 0
            var precio = document.getElementById('card_'+productId).dataset.precio
            var descuentoText = document.getElementById('display-descuento')
            var totalText = document.getElementById('display-total')

            if (action == 'aumentar') {
                if (parseInt(quantityText.innerHTML) < parseInt(botonAumentar.dataset.stock)) {
                    var suma = parseInt(quantityText.innerHTML) + 1
                    quantityText.innerHTML = suma             
                    subtotal = Number(subtotalText.dataset.subtotal)+Number(precio)
                    console.log('aumentado')
                }
            } else {
                if (parseInt(quantityText.innerHTML) > 1) {
                    var resta = parseInt(quantityText.innerHTML) - 1
                    quantityText.innerHTML = resta
                    subtotal = Number(subtotalText.dataset.subtotal)-Number(precio)
                    console.log('restando')
                }
            }
            
            if (parseInt(quantityText.innerHTML) >= botonAumentar.dataset.stock) {
                botonAumentar.disabled = true
            }else{
                botonAumentar.disabled = false
            }
            
            if (parseInt(quantityText.innerHTML) <= 1) {
                botonRestar.disabled = true
            }else {
                botonRestar.disabled = false
            }

            subtotalText.dataset.subtotal = subtotal
            subtotalText.innerHTML = '$'+subtotal.toLocaleString('es-CL')

            descuentoText.innerHTML = '$'+ Math.round(subtotal*descuento).toLocaleString('es-CL')
            totalText.innerHTML = '$'+(subtotal - Math.round(subtotal*descuento)).toLocaleString('es-CL')
            
        }else if (action == 'eliminar') {
            var quantityText = document.getElementById('displayQuantity_'+productId)
            var subtotalText = document.getElementById('display-subtotal')
            var descuentoText = document.getElementById('display-descuento')
            var totalText = document.getElementById('display-total')
            var cardHtml = document.getElementById('card_'+productId)
            var precio = cardHtml.dataset.precio

            var subtotal = Number(subtotalText.dataset.subtotal)-(Number(precio)*Number(quantityText.innerHTML))
            subtotalText.dataset.subtotal = subtotal
            subtotalText.innerHTML = '$'+subtotal.toLocaleString('es-CL')
            //aqui va multiplicado con el descuento
            descuentoText.innerHTML = '$'+ Math.round(subtotal*descuento).toLocaleString('es-CL')
            totalText.innerHTML = '$'+(subtotal - Math.round(subtotal*descuento)).toLocaleString('es-CL')

            var displayCartCount = document.getElementById('cart-count')
            displayCartCount.innerHTML = Number(displayCartCount.innerHTML)-1

            cardHtml.remove()
            console.log('eliminando')
            if (subtotalText.dataset.subtotal == 0) {
                var cartSection = document.getElementById('cart-section')
                var scrollingHtml = document.getElementById('scrolling')
                var comprarSection = document.getElementById('comprar-section')

                cartSection.classList.add('align-self-center')
                scrollingHtml.remove()
                cartSection.parentElement.style.height = '35em'
                cartSection.innerHTML = '<h1 class="text-center">No hay productos en tu carrito <i class="bi bi-bag"></i></h1>'
                comprarSection.innerHTML = `<div class="card border-success w-100 bg-light placeholder-wave" aria-hidden="true">
                                            <h4 class="card-header placeholder fw-bold text-white bg-dark w-100"></h4>
                                            <div class="card-body">
                                                <div class="row text-black">
                                                    <div class="col-6">
                                                        <p class="card-text placeholder w-100 rounded-3"></p>
                                                    </div>
                                                    <div class="col-6 text-end ">
                                                        <p class="card-text placeholder w-75 rounded-3" id="display-subtotal" data-subtotal=></p>
                                                    </div>
                                                </div>
                                                <div class="row text-black">
                                                    <div class="col-6">
                                                        <p class="card-text placeholder w-75 rounded-3"></p>
                                                    </div>
                                                    <div class="col-6 text-end">
                                                        <p class="card-text placeholder w-75 rounded-3"></p>
                                                    </div>
                                                </div>
                                                <div class="row mt-2 text-center">
                                                    <h3 style="width: 80%;" class="card-text bg-black rounded-pill mt-1 fw-bold placeholder mx-auto" id="display-total" data-total=""></h3>
                                                </div>
                                                <hr size="3" width="100%" color="black">
                                                <form action="">
                                                    <div class="row text-black justify-content-evenly">
                                                        <h5 class="card-title placeholder rounded-3 w-75"></h5>
                                                        <div class="col-6">
                                                            <input class="form-control placeholder h-75" type="text" disabled>
                                                        </div>
                                                        <div class="col-6">
                                                            <button type="summit" class="btn btn-dark w-100  h-75 disabled placeholder"></button>
                                                        </div>
                                                    </div>
                                                </form>
                                                <hr size="3" width="100%" color="black">
                                                <button id="btn-comprar" type="button" class="btn btn-success w-100 disabled placeholder"></button>
                                            </div>
                                        </div>`
            }
        }
        
        return response.json()
    })
    .then((data)=>{
        console.log('data:', data)
    })
}
// function descuento() {

// }

//#endregion




//#region comprar
if (page == 'carrito') {
    var btn_comprar = document.getElementById('btn-comprar')
    var displayTotal = document.getElementById('display-total').dataset.total
    btn_comprar.addEventListener('click', function () { 
        if (user != 'AnonymousUser') {
            var url = '/process_order/'
            // const toastLiveExample = document.getElementById('liveToast')

            fetch(url, {
                method: 'POST',
                headers:{
                    'Content-Type':'application/json',
                    'X-CSRFToken':csrftoken,
                },
                body: JSON.stringify({'user': user,'total':displayTotal})
            })

            .then((response)=> response.json())
            .then((data)=>{
                console.log('data:', data)
                window.location.href = "/"
            })
        }
    })
}
//#endregion