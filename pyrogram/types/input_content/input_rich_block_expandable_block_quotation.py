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

from typing import Optional, Union
from pyrogram import types
from ..object import Object


class InputRichBlockExpandableBlockQuotation(Object):
    """A block quotation to be sent, which can be expanded or collapsed back, corresponding to the HTML tag <blockquote> with custom attribute "collapsed".

    Parameters:
        text (``str`` | :obj:`~pyrogram.types.RichText`):
            Content of the block.

        credit (``str`` | :obj:`~pyrogram.types.RichText`, *optional*):
            Credit of the block.

        type (``str``, *optional*):
            Type of the block, always "expandable_blockquote".
    """

    def __init__(
        self,
        text: Union[str, "types.RichText"],
        credit: Optional[Union[str, "types.RichText"]] = None,
        type: str = "expandable_blockquote"
    ):
        super().__init__()
        self.text = text
        self.credit = credit
        self.type = type
