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

        if (contactForm.checkValidity() && paymentForm.checkValidity() && deliveryForm.checkValidity()) {
            paymentForm.submit()
        } else {
            if (!contactForm.checkValidity()) {
                $(contactForm).addClass('was-validated');
            }
            if (!paymentForm.checkValidity()) {
                $(paymentForm).addClass('was-validated');
            }
        }
    });
})