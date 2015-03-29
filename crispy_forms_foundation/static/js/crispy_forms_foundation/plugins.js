(function( $ ) {

/*
 * jQuery plugin to add support Foundation Abide within tabs so errors are 
 * visible from tab names
 */
$.fn.abide_support_for_tabs = function(options) {
    return this.each(function() {
        var $form = $(this),
            settings = $.extend({
                'error_classname': 'error',
                'error_mark_html': '<span class="label alert round mark">!</span>',
                'error_mark_selector': 'span.mark',
                'tabid_finder_selector': 'div.content',
                'tabname_selector': 'ul.tabs a',
            }, options);
        
        $form.on('invalid.fndtn.abide', function () {
            var tabnames_error = [],
                tabid;
            
            // Find all input errors, find up their tab id and store it
            $(this).find('[data-invalid]').each(function( index ) {
                // From input go back up to its tab content container to find its id
                tabid = $(this).parents(settings.tabid_finder_selector).attr('id');
                // Store unique ids
                if( $.inArray(tabid, tabnames_error) == -1 ){
                    tabnames_error.push(tabid);
                }
            });
            
            // Reset error marks from tabs
            $(settings.tabname_selector).removeClass('error').find(settings.error_mark_selector).remove();
            
            // Add error marks in tab names that have input errors from Abide
            $.each(tabnames_error, function( index, value ) {
                $(settings.tabname_selector+"[href='#"+value+"']")
                    .addClass(settings.error_classname)
                    .append(settings.error_mark_html);
            });
            
        });
    });
};

}( jQuery ));