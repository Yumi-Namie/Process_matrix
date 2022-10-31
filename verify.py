from itertools import groupby #Check if all elements in a list are identical



def is_numerical(mtx):
    for columns in mtx:
        if columns != []: 
            for elements in columns:
                if type(elements)==float or type(elements)==int:
                    return True
    else:
        print('⚠️'+ '  ' + 'Only works on numerical matrices')


def same_length(mtx):
    if len(mtx) ==1:
        return True
    elif len(mtx)>1:
        length = []
        #counting elements for each column
        while len(length) <= len(mtx):
            for columns in mtx:
                length.append(len(columns))
            # Comparing values (elements)
            if all_equal(length) == False:
                print ('⚠️'+ '  ' + "It's not a matrix")
                return False
            else:
                return True
        
    
        

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)