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
from pyrogram import raw, types
from ..object import Object
from .input_message_content import InputMessageContent


class InputRichMessageMedia(Object):
    """Represents a media attached to a rich formatted message.

    Parameters:
        media (:obj:`~pyrogram.types.InputMedia` | ``str``):
            The media element.
    """

    def __init__(self, media: Union["types.InputMedia", str]):
        super().__init__()
        self.media = media


class InputRichMessage(Object):
    """Describes a rich message to be sent. Exactly one of the fields html, markdown, or blocks must be used.

    Parameters:
        blocks (List of :obj:`~pyrogram.types.Object`, *optional*):
            Content of the rich message to send described as a list of blocks.

        html (``str``, *optional*):
            Content of the rich message to send described using HTML formatting.

        markdown (``str``, *optional*):
            Content of the rich message to send described using Markdown formatting.

        media (List of :obj:`~pyrogram.types.InputRichMessageMedia`, *optional*):
            List of media that are specified in the markdown or html fields using tg://photo?id=, tg://video?id=, tg://document?id=, and tg://audio?id= links.

        is_rtl (``bool``, *optional*):
            Pass True if the rich message must be shown right-to-left.

        skip_entity_detection (``bool``, *optional*):
            Pass True to skip automatic detection of entities in the text.
    """

    def __init__(
        self,
        blocks: Optional[List["types.Object"]] = None,
        html: Optional[str] = None,
        markdown: Optional[str] = None,
        media: Optional[List["types.InputRichMessageMedia"]] = None,
        is_rtl: Optional[bool] = None,
        skip_entity_detection: Optional[bool] = None,
    ):
        super().__init__()
        self.blocks = blocks
        self.html = html
        self.markdown = markdown
        self.media = media
        self.is_rtl = is_rtl
        self.skip_entity_detection = skip_entity_detection


class InputRichMessageContent(InputMessageContent):
    """Represents the content of a rich message to be sent as the result of an inline query.

    Parameters:
        rich_message (:obj:`~pyrogram.types.InputRichMessage` | ``str``):
            The rich message to send.

        link_preview_options (:obj:`~pyrogram.types.LinkPreviewOptions`, *optional*):
            Link preview generation options for the message.
    """

    def __init__(
        self,
        rich_message: Union["InputRichMessage", str],
        link_preview_options: Optional["types.LinkPreviewOptions"] = None
    ):
        super().__init__()
        self.rich_message = rich_message
        self.link_preview_options = link_preview_options
