

'''
*****************************************************************************
@filename   : world_distance_calculator.py
@author     : Ajay Prajapati
@teamLead   : Akash Kamble,Rajesh Dommaraju
@details    : It gives distance between two location of the world in kilometer..
@license    : SpanIdea Systems Pvt. Ltd. All rights reserved.
*****************************************************************************
'''


from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from tkinter import*
import time
import logging
import datetime

'''install these modules in your system run foloowing commands
--------------------------------------------------------------
	pip install tkinter
	pip install geopy
---------------------------------------------------------------
tkinter is Python GUI library and is used for front end design
logging module is used here to generate logs of search query.
 
datetime and time module are used to generate timestamps for naming the log files.
'''




def get_filename_datetime():
    # for getting file name of log file
    now = datetime.datetime.now()
    return "file-"+now.strftime("%Y-%m-%d %H:%M:%S")+".log"
name=get_filename_datetime()
#basic configuration for logging
logging.basicConfig(filename=name, level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%d/%m/%Y %I:%M:%S %p',filemode="w+")




def get_distance(source,destination):
	try:
		geolocator=Nominatim(user_agent="specify_your_app_name_here")
		locations=geolocator.geocode(source)
		locatione=geolocator.geocode(destination)

		s1=((locations.latitude,locations.longitude))
		s2=((locatione.latitude,locatione.longitude))


		miles_distance=geodesic(s1,s2).miles
		km_distance=format(1.6094*miles_distance,'.2f')
		print("your total distance in km is ",km_distance)
		logging.info(v.set("Straight line Distance is {0} km".format( km_distance)))
	
	
	except:
		logging.info(v.set("Please Enter your address properly"))

	
root=Tk()
#creating object of tkinter
root.geometry("400x400")
#defining geometry of window
root.title("Distance Calculator")
root.resizable(width=False, height=False)
#window resizing is false.

frame0=Frame(root,bg='light pink')
frame0.place(relheight=0.8,relwidth=0.89,relx=0.05,rely=0.05)
#window main frame 
label_title=Label(frame0,text="Welcome! Calculate Distance",font=('arial', 12, 'bold'),fg='blue')
label_title.place(relheight=0.1,relwidth=1)


#Entry frames
entry1=Entry(frame0)
entry1.place(relheight=0.1,relwidth=0.3,height=10,width=12,relx=0.15,rely=0.2)

label.place(relheight=0.3,relwidth=0.85,relx=0.07,rely=0.5)
entry2=Entry(frame0)
entry2.place(relheight=0.1,relwidth=0.3,height=10,width=12,relx=0.5,rely=0.2)

#buttons
#placing button in frame
button=Button(frame0,text="Get Distance",command=lambda: get_distance(entry1.get(),entry2.get()))
button.place(relheight=0.1,relwidth=0.3,relx=0.15,rely=0.37)
v=StringVar()
label=Label(frame0,text="  Source                 Destination",bg='pink',font=('arial', 12, 'bold'),fg='blue')
label.place(relheight=0.05,relwidth=0.68,relx=0.15,rely=0.15)

#Placing label for displaying the search results
label=Label(frame0,textvariable=v,bg='pink',font=('arial', 12, 'bold'),fg='blue')
label.place(relheight=0.3,relwidth=0.85,relx=0.07,rely=0.5)

root.mainloop()

