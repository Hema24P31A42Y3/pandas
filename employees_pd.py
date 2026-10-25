import pandas as pd
employees = [ 
    ['rk', 102, 15000],
    ['rama', 103, 20000],
    ['krishna', 104, 25000],
    ['arjun', 105, 18000],
    ['sita', 106, 22000],
    ['laxman', 107, 21000],
    ['radha', 108, 23000],
    ['mohan', 109, 19500],
    ['geeta', 110, 24000],
    ['vinay', 111, 26000],
    ["naveen", 112, 56000],
    ["rakesh", 113, 67000],
    ["jeevitha", 114, 88000]
]
employees
df1=pd.DataFrame(employees,columns=['name','id','salary'])
df1
