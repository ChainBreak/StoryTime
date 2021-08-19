
class Node():
    def __init__(self,name,base_class_set,has_class_set):
        self.name = name
        self.base_class_set = base_class_set
        self.sub_class_set = set()
        self.has_class_set = has_class_set

        self.is_a_visited = False

    def __str__(self):
        return self.name

class BrokenFarmStory():

    def __init__(self):
        self.node_dict = {}

        self.add_node("location")
        self.add_node("open_yard",["location"],["vehicle"])
        self.add_node("front yard", ["open_yard"])
        self.add_node("the area in front of the shed", ["open_yard"])

        self.add_node("device",)
        self.add_node("vehicle",["device"],["component_vehicle"])
        self.add_node("tractor",["vehicle"])
        self.add_node("ute",["vehicle"])
        self.add_node("motor bike",["vehicle"])

        self.add_node("component")
        self.add_node("component_vehicle",["component"])

        self.add_node("tire", ["component_vehicle"])
        self.add_node("battery", ["component_vehicle"])


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
            self.base_class_recursion(node)


        for node in self.node_dict.values():
            for name in list(node.base_class_set):
                base_node = self.node_dict[name]
                has_class_set = self.has_recursion(base_node)
                node.has_class_set.update(has_class_set)


        for node in self.node_dict.values():
            print(node.name,"is a", node.base_class_set)
            print(node.name,"parent of", node.sub_class_set)
            print(node.name,"has a ", node.has_class_set)

    def base_class_recursion(self,node):
        # print("recursion" ,node.name)
        # For all base classes of this node
        for name in list(node.base_class_set):
            base_node = self.node_dict[name]
            
            #Set this class as a sub class of the base class
            base_node.sub_class_set.update({node.name})
            base_node.sub_class_set.update(node.sub_class_set)
            all_base_class_set = self.base_class_recursion(base_node)
            node.base_class_set.update(all_base_class_set)

        return node.base_class_set

    def has_recursion(self,node):
        # print("has recursion" ,node.name)
   
        for name in list(node.has_class_set):
            has_node = self.node_dict[name]

            node.has_class_set.update({has_node.name})
            node.has_class_set.update(has_node.sub_class_set)
            node.has_class_set.update( self.has_recursion(has_node) )
            

        return node.has_class_set



if __name__ == "__main__":
    bfs = BrokenFarmStory()
    # print(bfs.node_dict)
