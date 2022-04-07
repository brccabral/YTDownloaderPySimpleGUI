import PySimpleGUI as sg

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
download_tab_layout = [[]]

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
