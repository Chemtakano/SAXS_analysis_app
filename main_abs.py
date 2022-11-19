import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import file_import as fi
import matplotlib.pyplot as plt
import os

    

#data
col_1=[
    [sg.Text('イオンチャンバーのテキストファイル')],
    [sg.FileBrowse('Browse', file_types=(('イオンチャンバーのtxtファイル', '*.txt'),)), sg.InputText(key='ICpath')],
    [sg.Text('水のchiファイル')],
    [sg.FileBrowse('Browse', file_types=(('水のchiファイル', '*.chi'),)), sg.InputText(key='waterpath')],
    [sg.Text('空キャピラリーのchiファイル')],
    [sg.FileBrowse('Browse', file_types=(('空キャピラリーのchiファイル', '*.chi'),)), sg.InputText(key='capipath')],
    [sg.Button('補正定数を算出する。', key='btn_F')],
    [sg.Radio('4 m', group_id='camera_length', key='-4m-', default=True), sg.Radio('1 m', group_id='camera_length', key='-1m-', default=False)]
]

col_2=[
    [sg.Canvas(size=(300, 300), key='-CANVAS_data-')],
]

col_3=[
    [sg.Text('グラフの保存')],
    [sg.Text('保存先フォルダー')],
    [sg.FolderBrowse('Browse'), sg.InputText(key='savepath')],
    [sg.Text('ファイル名'), sg.InputText(key='savename'), sg.Button('グラフを保存', key='btn_save')]
]

layout=[
    [col_1],
    [sg.Column(col_2), sg.Column(col_3)]
]


#sg.theme('Topanga')  
window=sg.Window(
    'Correction constant calculator version 1.0.1',
    layout,
    finalize=True,
    auto_size_text=True,
    location=(0,0),
    resizable=True
    )

#canvas

##plot code

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


fig = plt.figure(figsize=(3, 3))
ax = fig.add_subplot(111)

def setfig():
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('$q$')
    ax.set_ylabel('I($q$)')
    ax.set_xlim(10**(-2), 10*1)
    ax.grid(lw=1, c='gray', ls='dotted')
    fig.tight_layout()

def plot():
    
    ICfile=fi.read_IC(value['ICpath'])
    w_filename=os.path.splitext(os.path.basename(value['waterpath']))[0]
    c_filename=os.path.splitext(os.path.basename(value['capipath']))[0]

    IC2_w=ICfile.at[w_filename, 'IC2']
    IC2_c=ICfile.at[c_filename, 'IC2']

    if value['-4m-']==True:
        qmin, qmax=1, 1.5
    else:
        qmin, qmax=1, 3

    dfw=fi.read_chi(value['waterpath'])
    dfw['I']=dfw['I']/IC2_w
    dfw_q=dfw.query('@qmin<q<@qmax')
    dfc=fi.read_chi(value['capipath'])
    dfc['I']=dfc['I']/IC2_c
    dfc_q=dfc.query('@qmin<q<@qmax')



    ax.scatter(dfw['q'], dfw['I'], c='mistyrose', s=1)
    ax.scatter(dfc['q'], dfc['I'], c='lightcyan', s=1)
    ax.scatter(dfw['q'], dfw['I']-dfc['I'], c='lightgreen', s=1, alpha=0.5)
    ax.scatter(dfw_q['q'], dfw_q['I'], c='r', s=1, label='water')
    ax.scatter(dfc_q['q'], dfc_q['I'], c='b', s=1, label='capi')
    ax.scatter(dfw_q['q'], dfw_q['I']-dfc_q['I'], c='g', s=1)

    F=0.01632/(sum(dfw_q['I']-dfc_q['I'])/len(dfw_q['q']))

    ax.set_title('F={}'.format(F))
    ax.legend()
    setfig()
    fig_agg.draw()

setfig()

fig_agg = draw_figure(window['-CANVAS_data-'].TKCanvas, fig)


while True:
    event, value = window.read()
    if event == None:
        break
    if event=='btn_F':
        plot()
    if event=='btn_save':
        fig.savefig(value['savepath']+'/'+value['savename'])
        
        
window.close()

"""
created by Shin Takano
version 1.0.1 19/11/2022

"""