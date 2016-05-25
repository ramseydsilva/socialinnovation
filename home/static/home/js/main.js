$(document).ready(function(){

    $("ul.nav li").hover(function() {
        var el = $(this);
        var id = el.attr("id");
        $(".sub-menu .sm").addClass("hidden");
        $("#" + id + "-sm").removeClass("hidden");
    });

});
