import functions    ## -- functions.py
import os
import unittest




class TestFoldersPresence(unittest.TestCase):
    """Test the Presence of all required Folders.
    >>> ['assets', '.streamlit']
    """

    def test_folder_assets_exist(self):
        """Test Folders 'assets' Presence"""
        self.assertTrue(os.path.exists('assets'), "The necessary folder 'assets' have not been found")

    def test_folder_streamlit_exist(self):
        """Test Folders '.streamlit' Presence"""
        self.assertTrue(os.path.exists('.streamlit'), "The necessary folder '.streamlit' have not been found")


class TestFilesPresence(unittest.TestCase):
    """Test the Presence of all required Files.
    >>> ['app.py', 'functions.py', 'requirements.txt']
    """

    def test_file_app_exist(self):
        """Test File 'app.py' Presence"""
        self.assertTrue(os.path.exists('app.py'), "The necessary file 'app.py' have not been found")

    def test_file_functions_exist(self):
        """Test File 'functions.py' Presence"""
        self.assertTrue(os.path.exists('functions.py'), "The necessary file 'functions.py' have not been found")

    def test_file_requirements_exist(self):
        """Test File 'requirements.txt' Presence"""
        self.assertTrue(os.path.exists('requirements.txt'), "The necessary file 'requirements.txt' have not been found")


class TestFunctionsPresence(unittest.TestCase):
    """Test the Presence of all required Functions for app.
    >>> forms (to display the form page)
    >>> response_page (to display the prediction page)
    >>> display_score (to display fiability gauge score)
    >>> send_to_api (to send data from the form to api for prediction)
    >>> validation_response (to validate the api response and return it to the app)
    """

    def test_function_forms_exist(self):
        """Test Function 'forms()' Presence"""
        self.assertTrue(hasattr(functions, 'forms') and callable(getattr(functions, 'forms')), 
                        f"La fonction 'forms()' n'existe pas dans functions.py.")

    def test_function_response_page_exist(self):
        """Test Function 'response_page()' Presence"""
        self.assertTrue(hasattr(functions, 'response_page') and callable(getattr(functions, 'response_page')), 
                        f"La fonction 'response_page()' n'existe pas dans functions.py.")

    def test_function_display_score_exist(self):
        """Test Function 'display_score()' Presence"""
        self.assertTrue(hasattr(functions, 'display_score') and callable(getattr(functions, 'display_score')), 
                        f"La fonction 'display_score()' n'existe pas dans functions.py.")

    def test_function_send_to_api_exist(self):
        """Test Function 'send_to_api()' Presence"""
        self.assertTrue(hasattr(functions, 'send_to_api') and callable(getattr(functions, 'send_to_api')), 
                        f"La fonction 'send_to_api()' n'existe pas dans functions.py.")

    def test_function_validation_response_exist(self):
        """Test Function 'validation_response()' Presence"""
        self.assertTrue(hasattr(functions, 'validation_response') and callable(getattr(functions, 'validation_response')), 
                        f"La fonction 'validation_response()' n'existe pas dans functions.py.")


class TestRequestAPIFunction(unittest.TestCase):
    """Test the function for sending form data to the prediction API.
    The function send_to_api() call validation_response()
    """

    def test_request_api(self):
        """Test Function 'send_to_api()' to get the result from api
        Need to get a result (int > 1 or 0) and a score (int or float)
        """
        result, score = functions.send_to_api(36, "technicien", "Marié.e", 
                                              "tertiaire", False, 31000, False,
                                              True, "cellulaire", 7, "may", 560,
                                              4, True, 2)
        self.assertTrue(result in (0, 1), "Result is not 1 or 0")
        self.assertTrue(isinstance(score, (int, float)), "Score is not a int or float")




if __name__ == '__main__':
    unittest.main()