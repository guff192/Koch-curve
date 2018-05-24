
# coding: utf-8

# In[1]:


import turtle


def koch_turns(n):
    turns = []
    if n == 1:
        turns = [60, -120, 60]
    else:
        for turn in koch_turns(n-1):
            turns.append(60)
            turns.append(-120)
            turns.append(60)
            turns.append(turn)
        turns.append(60)
        turns.append(-120)
        turns.append(60)
    return turns

def turtle_koch_curve(n, line_length=10):
    for move in koch_turns(n):
        turtle.forward(line_length)
        turtle.left(move)
    turtle.forward(line_length)

