import requests
import pprint
 
# your api key
music_api_key = "xxxx"
# the api version
music_api_version = 3
# the users 8tracks login
music_login = "xxxx"
# the users 8tracks password
music_pwd = "xxxx"
# the endpoint for creating a new session
login_url = "https://8tracks.com/sessions.json"
# login payload
login_payload = {'login': music_login,'password': music_pwd,'api_version':3}
# the login request
login_request = requests.post(login_url, data=login_payload)
# get the user token
user_token = login_request.json()['user']['user_token']
# the subsequent request payload
subsequent_request_payload = {'api_key': music_api_key, 'api_version':music_api_version}
# the subsequent request header
header = {'X-User-Token': user_token}
# assign pretty printer to a variable
pp = pprint.PrettyPrinter()
 
def eight_tracks_api_testing_service():
        """
        This function allows you to test 8tracks API responses.  
        """
        print("Welcome to the 8tracks API testing service.\n\n"
        "This service will allow you to see the data and response models that are\n"
        "returned from various API calls.\n\n"
        "The following options are available:\n\n"
        "A = The response from a New Set Endpoint\n"    
        "B = The response from a MixSet SmartID Endpoint\n"
        "C = The response from a Mix (Playlist) Endpoint\n"
        "D = The response from a User Endpoint\n")
        testing_area = raw_input("Which option do you want to test? (blank entry to quit) :  ")
        if testing_area == "A" or testing_area == "a":
                while True:
                        try:
                                print("\nNew Set Endpoint Example:\n\nhttp://8tracks.com/sets/\" + play_token + \"/play.json?mix_id=\" + playlist_id\n"
                                "\nThe above URL has been assigned to a variable that includes a play token,\n"
                                "enter a numeric playlist id and the above endpoint will be accessed.\n")     
                                # test if input is an integer
                                newset_endpoint = raw_input("Enter a numeric playlist id (blank entry to quit) :  ")
                                newset_endpoint = int(newset_endpoint)
                                # BEGIN this will only be executed if input is not blank
                                playlist_id = newset_endpoint
                                print "\nSending Request...\n"
                                play_token_url = "http://8tracks.com/sets/new.json"
                                play_token_request = requests.get(play_token_url,
                                                                  data=subsequent_request_payload,
                                                                  headers=header,
                                                                  timeout=None)
                                play_token = play_token_request.json()['play_token']
                                play_url = "http://8tracks.com/sets/" + play_token + "/play.json?mix_id=" + str(playlist_id)
                                play_request = requests.get(play_url,
                                                            data=subsequent_request_payload,
                                                            headers=header, 
                                                            timeout=None)
                                pp.pprint(play_request.json())
                        except ValueError:
                                if newset_endpoint == '':
                                        break
                                print("\nALERT - PLEASE ENTER A NUMERIC PLAYLIST ID")
        elif testing_area == "B" or testing_area == "b":
                print ""
                print("MixSet SmartID Endpoint Example:\n\nhttp://8tracks.com/mix_sets/smart_type[:id-or-slug][:sort][:safe].format[?include=]\n")
                mixset_endpoint = raw_input("Enter a MixSet SmartID Endpoint (blank entry to quit) :  ")
                while mixset_endpoint != "":
                        subsequent_url = mixset_endpoint
                        print "\nSending Request...\n"
                        subsequent_request = requests.get(subsequent_url,
                                                        data=subsequent_request_payload,
                                                        headers=header, 
                                                        timeout=None)
                        pp.pprint(subsequent_request.json())
                        print ""
                        print("MixSet SmartID Endpoint Example:\n\nhttp://8tracks.com/mix_sets/smart_type[:id-or-slug][:sort][:safe].format[?include=]\n")
                        mixset_endpoint = raw_input("Enter a MixSet SmartID Endpoint (blank entry to quit) :  ")
        elif testing_area == "C" or testing_area == "c":
                print ""
                print("Mix (Playlist) Endpoint Example:\n\nhttp://8tracks.com/mixes/playlist_id_here.json\n")
                mix_endpoint = raw_input("Enter a Mix (Playlist) Endpoint (blank entry to quit) :  ")
                while mix_endpoint != "":
                        subsequent_url = mix_endpoint
                        print "\nSending Request...\n"
                        subsequent_request = requests.get(subsequent_url,
                                                        data=subsequent_request_payload,
                                                        headers=header, 
                                                        timeout=None)
                        pp.pprint(subsequent_request.json())
                        print ""
                        print("Mix (Playlist) Endpoint Example:\n\nhttp://8tracks.com/mixes/playlist_id_here.json\n")
                        mix_endpoint = raw_input("Enter a Mix (Playlist) Endpoint (blank entry to quit) :  ")
        elif testing_area == "D" or testing_area == "d":
                print ""
                print("User Collection Endpoint Example:\n\nhttp://8tracks.com/users/\" + user_id + \"/collections.json?include=mix_sets[mixes]\n")
                mixset_endpoint = raw_input("Enter a User Collection Endpoint (blank entry to quit) :  ")
                while mixset_endpoint != "":
                        subsequent_url = mixset_endpoint
                        print "\nSending Request...\n"
                        subsequent_request = requests.get(subsequent_url,
                                                        data=subsequent_request_payload,
                                                        headers=header, 
                                                        timeout=None)
                        pp.pprint(subsequent_request.json())
                        print ""
                        print("User Collection Endpoint Example:\n\nhttp://8tracks.com/users/\" + user_id + \"/collections.json?include=mix_sets[mixes]\n")
                        mixset_endpoint = raw_input("Enter a User Collection Endpoint (blank entry to quit) :  ")
        else:
                print "\nYou entered a non-existant option."
        print "\nThank You, Good Bye.\n"
 
eight_tracks_api_testing_service()
