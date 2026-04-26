"""example used as a sidecar to transform an .xls - doc: interchange y and x axis"""

import pandas as pd

file = input("File: ")

df = pd.read_excel(f"documents/{file}", header=None)
df.T.to_excel(f"documents/output_{file}", header=False, index=False)
