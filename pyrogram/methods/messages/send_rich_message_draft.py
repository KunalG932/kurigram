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
from pyrogram import enums, raw, types


class SendRichMessageDraft:
    async def send_rich_message_draft(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        draft_id: int,
        rich_message: Union[str, "types.InputRichMessage", "raw.base.InputRichMessage"],
        message_thread_id: Optional[int] = None,
        can_stop: Optional[bool] = None,
        keep_on_stop: Optional[bool] = None,
        is_rtl: Optional[bool] = None,
        skip_entity_detection: Optional[bool] = None,
    ) -> bool:
        """Use this method to stream a partial rich message to a user while the message is being generated.

        Note that the streamed draft is ephemeral and acts as a temporary 30-second preview - once the output is finalized,
        you must call :meth:`~pyrogram.Client.send_rich_message` or :meth:`~pyrogram.Client.send_message` with the complete message
        to persist it in the user's chat.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target private chat.

            draft_id (``int``):
                Unique identifier of the message draft; must be non-zero.
                Changes to drafts with the same identifier are animated.

            rich_message (``str`` | :obj:`~pyrogram.types.InputRichMessage`):
                The partial message to be streamed.

            message_thread_id (``int``, *optional*):
                Unique identifier for the target message thread.

            can_stop (``bool``, *optional*):
                Pass True to show the user a button to stop further drafts.
                The bot will receive an update (:obj:`~pyrogram.types.MessageGenerationStopped`) if the user presses the button.

            keep_on_stop (``bool``, *optional*):
                Pass True to keep the draft in the chat when the button is pressed.

            is_rtl (``bool``, *optional*):
                Pass True if the rich message must be shown right-to-left.

            skip_entity_detection (``bool``, *optional*):
                Pass True to skip automatic detection of entities.

        Returns:
            ``bool``: On success, True is returned.
        """
        return await self.send_message_draft(
            chat_id=chat_id,
            draft_id=draft_id,
            rich_message=rich_message,
            message_thread_id=message_thread_id,
            can_stop=can_stop,
            keep_on_stop=keep_on_stop,
            is_rtl=is_rtl,
            skip_entity_detection=skip_entity_detection,
        )
