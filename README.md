1. **Which Additional Challenge(s) You Selected**  
    I chose Challenge 1- Expand the Story Vocabulary. 
2. **Why You Chose Those Challenge(s)**  
    I chose to expand the Mad Libs activity by adding more word types, extending the story, and implementing a replay feature. I found this challenge exciting because:
    It enhances creativity by allowing users to generate even funnier and more unexpected stories.
    Expanding the vocabulary adds depth to the game, making it more engaging and immersive.
    Implementing a replay feature makes the program feel more interactive and fun for repeated plays.
    It provided a great opportunity to practice loops, string formatting (f-strings), and input handling in Python.
3. **Reflection Questions & Answers**  
     - **Question 1:** What was the most interesting or surprising part of implementing your chosen feature(s)? 
        The most interesting part was seeing how small changes, like adding new input prompts (e.g., exclamations, transformations), made the game much funnier and unpredictable.
        Users could create totally unexpected and hilarious scenarios, which made testing really fun!

     - **Question 2:** What was the greatest obstacle or bug you faced, and how did you overcome it? 
        One challenge was handling user input variations (e.g., if a user entered extra spaces or capitalized answers inconsistently).
        Solution: I used .strip().lower() to clean input where needed (e.g., the replay question) to ensure consistency.
        Another challenge was making sure the story flowed well with different word choices. I overcame this by tweaking sentence structures and testing with multiple inputs.

     - **Question 3:** How did the feature branch and merge workflow help in organizing your code changes? 
        Using a feature branch for the expanded version helped in:
        Keeping the original simple Mad Libs intact while experimenting with new features separately.
        Allowing for easier debugging, as I could isolate changes without affecting the working version.
        Making the merge process smoother, since I could test and refine before integrating the new version. 

    - **Question 4:** What Python concepts (e.g., conditionals, loops, functions, file I/O) do you feel more confident in after completing this assignment?
        This challenge helped me strengthen my skills in:
        Loops (while True) – Used to keep the game running until the user wants to exit.
        Conditionals (if-else) – Ensured proper handling of user choices (e.g., replay option).
        String Formatting (f-strings) – Created dynamic, well-structured sentences for the story.
        User Input Handling (input().strip().lower()) – Made the game more user-friendly by preventing formatting issues.
        Debugging & Testing – Learned how to refine prompts and tweak sentence structures for better user experience.  