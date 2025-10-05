Question 2: IMPLEMENT STACK (HARDER)

For this question, the directions clearly stated I couldn't use any sort of
container, so a list was out of the question. Immediately what came to mind was
a linked list approach: I could create my own special node class to keep track 
of values and use a next pointer to preserve the order of elements with a next pointer.
would ensure the stack dynamically resized and by mainting a dummy node, I
could push nodes onto the front of the stack in O(1) time and access the front
nodes in O(1) time for pop and peek.

Testing:

I added my testing for stack functionality in the repo. I made sure every 
method worked properly and error messages were thrown correctly. Here is the
testing terminal output:

aaravsonthalia@MacBook-Air-295 algo-group-take-home % python3 testing.py

Test stack creation and pop/peek from empty stack:
Error, pop from empty stack.
Error, peek from empty stack.

Test stack push:
Stack A peek:  15

Test stack pop, peek, and dynamic resizing:
Stack A size:  3
Stack A pop:  15
Stack A size:  2
Stack A peek:  10

Test draining the stack to empty then raising errors:
Stack A size:  0
Error, pop from empty stack.
Error, peek from empty stack.

aaravsonthalia@MacBook-Air-295 algo-group-take-home % 
