
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

class Location():
    def __init__(self,name,types):
        self.types = makeset(types)
        self.name = name



story = BrokenFarmStory()
story.addLocation("shed","workshop")
story.addLocation("shed","olive mill")
story.addLocation("shed","olive oil tank shed")
story.addLocation("yard","chicken coup")
story.addLocation("roof","house roof")
story.addLocation("roof","shed roof")

story.addEquipment(["shed","yard"],["engine","cable"],"red tractor")
story.addEquipment(["shed","yard"],["engine","cable"],"orange tractor")
story.addEquipment(["shed","yard"],["engine","cable"],"white ute")

story.addComponent([""])


print(engine.location_types)
print(engine.locations)

"""
Uncle Jim goes outside to see what is broken today.
He looks in the shed but nothing seems broken.
He looks in the chicken yard and everything is working fine.
But then he checks the carport and finds that the ute is broken is broken!
It looks like the goat has chewed the brake lights.
"screw you goat" say Uncle Jim.


"""


