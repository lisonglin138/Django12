(function($) {
    $.fn.jqueryzoom = function(options) {
        var settings = {
            xzoom: 200,
            yzoom: 200,
            offset: 10,
            position: "right",
            lens: 1,
            preload: 1
        };
        if (options) {
            $.extend(settings, options)
        }
        var noalt = '';
        $(this).hover(function() {
            var imageLeft = $(this).offset().left;
            var imageTop = $(this).offset().top;
            var imageWidth = $(this).children('img').get(0).offsetWidth;
            var imageHeight = $(this).children('img').get(0).offsetHeight;
            noalt = $(this).children("img").attr("alt");
            var bigimage = $(this).children("img").attr("alt");
            $(this).children("img").attr("alt", '');
            if ($("div.zoomdiv").get().length == 0) {
                $(this).after("<div class='zoomdiv'><img class='bigimg' src='" + bigimage + "'/></div>");
                $(this).append("<div class='jqZoomPup'>&nbsp;</div>")
            }
            if (settings.position == "right") {
                if (imageLeft + imageWidth + settings.offset + settings.xzoom > screen.width) {
                    leftpos = imageLeft - settings.offset - settings.xzoom
                } else {
                    leftpos = imageLeft + imageWidth + settings.offset
                }
            } else {
                leftpos = imageLeft - settings.xzoom - settings.offset;
                if (leftpos < 0) {
                    leftpos = imageLeft + imageWidth + settings.offset
                }
            }
            $("div.zoomdiv");
            $("div.zoomdiv").width(settings.xzoom);
            $("div.zoomdiv").height(settings.yzoom);
            $("div.zoomdiv").show();
            if (!settings.lens) {
                $(this).css('cursor', 'crosshair')
            }
            $(document.body).mousemove(function(e) {
                mouse = new MouseEvent(e);
                var bigwidth = $(".bigimg").get(0).offsetWidth;
                var bigheight = $(".bigimg").get(0).offsetHeight;
                var scaley = 'x';
                var scalex = 'y';
                if (isNaN(scalex) | isNaN(scaley)) {
                    var scalex = (bigwidth / imageWidth);
                    var scaley = (bigheight / imageHeight);
                    $("div.jqZoomPup").width((settings.xzoom) / scalex);
                    $("div.jqZoomPup").height((settings.yzoom) / scaley);
                    if (settings.lens) {
                        $("div.jqZoomPup").css('visibility', 'visible')
                    }
                }
                xpos = mouse.x - $("div.jqZoomPup").width() / 2 - imageLeft;
                ypos = mouse.y - $("div.jqZoomPup").height() / 2 - imageTop;
                if (settings.lens) {
                    xpos = (mouse.x - $("div.jqZoomPup").width() / 2 < imageLeft) ? 0 : (mouse.x + $("div.jqZoomPup").width() / 2 > imageWidth + imageLeft) ? (imageWidth - $("div.jqZoomPup").width() - 2) : xpos;
                    ypos = (mouse.y - $("div.jqZoomPup").height() / 2 < imageTop) ? 0 : (mouse.y + $("div.jqZoomPup").height() / 2 > imageHeight + imageTop) ? (imageHeight - $("div.jqZoomPup").height() - 2) : ypos
                }
                if (settings.lens) {
                    $("div.jqZoomPup").css({
                        top: ypos,
                        left: xpos
                    })
                }
                scrolly = ypos;
                $("div.zoomdiv").get(0).scrollTop = scrolly * scaley;
                scrollx = xpos;
                $("div.zoomdiv").get(0).scrollLeft = (scrollx) * scalex
            })
        },
        function() {
            $(this).children("img").attr("alt", noalt);
            $(document.body).unbind("mousemove");
            if (settings.lens) {
                $("div.jqZoomPup").remove()
            }
            $("div.zoomdiv").remove()
        });   
    }
})(jQuery);
function MouseEvent(e) {
    this.x = e.pageX;
    this.y = e.pageY
}