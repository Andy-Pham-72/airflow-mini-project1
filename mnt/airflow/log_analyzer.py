from pathlib import Path
import regex as re
import sys

class LogAnalyzer:
    """
    Class LogAnalyzer is used to count and find all the ERROR messages in all the log files
    """
    
    def __init__(self):
        self.insert_dir()
        
    def insert_dir(self, log_dir = sys.argv[1]): # input pramater with Command Line Argument
        '''
        This method has 'log_dir' parameter as the root directory to recursively list all the files ending with extension ".log"

        for example: "/Users/airflow/logs"

        We can run in Bash Shell as: 
        $ python3 log_analyzer.py /Users/airflow/logs 
        '''
        
        self.log_dir = log_dir
        # find all the log files from the root directory
        self.file_list = Path(self.log_dir).rglob('*.log')

        return self.file_list

    def analyze_file(self):
        """
        This method take all the log files list from "insert_dir" method and print the cummulative error count and messages 
        from all the log files that are analyzed

        For example:
        Total number of error: 6
        Here are all the errors:
        - [2020-09-27 20:12:59,742] {taskinstance.py:1150} ERROR - No columns to parse from file
        - [2020-09-27 20:15:59,364] {taskinstance.py:1150} ERROR - No columns to parse from file
        """
        
        # assign a list
        self.error_list = []

        # loop through the log list
        for dir in self.file_list:
            open_dir = open(dir)
            # Check all the sentences with 'ERROR' message
            for sentence in open_dir.read().splitlines():
                error_search = re.search(r'\bERROR\b', sentence)
                # append all the 'ERROR' message into the list
                if error_search:
                    self.error_list.append(sentence)

        print( 'Total number of errors: {n} \
                \nHere are all the errors:\n{m}'.\
                    format(n=len(self.error_list),\
                           m='\n'.join(["- " + self.error_list[i] for i in range(0,len(self.error_list))])))

if __name__ == '__main__':

    search= LogAnalyzer()

    search.analyze_file()