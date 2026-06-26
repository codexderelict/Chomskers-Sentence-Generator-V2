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
POSTags = ["Det", "N", "V", "Adj", "Adv"]
grammarList = [grammar1, grammar2]