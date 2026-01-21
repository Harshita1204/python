INTRODUCTION TO MACHINE LEARNING – PYTHON NOTES

1. What is Machine Learning
-> Machine Learning is a way to make computers learn from data
-> Instead of writing rules, we give examples
-> Computer finds patterns by itself
-> Learning means improving performance with experience (data)

Simple idea:
-> More data + learning algorithm = better decisions

Example:
-> Email spam filter
- We do not write rules for every spam mail
- We show emails labeled as spam or not spam
- Machine learns patterns and predicts new emails

2. Why Machine Learning is Needed :
-> Traditional programming uses fixed rules
-> Some problems are too complex for rules

Example:
Traditional programming:
-> If email has word "free" then spam
-> This fails many times

Machine learning:
-> Learns thousands of features automatically
-> Adapts to new spam types

Used when:
-> Data is large
-> Patterns are complex
-> Rules are hard to define

3. Machine Learning Using Python :
-> Python is most popular for ML
-> Simple syntax
-> Huge libraries available

Common Python libraries:
-> numpy for numbers
-> pandas for data handling
-> matplotlib for graphs
-> scikit-learn for ML algorithms

4. Types of Machine Learning :
-> There are three main types
- Supervised Learning
- Unsupervised Learning
- Reinforcement Learning

5. Supervised Learning:
-> Data is labeled
-> Input and correct output both are given
-> Model learns mapping from input to output

Example structure:
-> Input -> Model -> Output
-> Correct output already known

Real-life example:
-> Student marks prediction
- Input: hours studied
- Output: marks
- Past data available with correct marks

Another example:
-> House price prediction
- Input: size, location, rooms
- Output: price
- Past house prices known

Spam detection:
- Input: email text
- Output: spam or not spam

Types of Supervised Learning:
-> Classification
- Output is category
- Example: spam or not spam, disease yes or no

-> Regression:
- Output is number
- Example: price, salary, temperature

Python example idea:
-> Give dataset with labels
-> Train model
-> Predict new value

6. Unsupervised Learning :
-> Data is not labeled
-> No correct answers provided
-> Model finds patterns by itself

Main goal:
-> Discover hidden structure in data

Real-life example:
-> Customer grouping
- Input: shopping behavior
- No labels like "rich" or "poor"
- Model groups customers automatically

Another example:
-> Music recommendation
- Groups users with similar taste

Another example:
-> Image grouping
- Groups similar images together

Common tasks:
-> Clustering
- Group similar data
- Example: K-means clustering

-> Dimensionality reduction :
- Reduce number of features
- Example: compress data

Difference from supervised:
-> No teacher
-> No correct output
-> Only patterns

Python idea:
-> Give raw data
-> Algorithm groups data
-> You analyze the groups

7. Reinforcement Learning ;
-> Learning by trial and error
-> No dataset with answers
-> Agent interacts with environment

Key components:
-> Agent: learner
-> Environment: where agent acts
-> Action: what agent does
-> Reward: feedback

****** REMEMBER **********
-> Good action -> reward
-> Bad action -> penalty
-> Goal is to maximize reward

Real-life example:
-> Teaching a dog
- Sit -> treat
- Wrong action -> no treat

EXAMPLE of a game:
-> Video game AI
- Move right -> gain points
- Wrong move -> lose points

Difference from others:
-> Learning happens while acting
-> No fixed dataset
-> Continuous learning

Python usage:
-> Simulations
-> Games
-> Robotics models

8. Comparison of ML Types :
-> Supervised
- Labeled data
- Known output
- Prediction focused

-> Unsupervised :
- No labels
- Pattern discovery
- Grouping focused

-> Reinforcement :
- Reward based
- Trial and error
- Decision making over time

9. Simple ML Flow Using Python :
-> Collect data
-> Clean data
-> Choose algorithm
-> Train model
-> Test model
-> Use model for prediction




