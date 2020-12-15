class Stack(object):
    """
    Implementation of a custom stack 
    """
    def __init__(self):
        self.items =  []
    
    def isEmpty(self):
        return len(self.items) == 0


    def new_stack_item(self, item):
        self.items.append(item)

    
    def del_stack_item(self):
        return self.items.pop()

    
    def peek_at_top(self):
        return self.items[len(self.items)-1]

    
    def items_size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def balanced_brackets(s):
    """
    Determine whether a given string of parentheses (multiple types) is properly nested. 
    """
    openBr = set('[{<(')
    matches = set([( '(',')' ), ('{','}'), ('[',']'),('<','>')])

    stack= Stack()

    if len(s) % 2 != 0:
        return 0

    for bracket in s:

        if bracket in openBr:
            stack.new_stack_item(bracket)
                 

        else: # bracket not an opening one
            if stack.items_size() == 0: # No opening brackets so brackets unbalanced
                return 0
            
            last_open_bracket = stack.del_stack_item()
            
            t = (last_open_bracket,bracket) # Check if current closed bracket and opening are in matches
            if t not in matches:
                return 0
    
    return int(stack.items_size() == 0) # if length is zero brackets matched else not matched
        



    



