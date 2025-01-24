from googleapiclient.discovery import build

api_key = "AIzaSyCl2p_b1WqoVkBUEOXvEk137m_vVAU05hA"

youtube = build("youtube","v3",developerKey=api_key)


nextpagetoken = None
videos = []

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
        part = "statistics",
        id = ",".join(vid_list)
    )

    vid_response = vid_request.execute()
   
    for item in vid_response['items']:
        vid_views = item["statistics"]["viewCount"] 
        
        

        vid_id = item['id']
        vid_url = f'https://youtu.be/{vid_id}'

        videos.append(
            {
                'views':int(vid_views),
                'url':vid_url
            }
        )

    nextpagetoken = Pl_response.get('nextpagetoken')
    if not nextpagetoken:
        break


videos.sort(key=lambda vid:vid['views'],reverse=True)



print(f'The most popular video of the playlist is {vid_url} with {vid_views} Views')


        










