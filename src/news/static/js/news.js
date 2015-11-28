jQuery(function($) {
	
    function change_lang(ln) {
        $('#selected_lang').val(ln);
        $('#change_lang_form').submit();
        return false;
    }

    $('#change_lang_en').click(
        function() {
            return change_lang('en');
        });

    $('#change_lang_fr').click(
        function() {
            return change_lang('fr');
        });

});
