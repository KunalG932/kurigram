#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from typing import List, Optional, Union
from pyrogram import types
from ..object import Object


class RichBlockTableCell(Object):
    """Represents a cell in a table.

    Parameters:
        text (``str`` | :obj:`~pyrogram.types.RichText`):
            Text in the cell.

        is_header (``bool``, *optional*):
            True, if the cell is a header.

        align (``str``, *optional*):
            Horizontal alignment of the cell content. One of "left", "center", or "right".
    """

    def __init__(
        self,
        text: Union[str, "types.RichText"],
        is_header: Optional[bool] = None,
        align: Optional[str] = None
    ):
        super().__init__()
        self.text = text
        self.is_header = is_header
        self.align = align


class RichBlockTable(Object):
    """A table, corresponding to the HTML tag <table>.

    Parameters:
        cells (List of List of :obj:`~pyrogram.types.RichBlockTableCell`):
            Cells of the table.

        is_bordered (``bool``, *optional*):
            True, if the table has borders.

        is_striped (``bool``, *optional*):
            True, if the table is striped.

        is_compact (``bool``, *optional*):
            True, if table cells have smaller indents.

        caption (``str`` | :obj:`~pyrogram.types.RichText`, *optional*):
            Caption of the table.

        type (``str``, *optional*):
            Type of the block, always "table".
    """

    def __init__(
        self,
        cells: List[List["types.RichBlockTableCell"]],
        is_bordered: Optional[bool] = None,
        is_striped: Optional[bool] = None,
        is_compact: Optional[bool] = None,
        caption: Optional[Union[str, "types.RichText"]] = None,
        type: str = "table"
    ):
        super().__init__()
        self.cells = cells
        self.is_bordered = is_bordered
        self.is_striped = is_striped
        self.is_compact = is_compact
        self.caption = caption
        self.type = type
