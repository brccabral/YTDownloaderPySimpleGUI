import PySimpleGUI as sg


sg.theme("Darkred1")
info_tab_layout = [
    [sg.Text("Title:", key="-TitleLabel-"), sg.Text("", key="-TITLE-")],
    [sg.Text("Length:", key="-LengthLabel-"), sg.Text("", key="-LENGTH-")],
    [sg.Text("Views:", key="-ViewsLabel-"), sg.Text("", key="-VIEWS-")],
    [sg.Text("Author:", key="-AuthorLabel-"), sg.Text("", key="-AUTHOR-")],
    [
        sg.Text("Description:", key="-DescriptionLabel-"),
        sg.Multiline(
            key="-DESCRIPTION-", no_scrollbar=True, size=(40, 20), disabled=True
        ),
    ],
]
download_tab_layout = [
    [
        sg.Frame(
            "Best Quality",
            layout=[
                [
                    sg.Button("Download", key="-BEST-"),
                    sg.Text("", key="-BESTRES-"),
                    sg.Text("", key="-BESTSIZE-"),
                ]
            ],
        )
    ],
    [
        sg.Frame(
            "Worst Quality",
            layout=[
                [
                    sg.Button("Download", key="-WORST-"),
                    sg.Text("", key="-WORSTRES-"),
                    sg.Text("", key="-WORSTSIZE-"),
                ]
            ],
        )
    ],
    [
        sg.Frame(
            "Audio",
            layout=[
                [sg.Button("Download", key="-AUDIO-"), sg.Text("", key="-AUDIOSIZE-")]
            ],
        )
    ],
    [sg.VPush()],
    [sg.Progress(100, size=(20, 20), expand_x=True, key="-PROGRESS-")],
]

layout = [
    [
        sg.TabGroup(
            [
                [
                    sg.Tab("Info", layout=info_tab_layout),
                    sg.Tab("Download", layout=download_tab_layout),
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
