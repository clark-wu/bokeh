# coding=utf-8
"""
Create on 2020/12/31 13:32
@desc:
@author: wurenxi
"""
import logging # isort:skip
log = logging.getLogger(__name__)

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Bokeh imports
from ..message import Message

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------

__all__ = (
    'comm_req',
)

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

class comm_req(Message):
    ''' Define the ``OK`` message for acknowledging successful handling of a
    previous message.

    The ``content`` fragment of for this message is empty.

    '''

    msgtype  = 'COMM_REQ'

    @classmethod
    def create(cls, request_id, **metadata):
        ''' Create an ``comm`` message

        Args:
            request_id (str) :
                The message ID for the message the precipitated the OK.

        Any additional keyword arguments will be put into the message
        ``metadata`` fragment as-is.

        '''
        header = cls.create_header(request_id=request_id)
        return cls(header, metadata, {})

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
