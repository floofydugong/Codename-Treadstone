def format_duration(seconds):
    if seconds == 0:
        return("now")

    final_answer = []
    and_answer = ''
    #Solve for Years
    try:
        years = seconds//31536000
        if years > 0:
            if years == 1:
                final_answer.append('1 year')
            else:
                final_answer.append(str(years) + ' years')
            seconds = seconds-(years*31536000)
    except:
        pass

    #Days
    try:
        days = seconds//86400
        if days > 0:
            if days == 1:
                final_answer.append('1 day')
            else:
                final_answer.append(str(days) + ' days')
        seconds = seconds-(days*86400)
    except:
        pass

    #Hours
    try:
        hours = seconds//3600
        if hours > 0:
            if hours == 1:
                final_answer.append('1 hour')
            else:
                final_answer.append(str(hours) + ' hours')
        seconds = seconds-(hours*3600)
    except:
        pass

    #Minutes
    try:
        minutes = seconds//60
        if minutes > 0:
            if minutes == 1:
                final_answer.append('1 minute')
            else:
                final_answer.append(str(minutes) + ' minutes')
        seconds = seconds-(minutes*60)
    except:
        pass

    #Seconds
    if seconds > 0:
        if seconds==1:
            final_answer.append('1 second')
        else:
            final_answer.append(str(seconds) + ' seconds')

    if len(final_answer) > 1:
        and_answer = ''
        and_answer = ' and ' + final_answer.pop(-1)
    best_answer = ', '.join(final_answer)
    return (', '.join(final_answer) + and_answer)

format_duration(100)