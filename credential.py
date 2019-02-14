class credential:
    """
    Class that generates new instances of credential.
    """

    credential_list = [] # Empty credential list

    def __init__(self, app_name, password):

      # docstring removed for simplicity

        self.app_name = app_name
        self.password = password
    
    # Init method up here
    def save_credential(self)

        '''
        save_credential method saves credential objects into credential_list
        '''

        credential.credential_list.append(self)

    @classmethod
    def find_by_app_name(cls,app_name):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for credential in cls.credential_list:
            if credential.app_name == app_name:
                return credential  
