# Trent Duncan
# 9/10/24
# f-String Adventure Story

'''
Directions:

1. Update the comment block at the top of this script.

2. Use the Python `input( )` function to prompt (ask) the user for three pieces of information:

     - the hero's first name
     - the setting of the story (e.g., forest, desert, cave system)
     - the object the hero finds while on his/her adventure

3. Assign each piece of information collected to a variable with a short, specific name.

4. Declare (create) a variable named `story` and assign to it the `f-string` that is your adventure story

5. Use the `print( )` function to display your adventure story on the screen.

6. Execute (run) your script in Visual Studio Code and correct any errors.
'''

# heros first name

hero_name= input("what is your hero's name?")

print(f'so your journy starts your name {hero_name}')

# setting of the story

setting= input('where does this story take place?')

print(f' so {hero_name} your journy starts at {setting}')

# found object

object_found= input('what item did you find as you were exploring?')

print(f'while {hero_name} was exploring {setting} they stubbled acrossed {object_found}')