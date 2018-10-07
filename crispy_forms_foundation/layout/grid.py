"""
Grid
====

.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms
.. _Foundation: http://github.com/zurb/foundation
.. _crispy-forms-foundation-demo: https://github.com/sveetch/crispy-forms-foundation-demo
.. _Abide: http://foundation.zurb.com/docs/components/abide.html

References
    * `Foundation 5 Grid <http://foundation.zurb.com/sites/docs/v/5.5.3/components/grid.html>`_;
    * `Foundation 6 Grid <http://foundation.zurb.com/sites/docs/grid.html>`_;
    * `Foundation 6 XY Grid <http://foundation.zurb.com/sites/docs/xy-grid.html>`_;

"""  # noqa: E501
from crispy_forms_foundation.layout.base import Div


__all__ = [
    'Row', 'RowFluid', 'Column', 'GridX', 'GridY', 'Cell',
]


class Row(Div):
    """
    Wrap fields in a div whose default class is ``row``. Example:

    .. sourcecode:: python

        Row('form_field_1', 'form_field_2', 'form_field_3')

    Act as a div container row, it will embed its items in a div like that:

    .. sourcecode:: html

        <div class"row">Content</div>
    """
    css_class = 'row'


class RowFluid(Row):
    """
    Wrap fields in a div whose default class is "row row-fluid". Example:

    .. sourcecode:: python

        RowFluid('form_field_1', 'form_field_2', 'form_field_3')

    It has a same behaviour than *Row* but add a CSS class "row-fluid" that you
    can use to have top level row that take all the container width. You have
    to put the CSS for this class to your CSS stylesheets. It will embed its
    items in a div like that:

    .. sourcecode:: html

        <div class"row row-fluid">Content</div>

    The CSS to add should be something like that:

    .. sourcecode:: css

        /*
        * Fluid row takes the full width but keep normal row and columns
        * behaviors
        */
        @mixin row-fluid-mixin {
            max-width: 100%;
            // Restore the initial behavior restrained to the grid
            .row{
                margin: auto;
                @include grid-row;
                // Preserve nested fluid behavior
                &.row-fluid{
                    max-width: 100%;
                }
            }
        }
        .row.row-fluid{
            @include row-fluid-mixin;
        }
        @media #{$small-up} {
            .row.small-row-fluid{ @include row-fluid-mixin; }
        }
        @media #{$medium-up} {
            .row.medium-row-fluid{ @include row-fluid-mixin; }
        }
        @media #{$large-up} {
            .row.large-row-fluid{ @include row-fluid-mixin; }
        }
        @media #{$xlarge-up} {
            .row.xlarge-row-fluid{ @include row-fluid-mixin; }
        }
        @media #{$xxlarge-up} {
            .row.xxlarge-row-fluid{ @include row-fluid-mixin; }
        }

    It must be included after Foundation grid component is imported.
    """
    css_class = 'row row-fluid'


class Column(Div):
    """
    Wrap fields in a div. If not defined, CSS class will default to
    ``large-12 columns``. ``columns`` class is always appended, so you don't
    need to specify it.

    This is the column from the Foundation Grid component, all columns should
    be contained in a **Row** or a **RowFluid** and you will have to define the
    column type in the ``css_class`` attribute.

    Example:

    .. sourcecode:: python

        Column('form_field_1', 'form_field_2', css_class='small-12 large-6')

    Will render to something like that:

    .. sourcecode:: html

        <div class"small-12 large-6 columns">...</div>

    ``columns`` class is always appended, so you don't need to specify it.

    If not defined, ``css_class`` will default to ``large-12``.
    """
    css_class = 'columns'

    def __init__(self, field, *args, **kwargs):
        self.field = field
        if 'css_class' not in kwargs:
            kwargs['css_class'] = 'large-12'

        super(Column, self).__init__(field, *args, **kwargs)


class GridX(Div):
    """
    Wrap fields in a div whose default class is ``grid-x``. Example:

    .. sourcecode:: python

        Row('form_field_1', 'form_field_2', 'form_field_3')

    Act as an horizontal grid, it will embed its items in a div like that:

    .. sourcecode:: html

        <div class"grid-x">Content</div>
    """
    css_class = 'grid-x'


class GridY(Div):
    """
    Wrap fields in a div whose default class is ``grid-y``. Example:

    .. sourcecode:: python

        Row('form_field_1', 'form_field_2', 'form_field_3')

    Act as a vertical grid, it will embed its items in a div like that:

    .. sourcecode:: html

        <div class"grid-y">Content</div>
    """
    css_class = 'grid-y'


class Cell(Div):
    """
    Wrap fields in a div. If not defined, CSS class will default to ``cell``.
    It is always appended, so you don't need to specify it.

    This is the cell from the Foundation XY-Grid component, all cells should
    be contained in a **GridX** or a **GridY** and you will have to define the
    cell type in the ``css_class`` attribute.

    Example:

    .. sourcecode:: python

        Cell('form_field_1', 'form_field_2', css_class='large-6')

    Will render to something like that:

    .. sourcecode:: html

        <div class"large-6 cell">...</div>

    ``cell`` class is always appended, so you don't need to specify it.
    """
    css_class = 'cell'
