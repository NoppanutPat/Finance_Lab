import pandas as pd 
import numpy as np

ans_a = 0
ans_b = 0

def r_value(a,b):
    df_a = pd.read_csv(a)
    df_b = pd.read_csv(b)
    a_close = np.array(df_a['Close'])
    b_close = np.array(df_b['Close'])
    
    if len(a_close) > len(b_close):
        num = len(a_close) - len(b_close)
        a_close = a_close[num:]
    
    if len(a_close) < len(b_close):
        num = len(b_close) - len(a_close)
        b_close = b_close[num:]
       
    aa = np.corrcoef(a_close,b_close)

    r = aa[0][1]
    r = str(r)
    r = r[0:5]
    r = float(r)

    return (r)
    
if __name__ == "__main__":

    main()