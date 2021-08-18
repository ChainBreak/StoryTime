
class Node():
    def __init__(self,name,is_a,has_a):
        self.name = name
        self.is_a = is_a
        self.has_a = has_a

        self.is_a_visited = False

    def __str__(self):
        return self.name

class BrokenFarmStory():

    def __init__(self):
        self.node_dict = {}

        self.add_node("location")
        self.add_node("open_yard",is_a=["location"],has_a=["vehicle"])
        self.add_node("front yard", ["open_yard"])
        # self.add_node("the area in front of the shed", ["open_yard"])

        self.add_node("device",)
        self.add_node("vehicle",["device"])
        self.add_node("tractor",["vehicle"])


        self.build_graph()

    def add_node(self,name,is_a=None,has_a=None):
        if is_a is None:
            is_a = set()
        if has_a is None:
            has_a = set()
        if not isinstance(is_a,set):
            is_a = set(is_a)
        if not isinstance(has_a,set):
            has_a = set(has_a)
        node = Node(name,is_a,has_a)
        self.node_dict[name] = node

    def build_graph(self):
        for node in self.node_dict.values():
            self.is_recursion(node)


        for node in self.node_dict.values():
            for name in list(node.is_a):
                next_node = self.node_dict[name]
                has_a = self.has_recursion(next_node)
                node.has_a.update(has_a)
            node.has_a -= node.is_a
            # print(node.name,"has a", node.has_a)

        for node in self.node_dict.values():
            print(node.name,"is a", node.is_a)
            print(node.name,"has a", node.has_a)

    def is_recursion(self,node):
        # print("recursion" ,node.name)
        for name in list(node.is_a):
            next_node = self.node_dict[name]
            next_node.has_a.update({node.name})
            new_is_a = self.is_recursion(next_node)
            node.is_a.update(new_is_a)

        return node.is_a

    def has_recursion(self,node):
        # print("has recursion" ,node.name)
        has_a = set()
        for name in list(node.has_a):
            next_node = self.node_dict[name]
            has_a.update(next_node.has_a)
            new_has_a = self.has_recursion(next_node)
            has_a.update(new_has_a)

        return has_a



if __name__ == "__main__":
    bfs = BrokenFarmStory()
    # print(bfs.node_dict)
