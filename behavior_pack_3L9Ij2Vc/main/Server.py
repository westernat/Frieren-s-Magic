# coding=utf-8
from .QuModLibs.Server import *

@Listen(Events.GameTypeChangedServerEvent)
def test(args):
    playerId = args['playerId']
    msg = compFactory.CreateMsg(playerId)
    msg.NotifyOneMessage(playerId, str(Entity(playerId).getBox3D().height))
