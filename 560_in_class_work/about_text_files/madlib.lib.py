#Mad lib example for functions.

def madlib(adverb_1,noun_1,noun_2,adverb_2):
    '''Mad lib function'''

    story = f'''
Ahoy, ye landlubber! If ye want to talk like a pirate, ye best learn to shout with a {adverb_1} roar! When ye see yer fellow matey, 
don’t just greet 'em, call 'em a "scurvy {noun_1}" or a "bilge rat." 
And make sure to shout it loud, so all can hear! If ye be stompin' across the deck, 
do it with heavy {noun_2} like ye own the whole ship! When it’s time to work, yell "Hoist the sails!" with all yer strength, 
and if ye get into a scrap, make sure ye fight {adverb_2} until the other blokes run in fear!
Arrr, that's the way o' the pirate

'''
    return story


output_story = madlib('slowly','dog','boy','hard')
print(output_story)
