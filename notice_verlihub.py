##author hari_om
##email: nischal1251.11@bitmesra.ac.in
#######################################

####################uses###########################
#commands: !notice add <notice to be added>
#commands: !notice list
#commands: !notice del <id of notice>
#for ex to add notice run: !notice add Sample message of the day
#this will add a notice of "Sample message of the day"

#for ex to list all notice !notice list
#this will show all notice with their ids and valid time

#for deleting a particular notice
#first get id of the notcie then run: !notice del 22
#this will delte notice whose id is 22

####################requirements###################
# make a table named notice with three column id , msg, and utcvalid
#create table notice ( id integer(20) primary key auto_increment, msg varchar(1000), utcvalid integer(20))
#change permission of motd file to rw and create a file motd_intro  with read permission which will contain the starting texts which will be always shown
#chmod a+rwx motd
#chmod a+rwx motd_intro










import vh
import MySQLdb as mdb
import sys
import string


motd_intro_path='/etc/verlihub/motd_intro'
motd_path='/etc/verlihub/motd'

def OnOperatorCommand (nick, data):
	#vh.pm(data,nick)
	#print data
	i= data.find(' ')
	#print type(data)
	#print data[1:i]
	if data[1:i] == "notice":
		stri=data[i+1:]
		cmd=stri.split(' ')[0]
		if cmd == "add":
			i=stri.find(' ')
			val=stri[i+1:]
			con = mdb.connect('localhost', 'root', 'happyinbit', 'verlihub')
			with con:
				cur=con.cursor()
				print 'inserting val'
				cur.execute("insert into notice values(0,\'"+val+"\',123456)")
				content=''
				with open(motd_intro_path, 'r') as content_file:
					content = content_file.read()
				content_file=open(motd_path,'w')
				content_file.write(content+'\n')
				content_file.close()

				cur.execute("select msg from notice")
				rows=cur.fetchall()
				motd_file=open(motd_path,'a')
				for row in rows:
					#print "writing"
					motd_file.write("##########\n")
					motd_file.write(row[0]+'\n')
				motd_file.close()
			return 1
		if cmd== 'list':
			con = mdb.connect('localhost', 'root', 'happyinbit', 'verlihub')
			with con:
				cur=con.cursor()
				cur.execute("select id, utcvalid, msg from notice")
				rows=cur.fetchall()
				sendtxt='\nid\tutc valid\tmsg\n#############################################################\n\n'
				for row in rows:
					sendtxt=sendtxt+str(row[0])+'\t'+str(row[1])+'\t'+str(row[2])+'\n'
				print sendtxt
				vh.pm(sendtxt, nick)
			return 1
		if cmd =='del':
			i=stri.find(' ')
			val=stri[i+1:]
			con = mdb.connect('localhost', 'root', 'happyinbit', 'verlihub')
			with con:
				cur=con.cursor()
				cur.execute("delete from notice where id ="+val)
				content=''
				with open(motd_intro_path, 'r') as content_file:
					content = content_file.read()
				content_file=open(motd_path,'w')
				content_file.write(content+'\n')
				content_file.close()

				cur.execute("select msg from notice")
				rows=cur.fetchall()
				motd_file=open(motd_path,'a')
				for row in rows:
					#print "writing"
					motd_file.write("##########\n")
					motd_file.write(row[0]+'\n')
				motd_file.close()
			return 1

