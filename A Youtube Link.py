# Created June 29, 2021. Creates a timestamped youtube link.
# This file does basically the same thing as lines 36-39 in 
# the format_json_file.py file in the LivestreamDirectory.

while True:
    link = input("What's the link:  ")
    time = input("What's the time? ")

    time = time.split(':')

    realtime = 0
    position = 0

    for i in time:
        if len(time) == 3:
            if position == 0:
                num = int(i) * 3600
                realtime += num
            if position == 1:
                num = int(i)*60
                realtime += num
            if position == 2:
                realtime += int(i)

        if len(time) == 2:
            if position == 0:
                num = int(i)*60
                realtime += num
            else:
                realtime += int(i)
        position += 1
                
    link += ('?t='+str(realtime))
    print(f'\nThis is the link:\n{link}\n')
    


    
