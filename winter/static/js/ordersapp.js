"use strict";
(function($) {
    $(document).ready(function() {
        let counter = function() {
            let total_price = 0;
            let total_products = 0;
            $('.formset_row').each(function(){
                let quantity = parseInt($(this).find('input[name*=quantity]').val());
                let price = parseFloat($(this).find('span[class*=price]').data('price'));
                total_products += quantity;
                total_price += quantity * price;
            });

            $('#total-products').text(total_products);
            $('#total-price').text(total_price);

            if($('#id_total').length > 0) {
                $('#id_total').val(total_price);
            }

        };
        $('input[name*="quantity"], input[name*="price"]').on('click', function(){
            counter();
        });

        $('select[name*="product"]').on('change', function(){
            let product_id = $(this).val();
            let parent = $(this).parents('.formset_row');
            $.get('/admin/products/read/' + product_id, function(data) {
                parent.find('input[name*=quantity]').val(1);
                parent.find('input[name*=price]').val(data.price);
                parent.find('span[class*=price]').data('price', data.price).text(data.price);
                counter();
            }, 'json');
        })

        $('.formset_row').formset({
            addText: 'добавить',
            deleteText: 'удалить',
        });
    });


}(jQuery));