grammar1 = {
    "S": ["NP", "VP"],
    "NP": ["Det", "N"],
    "VP": ["V_intr"]
}
grammar2 = {
    "S": ["S_finite","C","S_finite"],
    "S_finite": ["NP", "VP"],
    "NP":["DP", "N"],
    "VP":["V_trans", "NP"],
    "DP":["Det","Adj"],

}
grammar3 = {
    "S": ["NP", "VP"],
    "S_finite":["NP, VP_finite"],
    "VP":["V", "NP", "CP"],
    "CP":["Conj_S", "S_finite"],
    "VP_finite":["V", "NP"]

}
# I deleted all of the grammars to make new ones that are more elegant and fit English CFG descriptions better. 

POSTags = ["Det", "N", "V_trans", "V_intr", "Adj", "Adv", "P", "C_n", "C_v", "Conj"]
grammarList = [grammar1, grammar2, grammar3]