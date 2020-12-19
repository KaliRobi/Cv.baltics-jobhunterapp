# Cv.baltics-jobtracker

Browsing over dozens of pages while looking for an oportunty in a certain area can be time consuming.

Much convenient to gently extract the needed data from the sites and query it in an sql database latter.
With the title, the location and the link to the advertisment there is enaought info. 

The script is working, additional featueres are planned:
1 database cleaner: no need to keep the same advertisment as many times as the script runs.
DELETE FROM jobtracker_main  where rowid not in (select rowid from jobtracker_main GROUP by path_url_lv
will run each time at the end of the script

2 additional sites: workinlatvia + duunitori.fi will be also involved. 

3 GUI, shows the title, the additional information the time it was posted and a button which opens the url.
