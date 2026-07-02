grammar1 = {
    "S": ["NP", "VP"],
    "NP": ["Det", "N"],
    "VP": ["V_intr"]
}
grammar2 = {
    "S": ["S_finite","Conj_c","S_finite"],
    "S_finite": ["NP", "VP"],
    "NP":["DP", "N"],
    "VP":["V_trans", "NP"],
    "DP":["Det","Adj"],

}
grammar3 = {
    "S": ["NP_name", "VP"],
    "S_finite":["NP", "VP_finite"],
    "VP":["V_trans", "NP", "CP"],
    "NP":["DP", "N"],
    "NP_name":["N_name"],
    "DP":["Det", "AdjP"],
    "AdjP":["Adv","Adj"],
    "CP":["Conj_S", "S_finite"],
    "VP_finite":["V_trans", "NP"]

}


# I deleted all of the grammars to make new ones that are more elegant and fit English CFG descriptions better. 

POSTags = ["Det", "N", "V_trans", "V_intr", "Adj", "Adv", "P", "C_n", "C_v", "Conj_c","Conj_p"]
grammarList = [grammar1, grammar2, grammar3]