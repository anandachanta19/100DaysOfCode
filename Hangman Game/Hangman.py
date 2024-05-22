import random
import Hangman_words
import Hangman_art
end_of_game = False
chosen_word = random.choice(Hangman_words.word_list)

empty = []
for i in range(len(chosen_word)):
    empty.append("_")

lives = 6

print(Hangman_art.logo)
while '_' in empty:
    geuss = input("Guess a Letter: ").lower()
    if geuss in empty:
        print(f"You've already guessed {geuss}")

    flag = False
    for i in range(len(chosen_word)):
        if chosen_word[i] == geuss:
            empty[i] = geuss
            flag = True
    if flag == True:
        flag = False
    else:
        lives -= 1
        print("No Match")
    print(Hangman_art.stages[lives])
    if lives == 0:
        print ("You loose!")
        break
    print(f"{' '.join(empty)}")


if "_" not in empty:
        end_of_game = True
        print("You win.")     