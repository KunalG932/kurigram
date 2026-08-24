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


class RichBlockDocument(Object):
    """A block with a general file, corresponding to the custom HTML tag <tg-document>.

    Parameters:
        document (:obj:`~pyrogram.types.Document`):
            The document.

        caption (``str`` | :obj:`~pyrogram.types.RichText`, *optional*):
            Caption of the block.

        type (``str``, *optional*):
            Type of the block, always "document".
    """

    def __init__(
        self,
        document: "types.Document",
        caption: Optional[Union[str, "types.RichText"]] = None,
        type: str = "document"
    ):
        super().__init__()
        self.document = document
        self.caption = caption
        self.type = type
