import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import t_module as tm


    

#data
col_1=[
    [sg.Text('chiファイルがあるフォルダー')],
    [sg.FolderBrowse('Browse'), sg.InputText(key='d_folderpath')],
    [sg.Text('ログシート(.xlsx)')],
    [sg.FileBrowse('Browse', file_types=(('Log Sheet', '*.xlsx'),)), sg.InputText(key='Logpath')],
    [sg.Text('イオンチャンバーのテキストファイル(.txt)')],
    [sg.FileBrowse('Browse', file_types=(('IC2file', '*.txt'),)), sg.InputText(key='IC2path')],
    [sg.Text('保存先のフォルダ')],
    [sg.FolderBrowse('Browse'), sg.InputText(key='s_folderpath')],
    [sg.Button('解析を実行。', key='btn_doit')],
    [sg.Radio('4 m', group_id='camera_length', key='-4m-', default=True), sg.Radio('1 m', group_id='camera_length', key='-1m-', default=False)],
]

col_2=[]

col_3=[]

layout=[
    [col_1],
    [sg.Column(col_2), sg.Column(col_3)]
]


#sg.theme('Topanga')  
window=sg.Window(
    'SAXS @BL40B2 Analysis App version 1.0.1',
    layout,
    finalize=True,
    auto_size_text=True,
    location=(0,0),
    resizable=True
    )


while True:
    event, value = window.read()
    if event == None:
        break
    if event=='btn_doit':
        if value['d_folderpath']=='':
            sg.popup('chiファイルが格納されているフォルダーが選択されていません！', title='エラー')
        if value['s_folderpath']=='':
            sg.popup('保存用フォルダーが選択されていません！', title='エラー')
        if value['Logpath']=='':
            sg.popup('LogSheetが選択されていません！', title='エラー')
        if value['IC2path']=='':
            sg.popup('イオンチャンバーのテキストファイルが選択されていません！', title='エラー')
        else:
            if value['-4m-']==True:
                qmin, qmax=0.025, 1.8
            else:
                qmin, qmax=0.5, 9
            tm.trans_cor(value['Logpath'], value['IC2path'], (qmin, qmax), value['d_folderpath'], value['s_folderpath'])

        
        
window.close()

"""
created by Shin Takano
version 1.0.1 19/11/2022

"""