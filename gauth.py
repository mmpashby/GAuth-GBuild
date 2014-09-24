####################################################################################
#### gauth.py - Class file dedicated to Authing with Googles OAuth2 API servers ####
####################################################################################


############################################
#### Import apiclient and oauth modules ####
############################################

import os
import httplib2
from oauth2client.file import Storage
from oauth2client.client import flow_from_clientsecrets


class GAuth(object):
    """ A class specifically designed for Google Authentication passthrough.

    """
    def __init__(self, appscope, credstorefilename, apikeysloc, redirecturi=None):
        """ Spawn GAuth Instance

        :param appscope:
        :param credstorefilename:
        :param apikeysloc:
        :param redirecturi:
        :return:
        """
        #####################################################
        #### Setting Auth Parameters For Object Instance ####
        #####################################################
        self.scope = appscope
        self.credfile = credstorefilename
        self.apikeys = apikeysloc
        self.redirecturi = redirecturi
        self.storage = self.build_credstore()
        self.credentials = self.storage.get()
        self.flow = self.build_auth_flow()
        self.auth = self.perform_auth()

    def build_credstore(self):
        """ Build an auth token credential store if it doesnt exist.

        :return:
        """
        if os.path.isfile(self.credfile):
            storage = Storage(self.credfile)
            return storage
        else:
            with open(self.credfile, 'w') as fout:
                fout.write('')
            storage = Storage(self.credfile)
            return storage

    def build_auth_flow(self):
        """ Build an auth flow

        :return:
        """
        flow = flow_from_clientsecrets(self.apikeys, self.scope, self.redirecturi)
        return flow

    def perform_auth(self):
        """ Perform Auth on Request

        :return:
        """
        if self.credentials is None or self.credentials.invalid is True:
            authorize_url = self.flow.step1_get_authorize_url()
            print 'Go to the following link in your browser: ' + authorize_url
            code = raw_input('Enter Verification Code:').strip()
            self.credentials = self.flow.step2_exchange(code)
            self.storage.put(self.credentials)
        #########################
        #### Build HTTP Auth ####
        #########################
        http = httplib2.Http()
        http = self.credentials.authorize(http)
        return http



