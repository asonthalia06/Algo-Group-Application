Question 2: IMPLEMENT STACK (HARDER)

For this question, the directions clearly stated I couldn't use any sort of
container, so a list was out of the question. Immediately what came to mind was
a linked list approach: I could create my own special node class to keep track 
of values and the order of elements with a next pointer. Also, a linked list 
would ensure the stack dynamically resized and by mainting a dummy node, I
could push nodes onto the front of the stack in O(1) time and access the front
nodes in O(1) time for pop and peek.

Testing:

I added my testing for stack functionality in the repo. I made sure every 
method worked properly and error messages were thrown correctly.