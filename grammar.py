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
POSTags = ["Det", "N", "V_trans", "V_intr", "Adj", "Adv", "P"]
grammarList = [grammar1, grammar2, grammar3, grammar4]