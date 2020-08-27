'''Before the advent of QWERTY keyboards, texts and numbers were placed on the same key.

Input Format

First Line Consists of text

Constraints

0

Output Format

Return the respective numbers

Sample Input 0

abaxtu

Sample Output 0

222988
'''
line=input()
line=list(line.lower())
alphabets="abcdefghijklmnopqrstuvwxyz+,."
numbers=[2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9,0,'*',1]
output=""
for letter in line:
    output+=str(numbers[alphabets.index(letter)])
print(output)

