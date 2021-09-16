print("*** Fun with countdown ***")
lst1 = list(map(int, input("Enter List : ").split()))
size = len(lst1)
idxlst = [idx + 1 for idx , val in enumerate(lst1) if val == 1 ]
res = [lst1[i:j] for i,j in zip([0] + idxlst,idxlst + 
        ([size] if idxlst[0] == size else []))]