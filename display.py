#display.py (D)
from PySide6.QtWidgets import QLineEdit
from variables import (var_big_font_size, var_text_margin, var_minimum_width)
from PySide6.QtCore import (Qt, Signal)
from PySide6.QtGui import QKeyEvent
from utils import func_isempty

from typing import TYPE_CHECKING # Just test.
if TYPE_CHECKING:
    from buttons import cls_button
var_button: 'cls_button'

class cls_display(QLineEdit):
    var_enterpressed = Signal()
    var_backspacepressed = Signal()
    var_scapepressed = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mtd_configstyle()

    def mtd_configstyle(self):
        self.setStyleSheet(f'font-size: {var_big_font_size}px;')
        self.setMinimumHeight(var_big_font_size * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)

        var_margins = []
        for _ in range(4):
            var_margins.append(var_text_margin)
        self.setTextMargins(var_margins[0], var_margins[1], var_margins[2], var_margins[3])
        # var_margins = [var_text_margin for _ in range(4)]
        # self.setTextMargins(*var_margins)
        self.setMinimumWidth(var_minimum_width)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        var_text = event.text().strip()
        var_key = event.key()
        var_keysqt = Qt.Key
        
        var_isenter = (var_key == var_keysqt.Key_Enter) or (var_key == var_keysqt.Key_Return)
        # var_isenter = (event.key() == Qt.Key.Key_Enter) or (event.key() == Qt.Key.Key_Return)
        var_isbackspace = (var_key == var_keysqt.Key_Backspace) or (var_key == var_keysqt.Key_Delete)
        var_isescape = (event.key() == Qt.Key.Key_Escape)

        if var_isenter:
            print('Enter button.', type(self).__name__)
            self.var_enterpressed.emit()
            return event.ignore()
        # return super().keyPressEvent(event)

        if var_isbackspace:
            print('Backspace button.', type(self).__name__)
            self.var_backspacepressed.emit()
            return event.ignore()

        if var_isescape:
            print('Escape button.', type(self).__name__)
            self.var_scapepressed.emit()
            return event.ignore()
        
        if func_isempty(var_text):
            return event.ignore()
        print('Text', var_text)
