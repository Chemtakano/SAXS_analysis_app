import file_import as fi

#透過率補正
def trans_cor(LogSheet, ICdata, qr=(0.025, 1.8), Dpath='', Spath=''):
    Log_df=fi.read_Log(LogSheet)
    IC_df=fi.read_IC(ICdata)
    qr=qr
    
    for i in Log_df.index:
        datafile=Log_df.at[i, 'filename']
        solname=Log_df.at[i, 'solvent_name']
        IC2_sam=IC_df.at[datafile, 'IC2']
        cons=Log_df.at[i, 'correc_cons']

        if solname=='skip':
            df=fi.read_chi(Dpath+'/'+datafile+'.chi')
            df['I_t']=df['I']/IC2_sam
            if cons!=1:
                df['absI']=df['I_t']*cons
        else:
            solfile=Log_df.at[solname, 'filename']
            IC2_sol=IC_df.at[solfile, 'IC2']

            df=fi.read_chi(Dpath+'/'+datafile+'.chi')
            df['Isol']=fi.read_chi(solfile)['I']
            df['I_t']=df['I']/IC2_sam
            df['Isol_t']=df['Isol']/IC2_sol
            df['exI']=df['I_t']-df['Isol_t']
            if cons!=1:
                df['absI']=df['exI']*cons
    
        df=df.query('@qr[0]<q<@qr[1]')
        df.to_csv(Spath+'/'+i+'.csv', index=None)
