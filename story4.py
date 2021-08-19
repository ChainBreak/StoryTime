import random 

class Node():
    def __init__(self,name,base_class_set,has_class_set):
        self.name = name
        self.leaf = False
        self.base_class_set = base_class_set
        self.sub_class_set = set()
        self.has_class_set = has_class_set


class ConceptGraph():

    def __init__(self):
        self.node_dict = {}

    def make_set(self,v):
        try:
            if v is None:
                v = set()
            elif type(v) is str:
                v = {v}
            else:
                v = set(v)
        except:
            v = {v}        
        return v

    def add(self,name,is_a=None,has_a=None):
        node = self.add_(name,is_a,has_a)
        node.leaf = True

    def add_(self,name,is_a=None,has_a=None):
        
        is_a = self.make_set(is_a)
        has_a = self.make_set(has_a)

        node = Node(name,is_a,has_a)
        self.node_dict[name] = node
        return node

    def build_graph(self):
        # For each class, recurse up the inheritance tree 
        # linking parents to children and visa versa
        for node in self.node_dict.values():
            self.base_class_recursion(node)

        # For each node
        for node in self.node_dict.values():
            
            # Collect all the class you own by following has a relationships
            has_class_set = self.has_recursion(node)
            node.has_class_set.update(has_class_set)

            # For each parent base class, collect all the classes they own
            for name in list(node.base_class_set):
                base_node = self.node_dict[name]
                has_class_set = self.has_recursion(base_node)
                node.has_class_set.update(has_class_set)


        # for node in self.node_dict.values():
        #     print(node.name,"is a", node.base_class_set)
        #     print(node.name,"parent of", node.sub_class_set)
        #     print(node.name,"has a ", node.has_class_set)

    def base_class_recursion(self,node):
        # For all base classes of this node
        for name in list(node.base_class_set):
            # Get the actual node
            base_node = self.node_dict[name]
            
            # Assign this class as a sub class of the base class
            base_node.sub_class_set.update({node.name})
            
            # Assign all my sub classes to sub classes of my base class
            base_node.sub_class_set.update(node.sub_class_set)
            
            # Recurse up the tree to get all the classes i inherit from
            all_base_class_set = self.base_class_recursion(base_node)

            # Append all parent bases to my base class set
            node.base_class_set.update(all_base_class_set)

        # return the base classes set for this node
        return node.base_class_set

    def has_recursion(self,node):
        
        # For each node that this class owns/has
        for name in list(node.has_class_set):

            # Get the node object
            has_node = self.node_dict[name]

            # Collect all sub classes of the class that you own
            node.has_class_set.update(has_node.sub_class_set)

            # Follow ownership and collect everything you also own/have
            node.has_class_set.update( self.has_recursion(has_node) )
            
        # Return the set of classes that this node owns
        return node.has_class_set

    def get(self,base_class_name,owned_by=None):
        node = self.node_dict[base_class_name]
        sub_class_set = node.sub_class_set


        if owned_by is not None:
            owner_node = self.node_dict[owned_by]
            sub_class_set = sub_class_set & owner_node.has_class_set

        sub_class_set = {name for name in sub_class_set if self.node_dict[name].leaf}

        


        return sub_class_set
    

def c(*args):
    return random.choice(args)
if __name__ == "__main__":
    cg = ConceptGraph()

    # NAME, IS A, HAS A
    ### LOCATIONS ####
    cg.add_("location")

    # Open yards have vehicle and animal access
    cg.add_("open_yard","location",["vehicle","animal"])
    cg.add_("closed_yard","location",["animal"])
    cg.add_("shed","location","shed_equipment")
    cg.add_("bore_shed","location",["bore_equipment"])
    cg.add_("lawn","location","lawn_irrigation_equipment")

    cg.add("the front lawn", ["open_yard","lawn"])
    cg.add("the back lawn", ["closed_yard","lawn"])
    cg.add("the drive way", "open_yard")
    cg.add("the small bore shed","bore_shed")
    cg.add("the big bore shed","bore_shed")
    cg.add("the olive mill","location","olive_pump")
    cg.add("the chop shop","shed")
    cg.add("the workshop","shed")

    ### BREAKABLE THINGS ###
    cg.add_("breakable_thing")

    cg.add_("animal","breakable_thing")

    cg.add_("vehicle","breakable_thing")
    cg.add_("tractor","vehicle",["diesel_motor","hydraulics"])
    cg.add("the orange kabota tractor","vehicle")
    cg.add("the red case tractor","vehicle")
    cg.add("the red starrian","vehicle")

    cg.add_("bore_equipment","breakable_thing")
    cg.add("the irrigation radio","bore_equipment")
    cg.add("the water filter","bore_equipment")

    cg.add_("olive_pump","breakable_thing")
    cg.add("the decanter feed pump","olive_pump")
    cg.add("the waste piston pump","olive_pump")
    cg.add("the waste piston pump","olive_pump")

    cg.add_("shed_equipment","breakable_thing")
    cg.add("the welder","shed_equipment")
    cg.add("the angle grinder","shed_equipment")
    cg.add("the drill press","shed_equipment")

    cg.add_("lawn_irrigation_equipment","breakable_thing")
    cg.add("a pop up sprinkler","lawn_irrigation_equipment")
    cg.add("the solenoid valve","lawn_irrigation_equipment")
    cg.add("the underground pipe","lawn_irrigation_equipment")

    ### COMPONENTS ###
    cg.add_("component")
    cg.add_("electric_motor","component",)
    cg.add_("diesel_motor","component")
    # cg.add("a fuel injector","")
    cg.add_("hydraulics","component",)


    
    # cg.add_("tractor",["vehicle"])
    # cg.add_("ute",["vehicle"])
    # cg.add_("motor bike",["vehicle"])
    # cg.add_("component")
    # cg.add_("component_vehicle",["component"])
    # cg.add_("tire", ["component_vehicle"])
    # cg.add_("battery", ["component_vehicle"])
    cg.build_graph()
    # print(bfs.node_dict)


    for location in cg.get("location"):
        breakable_things = cg.get("breakable_thing",owned_by=location)
        if len(breakable_things) == 0:
            print(location,"Has no breakable things")


    for breakable_thing in cg.get("breakable_thing"):
        component = cg.get("component",owned_by=breakable_thing)
        if len(component) == 0:
            print(breakable_thing,"Has no components")

    location1,location2,location3 = random.sample(cg.get("location"),3)
    broken_thing, = random.sample(cg.get("breakable_thing",owned_by=location3),1)

    text = f"""\
Uncle Jim checks the farm to see what is broken today.
He checks {location1} but everything is normal.
He checks {location2} and everything is working fine.
But then he checks {location3} and finds that something is wrong with {broken_thing}"""
# and finds that the {broken_equipment["name"]} is not working properly!
# It looks like the {animal["name"]} has {damage} it.
# \"Damn that {animal["name"]}\"! says Jim.
# This needs to be fixed right away.
# Uncle Jim.

# """

    print(text)
    
