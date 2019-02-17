21st Century Progress Bar
=========================

Ok, so, inspired by the amazing [Year Progress twitter account](https://twitter.com/year_progress) built by [Filip Hráček](https://filiph.net/), I started to think about having a progress bar for the whole twenty-first century, specially because who knows if people are actually gonna make it until then or if Twitter would still exist or if the Internet as we know it would still exist.

Fun little hack anyway.

The other inspiration I took to build this is to be able to run it on a complete different infrastructure apart from any of my home server installations or anything that I'd have to pay a lot for. I figured the current _serverless_ paradigm would be interesting for me to get familiar with, specially with [AWS Lambda](https://aws.amazon.com/lambda/). No, this is not an ad.

So AWS Lambda has some free tier limits that, if I kept under control in terms of bandwidth and resources, I could pretty much maintain free for life (or until they change their terms) or on an stupidly inexpensive cost. At the end, it was very easy and fun to set it up as I learned a few things about _modern_ AWS (I had not used AWS since pretty much 2009) and also about Python 2.x.

If everything goes well (you know, if mankind doesn't exterminate itself), the account will continue to tweet **FOREVER**. Well no, not really forever, but until December 31st, 2100 at 23:59:59. I'd be 116 years old at the time. I may have plans that day.

Explanation
-----------
The [@century_bar](http://twitter.com/century_bar) account currently (as of the time of writing, Feb 17 2019) calculates the elapsed time to be at 18.129% or so. This is because the definition of the century starts from 2001, not 2000, and finishes on 2100, not 2099. That definition is taken from [here](https://en.wikipedia.org/wiki/21st_century).

I've set up Amazon CloudWatch to run the function every 526 minutes, which is roughly when every 3rd decimal will see a change. This is roughly every 8.7 hours. I will change it to run every 5260 minutes later (roughly every 3.6 days) to allow for tweet on change of every 2nd decimal, but I'll do that after a few days.

Thanks!
-------
That's it. It was fun to learn a bunch of new things with this. Ping me on Twitter if you'd like to learn more.

David Moreno

https://damog.net

[@mrdamog](http://twitter.com/mrdamog)

