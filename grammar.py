grammar1 = {
    "S": ["NP", "VP"],
    "NP": ["Det", "N"],
    "VP": ["V_intr"]
}
grammar2 = {
    "S": ["NP", "VP"],
    "NP": ["Det", "Adj", "N"],
    "VP": ["V_trans", "NP"]
}
grammar3 = {
    "S": ["NP", "VP"],
    "NP": ["Det", "Adv", "Adj", "N"],
    "VP": ["V_trans", "NP", "Adv"]
}
grammar4 = {
    "S": ["NP", "VP"],
    "VP": ["V_intr", "PP"],
    "NP": ["Det", "Adj", "N"],
    "PP": ["P", "NP"]
}
grammar5 = {
    "S": ["NP'", "VP"],
    "NP'": ["Det", "Adj", "N", "C_n", "VP"],
    "VP": ["V_trans", "NP", "PP"],
    "NP": ["Det", "Adj", "N"],
    "PP": ["P", "NP"],
}
grammar6 = {
    "S": ["NP'", "VP"],
    "NP'": ["Det", "Adj", "N", "C_n", "VP"],
    "VP": ["V_trans", "NP"],
    "NP": ["Det", "Adj", "N"],
    "PP": ["P", "NP"],
}
grammar7 = {
    "S": ["NP", "VP"],
    "VP": ["VP'", "Conj", "NP", "VP'"], 
    # I know this is not how it works. I haven't slept last night and this is better than either S' or a RecursionError. I know it doesn't conform to how 
    # English CFGs are written, but it's STILL a valid CFG rule from a formal language theory perspective. A non-terminal on the LHS, a string on the RHS. SO SUCK ON IT! 
    "VP'": ["V_trans", "NP", "PP"],
    "PP": ["P", "NP"],
    "NP":["Det", "Adj", "N"]
}
POSTags = ["Det", "N", "V_trans", "V_intr", "Adj", "Adv", "P", "C_n", "C_v", "Conj"]
grammarList = [grammar1, grammar2, grammar3, grammar4, grammar5, grammar6, grammar7]