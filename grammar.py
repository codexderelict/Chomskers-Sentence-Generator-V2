grammar1 = {
    "S": ["NP", "VP"],
    "NP": ["Det", "N"],
    "VP": ["V"]
}
grammar2 = {
    "S": ["NP", "VP"],
    "NP": ["Det", "Adj", "N"],
    "VP": ["V", "NP"]
}
grammar3 = {
    "S": ["NP", "VP"],
    "NP": ["Det", "Adv", "Adj", "N"],
    "VP": ["V", "NP", "Adv"]
}
grammar4 = {
    "S": ["NP", "VP"],
    "VP": ["V", "PP"],
    "NP": ["Det", "Adj", "N"],
    "PP": ["P", "NP"]
}
POSTags = ["Det", "N", "V", "Adj", "Adv", "P"]
grammarList = [grammar1, grammar2, grammar3, grammar4]