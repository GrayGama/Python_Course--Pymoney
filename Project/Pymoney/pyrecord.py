import sys
import datetime 
import tkinter as tk
from tkinter import messagebox 

class Record:
    """Represent a record."""
    def __init__(self, date, category, description, amount):
        self._date = date
        self._category = category
        self._descrpt = description
        self._amount = int(amount)
    @property
    def date(self):
        return self._date
    @property
    def category(self):
        return self._category
    @property
    def description(self):
        return self._descrpt
    @property
    def amount(self):
        return self._amount
    
class Records:
# member data of Records:
# wallet, record_lst, filtered_records
    def __init__(self):
        """Initialize variables values, or 
        read them from the records.txt file.
        """
        try: 
            fh = open('records.txt', 'r')
        except FileNotFoundError:       # File does not exist. 
            
            self._wallet = 0
            self._record_lst = []
            # self._record_lst = [('2020-06-08', 'meal', 'breakfast', -50), ('2020-06-08', 'drink', 'coffee', -100), ('2022-05-21', 'meal', 'lunch', -70), ('2022-05-21', 'railway', 'MRT', -45)]
                
        else: 
        
            try:    # No line to read from the file. 
                walletstr = fh.readline()
                assert walletstr != '', 'The file is empty!'
            except AssertionError as err:      #(8) File is empty, by a possible undesired modification. 
                sys.stdout.write('\nError: %s\n' %err)
                sys.exit(1)

            try:    # The first line cannot be interpreted as initial amount of money.
                self._wallet = int(walletstr)
            except ValueError as err:
                sys.stdout.write('\nError: %s\nFail to read the first line of the file\n\n' %err)
                sys.exit(1)
            
            self._record_lst = fh.readlines()
            for line in self._record_lst: 
                try: # Fail to read any of the lines. 
                    bufferRecord = line.split()
                    assert len(bufferRecord) == 4
                except AssertionError: 
                    sys.stdout.write('\nError reading one of the lines of the file!\n\n')
                    sys.exit(1)
            
            indxL = 0 
            for elem in self._record_lst:
                self._record_lst[indxL] = elem.strip('\n')  # removing the '\n' from readlines().
                indxL += 1

            indxL = 0     
            for elem in self._record_lst:  
                # making my data structure -> (date, category, description, value).             
                spltrec = elem.split()
                num = int(spltrec[3])
                spltrec.pop(); spltrec.append(num)     
                
                Ltotp = tuple(spltrec)
                
                self._record_lst[indxL] = Ltotp
                indxL += 1 
            
            fh.close()
    
    def add(self, rec_toadd, catg_obj, mode=0):
        """Method to add a new record in the form 
        of (date, category, description, amount) and add it
        to self._record_lst
        """
        if mode == 1: 
            try:
                self._wallet = int(rec_toadd)
                print(self._wallet)
                
            except ValueError:
                messagebox.showerror('Pymoney Error', 'Invalid: Please enter a valid Money amount\n')    
        else:
            try:
                datetime.date.fromisoformat(rec_toadd[0])
            except ValueError:
                messagebox.showerror('Pymoney Error', 'The format of date should be YYYY-MM-DD\n\
                    \rFail to add the record.\n')
            
            try:
                if catg_obj.is_category_valid(rec_toadd[1], catg_obj._catg_lst) != True:
                    raise ValueError
            except ValueError: 
                messagebox.showerror('Pymoney Error', '''Error: The specified category is not in the category list.
                \rYou can check the category list by the command "view categories".
                \r--Failed to add a new record.--\n''')
                return
            
            try:
                num = int(rec_toadd[3])
            except ValueError as err: 
                messagebox.showerror('Pymoney Error', 'Error: %s\n Invalid: Please enter a valid Income/Expense value\n' %err)
                return
            
            rec_toadd.pop(); rec_toadd.append(num)  # replacing the str type value to int
            
            Ltotp = tuple(rec_toadd)
            self._wallet += Ltotp[3]
            self._record_lst.append(Ltotp)     # adding the records as (date, category, InEx, value)
    
    
    def delete(self, index):
        """Deletes the selected record from the list of records.
        """
        # try: 
        self._wallet -= self._record_lst[index][3]
        self._record_lst.pop(index);    
        # except IndexError: 
        #     messagebox.showerror('Pymoney Error', f'There is no \"{index}\" index, please choose a valid index.')
        
        return self._record_lst
  
    def find(self, target_catg):
        """Finds the category and sub-related categories asked by the user.
        """
        try:
            self._filtered_records = list(filter(lambda x: x[1] in target_catg, self._record_lst))
            assert self._filtered_records != []
        except AssertionError:
            messagebox.showerror('Pymoney Error', 'The specified record was not found.\nPlease choose a valid record.\n')
        # self.view(flag=True)
        
    def save(self):
        """Saves the records made from the user into records.txt.
        """
        recordstr = []
        for elem in self._record_lst:       
            # Converting my data structure into list of strings           
            int2str = str(elem[3])      # integer to string
            recordstr.append(elem[0] + ' ' + elem[1] + ' ' + elem[2] + ' ' + int2str)

        with open('records.txt', 'w') as fh: 
            fh.write('%s\n' %str(self._wallet))
            fh.writelines('%s\n' % line for line in recordstr)  
