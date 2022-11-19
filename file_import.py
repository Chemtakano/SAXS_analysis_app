import pandas as pd

def read_chi(file):
    df=pd.read_table(file, skiprows=4, header=None, sep='\s+', names=('q', 'I', 'noname'), usecols=('q', 'I'))
    df=df.dropna(how='any')
    return df

def read_IC(file):
    df=pd.read_table(file, header=None, usecols=[0,1,5,10], names=['filename', 'D&T', 'Ex_time', 'IC2'], index_col='filename')
    return df

def read_Log(file):
    df=pd.read_excel(file, skiprows=1, index_col='sample_name')
    df=df.fillna('skip')
    return df

    
def discription():
    print(
        
        """
        This code enables us to import data exported BL40B2 and logsheet.
        [read_chi]
        This code gives the DataFrame of SAXS result. The first col is q, the second one is I(q). 
        [read_IC]
        This code gives the DataFrame displays the IC data. 
        [read_Log]
        This code gives the DataFrame of logsheet that you prepared.
        """
    )

def show_code():
    print(
        """
import pandas as pd

def read_chi(file):
    df=pd.read_table(file, skiprows=[0,1,2,3], header=None, sep='\s+', names=('q', 'I', 'noname'), usecols=('q', 'I'))
    return df

def read_IC(file):
    df=pd.read_table(file, header=None, usecols=[0,1,5,10], names=['filename', 'D&T', 'Ex_time', 'IC2'], index_col='filename')
    return df

def read_Log(file):
    df=pd.read_excel(file)
    return df
        """
    )

