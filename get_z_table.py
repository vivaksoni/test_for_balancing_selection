import sys
import argparse
import pandas as pd
import numpy as np

#Example usage:
#python3 get_z_table.py -inPath '/home/vivak/rr_mu_demography_DFE/results/rr_fixed_mu_fixed/sim1_gene1_rep1.ms' -outFile '/home/vivak/rr_mu_demography_DFE/results'


#Parse arguments
parser = argparse.ArgumentParser(description='Information about number of sliding windows and step size')
parser.add_argument('-inPath', dest = 'inPath', action='store', nargs = 1, type = str, help = 'path to input files')
parser.add_argument('-outFile', dest = 'outFile', action='store', nargs = 1, type = str, help = 'path to output file')

#read input parameters
args = parser.parse_args()
inPath = args.inPath[0]
outFile = args.outFile[0]

#function combines MAF categories to create 0-0.1; 0.1-0.2; 0.2-0.3; 0.3-0.4; 0.4-0.5
def loadNeutralData(inPath, targetPop):
    pStep = np.around(np.linspace(0,0.49,50),2)
    lst = []
    if(targetPop=="p1"):
        for i in ['sN','sS','rN_p1', 'rS_p1']:
            df=pd.read_csv(inPath+i+".txt", sep=' ',
                      names=pStep, index_col=None)
            
            lst.append(df.sum())

        cdf=pd.DataFrame(lst)
        cdf.index=['sN','sS','rN', 'rS']
        df=cdf.T
        
    else:
        for i in ['sN','sS','rN_p2', 'rS_p2']:
            df=pd.read_csv(inPath+i+".txt", sep=' ',
                      names=pStep, index_col=None)

            lst.append(df.sum())
    
        cdf=pd.DataFrame(lst)
        cdf.index=['sN','sS','rN', 'rS']
        df=cdf.T

    sN=df['sN'].sum()
    sS=df['sS'].sum()
    df=pd.DataFrame([df.iloc[0:10].sum(),df.iloc[10:20].sum(),
             df.iloc[20:30].sum(),df.iloc[30:40].sum(),
             df.iloc[40:50].sum()])

    def divIf(a,b,c,d):
        if((b>0) & (c>0) & (d>0)):
            return((a/b)/(c/d))
        else:
            return(0)
    df['Z'] = df.apply(lambda x: divIf(x['sN'],x['sS'],x['rN'],x['rS']), axis=1)
    df.index=['0-0.1', '0.1-0.2', '0.2-0.3', '0.3-0.4', '0.4-0.5']
    return df

#Run function for each population separately
df1 = loadNeutralData(inPath, "p1")
df1['population'] = "p1"
df2 = loadNeutralData(inPath, "p2")
df2['population'] = "p2"
df = pd.concat([df1,df2])

#Output file to csv
df.to_csv(outFile, sep='\t', header=True, index=False)

