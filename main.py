import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import t_module as tm
import infomation as info

#menu bar

menubar_def=[
    ['about this app', ['how to use this app (ENG)', 'how to use this app (JPN)']],
    ['creator',['creator']]
]
    

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
    [sg.Button('解析を実行', key='btn_doit', button_color=('white', 'teal'))],
    [sg.Radio('4 m', group_id='camera_length', key='-4m-', default=True), sg.Radio('1 m', group_id='camera_length', key='-1m-', default=False)],
]


layout=[
    [sg.MenuBar(menubar_def)],
    [col_1]
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
                qmin, qmax=0.5, 8
            tm.trans_cor(value['Logpath'], value['IC2path'], (qmin, qmax), value['d_folderpath'], value['s_folderpath'])
            sg.popup('解析が終了しました。', title='成功')

    if event=='how to use this app (JPN)':
        sg.popup(info.HowTo4CAL('JPN'), title='アプリの使い方')
    if event=='how to use this app (ENG)':
        sg.popup(info.HowTo4CAL('ENG'), title='How to use')
    if event=='creator':
        sg.popup(info.creator(), title='creator')  
        
        
window.close()

"""
created by Shin Takano
version 1.0.1 19/11/2022

"""