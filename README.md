verlihub-motd-plugin
====================

A plugin to administer motd ( Message of the Day) in verlihub

##email: nischal1251.11@bitmesra.ac.in
#######################################

####################uses###########################
commands: !notice add <notice to be added>
commands: !notice list
commands: !notice del <id of notice>
for ex to add notice run: !notice add Sample message of the day
this will add a notice of "Sample message of the day"

for ex to list all notice !notice list
this will show all notice with their ids and valid time

for deleting a particular notice
first get id of the notcie then run: !notice del 22
this will delte notice whose id is 22

####################requirements###################
make a table named notice with three column id , msg, and utcvalid
create table notice ( id integer(20) primary key auto_increment, msg varchar(1000), utcvalid integer(20))
change permission of motd file to rw and create a file motd_intro  with read permission which will contain the starting exts which will be always shown
chmod a+rwx motd
chmod a+rwx motd_intro
