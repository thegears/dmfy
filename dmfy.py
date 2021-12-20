import youtube_dl,optparse;

parser = optparse.OptionParser();
parser.add_option("-l","--link",dest = "link",help = "Write the video's link");
(options,args) = parser.parse_args();
if not options.link:
	video_url = input("Write video's link : ");
	while len(video_url) < 1:
		video_url = input("Write video's link : ");
else:
	video_url = options.link;

video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False);

file_name = video_info["title"]+".mp3";

with youtube_dl.YoutubeDL({'format':'bestaudio/best','keepVideo':False,"outtmpl":file_name}) as ydl:
	ydl.download([video_info["webpage_url"]]);
