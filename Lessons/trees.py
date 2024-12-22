class generalNode:
    def __init__(self, data):
        # This is the start of the data structure (aka creating the node)
        self.data = data
        # This would be initializing empty children nodes as a list
        self.children = []
    def addChild(self, childNode):
        # Adding a child to the children's list
        self.children.append(childNode)
    def display(self, level=0):
        print(" " * level + str(self.data))
        for child in self.children:
            child.display(level + 1)
print("General Tree:")
general_root = generalNode('Root')
child1 = generalNode('Child1')
child2 = generalNode('Child2')
child3 = generalNode('Child3')

general_root.addChild(child1)
general_root.addChild(child2)
child2.addChild(generalNode("Child2.1"))
child2.addChild(generalNode("Child2.2"))
child3.addChild(generalNode("Child3.1"))
general_root.addChild(child3)

general_root.display()