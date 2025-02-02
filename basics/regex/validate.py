import re

email = input("Enter email ")

if re.search(r"^\w+@\w+\.com$",email,re.IGNORECASE):
    print('valid')

else:
    print('Invalid')

"""
    re.search(pattern,string,flags)

    .       any character except new line

    *       0 or more repetitors

    +       1 or more repetitors

    ?       0 or 1 repititions

    {m}     m repititions

    {m,n}   m-n reptitions

    new term : finite state machine more formally 
                (non diterministic finite automata)
    
    ^       matches the start of the string

    $       matches the end of the string or just before
            the newline at the end of the string

    []      set of charcters

    [^]     complementing the set

    \d      decimal digit

    \D      not a decimal digit

    \s      whitespace charcters

    \S      not a whitespace charcters

    \w      word charcter...as well as number and the underscore

    \W      not a word charcter

    A|B     either A or B

    (...)   a group   >> returns captured string sections

    (?...)  non-capturing version

    re.match(pattern,string,flags=0)     automatically matching from strart no need ^

    re.fullmatch(pattern,string,flags=0)    match both start and end of the string no need ^ and $

    
"""