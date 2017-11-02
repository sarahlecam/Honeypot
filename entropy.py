import sys
import numpy as np
import sklearn.cluster
import distance

roots=[]
roots_dict = {'asLESHA': 'AsLESHA, aSLEsHA, asLESHA, asLESHa', 'poOp': 'pZer, piKW, poOp, poop', 'sexy': '$exy, Sexy, XeAf, rELy, sdXm, sexy, vwl1', 'gDMB': 'VRe6, gDMB', '2cszi72': '2cszi72', '184211560': '184211560', 'Rock': '9FgO, N7au, ROCk, Rock, rock', '379075293': '379075293', '1SkZBn4VT': '1SkZBn4VT'}
for k, v in roots_dict.items():
    roots.append(k)

#entropy calculation
entropy=np.ones(len(roots))
for ind, sweetword in enumerate(roots):
    for char in sweetword:
        if char.isalpha():
            entropy[ind] = entropy[ind]*26
            # entropy[ind] += (1/26) * np.log(1/26)
        elif char.isdigit():
            entropy[ind] = entropy[ind]*10
            # entropy[ind] += (1/10) * np.log(1/10)
        elif set('[~!@#$%^&*()_+":;\]+$').intersection(char):
            entropy[ind] = entropy[ind]*20
            # entropy[ind] += (1/20) * np.log(1/20)
    # entropy[ind] = -1*entropy[ind]

    print(roots[ind], entropy[ind])
