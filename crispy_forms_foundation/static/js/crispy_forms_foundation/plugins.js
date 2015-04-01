(function( $ ) {

/*
 * jQuery plugin to add Foundation Abide support within tabs so errors are 
 * visible from tab names
 */
$.fn.abide_support_for_tabs = function(options) {
    return this.each(function() {
        var $form = $(this),
            settings = $.extend({
                'error_classname': 'error',
                'error_mark_html': '<span class="label alert round mark">!</span>',
                'error_mark_selector': 'span.mark',
                'itemid_finder_selector': '.content',
                'itemname_selector': '.tabs a',
            }, options);
        
        $form.on('invalid.fndtn.abide', function () {
            var tabnames_error = [],
                tabid;
            
            // Find all input errors, find up their container id and store it
            $(this).find('[data-invalid]').each(function( index ) {
                // From input go back up to its content container to find its id
                tabid = $(this).parents(settings.itemid_finder_selector).attr('id');
                // Store unique ids
                if( $.inArray(tabid, tabnames_error) == -1 ){
                    tabnames_error.push(tabid);
                }
            });
            
            // Reset error marks from tabs
            // TODO: Would be nice if it's used when inputs are changed, so the mark can 
            // be removed when the user fix input errors
            $(settings.itemname_selector, $form).removeClass('error').find(settings.error_mark_selector).remove();
            
            // Add error marks in container names that contains input errors from Abide
            $.each(tabnames_error, function( index, value ) {
                $(settings.itemname_selector+"[href='#"+value+"']", $form)
                    .addClass(settings.error_classname)
                    .append(settings.error_mark_html);
            });
            
        });
    });
};

/*
 * jQuery plugin to add Foundation Abide support within Accordion so errors are 
 * visible from their title
 */
$.fn.abide_support_for_accordions = function(options) {
    return this.each(function() {
        var $form = $(this),
            settings = $.extend({
                'error_classname': 'error',
                'error_mark_html': '<span class="label alert round mark">!</span>',
                'error_mark_selector': 'span.mark',
                'itemid_finder_selector': '.content',
                'itemname_selector': '.accordion .accordion-navigation a',
            }, options);
        
        $form.on('invalid.fndtn.abide', function () {
            var item_errors = [],
                itemid;
            
            // Find all input errors, find up their container id and store it
            $(this).find('[data-invalid]').each(function( index ) {
                // From input go back up to its content container to find its id
                itemid = $(this).parents(settings.itemid_finder_selector).attr('id');
                // Store unique ids
                if( $.inArray(itemid, item_errors) == -1 ){
                    item_errors.push(itemid);
                }
            });
            
            // Reset error marks from tabs
            $(settings.itemname_selector, $form).removeClass('error').find(settings.error_mark_selector).remove();
            
            // Add error marks in container names that contains input errors from Abide
            $.each(item_errors, function( index, value ) {
                $("#"+value, $form).prev()
                    .addClass(settings.error_classname)
                    .append(settings.error_mark_html);
            });
            
        });
    });
};

}( jQuery ));