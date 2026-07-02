from CFGengine import CFG 
from grammar import grammarList
import random
def main():
    cfg = CFG(random.choice(grammarList))
    cfg.pickWords()
    cfg.detAgree()
    string = cfg.returnString()
    print(string)
if __name__ == "__main__":
    main()
