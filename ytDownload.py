from pytube import YouTube
import inquirer
import time
import os
try:
    folder_name = "Downloads"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    open("links.txt", 'a+')

    if(os.stat("links.txt").st_size == 0):
        print("Please add links to links.txt file")
        input("Press Enter to continue...")
        exit()
    if(len(os.listdir("Downloads"))):
        print("WARNING: Downloads folder is not empty. Files will be overwritten")
        questions = [
        inquirer.List(
            "size",
            message="Do you wish to continue?",
            choices=["Yes", "No"],
            ),
        ]
        answers = inquirer.prompt(questions)
        if answers['size']=='No' or answers is None:
            exit()

    file_format = [
    inquirer.List('format',
                    message="Select the format",
                    choices=['Video', 'Audio'],
                ),
    ]
    format_answer = inquirer.prompt(file_format)

    if format_answer is None:
        exit();

    

    print("reading links...")

    for x in open("links.txt","r"):
        #link=input(x)
        yt=YouTube(x)
        print(yt.title,"| length:",yt.length,"seconds")

        if(format_answer['format']=='Video'):
            streams = yt.streams.filter(type="video")
            questions = [
            inquirer.List('stream',
                            message="Select the stream you want to download",
                            choices=[f"{s.itag}\t->({s.fps}FPS,{s.resolution},{s.mime_type.split('/')[1]})" for s in streams],
                        ),
            ]
            answers = inquirer.prompt(questions)
            if answers is None:
                exit()

            stream = streams.get_by_itag(int(answers['stream'].split('\t')[0]))

            stream.download("Downloads", filename_prefix=time.strftime("%Y_%m_%d_%H%M%S_"), filename=stream.default_filename.replace(" ", "_").replace("(", "").replace(")", ""))

            print("\t -> successfully downloaded")

        if (format_answer['format']=='Audio'):
            streams = yt.streams.filter(type="audio")
            questions = [
            inquirer.List('stream',
                            message="What size do you need?",
                            choices=[f"{s.itag}\t->({s.abr},{s.mime_type.split('/')[1]})" for s in streams],
                        ),
            ]
            answers = inquirer.prompt(questions)
            if answers is None:
                exit()

            stream = streams.get_by_itag(int(answers['stream'].split('\t')[0]))

            stream.download("Downloads", filename_prefix=time.strftime("%Y_%m_%d_%H%M%S_"), filename=stream.default_filename.replace(" ", "_").replace("(", "").replace(")", ""))
            print("\t -> successfully downloaded")
            input("Press Enter to continue...")
except Exception as e:
    print("Download failed!")