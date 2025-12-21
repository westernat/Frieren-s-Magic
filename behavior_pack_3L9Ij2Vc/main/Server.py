# coding=utf-8
from .QuModLibs.Modules.EventRegistry.ServerBus import SubscribeEvent, GameEvents
from .QuModLibs.Server import *

@SubscribeEvent
def test(event=GameEvents.GameTypeChangedServerEvent()):
    playerId = event.playerId
    msg = compFactory.CreateMsg(playerId)
    msg.NotifyOneMessage(playerId, str(Entity(playerId).getBox3D().height))
