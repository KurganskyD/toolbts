# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 14:31:42 2016

@author: device
"""

import pandas as pd
import re               #библиотека для работы с регулярными выражениями
#import numpy as np


def filter_pattern(arr_pattern, text):
    stack_trace_flag = 0
    temp_str = ' '
    cleaned_text = ' '
    cleaned_text = text
    temp_str = text
    for i, pattern in enumerate(arr_pattern):
#        print('.')
        if pattern.search(temp_str):
#            pattern_declaration = 'PATTERN %d' % i  
#            print(pattern_declaration)
            if ((i < 12) and (stack_trace_flag == 0)): #change i if number of stack-trace regex changes! 
                stack_trace_flag = 1
            matches = pattern.findall(temp_str)
            temp_str = pattern.sub('', temp_str)
            cleaned_text = temp_str
#            temp_str = " ".join(temp_str.split())
#            print('|||||||||||||||||||||||||||||||BEGIN MATCHES||||||||||||||||||||||||||||||')
#            print(matches)
#            print('|||||||||||||||||||||||||||||||END MATCHES||||||||||||||||||||||||||||||||')
#            print()
#            print()
#            print('|||||||||||||||||||||||||||||||BEGIN cleaned TEXT|||||||||||||||||||||||||||')
#            print(cleaned_text)
#            print('|||||||||||||||||||||||||||||||END cleaned TEXT|||||||||||||||||||||||||||||')
#            print()
#            print()    
#    print()
#    print()
    print('|||||||||||||||||||||||||||||||BEGIN cleaned TEXT|||||||||||||||||||||||||||')
#    cleaned_text = " ".join(cleaned_text.split())
    print(cleaned_text)
    print('|||||||||||||||||||||||||||||||END cleaned TEXT|||||||||||||||||||||||||||||')
    print()
    print()
    return [temp_str, stack_trace_flag]


number_of_bug_descr = list()
list_of_all_projects_cleaned_bugs_descriptions_with_stack_trace_flags = list()
for i in range(1,2):
    str_path = "F:\\mike\\hse\\exactpro\\all_projects\\JBoss%d.csv" % i
    data = pd.read_csv(str_path)
    data_description0 = data['Description'][1:]
    data_description0.dropna(inplace = True)
    data_description0.to_frame()
    data_len = len(data_description0)
    number_of_bug_descr.append(data_len)
    zeros_df = pd.DataFrame(0, index=data_description0.index, columns=['HasStackTrace'])
    data_description = pd.concat([data_description0, zeros_df], axis=1)
    
    subset = data_description[['Description', 'HasStackTrace']]
    list_of_bugs_descriptions_and_stack_trace_flags = [list(x) for x in subset.values]
    
    #LAST VARIANT (01/12/2016 00.00)
    pattern0 = re.compile('(?:.*ERROR.*|(?:.*INFO.*|(?:.*WARN.*|(?:.*CLOSE_WAIT.*|(?:.*BLOCKED.*|(?:.*DEBUG.*|.*WAITING.*))))))') 
    pattern1 = re.compile('(?:(((\\n.*ERROR.*)+)?((.*ERROR.*\\n)+)?((.*[a-zA-Z]Exception.*\\n)+)?((.*[a-zA-Z]Error.*\\n)+)?((.*at .*[(].*(?:java|(?:Unknown Source|Native Method)).*[)].*)+))|((((?:((\\n.*ERROR.*)+)|((.*ERROR.*\\n)+)))+)((((.*[a-zA-Z]Exception.*\\n)+)))))')
    pattern2 = re.compile('.*(?:waiting|locked).*0x.*[(].*[)].*')
    pattern3 = re.compile('.*0x.*0x.*')
    pattern4 = re.compile('.*(?:(".*ActiveMQ.*")|(".*Thread-7.*")).*')
#    ok
    pattern5 = re.compile('([a-zA-Z]+\.[a-zA-Z]+\.[a-zA-Z]+[(](?:.*java.*|(?:.*Native Method.*|.*No such file or directory.*))[)])')
#    ok
    pattern6 = re.compile('.*[Cc]aused by.*java.*\\n(.*[Cc]aused by.*java.*\\n)+')
#    ok    
    pattern7 = re.compile('.*at line.*\\n.*at line.*\\n((.*at line.*\\n)+)')
#    ok
    pattern8 = re.compile('((.*[0-9][0-9]:[0-9][0-9]:[0-9][0-9].*[[]error[]].*client.*)+)')
#    ok
    pattern9 = re.compile('.*java.*[(].*[)].*\\n.*java.*[(].*[)].*\\n')
#    pattern7 = re.compile('.*ERROR.*\\n')
    pattern10 = re.compile('.*[(].*".*".*=>.*".*".*[)].*')
    pattern11 = re.compile('failure description:.*[{].*[}]', re.DOTALL)
#    pattern11 = re.compile('.*WFLYPRT.*')
    
    arr_patterns = [pattern0, pattern1, pattern2, pattern3, pattern4, pattern5, pattern6, pattern7, pattern8, pattern9, pattern10, pattern11]

    
    for k,item in enumerate(list_of_bugs_descriptions_and_stack_trace_flags):
        if k < 40:
            continue
        if k == 50:
            print('|||||||||||||||||||||||||||||||||||||||||||')
            print('|||||||||||||||||||||||||||||||||||||||||||')
            print('|||||||||||||||||||||||||||||||||||||||||||')
            print('|||||||||||||||||||||||||||||||||||||||||||')
            print('|||||||||||||||||||||||||||||||||||||||||||')
            print('|||||||||||||||||||||||||||||||||||||||||||')
            print('|||||||||||||||||||||||||||||||||||||||||||')
            print('|||||||||||||||||||||||||||||||||||||||||||')
            print('|||||||||||||||||||||||||||||||||||||||||||')
            print('|||||||||||||||||||||||||||||||||||||||||||')
            break
        print('|||||||||||NUMBER OF TEXT||||||||||||')
        print(k)
        text = item[0]
#        print('|||||||||||||||||||||||||||||||BEGIN TEXT with trash|||||||||||||||||||||||||||')
#        print(text)
#        print('|||||||||||||||||||||||||||||||END TEXT with trash|||||||||||||||||||||||||||')
#        print()
#        print()
        list_of_bugs_descriptions_and_stack_trace_flags[k] = filter_pattern(arr_patterns, text)  
    list_of_all_projects_cleaned_bugs_descriptions_with_stack_trace_flags = list_of_all_projects_cleaned_bugs_descriptions_with_stack_trace_flags + list_of_bugs_descriptions_and_stack_trace_flags
#        print('-------------------THIS IS THE END-----------------------')
    str_for_print = 'Number of descriptions in %d project: ' % i
    print(str_for_print)
    print(len(list_of_bugs_descriptions_and_stack_trace_flags))


#print(list_of_all_projects_cleaned_bugs_descriptions_with_stack_trace_flags)
print('Number of all descriptions: ')
print(len(list_of_all_projects_cleaned_bugs_descriptions_with_stack_trace_flags))
 
