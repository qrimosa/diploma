$(document).ready(() => {
    $('.minus').click(function () {
        let id = $(this).data('id');
        let $input = $('.count[data-id="' + id + '"]');
        if ($input.val() > 1) {
            $input.val(Number($input.val()) - 1);
        }
    });

    $('.plus').click(function () {
        let id = $(this).data('id');
        let $input = $('.count[data-id="' + id + '"]');
        $input.val(Number($input.val()) + 1);
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
                        $('.cart-wrap').html(data.html);
                    }
                })
            }
        })
    })
})