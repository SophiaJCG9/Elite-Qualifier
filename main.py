#I want to practice pull requests ,so I am adding this comment.
#Practicing changing again.
import random
#header
print("Hello, Welcome to ChatBot. I am Bot: Sophia. Lets Chat! To end chat simply type: Stop. Lets chat! If chatting stops you can type: Question! or Joke!")

#Seperate header from Chat
print("*************************************************")

#Chat
ChatBot_Name = "Sophia"

quit_character = "Stop"

userName = (str(input(ChatBot_Name + ": Hello! Whats your name?\n")))
#Common Responses I could think of
responses = {"how are you?": "Good. And you?" , "good": "Narly!", "great": "Glad you're doing well", "fine": "Only fine? Darn.", "bad": "Oh no. I hope you feel better soon.", "terrible": "Tommorow will be better. I know it!", "what are you?": "I'm the best chatBot out there!", "ok": "Certainly."}

#Chat Continued (Using Common Responses)
def chat_1():
  
  
  userInput = str.lower(input(ChatBot_Name + ": " + "Greetings " + userName + "! How are you?\n"))

  #index = user_response.index(userInput
  #print (ChatBot_Name,": ", bot_answer[index])

  
  if userInput in responses.keys():
    print(ChatBot_Name + ": " + responses[userInput])

chat_1()

#Random facts retrieved from: https://parade.com/966564/parade/fun-facts/

def generate_fact(userInput):
  facts = [
    "1. Three presidents, all Founding Fathers—John Adams, Thomas Jefferson, and James Monroe—died on July 4. Presidents Adams and Jefferson also died the same year, 1826; President Monroe died in 1831. Coincidence? You decide. (constitutioncenter.org)",

  "2. The Barbie doll’s full name is Barbara Millicent Roberts, from Willows, Wisconsin. Her birthday is March 9, 1959, when she was first displayed at the New York Toy Fair. (barbiemedia.com)",

  "3. There actually aren’t “57 varieties” of Heinz ketchup, and never were. Company founder H.J. Heinz thought his product should have a number, and he liked 57. Hint: Hit the glass bottle on the “57,” not the bottom, to get the ketchup to flow. (heinz.com)",

  "4. One of President John Tyler’s grandsons is still alive today—and he was born in 1790. How is this possible? President Tyler, the 10th US president, was 63 when his son Lyon Tyler was born in 1853; Lyon’s son was born when he was 75. President Tyler’s living grandson, Harrison Tyler is 92. Lyon’s other son Lyon Jr. passed away in 2020 at the age of 95. The Tyler family still maintains the President’s home, Sherwood Forest Plantation in Virginia. (sherwoodforest.org)",

  "5. The tallest man ever recorded was American giant Robert Wadlow (1918–1940), who stood 8 feet 11 inches. Wadlow’s size was the result of abnormally enlarged pituitary gland. (guinnessworldrecords.com)",

  "6. The tallest living man is 37-year-old Sultan Kosen, from Turkey, who is 8 feet, 2.8 inches, who set the record in 2009. His growth is also due to a pituitary issue. (guinnessworldrecords.com)",

  "7. The oldest person ever to have lived (whose age could be authenticated), a French woman named Jeanne Louise Calment, was 122 years old when she died in 1997. (guinnessworldrecord.com)",

  "8. Sliced bread was first manufactured by machine and sold in the 1920s by the Chillicothe Baking Company in Missouri. It was the greatest thing since…unsliced bread? (chllicothenews.com)"
  ]
  return random.choice(facts)
  
#Random Jokes retrieved from: https://www.fatherly.com/play/best-funny-one-liners-clean-jokes-kids/

def generate_joke(userInputTwo):
  jokes = [
    "Don’t you hate it when someone answers their own question? I do.",

    "A sandwich tried to get a reservation at a restaurant, but the waiter said they don’t serve food there.",

    "There are three types of people: those who can count and those who can’t.",

    "Don’t spell part backward. It’s a trap.",

    "Don’t believe the hype. Velcro is the ultimate rip-off.",

    "Do you know how scientists freshen their breath? With experi-mints!",

    "I recently saw a sign that said: “Watch for Animals.” What a great deal!",

    "I’m throwing a space-themed party for my birthday, but I don’t want to planet."
  ]
  return random.choice(jokes)

def generate_questions(userInputThree):
  questions= [
  "If you were in a circus, which character would you be?",
  "What is the worst advice you have given?",
  "What is one thing you should never say at a wedding?",
  "What is the worst pickup line you have ever heard?",
  "If you could only store one type of food in your pocket, what would you carry?",
  "What is the worst present you have ever received and why?",
  "If you were a farm animal, which would you be and why?",
  "What is the weirdest food combination you’ve ever tried?"
  ]
  answers = [
    "How interesting!",
    "You don't say!",
    "Very cool!",
    "Programming is fun!"
  ]
  
  return random.choice(questions)
  return random.choice(answers)







def init_chat():

  userInput = input(" ")

  while userInput != "Random Fact!":
    userInput = input("Hmm I don't understand. Type: Stop. if you want to end chat. Ask me for a Random Fact by typing exactly: Random Fact!")
 
  while userInput == "Random Fact!":
    userInput = input(generate_fact(userInput) + "\n")
  
  while userInput == "Joke!":

    userInput = input(generate_joke(userInput)+ "\n")
    
  while userInput == "Question!":
    userInput = input(generate_questions(userInput)+ "\n")
  

 

if __name__ == "__main__":
  init_chat()






