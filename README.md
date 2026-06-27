# Chomskers Sentence Generator V2

## What is this?

This is a CLI Python program that generates random, nonsensical yet syntactically sound English sentences using a context-free grammar, in the style of Noam Chomsky's example sentence from Syntactic Structures (1957): "Colorless green ideas sleep furiously." I made this to better understand constituency/abstract syntax trees and formal language theory, as well as to integrate recursion into an original project that isn't a Fibonacci calculator or file finder. 

## Why the name? 

I have a friend who changes names that end with -y or -i to "ers". Emily becomes Emilers, Yomi becomes Yomers, and Chomsky becomes Chomskers, it's an inside joke between us. I often humorously call Noam Chomsky "Norman Chomskers", the former as a result of Ali G's interview with him wherein he calls him "Norman Chompsky". 

# What do I need to run it?

1. A standard Python install
2. A terminal
3. Nothing else, for the moment (though I might add a PySimpleGUI-based GUI). 
# How do I run it?

Use whatever terminal you desire and run main.py. You'll find a sentence printed on the screen. That's pretty much it. If a nonsensical sentence such as "the formerly incarcerated sentient croissant quietly resents the aggressively mediocre shrine maiden" comes up on the screen, you'll know it worked.

# What did I learn from this?

First of all, I learned how to implement a context-free grammar in Python using only standard data structures and no external libraries, as well as how to use recursion in a non-trivial way. I also learned why Lisp in all of its dialects is popular for symbolic programming; Python requires a good bit of effort for this kind of recursion. I'd like to implement this again in Racket, which is built for formal grammars. While I had to chew on nested arrays in Python, Lisp IS nested arrays. 

# What future additions could I add?
In the short term, new grammars and a wider lexicon, possibly allowing for user-created CFGs too (if an LHS isn't context-free, it might bug out, so I could put guardrails in place). 
In the long term:
1. Racket implementation (this should be the first thing; adding more functionality in Python's a pain)
2. GPSG-style feature passing and agreement rules
3. Possibly moving from context-free grammar to a mildly context-sensitive grammar for multilingual capabilities. If I need nonsensical sentences in Bambara or Swiss German. Maybe. 
4. Sentence representations in first-order logic (for fun!)
