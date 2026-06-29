grammar1 = {
    "S": ["NP", "VP"],
    "NP": ["Det", "N"],
    "VP": ["V_intr"]
}

# I deleted all of the grammars to make new ones that are more elegant and fit English CFG descriptions better. 

POSTags = ["Det", "N", "V_trans", "V_intr", "Adj", "Adv", "P", "C_n", "C_v", "Conj"]
grammarList = [grammar1]