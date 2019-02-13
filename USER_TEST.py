import unittest
from USER import user

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact = user("James","Muriuki","0712345678","james@ms.com") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_contact.first_name,"James")
        self.assertEqual(self.new_contact.last_name,"Muriuki")
        self.assertEqual(self.new_contact.phone_number,"0712345678")
        self.assertEqual(self.new_contact.email,"james@ms.com")
    def test_save_contact(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_contact.save_contact() # saving the new contact
        self.assertEqual(len(user.contact_list),1)
    # Items up here...
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Contact.contact_list = []

    def test_save_multiple_contact(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_contact.save_contact()
            test_contact = user("Test","user","0712345678","test@user.com") # new contact
            test_contact.save_contact()
            self.assertEqual(len(user.contact_list),3)

    def test_display_all_contacts(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(user.display_contacts(),user.contact_list)

    def test_find_contact_by_number(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_contact.save_contact()
        test_contact = user("Test","user","0711223344","test@user.com") # new contact
        test_contact.save_contact()

        found_contact = user.find_by_number("0711223344")

        self.assertEqual(found_contact.email,test_contact.email)    


if __name__ == '__main__':
    unittest.main()