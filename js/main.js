$(document).ready(function() {
    $(".formPopper").click(function() {
        $.ajax({
            url: this.href,
            success: function(data) {
                $("body").append("<div class='mask'></div>");
                $("body").append(data);
                $(".formPopup").find(".closer").click(function() {
                    $(".mask").remove();
                    $(".formPopup").remove();
                    return false;
                });
                $(".formPopup").find("input").first().focus();
            }
        });
        return false;
    });
    
    $(".formPopperButton").click(function() {
        $.ajax({
            url: $(this).closest('form')[0].action,
            success: function(data) {
                $("body").append("<div class='mask'></div>");
                $("body").append(data);
                $(".formPopup").find(".closer").click(function() {
                    $(".mask").remove();
                    $(".formPopup").remove();
                    return false;
                });
                $(".formPopup").find("input").first().focus();
            }
        });
        return false;
    });
});