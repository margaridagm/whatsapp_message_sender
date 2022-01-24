#imports
import pywhatkit
import datetime
import random

#messages
general_messages=['Hello!']


monday_messages_list=["Let's have a good week","You are strong! Let's start the week on a groove https://www.youtube.com/watch?v=arVVzuU8XIg&ab_channel=BrittanyHowardVEVO"]
tuesday_messages_list=["Let's have a good week","You are strong! Let's start the week on a groove https://www.youtube.com/watch?v=arVVzuU8XIg&ab_channel=BrittanyHowardVEVO"]
wednesday_messages_list=["Let's have a good week","You are strong! Let's start the week on a groove https://www.youtube.com/watch?v=arVVzuU8XIg&ab_channel=BrittanyHowardVEVO"]
thursday_messages_list=["Let's have a good week","You are strong! Let's start the week on a groove https://www.youtube.com/watch?v=arVVzuU8XIg&ab_channel=BrittanyHowardVEVO"]
friday_messages_list=["https://www.youtube.com/watch?v=mGgMZpGYiy8&ab_channel=TheCureVEVO"]

#FUNCTIONS

#message sender function
def message_sender(message,hour,min):

    pywhatkit.sendwhatmsg('+351915379848',message,hour,min)

#auto message selector  function
def message_selector(week_day):

    today=week_day
    if (today=='Monday'):
        random_message= random.randint(0, len(monday_messages_list))
        message_sender(monday_messages_list[0],9,15)
    elif (today=='Tuesday'):
        random_message= random.randint(0, len(tuesday_messages_list))
        message_sender(tuesday_messages_list[0],9,15)
    elif (today=='Wednesday'):
        random_message= random.randint(0, len(wednesday_messages_list))
        message_sender(wednesday_messages_list[0],9,15)
    elif (today=='Thursday'):
        random_message= random.randint(0, len(thursday_messages_list))
        message_sender(thursday_messages_list[0],9,15)
    elif (today=='Friday'):
        random_message= random.randint(0, len(friday_messages_list))
        message_sender(friday_messages_list[0],9,15)
    else:
        'No messages' 




#test_today=message_selector(datetime.datetime.today().strftime('%A'))




