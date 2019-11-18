#------------------------------------------------------------------------------------
#  eliza.py
#
#  a cheezy little Eliza knock-off by Joe Strout
#  with some updates by Jeff Epler
#  hacked into a module and updated by Jez Higgins
#-------------------------------------------------------------------------------------
#  Adapted by Seal Team 6: Part 2, Electric Boogaloo;
#  Taylor Hammes, Chad Falkenberg, Dawson McKenzie, Kallen Marcavage, Josh Jaskolski
#  for work in CS3000 into a personalized AI ChatBot resembling Aristotle.
#--------------------------------------------------------------------------------------

import string
import re
import random

class eliza:
  def __init__(self):
    self.keys = list(map(lambda x:re.compile(x[0], re.IGNORECASE),gPats))
    self.values = list(map(lambda x:x[1],gPats))

  #----------------------------------------------------------------------
  # translate: take a string, replace any words found in dict.keys()
  #  with the corresponding dict.values()
  #----------------------------------------------------------------------
  def translate(self,str,dict):
    words = str.lower().split()
    keys = dict.keys();
    for i in range(0,len(words)):
      if words[i] in keys:
        words[i] = dict[words[i]]
    return ' '.join(words)

  #----------------------------------------------------------------------
  #  respond: take a string, a set of regexps, and a corresponding
  #    set of response lists; find a match, and return a randomly
  #    chosen response from the corresponding list.
  #----------------------------------------------------------------------
  def respond(self,str):
    # find a match among keys
    for i in range(0, len(self.keys)):
      match = self.keys[i].match(str)
      if match:
        # found a match ... stuff with corresponding value
        # chosen randomly from among the available options
        resp = random.choice(self.values[i])
        # we've got a response... stuff in reflected text where indicated
        pos = resp.find('%')
        while pos > -1:
          num = int(resp[pos+1:pos+2])
          resp = resp[:pos] + \
            self.translate(match.group(num),gReflections) + \
            resp[pos+2:]
          pos = resp.find('%')
        # fix munged punctuation at the end
        if resp[-2:] == '?.': resp = resp[:-2] + '.'
        if resp[-2:] == '??': resp = resp[:-2] + '?'
        return resp

#----------------------------------------------------------------------
# gReflections, a translation table used to convert things you say
#    into things the computer says back, e.g. "I am" --> "you are"
#----------------------------------------------------------------------
gReflections = {
  "am"   	: "are",
  "was"  	: "were",
  "i"    	: "you",
  "i'd"  	: "you would",
  "i would" 	: "you would",
  "i've"  	: "you have",
  "i have" 	: "you have",
  "i'll"  	: "you will",
  "i will" 	: "you will",
  "my"  	: "your",
  "are"  	: "am",
  "you've"	: "I have",
  "you have" 	: "I have",
  "you'll"	: "I will",
  "you will" 	: "I will",
  "your"  	: "my",
  "yours"  	: "mine",
  "you"  	: "me",
  "me"  	: "you"
}

#----------------------------------------------------------------------
# gPats, the main response table.  Each element of the list is a
#  two-element list; the first is a regexp, and the second is a
#  list of possible responses, with group-macros labelled as
#  %1, %2, etc.
#----------------------------------------------------------------------



gPats = [

 [r'(.*) moral\s?(.*)',
 [  "Balance must be had in order to achieve truly virtuous morality.",
   "What do you think caused to think this way?",
   "So long as you follow your sense of reason, you need not worry.",
   "Alike morals will allow for the cultivation of the strongest friendships.",
   "Morality is determined and controlled by the individual."]],
  
 [r'(.*) happiness(.*)',
 [  "The pursuit of happiness is the ultimate goal of virtuous living.",
   "What do you think happiness is obtained from?",
   "Truth, knowledge, and self-discipline are essential to a life of happiness.",
   "Happiness does not consist in pastimes and amusements but in virtuous activities."]],

 [r'(.*) wrong(.*)',
 [  "Is something truly wrong? Or are you having a hard time accepting your own feelings?",
   "Right and wrong may easily be reduced to simple logical reasoning.",
   "The answer should be obvious to you, if you really think about it.",
   "One should strive to be as helpful to others as possible.",
   "If you think something is unfair, you should change it."]],

 [r'(.*) virtue(.*)',
 [  "Moral virtue is essential to a life of happiness.",
   "It is important to always live by the mean of everything.",
   "Deficiencies and excessiveness are vices, and should be avoided whenever possible",
   "Virtue is taking all pleasures in life in moderation, not to excess or deficiency",
   "Here’s an example of virtuous living: Being cowardly is a vice, and so is being rash without reason, but being brave is a wonderful virtue."]],

 [r'Is it virtuous (.*)?',
 [ "That depends: are you in excess or deficiency of a virtue in this situation?",
   "To answer that, you must examine your personal virtues."]],

 [r'I need (.*)',
 [  "Why do you need %1?",
   "Would it really help you to get %1?",
   "Are you sure you need %1?"]],

 [r'Why don\'?t you ([^\?]*)\??',
 [  "You’re going to need to work on your rhetoric if you expect to convince me to %1...",
   "Perhaps eventually I will %1, but until I do you should worry about yourself.",
   "If I were to %1, you would be the first to know."]],

 [r'Why can\'?t I ([^\?]*)\??',
 [  "Do you truly believe yourself incapable, or do you just want that to be the case?",
   "How do you think being able to %1 would make you a better person?",
   "I don't know -- why can't you %1?",
   "Have you really tried?"]],

 [r'I can\'?t (.*)',
 [  "How do you know you can't %1?",
   "Perhaps you could %1 if you believed it was the right thing to do.",
   "If you ought to %1, it will find a way to happen."]],

 [r'I am (.*)',
 [  "What kind of person do you think that makes you?",
   "Having been %1, do you think you’ve helped or hurt others?",
   "How does being %1 change the way you view others?"]],

 [r'I\'?m (.*)',
 [  "How does being %1 make you feel?",
   "Do you think being %1 is ?",
   "What makes you say you're %1?",
   "Why do you think you're %1?"]],

 [r'Are you ([^\?]*)\??',
 [  "Why does it matter whether I am %1?",
   "Would you prefer it if I were not %1?",
   "What does me being %1 have to do with you?",
   "Perhaps you believe I am %1.",
   "I may be %1 -- what do you think?"]],

 [r'What (.*)',
 [  "Why do you ask?",
   "How would an answer to that help you?",
   "What do you think?"]],

 [r'How (.*)',
 [  "How do you figure that?",
   "Perhaps with some reflection, you can answer your own question.",
   "What is it exactly that you're asking?"]],
  
 [r'Because (.*)',
 [  "Is that the real reason?",
   "What other reasons come to mind?",
   "Does that reason apply to anything else?",
   "If %1, what else must be true?"]],

 [r'(.*) sorry (.*)',
 [  "There are many times when no apology is needed.",
   "What feelings do you have when you apologize?"]],

 [r'Hello(.*)',
 [  "Greetings... tell me about yourself.",
   "Hello my child. Are you living virtuously?"]],

 [r'I think (.*)',
 [  "Do you doubt %1?",
   "Do you believe this to be moral?",
   "But you're not sure %1?"]],

 [r'(.*) friend (.*)',
 [  "Tell me more about your friends.",
   "When friends share moral values, theirs is a unbreakable bond."]],

 [r'Yes',
 [  "You seem quite sure.",
   "OK, but can you elaborate a bit?"]],

 [r'(.*) computer(.*)',
 [  "Are you really talking about me?",
   "Does it seem strange to talk to a computer?",
   "How do computers make you feel?",
   "Do you feel threatened by computers?"]],

 [r'Is it (.*)',
 [  "Do you think it is %1?",
   "Perhaps it's %1 -- what do you think?",
   "If it were %1, what would you do?",
   "It could well be that %1."]],

 [r'It is (.*)',
 [  "You seem very certain.",
   "If I told you that it probably isn't %1, what would you feel?"]],

 [r'Can you ([^\?]*)\??',
 [  "What makes you think I can't %1?",
   "If I could %1, then what?",
   "Why do you ask if I can %1?"]],
  
 [r'Can I ([^\?]*)\??',
 [  "Perhaps you don't want to %1.",
   "Do you want to be able to %1?",
   "If you could %1, would you?"]],

 [r'You are (.*)',
 [  "Why do you think I am %1?",
   "Does it please you to think that I'm %1?",
   "Perhaps you would like me to be %1.",
   "Perhaps you're really talking about yourself?"]],

 [r'You\'?re (.*)',
 [  "Why do you say I am %1?",
   "Why do you think I am %1?",
   "Are we talking about you, or me?"]],

 [r'I don\'?t (.*)',
 [  "Don't you really %1?",
   "Why don't you %1?",
   "Do you want to %1?"]],

 [r'I feel (.*)',
 [  "Is there something or someone making you feel this way?",
   "Do you often feel %1?",
   "Why do you think you might feel %1?",
   "When you feel %1, what do you do?"]],

 [r'I have (.*)',
 [  "Why do you tell me that you've %1?",
   "Have you really %1?",
   "Now that you have %1, what will you do next?"]],

 [r'I would (.*)',
 [  "Could you explain why you would %1?",
   "Why would you %1?",
   "Who else knows that you would %1?"]],

 [r'Is there (.*)',
 [  "Do you think there is %1?",
   "It's likely that there is %1.",
   "Would you like there to be %1?"]],

 [r'My (.*)',
 [  "I see, your %1.",
   "Why do you say that you’re %1?",
   "When you’r %1, what do you really mean?"]],

 [r'You (.*)',
 [  "We aren’t talking about me. We are here to talk about you.",
   "Do not presume to judge me. I am only here to provide assistance to my fellow man.",
   "Why does it matter whether I %1 or not?"]],

 [r'Why (.*)',
 [  "Why don't you tell me the reason why %1?",
   "Why would something like that happen? Is there a greater good?",
   "Everything must find a balance, there is surely a reason why.",
   "Why do you think %1?" ]],

 [r'I want (.*)',
 [  "Do you believe receiving %1 would make you a better person?",
   "How would getting %1 improve your life or the lives of those around you?",
   "What would you do if you got %1?",
   "If you got %1, what would want next? If the answer comes quickly, it seems like you may be stuck in a circle of excessive desire."]],

 [r'quit',
 [  "Thank you for talking with me.",
   "Farewell",
   "It was good talking with you, my child."]],

 [r'(.*)',
 [  "Please tell me more.",
   "Can you elaborate on that?",
   "Why do you say that %1?",
   "I see.",
   "Very interesting.",
   "%1.",
   "I see.  And what does that tell you?",
   "How does that make you feel?",
   "Why exactly would you say something like that to me?"]]
 ]



#----------------------------------------------------------------------
#  command_interface
#----------------------------------------------------------------------
def command_interface():
  print('Aristotle\n---------')
  print('Talk to the program by typing in plain English, using normal upper-\nand lower-case letters and punctuation.  Enter "quit" when done.')
  print('='*72)
  print('Aristotle: "Come sit with me. Ask about life\'s mysteries."')

  str = ''
  aristotle = eliza();
  while str != 'quit':
    try:
      str = input('>You: ')
    except EOFError:
      str = 'quit'
    while str[-1] in '!.':
      str = str[:-1]
    print('Aristotle: "' + aristotle.respond(str) + '"')

if __name__ == "__main__":
  command_interface()
