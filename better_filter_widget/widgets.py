from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms

class BetterFilterWidget(forms.SelectMultiple):
    class Media:
        extend = False
        css = {
            'all': ('css/better-filter-widget.css',)
        }
        js = ('js/better-filter-widget.js', )

    def __init__(self, attrs=None, choices=(), verbose_name=''):
        self.verbose_name = verbose_name

        super(BetterFilterWidget, self).__init__(attrs=attrs, choices=choices)

    def render(self, name, value, attrs=None, choices=()):
        output = super(BetterFilterWidget, self).render(name, value, attrs, choices)
        output += u'''
        	<script type="text/javascript">
				(function($) {
                    $(window).ready(function(){
                        BetterFilterWidget('%s', '%s');
                    });
                })(window.$ || django.jQuery);
        	</script>
        ''' % (name, self.verbose_name)
        return mark_safe(output)
