'''
Exercise 230 (file pp_230.py)
Create a class that will be responsible for reading text from file and writting text to file

Class data attributes:
filepath: str, file path of the file
start_line: int, the line number from which you start reading the file
_text:str, text that was read from file

Implement class procedural attributes:
def __init__(self, filepath, startline=0):
def get_text(self) -> str:
def read_from_file(self) -> None:
def write_to_file(self, text: str, f_path: str, mode: str = 'w') -> None:

Exception handling should be implemented

Enter filepath to read from file and startline using input() function
'''

class ReadWrite:
    def __init__(self, filepath, startline=0):
        self.filepath = filepath
        self.startline = startline
        self._text = '' # private text variable
    
    def get_text(self) -> str:
        if self._text:
            return self._text
        else:
            self.read_from_file()
            return self._text
    
    def read_from_file(self) -> None:
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                self._text = ''.join(f.readlines()[self.startline:])
        except Exception:
            print('Some error occurred in reading')

    def write_to_file(self, text: str, f_path: str, mode: str = 'w') -> None:
        with open(f_path, mode) as f:
            try:
                f.write(text)
            except Exception:
                print('Some error occurred.')

fpath = str(input('Please provide a filepath: '))
sline = int(input('Please provide a start line: '))
shake = ReadWrite(fpath, sline)
print(shake.get_text())

#shake.write_to_file(shake._text, 'testing.txt')