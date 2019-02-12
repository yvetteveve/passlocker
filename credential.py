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
    def save_credential(self):

        '''
        save_credential method saves credential objects into credential_list
        '''

        credential.credential_list.append(self)