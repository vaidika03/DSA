#1. N meetings in one room
def maxMeetings(start, end, n):
    meetings = list(zip(start, end))
    meetings.sort(key=lambda x: x[1])
    last_end_time = -1
    count = 0    
    for meeting in meetings:
        if meeting[0] > last_end_time:
            count += 1
            last_end_time = meeting[1]    
    return count

start = [1, 3, 0, 5, 8, 5]
end =  [2, 4, 6, 7, 9, 9]
print("1. n meetings in one room:",maxMeetings(start, end, len(start)))
