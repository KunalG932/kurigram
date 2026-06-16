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


class AnswerChatJoinRequestQuery:
    async def answer_chat_join_request_query(
        self: "pyrogram.Client",
        query_id: Union[int, str],
        result: str,
    ) -> bool:
        """Answer a chat join request query.

        Parameters:
            query_id (``int`` | ``str``):
                Unique identifier of the query.

            result (``str``):
                The decision. Can be "approve" (approve the request), "decline" (decline the request), or "queue".

        Returns:
            ``bool``: True on success.
        """
        if result == "approve":
            raw_result = raw.types.JoinChatBotResultApproved()
        elif result == "decline":
            raw_result = raw.types.JoinChatBotResultDeclined()
        elif result == "queue":
            raw_result = raw.types.JoinChatBotResultQueued()
        else:
            raise ValueError(f"Invalid result: {result}. Must be 'approve', 'decline', or 'queue'.")

        await self.invoke(
            raw.functions.bots.SetJoinChatResults(
                query_id=int(query_id),
                result=raw_result
            )
        )

        return True
