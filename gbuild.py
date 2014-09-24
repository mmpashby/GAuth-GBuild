###################################################################
#### gbuild.py - Class file dedicated to Building A Google App ####
###################################################################

from apiclient.discovery import build


class GBuild(object):
    """ Build Google App Instance

    """
    def __init__(self, sname, ver, authhttp):
        """ Initialize Google Build Instance based on service name, version of app and the authstat.

        :param sname:
        :param ver:
        :param authhttp:
        :return:
        """
        self.servicename = sname
        self.apiversion = ver
        self.authstatus = authhttp
        self.servicebuild = self.run_build()

    def run_build(self):
        """

        :return:
        """
        service = build(serviceName=self.servicename, version=self.apiversion, http=self.authstatus)
        return service