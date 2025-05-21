class DataScrubber:
    def __init__(self, df):
        self.df = df

    def clean(self):
        # Example cleaning logic: drop duplicates
        self.df = self.df.drop_duplicates()
        return self.df
    def remove_duplicate_records(self):
        # Example: drop duplicate rows
        self.df = self.df.drop_duplicates()
        return self.df


    