import moviepy.editor

#location of the video file
vid = 'path to the video file'

video = moviepy.editor.VideoFileClip(vid)

audio = video.audio

#saving the audio file with same file name as video
audio_file=vid.replace(".mp4",".wav")
audio.write_audiofile(audio_file)

print("convertion completed  done\n\n")
