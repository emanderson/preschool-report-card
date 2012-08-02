$(document).ready(function() {
    $(".formPopper").click(function() {
        $.ajax({
            url: this.href,
            success: function(data) {
                $("body").append(data);
                $(".formPopup").find(".closer").click(function() {
                    $(".formPopup").remove();
                    return false;
                });
                $(".formPopup").find("input").first().focus();
            }
        });
        return false;
    });
});