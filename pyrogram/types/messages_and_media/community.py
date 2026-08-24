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
from pyrogram import types
from ..object import Object


class Community(Object):
    """This object represents a community.

    Parameters:
        id (``int``):
            Unique identifier of the community.

        title (``str``):
            Title of the community.

        username (``str``, *optional*):
            Username of the community.

        photo (:obj:`~pyrogram.types.ChatPhoto`, *optional*):
            Photo of the community.
    """

    def __init__(
        self,
        id: int,
        title: str,
        username: Optional[str] = None,
        photo: Optional["types.ChatPhoto"] = None,
    ):
        super().__init__()
        self.id = id
        self.title = title
        self.username = username
        self.photo = photo


class CommunityChatAdded(Object):
    """Service message: chat or bot was added to a community.

    Parameters:
        community (:obj:`~pyrogram.types.Community`):
            The community to which the chat was added.
    """

    def __init__(self, community: "Community"):
        super().__init__()
        self.community = community


class CommunityChatRemoved(Object):
    """Service message: chat or bot was removed from a community.

    Parameters:
        community (:obj:`~pyrogram.types.Community`):
            The community from which the chat was removed.
    """

    def __init__(self, community: "Community"):
        super().__init__()
        self.community = community
