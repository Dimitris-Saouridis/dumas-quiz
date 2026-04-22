questions = (
    "What is the real name of the Count of Monte Cristo?",
    "How did Dantès appear (under which identities)?",
    "Who wanted to become a musketeer?",
    "Which of the four became an abbé?",
    "In which country does The Black Tulip take place?"
)

options = (
    "A) Danglars B) Fernand Mondego C) Gérard de Villefort D) Edmond Dantès",
    "A) Sinbad the Sailor B) The Count of Monte Cristo C) Abbé Busoni D) All of the above",
    "A) d’Artagnan B) Athos C) Aramis D) Porthos",
    "A) d’Artagnan B) Aramis C) Porthos D) Athos",
    "A) France B) Holland C) England D) Germany"
)

correct_answers = ("D", "D", "A", "B", "B")

Guesses = []
score = 0
print("This quiz is based on three novels: The Count of Monte Cristo, d’Artagnan and the Three Musketeers, and The Black Tulip, by the much-loved author Alexandre Dumas.")

print("The number of questions will increase in the future.")
for i in range(len(questions)):
    print("------------------------")
    print(questions[i])
    print()
    print(options[i])
    guess =input("Select (A,B,C,D): ").upper()
    Guesses.append(guess)
    if guess==correct_answers[i]:
        print("CORRECT!")
        score=score+1
    else:
        print("UNCORRECTED")
        print(f"The Correct answer is {correct_answers[i]}")

print("---------------")
print("----RESULTS----")
print("---------------")

for correct in correct_answers:
    print(correct, end=" ")
print()
for guess in Guesses:
    print(guess, end=" ")     
print()
percent_score = score/len(questions)*100
print(f"Your score is {percent_score}%")


