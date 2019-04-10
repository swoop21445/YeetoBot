#-------------------------------------------------------------------------------
# Name:        Yeeto_main
# Purpose:
#
# Author:      David Gordon
#
# Created:     13/03/2019
# Copyright:   (c) David Gordon 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sc2
from sc2.constants import *
from productionV04 import production_queue


class YeetoBot(sc2.BotAI):
    def __init__(self):
        self.iterations_per_minute = 165
        self.modules_loaded = False

    async def on_step(self,iteration):
        await self.distribute_workers()
        ##self.worker_numbers()
        if self.modules_loaded == False:
            self.produce = production_queue(self.units)
            self.modules_loaded = True
        await self.produce.start_production(self.units,self._game_data,self.minerals,self.vespene,self.state,self._game_info,self.townhalls,self.supply_left,self._client,self.workers,self.supply_used)

'''    def worker_numbers(self):
            expansions = self.owned_expansions()
            if len(expansions) < 2:
                self.max_workers = len(expansions)*22
            else:
                self.max_workers = 60
'''
