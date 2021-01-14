class Router:
    '''Router Class'''
    def __init__(self, model, swversion, ip_add):
        '''initialize value'''
        self.model = model
        self.swversion = swversion
        self.ip_add = ip_add

    def getdesc(self):
        '''return a formatted description of the router'''
        desc = f'Router model                 :{self.model}\n'\
               f'Software version             :{self.swversion}\n'\
               f'Router Management Address    :{self.ip_add}\n'\

        return desc

class Switch(Router):
    def getdesc(self):
        '''return a formatted desciption fo the switch'''
        desc = f'Switch model                 :{self.model}\n'\
               f'Software version             :{self.swversion}\n'\
               f'Switch Management Address    :{self.ip_add}\n'\



rtr1 = Router('iosV', '15.6.7', '192.168.155.71')
rtr2 = Router('isr4221', '15.9.5', '192.168.155.72')
sw1 = Switch('Cat9300', '16.9.5', '10.10.10.8')

print('Rtr1\n', rtr1.getdesc(), '\n', sep='')
print('Rtr2\n', rtr2.getdesc(),  sep='')
print('Sw1\n', sw1.getdesc(), '\n', sep='')
