$(document).ready(() => {
    $('#btn-register').click(() => {
        $.ajax({
            url: "/reg/",
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                email: $('input[name=email]').val(),
                login: $('input[name=login]').val(),
                password: $('input[name=password]').val(),
                repeat_password: $('input[name=repeat-password]').val(),
            },
            success: function (response) {
                if (response.isRegister) {
                    $('.hello-user-register').text(`Дякуємо за реєстрацію, ${response.login}!`)
                    $('input[name=login]').val('')
                    $('input[name=password]').val('')
                    $('input[name=email]').val('')
                    $('input[name=repeat-password]').val('')
                }
                if (response.error) {
                    $('.register-error').text(response.error)
                }
            }
        })
    })
    $('#btn-auth').click(() => {
        $.ajax({
            url: 'auth/',
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                username: $('input[name=username]').val(),
                password: $('input[name=loginPassword]').val(),
            },
            success: function (response) {
                console.log(response.isLogin)
                if (response.isLogin) {
                    $('.hello-user-login').text(`Вітаємо, ${response.username}!`)
                    $('input[name=username]').val('')
                    $('input[name=loginPassword]').val('')
                    // window.location = "auth"
                }
                if (response.error) {
                    $('.login-error').text(response.error)
                }
            }
        })
    })
    $('.btn-close').click(() => {
        $('.register-error').text('')
        $('.hello-user-register').text('')
        $('.hello-user-login').text('')
        $('.login-error').text('')
    })

    $('#add-cart').click(() => {
        var cartUrl = $('#add-cart').data('cart-url');
        $.ajax({
            url: cartUrl,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                product_id: $("input[name=product_id]").val(),
            }
        })
    })
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
    $('.delete-item-from-cookie').click(() => {
        var cartUrl = $('.delete-item-from-cookie').data('cart-url');
        $.ajax({
            url: cartUrl,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                index_array: $('input[name=index-array]').val(),
            }
        })
    })
})
