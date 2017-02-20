class Tower:
    def __init__(self, name, elements=[]):
        self.name = name
        self.elements = elements

    def __call__(self):
        print self.name
        return self.elements

    def push(self, tower):
        print "Pushing last element of {0} to {1}".format(tower.name, self.name)

        if (self.length() == 0) or self.pushable(tower):
            self.elements.append(tower.last())
            tower.chop()
            # print tower()
            # print self()
        else:
            raise Exception("Pushing larger element!")

    def pushable(self, tower):
        return self.elements[-1] > tower.last()

    def chop(self):
        self.elements.pop()

    def length(self):
        return len(self.elements)

    def last(self):
        return self.elements[-1]

ta = Tower('A', [3,2,1])
tb = Tower('B', [])
tc = Tower('C', [])

def moveTower(height, startPole, middlePole, endPole):
    if height >= 1:
        moveTower(height-1, startPole, endPole, middlePole)
        middlePole.push(startPole)
        moveTower(height-1, endPole, middlePole, startPole)

# Will move disks from towerA to towerB
moveTower(3, ta, tb, tc)
