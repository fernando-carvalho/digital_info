from linkedin import (LinkedInAuthentication, LinkedInApplication,
                               PERMISSIONS)

if __name__ == '__main__':
    API_KEY = '77se22zag9iejz'
    API_SECRET = 'kBpqQgsjTrWXu4wB'
    RETURN_URL = 'http://68.183.125.29:5000'
    authentication = LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL,
                                            PERMISSIONS.enums.values())
    print (authentication.authorization_url)
application = LinkedInApplication(authentication)
