# Infix Expression Evaluation

**Step 01: Infix to Postfix**  
Use a stack to convert Infix to Postfix  
Create a string for the output  
Loop the entire string and follow these rules.
Rules:  
  1. If it is a number add it immediately to the string
  2. Follows the order of precedence (a is highest):  
    2.1. Multiplication/ Division  
    2.2. Addition/Subtraction/Modulus  
    2.3. Open parenthesis '('  
    2.4. Close parenthesis ')' (Optional: May be the same as Open parenthesis)  
  3. If the operator to be pushed to the stack has a higher precedence than the top of the stack, then just push the operator to the stack.  
  4. If the operator to be pushed to the stack has a lower or equal precedence than the top of the stack, pop the stack continuously until the top of the stack has a lower precedence.
  5. If the character to be pushed to the stack is a closing parenthesis ')', continuously pop the stack until an opening parenthesis '(' is found.  
 
**Step 02: Postfix Evaluation**
Evaluate the answer of the postfix expression   
Loop the entire string and follow these rules.  
Rules:
  1. If the current character is a digit, convert it to an integer then push it to the stack
  2. If the current character is a space, move to the next character
  3. If it is an operator, pop two integers from the stack then apply the operator.  
    Example: 1 2 + becomes 2 + 1  
    1 2 3 * + becomes 1 + ( 2 * 3 )
  4. If the end of the string has been reached then the top of the stack is the answer
