# INITIAL DESCRIPTION
# Suppose you have a word document or a random piece of text and you want to add a numbering/bullets or any marker to each line of the text.
# This short python program can help you do that immediately with a click. Just copy the text by using Ctrl+C or (Mac-CTRL+C) and run 
# this program. And then press Ctrl+V (Mac-CTRL+V) in place of original text. And BOOM! You have the desired output.
# May be inefficient for small text files. Works wonders for very large files.
# Modules needed: pyperclip 
# This can be easily installed by typing pip install pyperclip

# CODE BEGINS HERE

# Importing required module
import pyperclip

# Bringing in the text to python. The pyperclip.paste() assigns all the text to text variable
text = pyperclip.paste()

# Splitting the text on each line
lines = text.split('\n')                      # using the .split() method with '\n' to split the 'text' on each new line
for line in range(len(lines)):
                  lines[line] = str(line + 1) + '. '  + lines[line]    # adds numbers (MODIFY CODE HERE to change numbers to something else)
 
# Joining the lines
text = '\n'.join(lines)

# Copy back the text to clipboard so that you can paste it back
pyperclip.copy(text)
