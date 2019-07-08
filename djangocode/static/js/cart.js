$(function () {
    $(".confirm").click(function () {
        console.log('change state');
        var $confirm = $(this);
        var $td=$confirm.parents('td');
        var cartid= $td.attr('cartid');
        console.log($td.attr('cartid'));
        var cartid = $td.attr('cartid');
        $.getJSON('/app/Shopping_Cart_select/',{'cartid':cartid},function (data) {
            console.log(data);


        })

    })









})