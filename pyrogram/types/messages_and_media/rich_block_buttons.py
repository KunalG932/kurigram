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

from typing import List, Optional
from pyrogram import types
from ..object import Object


class RichBlockButtons(Object):
    """A block containing a list of buttons that are shown in one row, corresponding to the custom HTML tag <tg-button-row>.

    Parameters:
        buttons (List of :obj:`~pyrogram.types.RichMessageButton`):
            The buttons.

        align (``str``, *optional*):
            Horizontal alignment of the buttons. Currently, must be one of "left", "center", or "right".

        type (``str``, *optional*):
            Type of the block, always "buttons".
    """

    def __init__(
        self,
        buttons: List["types.RichMessageButton"],
        align: Optional[str] = None,
        type: str = "buttons"
    ):
        super().__init__()
        self.buttons = buttons
        self.align = align
        self.type = type
