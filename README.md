# GAuth & GBuild

Helper Python Classes to assist with setting up authorization to Google API servers & then building a Google Service.

#### Dependencies

The following modules are required to run these helper classes:-

* OS
* HTTPLIB2
* GOOGLE API CLIENT
* OAUTH2CLIENT

> pip install --upgrade httplib2 oauth2client google-api-python-client

#### Installation

Useable on Windows/Linux/OSX x86/64 platforms.

```
mkdir projfolder
cd projfolder
git clone git@github.com:Pashbee/GAuth-GBuild.git

```

Usage Below

#### Usage:-

> from gauth import GAuth

> from gbuild import GBuild

Initialize a GAuth Object:-

> appauth = GAuth(scope, storetoken, apikeyfile, redirecturi)

Args are defined here in principal:-

http://google-api-python-client.googlecode.com/hg/docs/epy/oauth2client.client.OAuth2WebServerFlow-class.html

The storetoken file is a location for you to decide to save token base information to. The apikeyfile is the json formatted credentials you
can get from Google API Console when starting an application project.

Get Auth http object (needed to build a Google App Service):-

> appauth.auth

Thats that for Google Auth.

To build a Google Application:-

> process = GBuild(servicename, apiversion , http)

Args are defined here in principal:-

https://google-api-python-client.googlecode.com/hg/docs/epy/apiclient.discovery-module.html

servicename is name of application service being build (ie. calendar, docs). apiversion is google api version being used, v3 recommended.

http is httplib2.Http, An instance of httplib2.Http or something that acts like it that HTTP requests will be made through. In this case
appauth.auth returns a http object.

A Resource object with methods for interacting with the service.

Full Example Of Google API Calendar:-

```
from gauth import GAuth
from gbuild import GBuild

appauth = GAuth('https://www.googleapis.com/auth/calendar', 'token.data', 'apikeys.json', 'urn:ietf:wg:oauth:2.0:oob')

process = GBuild('calendar', 'v3', appauth.auth)
calid = domain.com_989ujpjpojpojporjpojpojpoj@group.calendar.google.com

event = {
  'summary': 'Appointment',
  'location': 'Somewhere',
  'start': {
    'dateTime': '2011-06-03T10:00:00.000-07:00'
  },
  'end': {
    'dateTime': '2011-06-03T10:25:00.000-07:00'
  },
  'attendees': [
    {
      'email': 'attendeeEmail',
      # Other attendee's data...
    },
    # ...
  ],
}

process.events().insert(calendarId=calid, body=event).execute()

```






