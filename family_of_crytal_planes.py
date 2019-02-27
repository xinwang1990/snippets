import itertools
import pandas as pd

df = pd.DataFrame(list(itertools.permutations([1,1,0],3))) # CHANGE THE MILLER INDEX YOU WANT
df = pd.concat([df, df.mul([-1, 1, 1]), df.mul([1, -1, 1]), df.mul([1, 1, -1]), df.mul([-1, -1, 1]), df.mul([-1, 1, -1]),df.mul([1, -1, -1]),df.mul([-1, -1, -1])], ignore_index=True)
df = df.drop_duplicates()
df = df.reset_index(drop=True)

print(df.to_string(index=False, header=False))

# THIS IS ONLY VALID FOR CUBIC CRYSTALS
