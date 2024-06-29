$(document).ready(() => {
    const forms = $('.needs-validation');
    forms.each(function () {
        $(this).on('submit', function (event) {
            if (!this.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            $(this).addClass('was-validated');
        });
    });
    $('.checkout-button').click(function (event) {
        event.preventDefault()
        const contactForm = $('#contact-form')[0];
        const paymentForm = $('#payment-form')[0];
        const deliveryForm = $('#delivery-form')[0];

        if (contactForm.checkValidity() && paymentForm.checkValidity()) {
            paymentForm.submit()
        } else {
            if (!contactForm.checkValidity()) {
                $(contactForm).addClass('was-validated');
            }
            if (!paymentForm.checkValidity()) {
                $(paymentForm).addClass('was-validated');
            }
        }
        url = $('input[name=url-checkout]').data('url')
        asdflkjasdf = []
        $('input[name=product_in_cart_id]').each(function () {
            asdflkjasdf.push($(this).val())
        })
        let total = 0
        $('.item-backet').each(function () {
            let price = parseInt($(this).find('.product-price').text())
            let count = $(this).find('.count').val()
            total += price * count
        })
        var deliveryOption = $('input[name=flexRadioDefault]:checked').next('label').text().trim()
        console.log(deliveryOption)
        $.ajax({
            url: url,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                'products[]': asdflkjasdf,
                name: $('input[name=name]').val(),
                surname: $('input[name=surname]').val(),
                sum_in_cart: total,
                amount: $('.count').val(),
                delivery: deliveryOption,
                street: $('#validationDefault01').val(),
                house: $('#validationDefault02').val(),
                flat: $('#validationDefault03').val(),
                floor: $('#validationDefault04').val(),
                elevator: $('#validationDefault05').val(),
                branch: $('#validationDefault06').val(),
            },
            success: function (data) {
                if (data.success) {
                    alert('Повідомлення надіслано до вашої поштової скриньки')
                }
            }
        })
    });
    if ($('#backet-header')) {
        $('#backet-header').remove()
    }
    if ($('#offcanvasBacket')) {
        $('#offcanvasBacket').remove()
    }
})