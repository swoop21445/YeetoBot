#-------------------------------------------------------------------------------
# Name:        Starcraft
# Purpose:
#
# Author:      Felicity
#
# Created:     13/02/2019
# Copyright:   (c) Felicity 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sc2
from sc2 import run_game,maps, Race , Difficulty
from sc2.player import Bot,Computer,Human,Observer
from Yeeto_mainV04 import YeetoBot

run_game(maps.get("AutomatonLE"), [
    Bot(Race.Zerg,YeetoBot(),"YeetoBot"),
    Computer(Race.Terran, Difficulty.Easy)
    ], realtime=True)
