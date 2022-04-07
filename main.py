import PySimpleGUI as sg
from pytube import YouTube, Stream


def update_on_progress(stream: Stream, chunk, bytes_remaining: int):
    progress_amount = 100 - round(100 * bytes_remaining / stream.filesize)
    window["-PROGRESS-"].update(progress_amount)


def update_on_complete(stream: Stream, file_path):
    window["-PROGRESS-"].update(0)


sg.theme("Darkred1")

start_layout = [[sg.Input(key="-INPUT-"), sg.Button("Submit", key="-LINK-")]]

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
    [
        sg.Progress(
            100,
            size=(20, 20),
            expand_x=True,
            key="-PROGRESS-",
            bar_color=("#FF5555", "#F8F8F8"),
        )
    ],
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

window = sg.Window("YT Downloader", start_layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "-LINK-":
        video_link = values["-INPUT-"]
        window.close()

        video_object = YouTube(
            video_link,
            on_progress_callback=update_on_progress,
            on_complete_callback=update_on_complete,
        )
        window = sg.Window("YT Downloader", layout, finalize=True)

        # video info
        window["-TITLE-"].update(video_object.title)
        window["-LENGTH-"].update(f"{round(video_object.length /60, 2)} minutes")
        window["-VIEWS-"].update(video_object.views)
        window["-AUTHOR-"].update(video_object.author)
        window["-DESCRIPTION-"].update(video_object.description)

        # download
        window["-BESTSIZE-"].update(
            f"{round(video_object.streams.get_highest_resolution().filesize / (1024*1024), 1)} MB"
        )
        window["-BESTRES-"].update(
            video_object.streams.get_highest_resolution().resolution
        )
        window["-WORSTSIZE-"].update(
            f"{round(video_object.streams.get_lowest_resolution().filesize / (1024*1024), 1)} MB"
        )
        window["-WORSTRES-"].update(
            video_object.streams.get_lowest_resolution().resolution
        )
        window["-AUDIOSIZE-"].update(
            f"{round(video_object.streams.get_audio_only().filesize / (1024*1024), 1)} MB"
        )

    # download() by default downloads in current folder
    if event == "-BEST-":
        video_object.streams.get_highest_resolution().download()
    if event == "-WORST-":
        video_object.streams.get_lowest_resolution().download()
    if event == "-AUDIO-":
        video_object.streams.get_audio_only().download()

window.close()
