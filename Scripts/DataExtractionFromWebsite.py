import pandas as pd

class DataExtractionFromWebsite:
    def __init__(self):
        pass

    def tablesExtraction(self, url):
        try:
            return pd.read_html(url)
        except Exception as e:
            print(f"{e} \nMake sure you provide a correct URL")
    
    def csvFilesExtraction(self, url):
        try:
            return pd.read_csv(url)
        except Exception as e:
            print(f"{e} \nMake sure you provide a correct URL")