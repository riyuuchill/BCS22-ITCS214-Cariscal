# Class: Node for Linked List
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


# Class: Stack in LinkedList
class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        new = Node(x)

        if self.top is None:
            self.top = new
            self.top.next = None

        else:
            new.next = self.top
            self.top = new

    def pop(self):
        if self.top is None:
            print("Stack underflow.")
            return

        elif self.top.next is None:
            popped = self.top.data
            self.top = None
            return popped

        else:
            temp = self.top
            popped = temp
            self.top = temp.next
            temp = None
            return popped
    
    def getList(self):
        if self.top is None:
            print("Stack underflow.")

        else:
            reversedList = []
            temp = self.top
            while temp:
                reversedList.append(temp.data)
                temp = temp.next
            return reversedList


# Function: Palindrome Checker
def checker(palInput):

    # Making sure that the inputted words are converted to lower cases
    palindrome = palInput.lower()

    # Here is where the cleaned output is stored
    cleanList = []

    # Reverses the letters of the stored output in cleanList
    reverseStack = Stack()

    for character in palindrome:

        # Filters the non-letter characters and stores the letter characters on cleanList
        if character.isalpha():
            cleanList.append(character)
            reverseStack.push(character)

    # Prepares the stored characters to be outputted
    reverseList = reverseStack.getList()
    clean = "".join(cleanList)
    reverse = "".join(reverseList)

    print(f"""==================================================
              PALINDROME CHECKER
    Original: {palInput}
    Cleaned: {clean}
    Reversed: {reverse}
    """)

    # Verifies if the sentence is a palindrome or not
    if clean == reverse:
        print("Palindrome.")
    else:
        print("Not a palindrome.")

    print("==================================================")



# Asks the user to input a word or sentence that will be checked whether it is a palindrome or not
palindrome = input("Enter your input: ")
checker(palindrome)