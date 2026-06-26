import grammar
from lexicon import lexicon 
import random 
vowels = ('a', 'e', 'i', 'o', 'u')
class CFG:
    def __init__(self, rules):
        self.rules = rules 
        self.POSTags = grammar.POSTags
        self.currentSymbols = self.flatten(self.expand(["S"]))
        self.lexicon = lexicon
    def expand(self, symbols):
        if self.validate(symbols):
            return symbols # Before it expands, it checks if all of them are POS tags. 
        newSymbols = [] # Lists can only be indexed by number, not by specific content. 
        for symbol in symbols:
            if isinstance(symbol, list): # Is the symbol a list?
                newSymbols.append(self.expand(symbol)) # Then expand the list. 
            elif symbol in self.rules: # Is the symbol an LHS?
                newSymbols.append(self.expand(self.rules[symbol])) # Then expand the RHS and repeat this procedure.
            else:
                newSymbols.append(symbol) # Current level can't be expanded. 
        return newSymbols # Return value so that list.append has something to append.
    def flatten(self, symbols):
        result = []
        for symbol in symbols:
            if isinstance(symbol, list):
                result.extend(self.flatten(symbol)) # Adds them one at a time, not as the entire thing all at once.
            else:
                result.append(symbol)
        return result
    def validate(self, symbols):
        for symbol in symbols:
            if isinstance(symbol, list):
                if not self.validate(symbol): # When it returns false, then the entire function returns false (the "not") part, and propagates it up.
                    return False 
            elif symbol not in self.POSTags:
                return False
        return True

    def pickWords(self):
        for index, symbol in enumerate(self.currentSymbols):
            self.currentSymbols[index] = random.choice(self.lexicon[symbol])
    def detAgree(self):
        for index, symbol in enumerate(self.currentSymbols):
            if symbol == "a" and index + 1 < len(self.currentSymbols):
                if self.currentSymbols[index+1].startswith(vowels):
                    self.currentSymbols[index] = "an"

    def display(self):
        print(" ".join(self.currentSymbols))    
