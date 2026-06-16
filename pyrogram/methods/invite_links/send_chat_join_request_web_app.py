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

from typing import Union
import pyrogram
from pyrogram import raw


class SendChatJoinRequestWebApp:
    async def send_chat_join_request_web_app(
        self: "pyrogram.Client",
        query_id: Union[int, str],
        web_app_url: str,
    ) -> bool:
        """Send a Web App to a user who requested to join a chat.

        Parameters:
            query_id (``int`` | ``str``):
                Unique identifier of the query.

            web_app_url (``str``):
                The URL of the Web App.

        Returns:
            ``bool``: True on success.
        """
        await self.invoke(
            raw.functions.bots.SetJoinChatResults(
                query_id=int(query_id),
                result=raw.types.JoinChatBotResultWebView(url=web_app_url)
            )
        )

        return True
