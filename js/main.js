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
    
    $(".formPopup").find("#edit").click(function() {
        var form = $(this).parents('form');
        var editingArea = '#' + form.find('[name=editingId]')[0].value;
        $.ajax({
            url: form[0].action,
            type: 'POST',
            data: form.serialize(),
            success: function(row_html) {
                $(editingArea).replaceWith(row_html);
                $(".mask").remove();
                $(".formPopup").remove();
            }
        });
        return false;
    });
    
    $(".formPopup").find("#delete").click(function() {
        var form = $(this).parents('form');
        var editingArea = '#' + form.find('[name=editingId]')[0].value;
        $.ajax({
            url: form[0].action,
            type: 'POST',
            data: form.serialize(),
            success: function() {
                $(editingArea).remove();
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
    $("body").on('click', ".formPopper", function() {
        $.ajax({
            url: this.href,
            success: showPopup
        });
        return false;
    });
    
    $("body").on('click', ".formPopperButton", function() {
        $.ajax({
            url: $(this).closest('form')[0].action,
            success: showPopup
        });
        return false;
    });
});