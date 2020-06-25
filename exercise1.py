## Convert seconds to hour:min:sec and print
seconds_past_midnight = 100000. #63252

if seconds_past_midnight > 24*3600 :
    print('That is more than the number of seconds in 24 hours.  Please try again.')
else :  
    hour = int(seconds_past_midnight/3600)
    remain_h = seconds_past_midnight - hour*3600
    minutes = int(remain_h/60)
    seconds = remain_h - minutes*60
    print('At ', seconds_past_midnight, ' seconds past midnight the time is ', hour,':',minutes,':',seconds, sep='')