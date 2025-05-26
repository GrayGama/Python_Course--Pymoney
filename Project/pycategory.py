class Categories():
    def __init__(self):
        self.catg_lst = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', \
        ['bus', 'railway']], 'income', ['salary', 'bonus']]
    
    def is_category_valid(self, category, categors):
        """recursive function to look if the given category is valid
        """
        if type(categors) is list:
            for v in categors: 
                p = self.is_category_valid(category, v)
                if p == True:
                    return p 
        return categors == category
    
    def view(self, categories, prefix=()):
        """Display the (default) available categories."""
        #From the source code of the Outline numbering. 
        if type(categories) is list:
            i = 0
            for v in categories: 
                if type(v) is not list:
                    i += 1
                self.view(v, prefix+(i,))
        else: 
            s = ' '*4*(len(prefix) - 1)
            s += '- ' + categories
            print(s)  
    
    def find_subcategories(self, category):
        """Method used by the find function. It will return a flatten list
        of category and subcategories.
        """
        def find_subcategories_gen(category, categories, found=False):
            #Generator
            if type(categories) == list:
                for index, child in enumerate(categories):
                    yield from find_subcategories_gen(category, child, found)
                    if child == category and index + 1 < len(categories) \
                        and type(categories[index + 1]) == list:
                        # When the target category is found,
                        # recursively call this generator on the subcategories
                        # with the flag set as True.
                        yield from find_subcategories_gen(category, categories[index+1], True)
            else:
                if categories == category or found == True:
                    yield categories
      
        targetcat_lst = [i for i in find_subcategories_gen(category, self.catg_lst)]
        return targetcat_lst