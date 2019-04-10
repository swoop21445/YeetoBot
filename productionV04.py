#-------------------------------------------------------------------------------
# Name:        production
# Purpose:
#
# Author:      David Gordon
#
# Created:     19/03/2019
# Copyright:   (c) David Gordon 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sc2
from sc2.constants import *
from BuildV04 import build_order
import unit_dictV04

class production_queue(sc2.BotAI):
    def __init__(self,units):
        self.units = units

    '''def convert_type_id(unit):'''



    async def start_production(self,units,_game_data,minerals,vespene,state,_game_info,townhalls,supply_left,_client,workers,supply_used):
        self.units = units
        self._game_data = _game_data
        self._game_info = _game_info
        self.minerals = minerals
        self.vespene = vespene
        self.state = state
        self.supply_left = supply_left
        self.townhalls = townhalls
        self._client = _client
        self.workers = workers
        self.supply_used = supply_used
        self.build_order = build_order()
        await self.production_assignment()

    async def production_assignment(self):
        unit = await self.build_order.current_build(self.supply_left,self.supply_used)
        print(unit[1])
        print (unit[0])
        if unit[1] == "unit":
            print("if entered")
            self.train_units(unit[0])
            pass
        elif unit[1] == "building":
            self.build_structure(unit[0])
        else:
            print("assignment error")


    async def train_units(self,unit):
        '''building units function'''
        print("entering train function")
        for larva in self.units(LARVA):
            if self.can_afford(unit):
                await self.do(larva.train(unit))

    async def train_overlord(self):
        larva = self.units(LARVA)
        if self.can_afford(OVERLORD) and self.supply_left < 5 and not self.already_pending(OVERLORD):
            try:
                await self.do(larva[0].train(OVERLORD))
            except:
                pass
        else:
            pass

    async def build_structure(self,structure):
        '''generic building function for all buildings apart from hatcheries, will build near first hatchery test after expansion to see if this remains true'''
        hatchery = self.units(HATCHERY)
        if self.can_afford(structure):
            await self.build(structure, near = hatchery[0])
        else:
            pass
