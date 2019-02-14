import unittest
from credential import credential

class Testcredential(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = credential("instagram","veve") # create credential object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.app_name,"instagram")
        self.assertEqual(self.new_credential.password,"veve")
        
    def test_save_credential(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the ccredential list
        '''
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(credential.credential_list),1)
    #Items up here...
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            credential.credential_list = []

    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credential to check if we can save multiple contact
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_save_credential = credential("instagram","veve") # new credential
            test_save_credential.save_credential()
            self.assertEqual(len(credential.credential_list),2)

     def test_find_contact_by_app_name(self):
        '''
        test to check if we can find a credential by app_name and display information
        '''

        self.new_credential.save_credential()
        test_credential = credential("instagram","veve") # new contact
        test_credential.save_credential()

        found_credential = credential.find_by_app_name(instagram)

        self.assertEqual(found_credential.password,test_credential.password)   


if __name__ == '__main__':
    unittest.main()