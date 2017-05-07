const log = function log(){
  console.log.apply(console, arguments);
}

let cart_calculate = function(product_tr, op) {
    let count_span = product_tr.find('span.cart-product-count')
    let tr_sum_span = product_tr.find('span.cart-product-sum')
    let cart_count_span = $('.class-cart-count')
    let cart_total_span = $('.class-cart-total')

    let count = parseInt(product_tr.find('span.cart-product-count').text())
    let cart_count = parseInt($(cart_count_span[0]).text())

    let price = parseFloat(product_tr.find('span.cart-product-price').text())
    let cart_total = parseFloat(cart_total_span.text())

    if (op == '+') {
        count += 1
        cart_count += 1
        cart_total += price
    } else if (op == '-') {
        count -= 1
        cart_count -= 1
        cart_total -= price
    }
    let tr_sum = (price * count).toFixed(2)
    cart_total = cart_total.toFixed(2)
    count_span.text(count)
    tr_sum_span.text(tr_sum)
    cart_count_span.text(cart_count)
    cart_total_span.text(cart_total)
    if(count <= 0) {
        product_tr.remove()
    }
}

$('a.cart-add').click(function(){
    let target = $(event.target)
    let product_tr = target.closest('tr')
    let data = {
        'product_id': product_tr.data('id')
    }
    let request = {
        url: '/api/cart_add',
        type: 'post',
        contentType: 'application/json',
        data: JSON.stringify(data),
        success: function(r){
            r = JSON.parse(r)
            if(r.status == 'OK') {
                cart_calculate(product_tr, '+')
            }
        },
        error: function(err) {
            log('error', err);
        }
    };
    $.ajax(request)
    return false
})

$('a.cart-sub').click(function(){
    let target = $(event.target)
    let product_tr = target.closest('tr')
    let data = {
        'product_id': product_tr.data('id')
    }
    let request = {
        url: '/api/cart_sub',
        type: 'post',
        contentType: 'application/json',
        data: JSON.stringify(data),
        success: function(r){
            r = JSON.parse(r)
            if(r.status == 'OK') {
                cart_calculate(product_tr, '-')
            }
        },
        error: function(err) {
            log('error', err);
        }
    };
    $.ajax(request)
    return false
})
