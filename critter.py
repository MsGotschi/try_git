class Critter(object):
    
    '''A virtual Pet'''
    total = 0
    @staticmethod
    def status():
        print('the total number of critters is', Critter.total)
        
    def __init__(self, name, hunger, boredom, mood):
        print('a new critter has been born')
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        self.__mood = mood
        Critter.total+=1

    def __passtime(self):
        self.hunger += 1
        self.boredom += 1

    def talk(self):
        print("i'm ", self.name, "and I feel ", self.__mood)
        self.__passtime()

    def eat(self, food=4):
        print('yum yum am eating mamf mamf')
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__passtime()

    def __kill(self):
        print('Critter dies :(')
        self.name='dead'
        self.__mood = 'dead'
        Critter.total-=1

    def death(self):
        self.__kill()
    
    def __str__(self):
        s='Critter Object\n'
        s+='name: '+self.name+'\n'
        s+='mood: '+self.__mood+'\n'
        s+='hunger: '+str(self.hunger)+'\n'
        s+='boredom: '+str(self.boredom)+'\n'
        s+='number: '+str(Critter.total)+'\n'
        return s

#main program
if __name__ == "__main__":
    fred = Critter('fred', 20,15,'happy')
    print(fred)
    fred.eat(10)
    print(fred)
    input('press ENTER to exit')
    
