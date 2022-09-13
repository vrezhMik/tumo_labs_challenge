def timing(total):
    days = int(total/86400)
    total -=days*86400
    hours = int(total/3600)
    total -=hours*3600
    mins = int(total/60)
    total -=mins*60
    sec = total
    return f'{days} days, {hours} hours, {mins} minutes, {sec} seconds'
    