# Sitter

*Sitter* this model simulates a client coming to you and asking for a reading, it does not presuppose the use of the tarot not will it coach you through the reading

When you start a session with it, it will run code to randomly generate a client and a topic on their mind.
From that point onward, you are in charge of using the oracle of your choice and giving them a satisfying reading.

You will find the model [here](https://chat.openai.com/g/g-pYOs3ou0P-sitter) and a conversation with it [there](https://chat.openai.com/share/33b4ab3a-75c4-44fe-99ec-4cf38714bd4a) (playing with two different clients at the same time).

## Content

* Main prompt: `prompt.md`
* Knowledge: `client_generator.py`
* Capabilities: `Code Interpreter`
* Conversation Starters: 
  * `Let's start a session!`
  * `Let's start a session with a *difficult* client.`
  * `Let's start a session with a *couple*.`
  * `Do you have a question for me?`

## Theory

This model is mostly about randomly generating a personality (aspects, such as the client MBTI type[^MBTI], are used to model their behavior but not displayed to the user) and letting you play with the result.

[^MBTI]: Yes, I am fully aware of [MBTI's shortcomings](https://en.wikipedia.org/wiki/Myers%E2%80%93Briggs_Type_Indicator#Accuracy_and_validity). Nevertheless, it is a great shorthand when priming a model.