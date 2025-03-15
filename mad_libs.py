import time  # Adding delay for a fun storytelling experience

# Python Mad Libs Warm-Up Activity - Expanded Version
print("Welcome to Python Mad Libs!")
print("Answer the following questions to create your very own silly story.\n")

while True:  # Loop to allow replay
    # Gather user inputs
    name = input("Enter a person's name: ")
    place = input("Enter a place: ")
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    adverb1 = input("Enter an adverb: ")
    adjective2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    verb2 = input("Enter another verb: ")
    adverb2 = input("Enter another adverb: ")
    exclamation = input("Enter an exclamation (e.g., Wow!, Oh no!): ")

    # Build the longer, more detailed story
    story = (
        f"\nHere is your silly story:\n"
        f"Today, {name} saw a {adjective1} {noun1} in {place} that decided to {verb1} {adverb1}.\n"
        f"I couldn't believe my eyes! It was unlike anything I had ever seen before.\n\n"
        
        f"As I got closer, the {noun1} suddenly transformed into a {adjective2} {noun2}!\n"
        f"Without warning, it started to {verb2} {adverb2}, making a loud noise that echoed through the air.\n\n"
        
        f"'{exclamation}!' I shouted, stumbling backward. Was I dreaming? Was this real?\n"
        f"I reached out to touch the {noun2}, but before I could, it vanished into thin air.\n\n"
        
        f"Now, no one believes me when I tell them about the {adjective1} {noun1} that turned into a {adjective2} {noun2}...\n"
        f"But I know what I saw! And one day, I'll prove it to the world!"
    )

    # Add a dramatic pause before revealing the story
    print("\nGenerating your story...")
    time.sleep(2)
    print(story)

    # Ask if the user wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Keep dreaming big!")
        break  # Exit the loop if the user doesn't enter 'yes'
