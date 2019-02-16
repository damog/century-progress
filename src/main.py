from datetime import datetime, date, time

def elapsed(now = datetime.now()):
    # TODO: UTC lol

    # 0%
    start = datetime(2001, 1, 1, 0, 0, 0)

    # 100%
    end = datetime(2100, 12, 31, 23, 59, 59)

    full = end - start

    # now = datetime(2020, 1, 1, 0, 0, 0)

    return ( (now - start).total_seconds() / full.total_seconds() ) * 100

def bar(elapsed):
    on = ( 15 * elapsed ) / 100
    off = 15 - on
    bar_on = u'\u2593' * int(on)
    bar_off = u'\u2591' * int(off)
    return '[' + bar_on + bar_off + ']'

elapsed = elapsed()

print bar(elapsed) + ' ' + "%.4f" % elapsed + '%'

#print "%d %.4f " % ( how_many_chars(elapsed), elapsed )


