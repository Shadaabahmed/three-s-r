"""
This file process converted text and perform actions accordingly.
This file can be extended with more action.
"""
import valib as va
import action as a
import time
import logging

logger = logging.getLogger('voice assistant')


def process_text(text, pa):

    """
    asking who are you?
    """
    if "who are you" in text:
        va.audio_playback("i am a i voice assistant system")
    elif "What are you" in text:
         va.audio_playback("I am a robot")
    elif "Hi" in text:
        va.audio_playback("Hello")
    elif "what is your name?" in text:
         va.audio_playback("My name is 3SR")
    elif "What is 3SR?" in text:
        va.audio_playback("Socio service smart robot")
    elif "Good morning" in text:
        va.audio_playback("Very good morning")
    elif "Good afternoon" in text:
        va.audio_playback("Good afternoon")
    elif "Good evening" in text:
        va.audio_playback("Good evening")
    elif "Good night" in text:
        va.audio_playback("Good night")
    elif "How are you?" in text:
        va.audio_playback("I'am fine, thank you. How are you? ")
    elif "what is your college name?" in text:
        va.audio_playback("Maharaja Institute of Technology Mysore ")
    elif "who is the HOD of ECE department" in text:
        va.audio_playback("Doctor Ravichandra Kulkarni")
    elif "who is the principal of M I T mysuru" in text:
        va.audio_playback("Doctor Naresh Kumar B G")
    elif "who is the Renuka mam" in text:
        va.audio_playback("Renuka mam is the assistent professor of ECE department")
    elif "who is the Smitha mam" in text:
        va.audio_playback("Smitha mam is the assistent professor of ECE department")
    elif "who created you" in text:
        va.audio_playback("I was created by group of 4 individuals they are Shadaab subramanya sneha reshma")
    elif "who is the Renuka mam" in text:
        va.audio_playback("Renuka mam is the assistent professor of ECE department")
    else:
        va.audio_playback("Sorry, I din't get you")
    


    """
    asking about weather information.
    """
    if "weather" in text:
        va.audio_playback("which city")
        time.sleep(0.5)
        file_name = pa.process(3)
        city = pa.voice_command_processor(file_name)
        logger.info("process_text : City :: " + city)
        try:
            humidity, temp, phrase = a.weatherReport(city)
            va.audio_playback(
                "currently in " + city + " temperature is " + str(temp) + " degree celsius, " + "humidity is " + str(
                    humidity) + " percent and sky is " + phrase)
            logger.info("currently in " + city + " temperature is " + str(temp) + "degree celsius, " + "humidity is " + str(
                humidity) + " percent and sky is " + phrase)
        except KeyError as e:
            va.audio_playback("sorry, i couldn't get the location")

            
    """
    asking for search somthing like:
    what is raspberry pi
    who is isac newton etc.
    """
    if "search" in text or "Search" in text:
        va.audio_playback("tell me what to search")
        time.sleep(0.5)
        file_name = pa.process(5)
        search_data = pa.voice_command_processor(file_name)
        try:
            result = a.google_search(search_data)
            if result:
                va.audio_playback(result)
            else:
                va.audio_playback("sorry, i couldn't find any result for " + search_data)
        except KeyError as e:
            va.audio_playback("sorry, i couldn't find any result for " + search_data)
            pass

        
    """
    asking aboout current time.
    """
    if "time" in text or "Time" in text:
        current_time = a.current_datetime("time")
        va.audio_playback("right now it is " + current_time)

    """
    asking about today's date.
    """
    if "date" in text or "Date" in text:
        date = a.current_datetime("date")
        va.audio_playback("today it is " + date)

        
    """
    asking for rebooting the voice assistant system.
    """
    if "reboot" in text or "Reboot" in text:
        va.audio_playback("ok.. rebooting the server")
        a.reboot_server()

    return "done"
