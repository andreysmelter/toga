from .base import Widget


class ScrollContainer(Widget):
    def __init__(self, id=None, style=None, horizontal=True,
                 vertical=True, content=None, factory=None):
        """ Instantiate a new instance of the scrollable container widget.

        Args:
            id (str): An identifier for this widget.
            style (:class:`colosseum.CSSNode`): An optional style object.
                If no style is provided then a new one will be created for the widget.
            horizontal (bool):  If True enable horizontal scroll bar.
            vertical (bool): If True enable vertical scroll bar.
            content (:class:`toga.Widget`): The content of the scroll window.
            factory (:module:): A provided factory module will be used to create the
                implementation of the ScrollContainer.
        """
        super().__init__(id=id, style=style, factory=factory)

        # Create a platform specific implementation of a Scroll Container
        self._impl = self.factory.ScrollContainer(interface=self)

        # Set all attributes
        self.horizontal = horizontal
        self.vertical = vertical
        self.content = content

    @property
    def content(self):
        """ Content of the scroll container.

        Returns:
            The content of the widget (:class:`toga.Widget`).
        """
        return self._content

    @content.setter
    def content(self, widget):
        self._content = widget
        if widget:
            widget._update_layout()
            self._content.app = self.app
            self._content.window = self.window

            self._impl.set_content(widget._impl)

    @property
    def vertical(self):
        """ Shows whether vertical scrolling is enabled.

        Returns:
            (bool) True if enabled, False if disabled.
        """
        return self._vertical

    @vertical.setter
    def vertical(self, value):
        self._vertical = value
        self._impl.set_vertical(value)

    @property
    def horizontal(self):
        """ Shows whether horizontal scrolling is enabled.

        Returns:
            (bool) True if enabled, False if disabled.
        """
        return self._horizontal

    @horizontal.setter
    def horizontal(self, value):
        self._horizontal = value
        self._impl.set_horizontal(value)