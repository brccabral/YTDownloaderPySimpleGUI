import PySimpleGUI as sg

info_tab_layout = [[]]
download_tab_layout = [[]]

layout = [
    [
        sg.TabGroup(
            [
                [
                    sg.Tab("Info", info_tab_layout),
                    sg.Tab("Download", download_tab_layout),
                ]
            ]
        )
    ]
]

window = sg.Window("YT Downloader", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
