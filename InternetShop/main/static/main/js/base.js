$(document).ready(() => {
    burgerItems = $('.burger-item')
    burgerItems.hover(function () {
        $(this).find('.burger-img').addClass('hidden')
        $(this).find('.h1').addClass('text-decoration-underline')
    }, function () {
        $('.burger-img').removeClass('hidden')
        $(this).find('.h1').removeClass('text-decoration-underline')
    })

})