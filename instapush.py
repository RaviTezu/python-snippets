#!/usr/bin/python
import sys
import pycurl, json

appID = "xxxxxxxxxxxxxxxxxxxxxxx"
appSecret = "xxxxxxxxxxxxxxxxxxxxx"
pushEvent = "Status"

def main():
    #use Curl to post the Instapush API
    c = pycurl.Curl()

    #set Instapush API URL
    c.setopt(c.URL, 'https://api.instapush.im/v1/post')

    #setup custom headers for authentication variables and content type
    c.setopt(c.HTTPHEADER, ['x-instapush-appid: ' + appID,
                            'x-instapush-appsecret: ' + appSecret, 
                            'Content-Type: application/json'])

    #create a dictionary structure for the JSON data to post to Instapush
    json_fields = {}

    #setup JSON values
    json_fields['event']=pushEvent
    json_fields['trackers'] = {}
    json_fields['trackers']['message']=pushMessage
    postfields = json.dumps(json_fields)

    #make sure to send the JSON with post
    c.setopt(c.POSTFIELDS, postfields)

    #send push notification
    c.perform()

    #cleanup
    c.close()

if __name__ == "__main__" and len(sys.argv)>1:
    pushMessage = str(sys.argv[1])
    main()
else: 
    print "instapush.py <Message>"
    sys.exit(1)
