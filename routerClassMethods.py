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



rtr1 = Router('iosV', '15.6.7', '192.168.155.71')
rtr2 = Router('isr4221', '15.9.5', '192.168.155.72')

print('Rtr1\n', rtr1.getdesc(), '\n', sep='')
print('Rtr2\n', rtr2.getdesc(),  sep='')
