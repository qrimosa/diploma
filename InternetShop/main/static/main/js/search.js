$(document).ready(() => {
    let availableProducts = [];
    const resultsBox = $(".result-box")
    const inputBox = $("#search-header")
    inputBox.on("keyup", function () {

        resultsBox.show()
        $('main').addClass('fade')
        $('main').css('opacity', 0.5)
        let input = inputBox.val().toLowerCase().trim();
        let result = availableProducts.filter((product) => {
            return product.name.toLowerCase().includes(input);
        });
        display(result.slice(0, 5));
        if (!result.length) {
            resultsBox.html('');
        }
    });
    function display(result) {
        const content = result.map((product) => {
            return `<li onclick="selectInput('${product.slug}')">${product.name}</li>`;
        });
        resultsBox.html("<ul>" + content.join('') + "</ul>");
    }
    window.selectInput = function (url) {
        window.location.href = `product/${url}`
    }
    inputBox.blur(() => {
        setTimeout(function () {
            resultsBox.html('');
        }, 200);
    })
    $.ajax({
        url: $('#data-get-products-url').data('get-products-url'),
        method: 'GET',
        success: function (data) {
            availableProducts = data
            console.log(availableProducts)
        }
    });
})

//$('#data-get-products-url').data('get-products-url')
