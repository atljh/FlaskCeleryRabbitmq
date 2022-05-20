
from celery import Celery
import moviepy.editor as moviepy


app = Celery('celery_app', broker='pyamqp://guest@localhost//')


def convert_video(filename):
    clip = moviepy.VideoFileClip(f"/dir/{filename}.mp4")
    clip.audio.write_audiofile(f"/dir/{filename}.mp3")




@app.task
def task_convert(filename):
    convert_video(filename)
    return True
