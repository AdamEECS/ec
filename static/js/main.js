const log = function log(){
  console.log.apply(console, arguments);
}

$('a.cart-add').click(function(){
    let a = $(event.target)
    let tr = a.closest('tr')
    let count_span = tr.find('span.cart-product-count')
    let sum_span = tr.find('span.cart-product-sum')
    let count = parseInt(tr.find('span.cart-product-count').text())
    let price = parseFloat(tr.find('span.cart-product-price').text())
    let data = {
        'product_id': tr.data('id')
    }
    let request = {
        url: '/api/cart_add',
        type: 'post',
        contentType: 'application/json',
        data: JSON.stringify(data),
        success: function(r){
            r = JSON.parse(r)
            if(r.status == 'OK') {
                count_span.text(count + 1)
                sum_span.text(price * (count + 1))
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
    let a = $(event.target)
    let tr = a.closest('tr')
    let count_span = tr.find('span.cart-product-count')
    let sum_span = tr.find('span.cart-product-sum')
    let count = parseInt(tr.find('span.cart-product-count').text())
    let price = parseFloat(tr.find('span.cart-product-price').text())
    let data = {
        'product_id': tr.data('id')
    }
    let request = {
        url: '/api/cart_sub',
        type: 'post',
        contentType: 'application/json',
        data: JSON.stringify(data),
        success: function(r){
            r = JSON.parse(r)
            if(r.status == 'OK') {
                count_span.text(count - 1)
                sum_span.text(price * (count - 1))
                if((count - 1) <= 0) {
                    tr.remove()
                }
            }
        },
        error: function(err) {
            log('error', err);
        }
    };
    $.ajax(request)
    return false
})
