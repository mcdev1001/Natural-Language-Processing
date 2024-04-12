import re
import random

class Eliza:
    def __init__(self):
        self.username = None

    def run(self):
        print("""INTRO: 
        Author: Devon McDermott
        Date: 2.04.24
        This program implements an Eliza rogerian psychotherapist chatbot and is a psychotherapist simulation. The user interacts with Eliza, and Eliza responds with predefined responses based on patterns. 
        Problem Description:
        Eliza operates by recognizing specific input patterns and generating appropriate responses. It uses regular expressions for pattern matching/searching and sentence transformation, simulating a basic understanding of language. The program aims to create an illusion of deep conversation by responding to user input in a psychologically relevant manner. 
        Type "exit", "quit", or "bye" to end the program. 
        Example:
        User Input: "I feel sad" 
        Eliza Response: "Can you tell me more about your feelings?" 
        Usage Instructions:
        1. Run the program. 
        2. Enter your name when prompted. 
        3. Engage in a conversation by typing your thoughts to Eliza. 
        4. Type "exit", "quit", or "bye" to end the conversation. 

        Algorithm 
        Overview:
        1. Initialize the Eliza chatbot by entering your name when prompted. 
        2. Continuously prompt the user for input until an exit command is received. 
        3. Use regular expressions to identify specific input patterns. 
        4. Generate prewritten responses based on the patterns. 
        5. Apply grammatical transformations using pronoun swapping. 
        6. Display Eliza response to the user.""")

        print("[eliza] Hi, I'm a psychotherapist. What is your name?")
        self.username = input("=> [user] ")

        print(f"[eliza] Hi {self.username}. How can I help you today?")

        while True:
            user_input = input("=> [{}] ".format(self.username))

            if self.is_exit_command(user_input):
                print("[eliza] Goodbye!")
                break

            response = self.generate_response(user_input)
            print("-> [eliza] {}".format(response))

    def is_exit_command(self, user_input):
        return user_input.lower() in ['exit', 'quit', 'bye']

    def generate_response(self, user_input):

        # Greetings
        if re.search(r'\b(?:hello|hi|hey|whats up)\b', user_input, re.IGNORECASE):
            return f"Hello, {self.username}! How can I help you today?"
        # Feelings
        elif re.search(r'\b(?:feel|feeling|feels|sad|mad|angry|depressed|down|happy|glad|excited|hopeful|hopeless|thrilled)\b', user_input, re.IGNORECASE):
            return f"{self.username}, can you tell me more about your feelings?"

        # well-being
        elif re.search(r'\b(?:how are you|hows it going|how ya doin|how are you doing)\b', user_input, re.IGNORECASE):
            return f"I'm just a computer program, but thank you for asking, {self.username}! How about you?"

        # Word spotting wants
        if re.search(r'\b(?:crave|want|desire|dying to|need|trying)\b', user_input, re.IGNORECASE):
            return f"{self.username}, why do you want that?"

        # Asking about family
        family_pattern = r'\b(?:family|mom|dad|mother|father|sister|brother|sibling|grandmother|grandfather|uncle|aunt)\b'
        if re.search(family_pattern, user_input, re.IGNORECASE):
            return f"{self.username}, can you tell me more about your family?"

        # Handling "why" questions
        why_pattern = r'\b(?:why)\s*([^?.!]*[?.!])?'
        if re.search(why_pattern, user_input, re.IGNORECASE):
         return f"{self.username}, why do you ask that?"

        #handling idk
        dont_know_pattern = r'\b(?:I don\'?t know)\b'
        if re.search(dont_know_pattern, user_input, re.IGNORECASE):
         return f"{self.username}, tell me about your doubts."


        # Handling "I think"
        if re.search(r'\b(?:I think)\b', user_input, re.IGNORECASE):
            transformed_sentence = self.swap_pronouns(re.sub(r'\b(?:I think)\b', '', user_input, flags=re.IGNORECASE))
            return f"{self.username}, why do you think {transformed_sentence.strip()}?"

        # Handling "are you" questions
        #will only switch response to a different question not same question repeated
        are_you_pattern = r'\b(?:are you)\b'
        are_you_responses = [
                "What does that question mean to you?",
                "Can you elaborate on that?",
                "I'm here to help. What are your thoughts on the question?"
            ]

        if re.search(are_you_pattern, user_input, re.IGNORECASE):
                return f"{self.username}, {random.choice(are_you_responses)}"



        # Discussing future plans
        elif re.search(r'\b(?:future|plans|life)\b', user_input, re.IGNORECASE):
            return f"{self.username}, what are your aspirations for the future?"

        # Mentioning a challenge or problem
        elif re.search(r'\b(?:problem|challenge|issue|dilemma|pickle|hardship|hard time|emergency|911|sos)\b', user_input, re.IGNORECASE):
            return f"I understand, {self.username}. Can you tell me more about the challenge you're facing?"

        # Expressions of gratitude
        elif re.search(r'\b(?:thank you|thanks|thanks alot|Im grateful)\b', user_input, re.IGNORECASE):
            return f"You're welcome, {self.username}! Is there anything else you'd like to talk about?"

         # if statements
        information = self.extract_information(r'\bif\b\s*(.*)', user_input)
        if information:
            transformed_information = self.swap_pronouns(information)
            return f"Interesting question, {self.username}. Can you tell me more about if {transformed_information}?"

        # Grammatical transformation using pronoun swapping
        transformed_input = self.swap_pronouns(user_input)
        if transformed_input != user_input:
            return f"{self.username}, {transformed_input}?"



        # Default response for unrecognized input
        return "Tell me more about that."
    def extract_information(self, pattern, message):
        match = re.search(pattern, message)
        if match:
            return match.group(1)
        else:
            return None

    def swap_pronouns(self, phrase):
        # Handle "I'm"
        phrase = re.sub(r'\bI\'?m\b', 'you are', phrase, flags=re.IGNORECASE)

        # Handle "I am"
        phrase = re.sub(r'\bI am\b', 'you are', phrase, flags=re.IGNORECASE)

        # Handle "You" NOT WORKING IDK WHYYYY
        phrase = re.sub(r'\bYou\b', 'I', phrase, flags=re.IGNORECASE)

        # Handle "I"
        phrase = re.sub(r'\bI\b', 'you', phrase, flags=re.IGNORECASE)

        # Handle "my"
        phrase = re.sub(r'\bmy\b', 'your', phrase, flags=re.IGNORECASE)

        return phrase


#main
if __name__ == "__main__":
    eliza = Eliza()
    eliza.run()
