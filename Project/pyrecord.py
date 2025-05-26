import sys
import datetime 

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
            
            try:     # The user want to input a not convertible string
                self._wallet = int(input('How much money do you have? '))  
                self._record_lst = []
            except ValueError:
                sys.stdout.write('\nInvalid: Setting wallet to 0 by default\n')
                self.wallet = 0
                
        else: 
            print('Welcome back!')
            
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
    
    def add(self, rec_toadd, catg_obj):
        """Method to add a new record in the form 
        of (date, category, description, amount) and add it
        to self._record_lst
        """
        flag = False 
        if len(rec_toadd) == 4:
            try:
                datetime.date.fromisoformat(rec_toadd[0])
            except ValueError:
                sys.stdout.write('The format of date should be YYYY-MM-DD\n\
                    \rFail to add the record.\n')
            temp = rec_toadd[0]; flag = True
            rec_toadd.pop(0)
            
        try:
            assert len(rec_toadd) == 3, '\nError: Invalid record given, please add a valid Income/Expense record.'
            if catg_obj.is_category_valid(rec_toadd[0], catg_obj.catg_lst) != True:
                raise ValueError
        except AssertionError as err: 
            sys.stdout.write('%s\n' %err)
            return
        except ValueError: 
            sys.stdout.write('''Error: The specified category is not in the category list.
            \rYou can check the category list by the command "view categories".
            \r--Failed to add a new record.--\n''')
            return
        
        try:
            num = int(rec_toadd[2])
        except ValueError as err: 
            sys.stdout.write('\nError: %s\n' %err)
            print('Invalid: Please enter a valid Income/Expense value\n')
            return
        except UnboundLocalError:
            return
        
        rec_toadd.pop(); rec_toadd.append(num)  # replacing the str type value to int
        
        # inserting the date in my data structure
        if flag == True: 
            rec_toadd.insert(0, temp)
        else:
            rec_toadd.insert(0, str(datetime.date.today()))
        
        Ltotp = tuple(rec_toadd)
        self._record_lst.append(Ltotp)     # adding the records as (date, category, InEx, value)
    
        
    def view(self, flag=False):
        """Show all the records updated, made by the user.
        flag         -- to identify if the function was called
                        from the funtion find().
        """
        total_sum = 0
        print('Here\'s your expenses and incomes records:')
        print('{:<10} {:<15s} {:<20s} {}'.format('Date', 'Category', 'Description', 'Amount'))
        print('='*9, end=''); print('='*15, end=''); print(' ', end=''); print('='*20, end=''); print(' ', end=''); print('='*6)
        if flag == False: 
            for elem in self._record_lst:
                print('{:<10} {:<15s} {:<20} {}'.format(elem[0], elem[1], elem[2], elem[3]))
                total_sum += elem[3]
            print('='*9, end=''); print('='*15, end=''); print(' ', end=''); print('='*20, end=''); print(' ', end=''); print('='*6)
            print(f'Now you have {self._wallet+total_sum} dollars.')
        else:
            #view function was called from find()
            for elem in self._filtered_records:
                print('{:<10} {:<15s} {:<20} {}'.format(elem[0], elem[1], elem[2], elem[3])) 
                total_sum += elem[3]
            print('='*9, end=''); print('='*15, end=''); print(' ', end=''); print('='*20, end=''); print(' ', end=''); print('='*6)
            print(f'Total from the records above: {total_sum}.')
    
    def delete(self):
        """Deletes the selected record from the list of records.
        """
        try: # User doesn't follow design instructions. 
            indxD = int(input())
        except ValueError as err:
            print('Invalid index: Please choose an available record number')
            sys.stdout.write('Error: %s\n\n' %err)
        else: 
            try: 
                self._record_lst.pop(indxD-1);    # decrease the record qt by 1
            except IndexError: 
                sys.stdout.write(f'There is no \"{indxD}\" index, please choose a valid index.')
        
        return self._record_lst
  
    def find(self, target_catg):
        """Finds the category and sub-related categories asked by the user.
        """
        self._filtered_records = list(filter(lambda x: x[1] in target_catg, self._record_lst))
        self.view(flag=True)
        
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
