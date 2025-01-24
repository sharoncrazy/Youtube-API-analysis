import re
from googleapiclient.discovery import build
from datetime import timedelta

api_key = "AIzaSyCl2p_b1WqoVkBUEOXvEk137m_vVAU05hA"

youtube = build("youtube","v3",developerKey=api_key)

minutes_pattern = re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')
hours_pattern = re.compile(r'(\d+)H')

nextpagetoken = None
total_seconds = 0 

while True:
    Pl_req = youtube.playlistItems().list(
        part = "contentDetails",
        playlistId = "PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS"	,
        maxResults = 50,
        pageToken = nextpagetoken
    )
    vid_list = []
    Pl_response = Pl_req.execute()
    for item in Pl_response['items']:
        vid_list.append(item['contentDetails']['videoId'])

    vid_request = youtube.videos().list(
        part = "contentDetails",
        id = ",".join(vid_list)
    )

    vid_response = vid_request.execute()

    


    
    for item in vid_response['items']:
        duration = item['contentDetails']['duration']

        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0 
        minutes = int(minutes.group(1)) if minutes else 0 
        seconds = int(seconds.group(1)) if seconds else 0 

        video_seconds = timedelta(
            hours = hours,
            minutes=minutes,
            seconds=seconds
        ).total_seconds()


        total_seconds += video_seconds
        

    nextpagetoken = Pl_response.get('nextpagetoken')
    if not nextpagetoken:
        break

Total_length = total_seconds/60
print(f'{Total_length} Minutes')
        










