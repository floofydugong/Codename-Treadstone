def format_duration(seconds):
    if seconds == 0:
        return("now")

    and_answer = ''

    times = [("year", 365 * 24 * 60 * 60),
             ("day", 24 * 60 * 60),
             ("hour", 60 * 60),
             ("minute", 60),
             ("second", 1)]

    final_answer = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            final_answer.append(str(qty) + " " + name)

        seconds = seconds % secs

    if len(final_answer) > 1:
        and_answer = ''
        and_answer = ' and ' + final_answer.pop(-1)

    return (', '.join(final_answer) + and_answer)