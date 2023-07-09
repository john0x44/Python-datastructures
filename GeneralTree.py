#General tree structure 
class GTree:
    def __init__(self,data):
            self.data = data 
            self.children = [] 
            self.parent = None 

    def addChild(self,child):
          child.parent = self 
          self.children.append(child)

    def getLevel(self):
        level = 0 
        p = self.parent 
        while p:
              level += 1 
              p = p.parent 
        return level 

    def print(self):
        print(f"{' ' * self.getLevel() * 5}{self.data}")
        if self.children:
            for child in self.children:
                child.print()

# Test the general tree 
root = GTree("Electronics")
phones = GTree("Phones")
phones.addChild(GTree("Iphone"))
phones.addChild(GTree("Android"))
tv = GTree("TV")
tv.addChild(GTree("Samsung"))
tv.addChild(GTree("Panasonic"))
expensiveTV = GTree("ExpensiveTV")
expensiveTV.addChild(GTree("GoldTV"))
expensiveTV.addChild(GTree("DiamondTV"))
tv.addChild(expensiveTV)

root.addChild(phones)
root.addChild(tv)


root.print()