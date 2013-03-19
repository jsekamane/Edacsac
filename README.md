# Edacsac – Visualizing Discussions

[**Visit the project page**](http://jonas.sekamane.com/projects/edacsac/)

## Explanation
> I go to a website and read an article. Man, that was really great. I’d like to comment and ask the author a question. I scroll down… 384 comments. Ugh. Screw this.
[Jason Santa Maria](http://v4.jasonsantamaria.com/articles/cultivating-conversations/)

This is first and for most me trying to familiarise myself with the [D3.js – Data-Driven Documents library](http://d3js.org/). Its learning by doing, and learning by playing around with some real-world data. I am trying to master more visualisation tools and gain practical experience within [Graph Theory](http://en.wikipedia.org/wiki/Graph_theory).

It is however also an (prematurely) early attempt at providing a quick overview of large online discussions (often 100+ comments long, and spread over multiple pages). A long time ago, I read [Jason Santa Maria's **Cultivating Conversation**](http://jasonsantamaria.com/articles/cultivating-conversations/) article, about how long discussions overwhelm users and create repetition. This of course depreciates the value of the conversation and discourages users from further adding to it. Needless to say the problem (and possible solutions) intrigued me. And at infrequent intervals my thoughts have return to the issue. Only now has it become something more than skittish and spooky ideas. What I [present here](http://jonas.sekamane.com/projects/edacsac/) is not a solution to the problem describe by Jason as such. It does not automatically create 10-20 milemakers for every 200 comments. Neatly summarising the entire conversation and lowering the barrier of entry. But it might provide hints as were to start.

> When that author’s comments are highlighted, they form a natural series of milemarkers in the discussion; chances are if something important happened, the author came back to address it. ... What if we could take the idea of highlighting author comments a step further and set real milemarkers in comment threads?
[Jason Santa Maria](http://v4.jasonsantamaria.com/articles/cultivating-conversations/)

How would you go about automating these milemakers? Keep in mind that the less ambitious proposal is an editor manually creating them. But even for an editor a 100+ discussion is a feat to quickly summarise. Where to start? What to include? What not to include? etc. By structuring the conversation around the referrals made by users (e.g. mentioning or replying to other users) I believe the problem can be greatly reduced, to something more manageable. Irrespectively of whether you favour the editorial or automated approach. The threads of the conversation are exposed. And one could start by summarising the major threads of the discussion – they take up a lot of "space", but most often treat and discuss only a single theme. Eliminating these (or having summarise them), one could then continue to smaller and smaller threads.

As you can read this is all still very vague and speculative. Including other metrics, weighting connections and trying out various algorithms, as well as text analysis, would be a natural next step. However the presence of actual data, in a visualised an understandable format, will hopefully make it all more earth-bound.

## Inspiration
This project is inspired by The New York Times Company Research & Development Lab's [Cascade project](http://nytlabs.com/projects/cascade.html).