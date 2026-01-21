PYTHON PROGRAMMING NOTES:

1. What Python Is
-> Python is a high-level programming language
-> High-level means human-readable and close to English
-> Programmer does not manage memory manually
-> Python handles memory, data types, and execution internally
-> Used for scripting, web, data science, AI, automation

2. Python Execution Model
-> Python is an interpreted language
-> Code executes line by line
-> No separate compile step like C or C++
-> If an error occurs, execution stops at that line
-> Previous lines remain executed

Example:
print("Start")
print(10 / 0)
print("End")

-> Output stops at division error
-> "End" never runs

3. Indentation Rule
-> Python uses indentation instead of curly braces
-> Indentation defines a block of code
-> Standard indentation is 4 spaces
-> Wrong indentation causes IndentationError

Example:
if True:
    print("Valid")

4. Variables
-> Variable is a name that stores a value
-> No need to declare data type
-> Type is assigned at runtime
-> Variable type can change

Example:
a = 10
a = "hello"

5. Variable Naming Rules
-> Must start with a letter or underscore
-> Cannot start with a number
-> Cannot contain spaces or special characters
-> Case-sensitive

Valid:
user_name
_age
totalMarks

Invalid:
2value
user-name
total marks

6. Core Data Types
-> int for whole numbers
-> float for decimal numbers
-> str for text
-> bool for True or False
-> None for no value

Example:
x = 10
y = 2.5
name = "Ram"
is_valid = True
data = None

7. Type Checking
-> Use type() to check data type

Example:
type(x)

8. Type Conversion
-> input() always returns string
-> Convert explicitly when needed

Conversions:
int("10")
float("3.5")
str(100)

Example:
age = int(input("Enter age: "))

9. Operators
-> Arithmetic operators
- + addition
- - subtraction
- * multiplication
- / division
- % remainder
- // floor division
- ** power

-> Comparison operators
- == equal
- != not equal
- > greater than
- < less than
- >= greater or equal
- <= less or equal

-> Logical operators
- and
- or
- not

10. Conditional Statements
-> Used for decision making
-> Code executes based on condition result

Structure:
if condition:
    statement
elif condition:
    statement
else:
    statement

-> Only first true condition executes

11. Truthy and Falsy Values
-> Falsy values
- 0
- ""
- []
- None
- False

-> All other values are truthy

12. Loops
-> Used to repeat code

for loop:
-> Used when number of iterations is known
Example:
for i in range(1, 6):
    print(i)

-> range(start, end) where end is excluded

while loop:
-> Used when condition controls loop
Example:
i = 1
while i <= 5:
    print(i)
    i += 1

13. Loop Control Statements
-> break exits the loop
-> continue skips current iteration

14. Lists
-> List stores multiple values
-> Ordered and mutable
-> Index starts from 0

Example:
nums = [10, 20, 30]

Access:
nums[0]
nums[-1]

Modify:
nums.append(40)
nums.remove(20)

Looping:
for n in nums:
    print(n)

***************************************************
-> Python favors readability over performance
-> Fewer lines of code
-> Heavy use of built-in functions
-> Dynamic typing requires careful handling

