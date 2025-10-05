from option2 import IntStack

# test stack creation and pop/peek from empty stack
print("")
print("Test stack creation and pop/peek from empty stack:")
emptyStack = IntStack()
try: emptyStack.pop()
except IndexError as e: print(e) # error
try: emptyStack.peek()
except IndexError as e: print(e) # error
print("")

# test stack creation and pushing values
print("Test stack push:")
stackA = IntStack()
try: stackA.push("hello")
except TypeError as e: print(e) # error
stackA.push(5)
stackA.push(10)
stackA.push(15) # stack is now 5,10,15
print("Stack A peek: ", stackA.peek()) # 15
print("")

# test stack pop and dynamic resizing
print("Test stack pop, peek, and dynamic resizing:")
print("Stack A size: ", stackA.size()) # 3
print("Stack A pop: ", stackA.pop()) # 15
print("Stack A size: ", stackA.size()) # 2
print("Stack A peek: ", stackA.peek()) # 10
print("")

# test draining the stack to empty then raising errors
print("Test draining the stack to empty then raising errors:")
stackA.pop()
stackA.pop()
print("Stack A size: ", stackA.size()) # 0
try: stackA.pop()
except IndexError as e: print(e) # error
try: stackA.peek()
except IndexError as e: print(e) # error
print("")
