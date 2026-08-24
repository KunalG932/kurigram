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

import pyrogram
from pyrogram import enums, types
from ..object import Object


class RichMessageButton(Object):
    """This object represents a button in a :obj:`~pyrogram.types.RichMessage`.

    Exactly one of the optional fields other than *text* and *style* must be used to specify the type of the button.

    Parameters:
        text (``str`` | :obj:`~pyrogram.types.RichText`):
            Text of the button. May contain plain text, RichTextCustomEmoji and RichTextDateTime entities.

        style (:obj:`~pyrogram.enums.ButtonStyle` | ``str``, *optional*):
            Style of the button. Must be one of ``PRIMARY`` (blue), ``SUCCESS`` (green), ``DANGER`` (red) or ``LINK`` (link without borders).

        url (``str``, *optional*):
            HTTP or tg:// URL to be opened when the button is pressed.

        callback_data (``str`` | ``bytes``, *optional*):
            Data to be sent in a callback query to the bot when the button is pressed, 1-64 bytes.

        web_app (:obj:`~pyrogram.types.WebAppInfo`, *optional*):
            Description of the Web App that will be launched when the user presses the button.

        login_url (:obj:`~pyrogram.types.LoginUrl`, *optional*):
            An HTTPS URL used to automatically authorize the user.

        switch_inline_query (``str``, *optional*):
            If set, pressing the button will prompt the user to select one of their chats, open that chat and insert
            the bot's username and the specified inline query in the input field.

        switch_inline_query_current_chat (``str``, *optional*):
            If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field.

        switch_inline_query_chosen_chat (:obj:`~pyrogram.types.SwitchInlineQueryChosenChat`, *optional*):
            If set, pressing the button will prompt the user to select one of their chats of the specified type.

        copy_text (``str`` | :obj:`~pyrogram.types.CopyTextButton`, *optional*):
            A button that copies the specified text to clipboard.

        disabled (``bool`` | :obj:`~pyrogram.types.DisabledButton`, *optional*):
            If set, then the button is disabled and does nothing.
    """

    def __init__(
        self,
        text: Union[str, "types.RichText"],
        style: Optional[Union["enums.ButtonStyle", str]] = enums.ButtonStyle.DEFAULT,
        url: Optional[str] = None,
        callback_data: Optional[Union[str, bytes]] = None,
        web_app: Optional["types.WebAppInfo"] = None,
        login_url: Optional["types.LoginUrl"] = None,
        switch_inline_query: Optional[str] = None,
        switch_inline_query_current_chat: Optional[str] = None,
        switch_inline_query_chosen_chat: Optional["types.SwitchInlineQueryChosenChat"] = None,
        copy_text: Optional[Union[str, "types.CopyTextButton"]] = None,
        disabled: Optional[Union[bool, "types.DisabledButton"]] = None,
    ):
        super().__init__()
        self.text = text
        self.style = style
        self.url = url
        self.callback_data = callback_data
        self.web_app = web_app
        self.login_url = login_url
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        self.switch_inline_query_chosen_chat = switch_inline_query_chosen_chat
        self.copy_text = copy_text
        self.disabled = disabled
