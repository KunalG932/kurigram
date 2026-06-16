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
from pyrogram import raw, types
from ..object import Object


class RichMessage(Object):
    """Represents a rich formatted message.

    Parameters:
        rtl (``bool``, *optional*):
            Whether the text is right-to-left.

        part (``bool``, *optional*):
            Whether this is a partial rich message (e.g. streaming update).

        blocks (List of :obj:`~pyrogram.raw.base.PageBlock`, *optional*):
            Structured layout blocks composing the rich message.

        photos (List of :obj:`~pyrogram.types.Photo`, *optional*):
            Photos referenced in the rich message.

        documents (List of :obj:`~pyrogram.types.Document`, *optional*):
            Documents/media files referenced in the rich message.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        rtl: Optional[bool] = None,
        part: Optional[bool] = None,
        blocks: Optional[List["raw.base.PageBlock"]] = None,
        photos: Optional[List["types.Photo"]] = None,
        documents: Optional[List["types.Document"]] = None,
        raw: Optional["raw.types.RichMessage"] = None,
    ):
        super().__init__(client)
        self.rtl = rtl
        self.part = part
        self.blocks = blocks
        self.photos = photos
        self.documents = documents
        self.raw = raw

    @staticmethod
    def _parse(client, rich_message: "raw.types.RichMessage") -> Optional["RichMessage"]:
        if not isinstance(rich_message, raw.types.RichMessage):
            return None

        parsed_photos = types.List([
            types.Photo._parse(client, photo)
            for photo in rich_message.photos
        ]) if rich_message.photos else None

        parsed_documents = types.List([
            types.Document._parse(client, doc, getattr(doc, "file_name", None))
            for doc in rich_message.documents
        ]) if rich_message.documents else None

        return RichMessage(
            client=client,
            rtl=rich_message.rtl,
            part=rich_message.part,
            blocks=rich_message.blocks,
            photos=parsed_photos,
            documents=parsed_documents,
            raw=rich_message
        )
