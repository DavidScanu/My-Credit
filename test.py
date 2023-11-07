import os
import unittest




class TestFoldersPresence(unittest.TestCase):
    """Test the Presence of all required Folders for the function.
    >>> ['assets', '.streamlit']
    """

    def test_folder_assets_exist(self):
        """Test Folders 'assets' Presence"""
        self.assertTrue(os.path.exists('assets'), "The necessary folder 'assets' have not been found")

    def test_folder_streamlit_exist(self):
        """Test Folders '.streamlit' Presence"""
        self.assertTrue(os.path.exists('.streamlit'), "The necessary folder '.streamlit' have not been found")


class TestFilesPresence(unittest.TestCase):
    """Test the Presence of all required Files for the function.
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
    """Test the Presence of all required Functions for app."""
    pass


class TestRequestAPIFunction(unittest.TestCase):
    """Test the function for sending form data to the prediction API."""
    pass



if __name__ == '__main__':
    unittest.main()