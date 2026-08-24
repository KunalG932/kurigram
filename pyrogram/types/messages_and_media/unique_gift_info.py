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


class UniqueGiftInfo(Object):
    """Describes a service message about a unique gift that was sent or received.

    Parameters:
        gift (:obj:`~pyrogram.types.Gift`):
            Information about the gift.

        origin (``str``):
            Origin of the gift. Currently, either "upgrade", "transfer", "resale", "gifted_upgrade", or "offer".

        text (``str``, *optional*):
            Text of the message that was added to the gift.

        entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
            Special entities that appear in the text.

        is_private (``bool``, *optional*):
            True, if the sender and gift text are shown only to the gift receiver.

        last_resale_currency (``str``, *optional*):
            For gifts bought from other users, currency in which payment was done ("XTR" or "TON").

        last_resale_amount (``int``, *optional*):
            For gifts bought from other users, price paid for the gift in Stars or nanograms.

        owned_gift_id (``str``, *optional*):
            Unique identifier of the received gift for the bot (on behalf of business accounts).

        transfer_star_count (``int``, *optional*):
            Number of Telegram Stars that must be paid to transfer the gift.

        next_transfer_date (``int``, *optional*):
            Point in time (Unix timestamp) when the gift can be transferred.
    """

    def __init__(
        self,
        gift: "types.Gift",
        origin: str,
        text: Optional[str] = None,
        entities: Optional[List["types.MessageEntity"]] = None,
        is_private: Optional[bool] = None,
        last_resale_currency: Optional[str] = None,
        last_resale_amount: Optional[int] = None,
        owned_gift_id: Optional[str] = None,
        transfer_star_count: Optional[int] = None,
        next_transfer_date: Optional[int] = None,
    ):
        super().__init__()
        self.gift = gift
        self.origin = origin
        self.text = text
        self.entities = entities
        self.is_private = is_private
        self.last_resale_currency = last_resale_currency
        self.last_resale_amount = last_resale_amount
        self.owned_gift_id = owned_gift_id
        self.transfer_star_count = transfer_star_count
        self.next_transfer_date = next_transfer_date
