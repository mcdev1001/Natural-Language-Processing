program should engage in a dialogue with the user, with your program Eliza playing the role of a psychotherapist. Your program should be able carry out "word spotting", that is it should recognize certain key words and respond simply based on that word being present in the input. It should also be able to transform certain simple sentence forms from statements (from the user) into questions (that Eliza will ask). Also, try to personalize the dialogue by asking and using the user's name.

Here's the start of an example dialogue...

eliza.py

-> [eliza] Hi, I'm a psychotherapist. What is your name?

=> [user] My name is Bridget.

-> [eliza] Hi Bridget. How can I help you today?

=> [Bridget] I want to rule the world.

-> [eliza] Bridget, why do you want to rule the world? [transform statement into ?]

=> [Bridget] I don't know, I think I crave power.

-> [eliza] Why don't you tell me more about your cravings. [word spot "crave" and respond.]

=> [Bridget] ...

Your program should be robust. If the user inputs gibberish or a very complicated question, Eliza should respond in some plausible way (I didn't quite understand, can you say that another way, etc.)

This program should rely heavily on the use of regular expressions,
