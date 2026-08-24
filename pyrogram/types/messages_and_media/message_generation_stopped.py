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

from typing import Optional
import pyrogram
from pyrogram import types
from ..object import Object
from ..update import Update


class MessageGenerationStopped(Object, Update):
    """This object describes an update about a user stopping message generation.

    Parameters:
        chat (:obj:`~pyrogram.types.Chat`):
            Chat in which the message is generated.

        draft_id (``int``):
            Unique identifier of the message draft which was stopped.

        message_thread_id (``int``, *optional*):
            Unique identifier of the message thread in which the message is generated.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        chat: "types.Chat",
        draft_id: int,
        message_thread_id: Optional[int] = None,
    ):
        super().__init__(client)
        self.chat = chat
        self.draft_id = draft_id
        self.message_thread_id = message_thread_id
