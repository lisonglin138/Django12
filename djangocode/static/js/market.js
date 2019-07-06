$(function () {

    $(".subShopping").click(function () {
        console.log('sub');
        var $add=$(this);
            console.log($add.attr('class'))

            console.log($add.attr('goodid'));


        // var goodsid = $add.attr("goodid");
        // var goodsid = $add.prop("goodid");
        //
    })

    $(".addShopping").click(function () {
        console.log('add');
        var $add =$(this);

            console.log($add.attr('class'));
            console.log($add.attr('goodid'));

        // var $add = $add.attr('goodid');
        // var $add = $add.prop('goodid');
        var goodid=$add.attr('goodid');
        //ajax发送git请求
        $.get('/axf/addtocart/',{'goodid':goodsid},function (data) {
            console.log(data);

        })


        })
})
