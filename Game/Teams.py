__author__ = 'AnkuR'


class Team:
    def __init__(self,*args):
        self.members=[]
        for i in args:
            i.team=self
            self.members.append(i)

    def start(self):
        for i in self.members:
            i.start()

    def attackedby(self,target):
        for i in self.members:
            if i.health<=0:
                self.members.remove(i)
            else:
                if i.target is None:
                    i.target=target
    def target(self,target):
        for i in self.members:
            i.target=target


    def register(self,member):
        self.members.append(member)
        member.team=self






