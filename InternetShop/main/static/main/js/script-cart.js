$(document).ready(() => {
    $('.minus').off('click').click(function (event) {
        event.stopPropagation()
        let id = $(this).data('id');
        let $input = $('.count[data-id="' + id + '"]');
        let total = 0
        if ($input.val() > 1) {
            $input.val(Number($input.val()) - 1);
        }
        $('.item-backet').each(function () {
            let price = parseInt($(this).find('.product-price').text())
            let count = $(this).find('.count').val()
            total += price * count
        })
        $('.cart-footer-price').text(`Разом: ${total} грн`);
    });
    $('.plus').off('click').click(function (event) {
        event.stopPropagation()
        let id = $(this).data('id');
        let $input = $('.count[data-id="' + id + '"]');
        $input.val(Number($input.val()) + 1);
        let total = 0
        $('.item-backet').each(function () {
            let price = parseInt($(this).find('.product-price').text())
            let count = $(this).find('.count').val()
            total += price * count
        })
        $('.cart-footer-price').text(`Разом: ${total} грн`);
    });
    $('.delete-item-from-cart').click(function () {
        var cartUrl = $('.delete-item-from-cart').data('cart-url');
        var product_id = $(this).data('product-id');
        var cartviewUrl = $('#backet-header').data('cart-url');
        $.ajax({
            url: cartUrl,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                product_in_cart_id: product_id,
            },
            success: () => {
                $.ajax({
                    url: cartviewUrl,
                    type: 'POST',
                    data: {
                        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                        product_in_cart_id: $('input[name=product_in_cart_id]').val(),
                    },
                    success: (data) => {
                        // console.log(data.html)
                        if (data.cart_count == 0) {
                            $('.badge').addClass('d-none')
                        }
                        else {
                            $('.badge').text(data.cart_count)
                        }
                        $('.cart-wrap').html(data.html);
                        let total = 0;
                        $('.item-backet').each(function () {
                            console.log(this)
                            // $('.cart-footer-price').text(`Разом: ${parseInt($('.product-price').text()) * $('#count').val()} грн`)
                            let price = parseInt($(this).find('.product-price').text())
                            let count = $(this).find('.count').val()
                            total += price * count
                        })
                        $('.cart-footer-price').text(`Разом: ${total} грн`);
                    }
                })
            }
        })
    })
})