

import re

tokenString = []


# Define tokens and corresponding regular expressions
tokens = [
    ('BOOL_VAL', r'T|F'),
    ('FUNC_ID', r'\d{1,2}'),
    ('EQUIV_OP', r'=='),
    ('AND_OP', r'&&'),
    ('OR_OP', r'\|\|'),
    ('XOR_OP', r'xor'),
    ('NOT', r'~'),
    ('IN_OP', r'in'),
    ('IF_OP', r'if'),
    ('IFF_OP', r'iff'),
    ('PAR_L', r'\('),
    ('PAR_R', r'\)'),
    ('SET_VAL', r'='),
    ('APPEND_OP', r'\+='),
    ('REMOVE_OP', r'-='),
    ('BRACE_L', r'{'),
    ('BRACE_R', r'}'),
    ('FUNC_CALL', r'do'),
    ('WHILE', r'while'),
    ('END', r'end'),
    ('PRINT', r'print'),
    ('ENTER', r'\n'),
    ('SUCH_THAT', r'\|'),
    ('BOOL_ID', r'[a-z]'),
    ('SET_ID', r'[A-Z]'),
]



# Combine tokens into a single regular expression pattern
lexer_regex = '|'.join('(?P<{}>{})'.format(token[0], token[1]) for token in tokens)

def lexer(source_code):
    # Tokenize the source code
    for match in re.finditer(lexer_regex, source_code):
        token_type = match.lastgroup
        lexeme = match.group(token_type)
        yield token_type, lexeme

# Example usage:
source_code = """
A = {}
B = {}

A += a
A += b
A += c

a = T
print a

a = b in {a b c}

a = A in B

12
A += B
end


do 12

b = T
c = T

while a == T
do 3
end

3
b = ~b
c = ~c
a = ~(b && c) || ((A == B) == (B xor A || B))
end
"""

for token_type, lexeme in lexer(source_code):
    print(token_type, ':', lexeme)
    tokenString.append(token_type)
    


"""
a = T    
b = F
c = a && b
d = c xor b
a = ~d
"""


"""
a = T
b = T
c = T

0
a = ~b

2024
b = T
c = F
end

do 2024
do 0
do 2024
do 0
"""



"""
A = {}
B = {}

A += a
A += b
A += c

a = T
print a

a = b in {a b c}

a = A in B

12
A += B
end


do 12

b = T
c = T

while a == T
do 3
end

3
b = ~b
c = ~c
a = ~(b && c) || ((A == B) == (B xor A || B))
end
"""





#class treeNode:
    # The node's token (only relevant to leaf nodes)
#    token = ""
    # The indexes of the node's children
#    next = []
    # The index of the node's parent
#    parent = 0
    


syntaxError = False




# The index of the node currently being parsed
#currentParsingNode = 0

# The AST
#ast = []



# Creates a new leaf in the ast
#def createNode(t):
    #newNode = treeNode
    #newNode.token = t
    #newNode.parent = currentParsingNode
    #ast.append(treeNode)
    #ast[currentParsingNode].next.append[len(ast) - 1]
    


    # Determines whether a specific token is on top, "" specifies any token
def canParse(str):
    if (len(tokenString) > 0):
        if (str == "" or tokenString[0] == str):
            return True
        else:
            return False
    else:
        return False



def PROGRAM():
    # <program> --> { EXPRESSION ENTER }
    print("enter PROGRAM")
    
    
    while (canParse("ENTER")): # code can start anywhere
        tokenString.pop(0)
        print("----------------------------------------ENTER")
    
    # The PROGRAM non-terminal will create a new expression as long as there are still tokens left   
    while (canParse("")):
        
        
        
        EXPRESSION()
        
        if (canParse("ENTER")):
            while (canParse("ENTER")): # code can start anywhere
                tokenString.pop(0)
                print("----------------------------------------ENTER")

        else:
            print("exit PROGRAM")
            return
    
    print("exit PROGRAM")
    return



def EXPRESSION():   
    # <expression> --> 
    # | <change_bool> 
    # | <change_set> 
    # |  "print” {<bool_val>} 
    # | <func_def> 
    # | do <func_id> 
    # | <while_loop> 

    print("enter EXPRESSION")
    #currentParsingNode = [len(ast) - 1]
    

    if (canParse("BOOL_ID")):            
        CHANGE_BOOL()
        print("exit EXPRESSION")
        return
    
        
    elif (canParse("SET_ID")):
        CHANGE_SET()  
        print("exit EXPRESSION")
        return
    
        
    elif (canParse("PRINT")):
        tokenString.pop(0)
        print("----------------------------------------PRINT")
        if (canParse("BOOL_ID")):
            print("----------------------------------------BOOL_ID")
            tokenString.pop(0)
        elif (canParse("BOOL_VAL")):
            print("----------------------------------------BOOL_ID")
        else:
            syntaxError = True
        print("exit EXPRESSION")
        return
     
        
    elif (canParse("FUNC_ID")):
        FUNC_DEF()
        print("exit EXPRESSION")
        return
    

    elif (canParse("FUNC_CALL")):
        tokenString.pop(0)
        print("----------------------------------------FUNC_CALL")
        
        if (canParse("FUNC_ID")):
            tokenString.pop(0)
            print("----------------------------------------FUNC_ID")

        print("exit EXPRESSION")
        return
     
        
    elif (canParse("WHILE")):
        WHILE_LOOP()
        print("exit EXPRESSION")
        return


    print("exit EXPRESSION")
    return



def FUNC_DEF():
    # <func_def> --> 
    # <func_id> "enter" { <expression> "enter" } "end"
    
    print("enter FUNC_DEF")
    
    tokenString.pop(0)
    print("----------------------------------------FUNC_ID")
    

    if (canParse("ENTER")):  
         tokenString.pop(0)
         print("----------------------------------------ENTER")  
    else:
        syntaxError = True
    
        
    while True:
        
        EXPRESSION()
        
        if (canParse("END")):
            tokenString.pop(0)
            print("----------------------------------------END")
            print("exit FUNC_DEF")
            return
        
        elif (canParse("ENTER")):
            tokenString.pop(0)       
            print("----------------------------------------ENTER")
            
        else:
            syntaxError = True
            print("exit FUNC_DEF")
            return



def WHILE_LOOP():
    # <func_def> --> 
    # "<while" <bool_expr> "enter" { <expression> "enter" } "end"

    print("enter WHILE_LOOP")
    
    if (canParse("")):
        tokenString.pop(0)
        print("----------------------------------------WHILE")
    else:
        syntaxError = True
    
    BOOL_EXPR()
    
    if (canParse("ENTER")):
        tokenString.pop(0)
        print("----------------------------------------ENTER")
    else:
        syntaxError = True

        
    while (True):
        
        EXPRESSION()

        
        if (canParse("ENTER")):
            tokenString.pop(0)
            print("----------------------------------------ENTER")
            
        if (canParse("END")):
            tokenString.pop(0)
            print("----------------------------------------END")
            print("exit WHILE_LOOP")
            return
                
        elif(not canParse("ENTER")):
            syntaxError = True
            print("exit WHILE_LOOP")
            return



def CHANGE_BOOL():
    # <change_bool> --> 
    # <bool_id> "=" <bool_expr> 

    print("enter CHANGE_BOOL")
    
    tokenString.pop(0)
    print("----------------------------------------BOOL_ID")
       
    if (canParse("SET_VAL")):
        tokenString.pop(0)
        print("----------------------------------------SET_VAL")
    else:
        syntaxError = True
    
    
    BOOL_EXPR()

    
    print("exit CHANGE_BOOL")
    return



def CHANGE_SET():
    # <change_bool> --> 
    # <set_id> “=” <set_expr>  
    # <set_id> “+=” <bool_id> 
    # <set_id> “+=” <set_id> 
    # <set_id> “-=” <bool_id> 
    # <set_id> “-=” <set_id> 

    print("enter CHANGE_SET")
    
    if (canParse("SET_ID")):
        tokenString.pop(0)
        print("----------------------------------------SET_ID")
    else:
        syntaxError = True

    if (canParse("SET_VAL")):
        tokenString.pop(0)
        print("----------------------------------------SET_VAL")
        SET_EXPR()
        
        
    elif (canParse("APPEND_OP")):
        tokenString.pop(0)
        print("----------------------------------------APPEND_OP")
        
        if (canParse("BOOL_ID")):
            tokenString.pop(0)
            print("----------------------------------------BOOL_ID")
            
        elif (canParse("SET_ID")):
            tokenString.pop(0)
            print("----------------------------------------SET_ID")
        else:
            syntaxError = True
            

    elif (canParse("REMOVE_OP")):
        tokenString.pop(0)
        print("----------------------------------------REMOVE_OP")
        
        if (canParse("BOOL_ID")):
            tokenString.pop(0)
            print("----------------------------------------BOOL_ID")
            
        elif (canParse("SET_ID")):
            tokenString.pop(0)
            print("----------------------------------------SET_ID")
        else:
            syntaxError = True

    else:
        syntaxError = True
        
    
    print("exit CHANGE_SET")
    return



def BOOL_EXPR():
    #<bool_expr> --> 
    #<bool_expr> (“==” | “&&” | “||” | “xor” | “if” | “iff”) <bool_expr> 
    #| “(“ <bool_expr> “)” 
    #| “~” <bool_expr> 
    #| <bool_id “in” <set> 
    #| <boolean> 
    #| <set> (“==” “in”) <set> 
         
    print("enter BOOL_EXPR")
       
    if (canParse("PAR_L")):
        tokenString.pop(0)
        print("----------------------------------------PAR_L")
        BOOL_EXPR()
        
        if (canParse("PAR_R")):
            tokenString.pop(0)
            print("----------------------------------------PAR_R")
        else:
            syntaxError = True
            print("exit BOOL_EXPR")
            return      
            

    elif (canParse("NOT")):
        tokenString.pop(0)
        print("----------------------------------------NOT")
        BOOL_EXPR()
        
      
    elif (canParse("BOOL_ID")):
        tokenString.pop(0)
        print("----------------------------------------BOOL_ID")
        
        if (canParse("IN_OP")):
            tokenString.pop(0)
            print("----------------------------------------IN_OP")
                
            SET_EXPR()
         
        else:
            syntaxError = True


    elif (canParse("BOOL_VAL")):
        tokenString.pop(0)
        print("----------------------------------------BOOL_VAL")
        
    
    else:
        SET()
        if (canParse("IN_OP") or canParse("EQUIV_OP")):
            
            if (canParse("IN_OP")):
                print("----------------------------------------IN_OP")
            elif (canParse("EQUIV_OP")):
                print("----------------------------------------EQUIV_OP")

            tokenString.pop(0)

            SET_EXPR()

    
    
    if (canParse("EQUIV_OP") or canParse("AND_OP") or canParse("OR_OP") or canParse("XOR_OP") or canParse("IF_OP") or canParse("IFF_OP")):
        
        if (canParse("EQUIV_OP")):
                print("----------------------------------------EQUIV_OP")
        elif (canParse("AND_OP")):
                print("----------------------------------------AND_OP")
        elif (canParse("OR_OP")):
                print("----------------------------------------OR_OP")
        elif (canParse("XOR_OP")):
                print("----------------------------------------XOR_OP")
        elif (canParse("IF_OP")):
                print("----------------------------------------IF_OP")
        elif (canParse("IFF_OP")):
                print("----------------------------------------IFF_OP")
        
        tokenString.pop(0)
        BOOL_EXPR()

    else:
        syntaxError = True

    
    print("exit BOOL_EXPR")
    return



def SET_EXPR():
    # <set_expr> --> 
    # <set_expr> (“&&” | “||” “xor”) <set_expr> 

    print("enter SET_EXPR")
    
    SET()
    
    if (canParse("PAR_L")):
        tokenString.pop(0)
        print("----------------------------------------PAR_L")
        SET_EXPR()
        
        if (canParse("PAR_R")):
            tokenString.pop(0)
            print("----------------------------------------PAR_R")
        else:
            syntaxError = True
            print("exit SET_EXPR")
            return
    
    
    if (canParse("AND_OP") or canParse("OR_OP") or canParse("XOR_OP")):
        
        if (canParse("AND_OP")):
            print("----------------------------------------AND_OP")
        elif (canParse("OR_OP")):
            print("----------------------------------------OR_OP")
        elif (canParse("XOR_OP")):
            print("----------------------------------------XOR_OP")
            
        tokenString.pop(0)
        
        SET_EXPR()
        
    else:
        syntaxError = True
        
    
    print("exit SET_EXPR")
    return



def SET():
    # “{“ { <bool_id> } “}” 
    # | “{“ <bool_id> “in” <set_id> { <bool_id> “in” <set_id> } “|” <bool_expr> “}” 
    # | <set_id> 
    print("enter SET")
    
    
    if (canParse("BRACE_L")):
        
        print("----------------------------------------BRACE_L")
        tokenString.pop(0)
        
        if (canParse("BOOL_ID")):
            tokenString.pop(0)
            print("----------------------------------------BOOL_ID")
            
            if (canParse("IN_OP")):
                tokenString.pop(0)
                print("----------------------------------------IN_ID")
                
                tokenString.pop(0)
                print("----------------------------------------SET_ID")
                
                loop = 1
                
                while (loop == 1):
                    
                    if (canParse("BOOL_ID")):
                        print("----------------------------------------BOOL_ID")
                        tokenString.pop(0)
                    if (canParse("IN_OP")):
                        print("----------------------------------------IN_OP")
                        tokenString.pop(0)
                    if (canParse("SET_ID")):
                        print("----------------------------------------SET_ID")
                        tokenString.pop(0)
                    if (not canParse("BOOL_ID") and canParse("")):
                        tokenString.pop(0)
                        print("----------------------------------------SUCH_THAT")
                        loop = 0
                    elif (not canParse("")):
                        syntaxError = True
                        print("exit SET")
                        return
                
                BOOL_EXPR()
                if (canParse("BRACE_R")):
                    tokenString.pop(0)
                    print("----------------------------------------BRACE_R")
                    
                else:
                    syntaxError = True
                
                print("exit SET")
                return
                
            else:
               
                while (canParse("BOOL_ID")):
            
                    tokenString.pop(0)
                    print("----------------------------------------BOOL_ID")
            
            if (canParse("BRACE_R")):
                tokenString.pop(0)
                print("----------------------------------------BRACE_R")
            
            else:
                syntaxError = True
                
            print("exit SET")
            return
        
        elif (canParse("BRACE_R")):
            tokenString.pop(0)
            print("----------------------------------------BRACE_R")

         
    elif (canParse("SET_ID")):
        tokenString.pop(0)
        print("----------------------------------------SET_ID")
        print("exit SET")
        return
    
    else:
        syntaxError = True
        print("exit SET")
        return





# Recursive-Descent Parsing function
def parser():
    
    # Clear the ast
    #ast = []
    #currentParsingNode = 0
    
    # Create the AST root node
    #ast.append(treeNode())
    
    # Run the parser
    # The parser works by taking the first token from the end of the token stream. A token is removed from the token stream when the next token is used
    PROGRAM()
    


    return 0


# Run the parser
parser()