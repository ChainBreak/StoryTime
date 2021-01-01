
#Noun: name of a person, place, thing or idea. eg. man, adelaide
#Pronoun: A work used in place of a noun. eg. she, we, they
#Verb: Action or being. eg. jump, is, write
#Adjective: Modefies or describes a noun or pronoun. eg. pretty, blue, smart
#Adverb: Modefies or describes a verb, adjective or another adverb. eg. extremely, gently


import random 

def c(*args):
    return random.choice(args)


name = "Lauren"
boygirl = "girl"
heshe = "she"
hisher = 'her'
bodypart = c('foot','hand','nose','mouth','hair','tooth','toe','finger','arm','leg')

skill = c(
    'building lego ' + c('houses','towers','toilets'), 
    'cooking ' + c('birthday cake','booger bread','poo pie'),
     )

like_list = [
    f"climbing {c('the walls','trees','on the roof')}",
    f"riding {hisher} {c('electric kart','bike')}",
]

story = f"""{name} was a {c('smart','silly','funny','loud')} {boygirl} \
who was {c('very','extremly')} {c('skilled','good')} at {skill}. 
{heshe} liked {c(*like_list)} and doing {c('farts','raspberries','head stands')}.
One day {heshe} woke up to find that {hisher} {bodypart} was missing. 
{heshe} couldn't find it anywhere. 
The last time {heshe} used it was when {heshe} was making a cake.
{heshe} needed to find it 
{heshe} looked in her bed.
{heshe} looked in her wardrobe.
And {heshe} looked outside in the sand pit"""
    

print(story)


