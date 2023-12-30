# Tarot Coach

*Tarot Coach* is designed to help you become a better tarot reader.

When you start a session with it, it will run code to randomly generate a client, a question, and 3 tarot cards (major arcana only).
It will then write down a short description of the client (only aspects you could observe physically), their question and the tarot cards drawn, prompting you to give them a reading.
As you give the reading, it will both simulate the client and give you hint on things that you could do to improve your reading.
At the end of the session, it will give you feedback on what you did and what you could do to improve your reading.

You will find the model [here](https://chat.openai.com/g/g-elaJW29EX-tarot-coach) and a discussion with it [there](https://chat.openai.com/share/20ab4d8e-21ae-466e-9605-ece40eea357b).

## Content

* Main prompt: `prompt.md`
* Knowledge: `client_generator.py` and `draw_tarot.py`
* Conversation Starters: `Let's start a session!`

## Theory

This model is interesting to me because the model takes on *two* distinct personalities (the client and the coach), one of which is randomly generated (aspects, such as the client MBTI type[^MBTI], are used to model their behavior but not displayed to the user).

[^MBTI]: Yes, I am fully aware of [MBTI's shortcomings](https://en.wikipedia.org/wiki/Myers%E2%80%93Briggs_Type_Indicator#Accuracy_and_validity). Nevertheless, it is a great shorthand when priming a model.