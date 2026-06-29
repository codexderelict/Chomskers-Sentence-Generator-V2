grammar1 = {
    "S": ["NP", "VP"],
    "NP": ["Det", "N"],
    "VP": ["V_intr"]
}

# I deleted all of the grammars to make new ones that are more elegant and fit English CFG descriptions better. 


# I fixed it. S' is now a proper non-terminal and it fits an English CFG. I have no clue why I didn't do this earlier. Probably because of sleep deprivation.
# I need a Monster... 
POSTags = ["Det", "N", "V_trans", "V_intr", "Adj", "Adv", "P", "C_n", "C_v", "Conj"]
grammarList = [grammar1, grammar2, grammar3, grammar4, grammar5, grammar6, grammar7]