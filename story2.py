
#Noun: name of a person, place, thing or idea. eg. man, adelaide
#Pronoun: A work used in place of a noun. eg. she, we, they
#Verb: Action or being. eg. jump, is, write
#Adjective: Modefies or describes a noun or pronoun. eg. pretty, blue, smart
#Adverb: Modefies or describes a verb, adjective or another adverb. eg. extremely, gently


import random 

def c(*args):
    return random.choice(args)


def makeset(v):
    try:
        if type(v) is str:
            v = {v}
        else:
            v = set(v)
    except:
        v = {v}        
    return v

assert type(makeset(5)) is set
assert type(makeset((1,2))) is set
assert type(makeset([1,2])) is set
assert type(makeset({1,2})) is set



class BrokenFarmStory():

    def __init__(self):
        self.locations = []
        self.equipment = []
        self.animals   = []

        self.addLocation("workshop"           ,"shed")
        self.addLocation("olive mill"         ,["shed","pumpshed"])
        self.addLocation("big tank shed"      ,["shed","pumpshed"])
        self.addLocation("house bore shed"    ,["pumpshed"])
        self.addLocation("main bore shed"     ,["pumpshed"])
        self.addLocation("big tank shed"      ,["shed","pumpshed"])
        self.addLocation("chicken yard"       ,"fenced")
        self.addLocation("backyard yard"      ,"fenced")
        self.addLocation("front of the house" ,"yard")
        self.addLocation("house roof"         ,"roof")
        self.addLocation("shed roof"          ,"roof")
        self.addLocation("olive orchid"       ,"orchid")

        self.addEquipment("red tractor"     ,["yard", "orchid"]    , ["chew","bunt"])
        self.addEquipment("orange tractor"  ,["yard", "orchid"]    , ["chew","bunt"])
        self.addEquipment("white ute"       ,["yard"]              , ["chew","bunt"])
        self.addEquipment("fence"           ,["fenced"]            , ["push"])
        self.addEquipment("antenna"         ,["roof"]              , ["bite"])
        self.addEquipment("irrigation radio",["orchid","pumpshed"] , ["bite"])
        self.addEquipment("drip line"       ,["orchid"]            , ["chew","bite"])
        self.addEquipment("irrigation valve",["orchid"]            , ["chew","block"])

        self.addAnimal("goat",["bunt","chew","scratch"])
        self.addAnimal("sheep",["bunt","chew"])
        self.addAnimal("peacock",["bite","poo"])
        self.addAnimal("crow",["bite","poo"])
        self.addAnimal("kangaroo",["chew","poo","pull"])
        self.addAnimal("sand",["block"])

    def addLocation(self, location_name, location_flags):
        location_flags = makeset(location_flags)
        self.locations.append({"location_flags":location_flags, "name":location_name})

    def addEquipment(self, equipment_name, location_flags,damage_flags):
        location_flags = makeset(location_flags)
        damage_flags   = makeset(damage_flags)
        self.equipment.append({"location_flags":location_flags,"damage_flags":damage_flags, "name":equipment_name})


    def addAnimal(self, animal_name, damage_flags):
        damage_flags = makeset(damage_flags)
        self.animals.append({"damage_flags":damage_flags, "name":animal_name})
       

    def __str__(self):
        broken_equipment = random.choice(self.equipment)

        possible_locations = [l for l in self.locations if bool(broken_equipment["location_flags"] & l["location_flags"] )]
        broken_location = random.choice(possible_locations)
        

        other_locations = self.locations.copy()
        other_locations.remove(broken_location)
        
        location1, location2 = random.sample(other_locations,2)

        possible_animals = [l for l in self.animals if bool(broken_equipment["damage_flags"] & l["damage_flags"] )]
        animal = random.choice(possible_animals)


        possible_damage = broken_equipment["damage_flags"] & animal["damage_flags"] 
        damage = random.choice(list(possible_damage))


        text = f"""\
Uncle Jim checks the farm to see what is working today.
He checks the {location1["name"]} but nothing seems broken.
He checks the {location2["name"]} and everything is working fine.
But then he checks the {broken_location["name"]}
and finds that the {broken_equipment["name"]} is not working properly!
It looks like the {animal["name"]} has {damage} it.
\"Damn that {animal["name"]}\"! says Jim.
This needs to be fixed right away.
Uncle Jim.

"""

        return text

story = BrokenFarmStory()

print(story)





"""
Uncle Jim goes outside to see what is broken today.
He looks in the shed but nothing seems broken.
He looks in the chicken yard and everything is working fine.
But then he checks the carport and finds that the ute is broken!
It looks like the goat has chewed the brake lights.
"screw you goat" say Uncle Jim.

but when he checks the shed he finds that the tractor is broken.
It looks like the peckock has wrecked the window wipers

but when he checks the orchid he finds the the irrigation radio is broken.
It looks like the crow as chewed the wire.
"""


