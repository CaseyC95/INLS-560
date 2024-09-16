# This is a mad lib example for functions.

def madlib(adverb_1,noun_1,noun_2,adverb_2):
    '''Mad lib function''' #Docstring must be indented.

    story = f'''
Ahoy, ye landlubber! If ye want to talk like a pirate, ye best learn to shout with a {adverb_1} roar! When ye see yer fellow matey, 
don’t just greet 'em, call 'em a "scurvy {noun_1}" or a "bilge rat." 
And make sure to shout it loud, so all can hear! If ye be stompin' across the deck, 
do it with heavy {noun_2} like ye own the whole ship! When it’s time to work, yell "Hoist the sails!" with all yer strength, 
and if ye get into a scrap, make sure ye fight {adverb_2} until the other blokes run in fear!
Arrr, that's the way o' the pirate

'''
    return story  

def get_user_input():
    '''Prompt the user for input for the mad lib.'''
adverb_1 = input("enter another adverb")
noun_1 = input("enter another noun")
noun_2 = input("enter anopther noun")
adverb_2 = input("enter another adverb")


#get user input
user_inputs = get_user_input()

def duplicate_get_input():
    '''prompt....'''
adverb_1 = input("enter   ")
noun_1 = input("enter   ")
noun_2 = input("enter   ")
adverb_2 = input("enter   ")




print (madlib('slowly','dog','boy','hard') )

