from asyncio import shield
from ...utils.constants import SHIELD, SHIELD_TYPE
from .power_up import PowerUp

class Shield(PowerUp):
    
    def __init__(self):
        self.image = SHIELD
        self.type = SHIELD_TYPE
        super(Shield, self).__init__(self.image, self.type)
