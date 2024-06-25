$(document).ready(() => {
    if (localStorage.getItem('isAuthenticated')) {
        $('.auth-link').removeClass('d-none');
        $('.login-button').addClass('d-none');
    }
    $('.courier-to-your-address').click(() => {
        $('.courier-to-your-address-form').removeClass('d-none')
        $('.pickup-from-nova-poshta-form').addClass('d-none')
    })
    $('.pickup-from-nova-poshta').click(() => {
        $('.courier-to-your-address-form').addClass('d-none')
        $('.pickup-from-nova-poshta-form').removeClass('d-none')
    })
    if (Number($('.incartproduct-amount').text()) != 0) {
        $('.incartproduct-amount').removeClass('d-none')
    }
    $('#btn-register').click(() => {
        var url = $('#btn-register').data('cart-url');
        $.ajax({
            url: url,
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
        var url = $('#btn-auth').data('cart-url');
        $.ajax({
            url: url,
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
                    localStorage.setItem('isAuthenticated', 'true')
                    $('.auth-link').removeClass('d-none')
                    $('.login-button').addClass('d-none')
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
    $('.add-cart').click(function () {
        var cartUrl = $(this).data('cart-url')
        $.ajax({
            url: cartUrl,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                product_id: $(this).closest('.card').find('input[name=product_id]').val(),
            },
            success: function (data) {
                $('.badge').removeClass('d-none')
                $('.badge').text(data.cart_count)
            }
        })
    })
    $('#add-cart').click(() => {
        var cartUrl = $('#add-cart').data('cart-url')
        var cartviewUrl = $('#add-cart').data('cart-view-url')
        $.ajax({
            url: cartUrl,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                product_id: $("input[name=product_id]").val(),
            },
            success: function (data) {
                $('.badge').removeClass('d-none')
                $('.badge').text(data.cart_count)
            }
        })
        // $.ajax({
        //     url: cartviewUrl,
        //     type: 'POST',
        //     data: {
        //         csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        //         product_id: $("input[name=product_id]").val(),
        //     },
        //     success: (data) => {
        //         console.log(data.html)
        //         $('.cart-wrap').html(data.html);
        //     }
        // })
    })
    $('#backet-header').click(() => {
        var cartviewUrl = $('#backet-header').data('cart-url')
        $.ajax({
            url: cartviewUrl,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: (data) => {
                // console.log(data.html)
                $('.cart-wrap').html(data.html);
                let total = 0
                $('.item-backet').each(function () {
                    // console.log(this)
                    // $('.cart-footer-price').text(`Разом: ${parseInt($('.product-price').text()) * $('#count').val()} грн`)
                    let price = parseInt($(this).find('.product-price').text())
                    let count = $(this).find('.count').val()
                    total += price * count
                })
                $('.cart-footer-price').text(`Разом: ${total} грн`)
            }
        })
    })
    $('.category-name').hover(function () {
        var categoryId = $(this).data('category-id')
        var categoryImage = $(`.category-image-${categoryId}`)
        // categoryImage.show()
        categoryImage.removeClass('d-none')
    }, function () {
        var categoryId = $(this).data('category-id');
        var categoryImage = $(`.category-image-${categoryId}`)
        categoryImage.addClass('d-none')
    })
    function updatePriceFilter() {
        url = $('#category-url').data('category-url')
        minPrice = ($('#min-price-slider').val())
        maxPrice = ($('#max-price-slider').val())
        colors = []
        $('input[name="colors-filter"]:checked').each(function () {
            colors.push($(this).attr('id'))
        })

        $.ajax({
            url: url,
            type: 'GET',
            data: {
                min_price: minPrice,
                max_price: maxPrice,
                colors: colors,
            },
            success: function (data) {
                $('#product-list').html(data.html);
                var newUrl = url + '?price_from=' + minPrice + '&price_to=' + maxPrice;
                if (colors.length > 0) {
                    newUrl += '&colors=' + colors.join(',')
                }
                history.pushState({}, '', newUrl)
            }
        })
    }
    $('#min-price-slider, #max-price-slider, input[name="colors-filter"]').on('change', updatePriceFilter);
    let priceGap = 0;
    function updateProgress() {
        let minVal = parseInt($(".range-input input:eq(0)").val()),
            maxVal = parseInt($(".range-input input:eq(1)").val())
        let minRange = parseInt($("#min-price-slider").attr("min")),
            maxRange = parseInt($("#max-price-slider").attr("max"))
        let leftValue = ((minVal - minRange) / (maxRange - minRange)) * 100 + "%"
        let rightValue = ((maxRange - maxVal) / (maxRange - minRange)) * 100 + "%"
        $(".progress").css({
            "left": leftValue,
            "right": rightValue
        });
        $('.input-min').val(minVal);
        $('.input-max').val(maxVal);
    }
    updateProgress();
    $(".price-input input").each(function (index, input) {
        $(input).on("input", function (e) {
            let minPrice = parseInt($(".price-input input:eq(0)").val()),
                maxPrice = parseInt($(".price-input input:eq(1)").val())

            if ((maxPrice - minPrice >= priceGap) && maxPrice <= $("#max-price-slider").attr("max")) {
                if ($(this).hasClass("input-min")) {
                    $("#min-price-slider").val(minPrice)
                    updateProgress()
                } else {
                    $("#max-price-slider").val(maxPrice)
                    updateProgress()
                }
            }
        });
    });
    $(".range-input input").each(function (index, input) {
        $(input).on("input", function (e) {
            let minVal = parseInt($(".range-input input:eq(0)").val()),
                maxVal = parseInt($(".range-input input:eq(1)").val())
            if ((maxVal - minVal) < priceGap) {
                if ($(this).hasClass("range-min")) {
                    $(".range-input input:eq(0)").val(maxVal - priceGap)
                    updateProgress();
                } else {
                    $(".range-input input:eq(1)").val(minVal + priceGap)
                    updateProgress();
                }
            } else {
                updateProgress();
            }
        });
    });
})
