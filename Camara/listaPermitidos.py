class flabianos:
    
    def __init__(self):
        self.Invitados=['Carlos','Lucas']

    def TuSiTuNo(self,EllosSi):        
        if EllosSi in self.Invitados:
            print('Bienvenido {}'.format(EllosSi))
        else:
            print('NO'.format(EllosSi))
