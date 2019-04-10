#-------------------------------------------------------------------------------
# Name:        Build
# Purpose:
#
# Author:      David Gordon
#
# Created:     25/03/2019
# Copyright:   (c) David Gordon 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sc2
from sc2.constants import *



class build_order(sc2.BotAI):
    async def current_build(self,supply_left,supply):
        return [DRONE,"unit"]
        '''if supply < 22:
            opener(supply_left,supply)'''



    async def opener(self,supply_left,supply):
        return [DRONE,"unit"]
