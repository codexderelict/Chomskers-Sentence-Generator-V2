from CFGengine import CFG 
from grammar import grammarList
import random
def main():
    cfg = CFG(random.choice(grammarList))
    cfg.pickWords()
    cfg.detAgree()
    cfg.display()
if __name__ == "__main__":
    main()
