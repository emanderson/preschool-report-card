var showPopup = function(data) {
    $("body").append("<div class='mask'></div>");
    $("body").append(data);
    $(".formPopup").find("input").first().focus();
    
    $(".formPopup").find("#add").click(function() {
        var form = $(this).parents('form');
        var editingTable = '#' + form.find('[name=editingTable]')[0].value;
        $.ajax({
            url: form[0].action,
            type: 'POST',
            data: form.serialize(),
            success: function(row_html) {
                $(editingTable).append(row_html);
                $(".mask").remove();
                $(".formPopup").remove();
            }
        });
        return false;
    });
    
    $(".formPopup").find(".closer").click(function() {
        $(".mask").remove();
        $(".formPopup").remove();
        return false;
    });
};

$(document).ready(function() {
    $(".formPopper").click(function() {
        $.ajax({
            url: this.href,
            success: showPopup
        });
        return false;
    });
    
    $(".reportSection").on('click', ".formPopperButton", function() {
        $.ajax({
            url: $(this).closest('form')[0].action,
            success: showPopup
        });
        return false;
    });
});