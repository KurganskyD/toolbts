import os
import pandas as pd
import re
from nltk.corpus import stopwords 
from nltk.util import ngrams 
from nltk.stem.api import StemmerI
from nltk.stem.regexp import RegexpStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.isri import ISRIStemmer
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.rslp import RSLPStemmer


def filter_pattern(arr_pattern, text):
    print('||||||||||||||||||||RAW TEXT|||||||||||||||||||||||')
    print(text)
    print('||||||||||||||||||||RAW TEXT|||||||||||||||||||||||')
    print()
    stack_trace_flag = 0
    temp_str = ' '
    cleaned_text = ' '
    cleaned_text = text
    temp_str = text
    
    pattern_a_lot_of_ERROR = re.compile('.*ERROR.*\\n.*ERROR.*\\n.*ERROR.*\\n.*ERROR.*\\n.*ERROR.*\\n.*ERROR.*')
    if pattern_a_lot_of_ERROR.search(temp_str):
        pattern_declaration = 'PATTERN a lot of ERROR'  
        print(pattern_declaration)
        stack_trace_flag = 1
#        print('first if')
        matches = pattern_a_lot_of_ERROR.findall(temp_str)
        temp_str = pattern_a_lot_of_ERROR.sub(' ', temp_str)
        cleaned_text = temp_str
        print('|||||||||||||||||||||||||||||||BEGIN MATCHES||||||||||||||||||||||||||||||') #mt
        print(matches) #mt
        print('|||||||||||||||||||||||||||||||END MATCHES||||||||||||||||||||||||||||||||') #mt
        print() #mt
        print() #mt  
            
    
    for i, pattern in enumerate(arr_pattern):
        if ( ((i > 8) and (i <= 19)) or (i == 27) or (i == 35) or (i == 40) ):
            if pattern.search(temp_str):
                stack_trace_flag = 1
                print('second if')
                print(i)
                
    for i, pattern in enumerate(arr_pattern):
#        print('.')
        if pattern.search(temp_str):
            pattern_declaration = 'PATTERN %d' % i  
            print(pattern_declaration)
            if ( ((i > 8) and (i <= 19)) or (i == 27) or (i == 35) or (i == 40) ): #change i if number of stack-trace regex changes! 
                stack_trace_flag = 1
#                print('third if')
            matches = pattern.findall(temp_str)
#            if (i == 78): #haven't -> havent, don't -> dont, pattern 54
#                temp_str = pattern.sub(' ', temp_str)
#            else:
            temp_str = pattern.sub(' ', temp_str)
            cleaned_text = temp_str
            print('|||||||||||||||||||||||||||||||BEGIN MATCHES||||||||||||||||||||||||||||||') #mt
            print(matches) #mt
            print('|||||||||||||||||||||||||||||||END MATCHES||||||||||||||||||||||||||||||||') #mt
            print() #mt
            print() #mt  
    print('|||||||||||||||||||||||||||||||BEGIN cleaned TEXT|||||||||||||||||||||||||||') #ct
#    cleaned_text = " ".join(cleaned_text.split()) #for text 9 ONLY!!!
#    cleaned_text = '\n'.join(' '.join(line.split()) for line in cleaned_text.split('\n'))
    cleaned_text = os.linesep.join([s for s in cleaned_text.splitlines() if s]) #ct
    print(cleaned_text) #ct
    print('|||||||||||||||||||||||||||||||END cleaned TEXT|||||||||||||||||||||||||||||') #ct
    print('STACK TRACE FLAG = '), print(stack_trace_flag)
    print('----------------------------------------------------------------------------')
    print() #ct
    print() #ct
    temp_str = " ".join(temp_str.split())
    return [temp_str, stack_trace_flag]

pattern0 = re.compile(r'({{.*?}})', re.DOTALL) #теперь работают верно
pattern1 = re.compile(r'({code.*?{code})', re.DOTALL)
pattern2 = re.compile(r'({noformat.*?{noformat})', re.DOTALL)
pattern3 = re.compile(r'({panel.*?{panel})', re.DOTALL)
pattern4 = re.compile(r'({quote.*?{quote})', re.DOTALL)
pattern5 = re.compile('\\nmysql>.* sec[)]', re.DOTALL) #for sql
pattern6 = re.compile('Original Message.*\\n(>\\s)?Subject:.*\\n(>\\s)?Date:.*\\n(>\\s)?From:.*\\n(>\\s)?To:.*')
pattern7 = re.compile('\\n(>\\s)?Service Level:.*\\n(>\\s)?Product:.*\\n(>\\s)?Response Time:.*\\n(>\\s)?Time of Expiration:.*\\n(>\\s)?Created:.*\\n(>\\s)?URL:.*\\n(>\\s)?Subject:.*')
pattern8 = re.compile('[[(][0-9][0-9]:[0-9][0-9].*(?:(PM)|(AM)).*:')

pattern9 = re.compile('\\n(>\\s)?Resolving.*\\n(>\\s)?Connecting.*\\n(>\\s)?HTTP.*\\n(>\\s)?(\\s)+HTTP.*\\n(>\\s)?(\\s)+Date:.*\\n(>\\s)?(\\s)+Server:.*(?:(\\n(>\\s)?(\\s)+Location:.*\\n(>\\s)?(\\s)+Content-Length:.*\\n(>\\s)?(\\s)+Keep-Alive:.*\\n(>\\s)?(\\s)+Connection:.*\\n(>\\s)?(\\s)+Content-Type:.*(\\n(>\\s)?(\\s)+Location:.*)?)|(\\n(>\\s)?(\\s)+X-Powered-By:.*\\n(>\\s)?(\\s)+Content-Type:.*\\n(>\\s)?(\\s)+(?:(Content-Language:)|(Content-Length:)).*(\\n(>\\s)?(\\s)+Set-Cookie:.*)?(\\n(>\\s)?(\\s)+Via:.*)?(\\n(>\\s)?(\\s)+Connection:.*)?))(.*Length:.*)?')
pattern10 = re.compile('(?:(.*ALERT.*)|(?:(.*ERROR.*)|(?:.*ERROR.*|(?:.*INFO.*|(?:.*WARN.*|(?:.*CLOSE_WAIT.*|(?:.*BLOCKED.*|(?:.*DEBUG.*|.*WAITING.*))))))))') 
pattern11 = re.compile('(?:(((\\n.*ERROR.*)+)?((.*ERROR.*\\n)+)?((.*[a-zA-Z]Exception.*\\n)+)?((.*[a-zA-Z]Error.*\\n)+)?((.*at .*[(].*(?:java|(?:Unknown Source|Native Method)).*[)].*)+))|((((?:((\\n.*ERROR.*)+)|((.*ERROR.*\\n)+)))+)((((.*[a-zA-Z]Exception.*\\n)+)))))')
pattern12 = re.compile('.*(?:waiting|locked).*0x.*[(].*[)].*')
pattern13 = re.compile('.*0x.*0x.*')
pattern14 = re.compile('.*(?:(".*ActiveMQ.*")|(".*Thread-7.*")).*')
pattern15 = re.compile('([a-zA-Z]+\.[a-zA-Z]+\.[a-zA-Z]+[(](?:.*java.*|(?:.*Native Method.*|.*No such file or directory.*))[)])')
pattern16 = re.compile('.*[Cc]aused by.*java.*\\n(.*[Cc]aused by.*java.*\\n)+') 
pattern17 = re.compile('.*at line.*\\n.*at line.*\\n((.*at line.*\\n)+)')
pattern18 = re.compile('((.*[0-9][0-9]:[0-9][0-9]:[0-9][0-9].*[[]error[]].*client.*)+)')
pattern19 = re.compile('.*java.*[(].*[)].*\\n.*java.*[(].*[)].*\\n')
pattern20 = re.compile('.*[(].*".*".*=>.*".*".*[)].*')
pattern21 = re.compile('failure description:.*[{].*[}]', re.DOTALL)
#ok
#pattern12 = re.compile('[\\s][{][\\s].*[\\s][}][\\s]', re.DOTALL)
pattern22 = re.compile('\\n[{]\\r\\n.*\\r\\n[}]\\r', re.DOTALL) #12, 17 и 20 не конфликтуют?
pattern23 = re.compile('[/][^\\s]*=[^\\s]*[/][^\\s]*=[^\\s]*')
pattern24 = re.compile('[^\\s]+[.][^\\s"]+')
pattern25 = re.compile('{{.*}}')                                #
pattern26 = re.compile('[^\\s]+[/][^\\s]+')
pattern27 = re.compile('.*Event.*receive.*from remote server.*\\nInternal Server Error.*')
pattern28 = re.compile('<.*>\\s.*<[/].*>\\s', re.DOTALL)
#pattern28 = re.compile('[\\w"-[.]]+(?:(=)|(==))[\\w"-[.]]+')
pattern29 = re.compile('(?:({panel})|(?:({code[^\\s]*})|(?:({noformat})|({quote}))))')
pattern30 = re.compile('[a-z]+[A-Z][a-z]+( )?[{].*[}]', re.DOTALL)
pattern31 = re.compile('[A-Z][a-z]+[A-Z][a-z]+[(].*[)]')
pattern32 = re.compile('{.*return.*}', re.DOTALL)
pattern33 = re.compile('[^\\s]*@[^\\s]*')
pattern34 = re.compile('[A-Z]+?[a-z]+[A-Z][a-z]+[^\\s]*')
pattern35 = re.compile('[0-9]+.*has been deprecated')
#pattern32 = re.compile('[[][0-9][0-9]:[0-9][0-9] (?:(PM)|(AM))[]].*:')
pattern36 = re.compile('@[^\\s]*')
pattern37 = re.compile('[.][a-z]+[^\\s]*') #changed 06/12 20.14
pattern38 = re.compile('<[^\\s]*>')
pattern39 = re.compile('<[[].*[]]>')
pattern40 = re.compile('[[]disconnected.*[/][]]')
pattern41 = re.compile('[-][-][a-z]*')
pattern42 = re.compile('try.*{.*}')
pattern43 = re.compile('catch.*{.*}')
pattern44 = re.compile('{.*throw.*}')
pattern45 = re.compile('check.*{.*}')
pattern46 = re.compile('public void')
pattern47 = re.compile('private void')
pattern48 = re.compile('[[][[].*[]][]]')
pattern49 = re.compile('<.*[/]>')
pattern50 = re.compile('(?:a2p|ac|addgroup|adduser|agrep|alias|apropos|apt-cache|apt-get|aptitude|ar|arch|arp|as|aspell|at|awk|basename|bash|bc|bdiff|bfs|bg|biff|break|bs|bye|cal|calendar|cancel|cat|cc|cd|cfdisk|chdir|checkeq|checknr|chfn|chgrp|chkey|chmod|chown|chroot|chsh|cksum|clear|cmp|col|comm|compress|continue|cp|cpio|crontab|csh|csplit|ctags|cu|curl|cut|date|dc|dd|delgroup|deluser|depmod|deroff|df|dhclient|diff|dig|dircmp|dirname|dmesg|dos2unix|dpkg|dpost|du|echo|ed|edit|egrep|eject|elm|emacs|enable|env|eqn|ex|exit|expand|expr|fc|fdisk|fg|fgrep|file|find|findsmb|finger|fmt|fold|for|foreach|free|fsck|ftp|fuser|gawk|getfacl|gpasswd|gprof|grep|groupadd|groupdel|groupmod|gunzip|gview|gvim|gzip|halt|hash|hashstat|head|help|history|host|hostid|hostname|id|ifconfig|ifdown|ifquery|ifup|info|init|insmod|iostat|ip|isalist|iwconfig|jobs|join|keylogin|kill|killall|ksh|last|ld|ldd|less|lex|link|ln|lo|locate|login|logname|logout|losetup|lp|lpadmin|lpc|lpq|lpr|lprm|lpstat|ls|lsmod|lsof|lzcat|lzma|mach|mail|mailcompat|mailx|make|man|merge|mesg|mii-tool|mkdir|mkfs|mkswap|modinfo|modprobe|more|mount|mt|mv|myisamchk|mysql|mysqldump|nc|neqn|netstat|newalias|newform|newgrp|nice|niscat|nischmod|nischown|nischttl|nisdefaults|nisgrep|nismatch|nispasswd|nistbladm|nl|nmap|nohup|nroff|nslookup|od|on|onintr|optisa|pack|pagesize|parted|partprobe|passwd|paste|pax|pcat|perl|pg|pgrep|pico|pine|ping|pkill|poweroff|pr|printenv|printf|priocntl|ps|pstree|pvs|pwd|quit|rcp|readlink|reboot|red|rehash|rename|renice|repeat|replace|rgview rgvim|rlogin|rm|rmdir|rmmod|rn|route|rpcinfo|rsh|rsync|rview|rvim|s2p|sag|sar|scp|screen|script|sdiff|sed|sendmail|service|set|setenv|setfacl|sfdisk|sftp|sh|shred|shutdown|sleep|slogin|smbclient|sort|spell|split|startx|stat|stop|strftime|strip|stty|su|sudo|swapoff|swapon|sysklogd|tabs|tac|tail|talk|tar|tbl|tcopy|tcpdump|tcsh|tee|telinit|telnet|test|time|timex|todos|top|touch|tput|tr|traceroute|trap|tree|troff|tty|ul|umask|umount|unalias|uname|uncompress|unhash|uniq|unlink|unlzma|unpack|until|unxz|unzip|uptime|useradd|userdel|usermod|vacation|vgrind|vi|view|vim|vipw|visudo|vmstat|w|wait|wall|wc|wget|whatis|whereis|which|while|who|whoami|whois|write|X|Xorg|xargs|xfd|xhost|xinit|xlsfonts|xrdb|xset|xterm|xz|xzcat|yacc|yes|yppasswd|yum|zcat|zip|zipcloak|zipinfo|zipnote|zipsplit) -{1,2}\w+ \w*')
#add regex for deleting linux comand:
pattern51 = re.compile(r'\b(a2p|ac|addgroup|adduser|agrep|alias|apropos|apt-cache|apt-get|aptitude|ar|arch|arp|as|aspell|at|awk|basename|bash|bc|bdiff|bfs|bg|biff|break|bs|bye|cal|calendar|cat|cc|cd|cfdisk|chdir|checkeq|checknr|chfn|chgrp|chkey|chmod|chown|chroot|chsh|cksum|cmp|col|comm|compress|cp|cpio|crontab|csh|csplit|ctags|cu|curl|date|dc|dd|delgroup|deluser|depmod|deroff|df|dhclient|diff|dig|dircmp|dirname|dmesg|dos2unix|dpkg|dpost|du|echo|ed|egrep|eject|elm|emacs|env|eqn|ex|expr|fc|fdisk|fg|fgrep|findsmb|finger|fmt|foreach|fsck|ftp|fuser|gawk|getfacl|gpasswd|gprof|grep|groupadd|groupdel|groupmod|gunzip|gview|gvim|gzip|halt|hash|hashstat|hostid|ifconfig|ifdown|ifquery|ifup|init|insmod|iostat|ip|isalist|iwconfig|keylogin|kill|killall|ksh|last|ld|ldd|less|lex|link|ln|lo|logname|logout|losetup|lp|lpadmin|lpc|lpq|lpr|lprm|lpstat|ls|lsmod|lsof|lzcat|lzma|mach|mailcompat|mailx|mesg|miitool|mkdir|mkfs|mkswap|modinfo|modprobe|mount|mt|mv|myisamchk|mysqldump|nc|neqn|netstat|newalias|newform|newgrp|niscat|nischmod|nischown|nischttl|nisdefaults|nisgrep|nismatch|nispasswd|nistbladm|nl|nmap|nohup|nroff|nslookup|od|on|onintr|optisa|pack|pagesize|parted|partprobe|passwd|pax|pcat|perl|pg|pgrep|pico|pine|pkill|poweroff|pr|printenv|printf|priocntl|ps|pstree|pvs|pwd|rcp|readlink|red|rehash|renice|repeat|rgview|rgvim|rlogin|rm|rmdir|rmmod|rn|route|rpcinfo|rsh|rsync|rview|rvim|s2p|sag|sar|scp|sdiff|sed|sendmail|setenv|setfacl|sfdisk|sftp|sh|shred|slogin|smbclient|sort|spell|split|startx|stat|strftime|strip|stty|su|sudo|swapoff|swapon|sysklogd|tac|tar|tbl|tcopy|tcpdump|tcsh|tee|telinit|telnet|timex|todos|tput|tr|traceroute|trap|tree|troff|tty|ul|umask|umount|unalias|uname|uncompress|unhash|uniq|unlink|unlzma|unpack|until|unxz|unzip|uptime|useradd|userdel|usermod|vacation|vgrind|vi|vim|vipw|visudo|vmstat|w|wall|wc|wget|whatis|whereis|which|while|who|whoami|whois|X|Xorg|xargs|xfd|xhost|xinit|xlsfonts|xrdb|xset|xterm|xz|xzcat|yacc|yppasswd|yum|zcat|zip|zipcloak|zipinfo|zipnote|zipsplit)\b')
pattern52 = re.compile('(?:https|http)://\w*\S*\d*', re.DOTALL)
#pattern50 = re.compile(r'\(\d{2}:.*?\n', re.DOTALL)
pattern53 = re.compile('[^\\s]*[0-9][^\\s]*')
#pattern53_1 = re.compile('\\s[^a-zA-Z\\s]*[a-zA-Z]+[^a-zA-Z\\s]*.*\\s') #deleting all words with no-letters
pattern54 = re.compile('[^a-zA-Z\\s]+') #varsion with deleting words like doesn't i'll
pattern55 = re.compile('\\sPM\\s')
pattern56 = re.compile('\\sAM\\s')

#deleting java key-words
pattern57 = re.compile('(?:(\\sabstract\\s)|(\\sassert\\s))')
pattern58 = re.compile('(?:(\\sboolean\\s)|(\\sbreak\\s))')
pattern59 = re.compile('(?:(\\sbyte\\s)|(\\scase\\s))')
pattern60 = re.compile('(?:(\\scatch\\s)|(\\schar\\s))')
pattern61 = re.compile('(?:(\\sclass\\s)|(\\sconst\\s))')
pattern62 = re.compile('(?:(\\scontinue\\s)|(\\sdefault\\s))')
pattern63 = re.compile('(?:(\\sdo\\s)|(\\sdouble\\s))')
pattern64 = re.compile('(?:(\\selse\\s)|(\\senum\\s))')
pattern65 = re.compile('(?:(\\sfor\\s)|(\\sfloat\\s))')
pattern66 = re.compile('(?:(\\sgoto\\s)|(\\sif\\s))')
pattern67 = re.compile('(?:(\\sinstanceof\\s)|(\\sint\\s))')
pattern68 = re.compile('(?:(\\snew\\s)|(\\sprivate\\s))')
pattern69 = re.compile('(?:(\\sprotected\\s)|(\\spublic\\s))')
pattern70 = re.compile('(?:(\\sreturn\\s)|(\\sstatic\\s))')
pattern71 = re.compile('(?:(\\sstrictfp\\s)|(\\sswitch\\s))')
pattern72 = re.compile('(?:(\\sthis\\s)|(\\sthrow\\s))')
pattern73 = re.compile('(?:(\\sthrows\\s)|(\\stransient\\s))')
pattern74 = re.compile('(?:(\\stry\\s)|(\\svoid\\s))')
pattern75 = re.compile('(?:(\\svolatile\\s)|(\\swhile\\s))')
pattern76 = re.compile('(?:(\\strue\\s)|(\\sfalse\\s))')
pattern77 = re.compile('\\snull\\s')

pattern78 = re.compile('[a-zA-Z]+\'[a-zA-Z]+') #deleting words with ' symbol inside
pattern79 = re.compile('\\s[a-zA-Z]\\s') #deleting words from one symbol
pattern80 = re.compile('\\s[A-Z]+\\s') #deleting abbreviation
pattern81 = re.compile('.*undefined.*\\n.*undefined.*\\n.*undefined.*\\n.*undefined.*\\n.*undefined.*\\n') #215 in project 2
pattern82 = re.compile('relay.*undefined.*\\n.*transport.*\\n.*undefined.*\\n.*undefined') #215 in project 2
pattern83 = re.compile('drwxr xr.*') #458 project 2
pattern84 = re.compile('\\t\\t\\t\\t\\t\\soption.*\\n\\t\\t\\t\\t\\t\\soption.*\\n\\t\\t\\t\\t\\t\\soption.*\\n')
pattern85 = re.compile('\\t\\smodule option.*\\n\\t\\smodule option.*\\n\\t\\smodule option.*\\n')
pattern86 = re.compile('\\s\\sFailed to load module\\s\\s\\sextension.*\\n.*\\n\\s\\sFailed to load module\\s\\s\\sextension.*\\n.*\\n') #709 in project 2
pattern87 = re.compile('\\sdoes\\s')
pattern88 = re.compile('\\sdoesnt\\s')
pattern89 = re.compile('\\sive\\s')
pattern90 = re.compile('\\sdont\\s')
pattern91 = re.compile('\\shes\\s')
pattern92 = re.compile('\\sill\\s')
pattern93 = re.compile('\\sdid\\s')
pattern94 = re.compile('\\syoull\\s')
pattern95 = re.compile('\\sdoesn\\s')
pattern96 = re.compile('\\shaven\\s')
pattern97 = re.compile('\\sdon\\s')

#нужно добавить шаблонов
arr_patterns = [pattern0, pattern1, pattern2, pattern3, pattern4, 
                pattern5, pattern6, pattern7, pattern8, pattern9, pattern10,
                pattern11, pattern12, pattern13, pattern14,
                pattern15, pattern16, pattern17, pattern18, pattern19, pattern20, pattern21,
                pattern22, pattern23, pattern24, pattern25, pattern26, pattern27, pattern28,
                pattern29, pattern30, pattern31, pattern32, pattern33, pattern34, pattern35,
                pattern36, pattern37, pattern38, pattern39, pattern40, pattern41, pattern42,
                pattern43, pattern44, pattern45, pattern46, pattern47, pattern48, pattern49,
                pattern50, pattern51, pattern52, pattern53, pattern54, pattern55,
                pattern56, pattern57, pattern58, pattern59, pattern60, pattern61, pattern62,
                pattern63, pattern64, pattern65, pattern66, pattern67, pattern68, pattern69,
                pattern70, pattern71, pattern72, pattern73, pattern74, pattern75, pattern76,
                pattern77, pattern78, pattern79, pattern80, pattern81, pattern82, pattern83,
                pattern84, pattern85, pattern86, pattern87, pattern88, pattern89,
                pattern90, pattern91, pattern92, pattern93, pattern94, pattern95, pattern96,
                pattern97]

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
#   

    for k,item in enumerate(list_of_bugs_descriptions_and_stack_trace_flags):
        if k < 1:
            continue
        if k == 1:
##            print('|||||||||||||||||||||||||||||||||||||||||||')
##            print('|||||||||||||||||||||||||||||||||||||||||||')
##            print('|||||||||||||||||||||||||||||||||||||||||||')
##            print('|||||||||||||||||||||||||||||||||||||||||||')
##            print('|||||||||||||||||||||||||||||||||||||||||||')
##            print('|||||||||||||||||||||||||||||||||||||||||||')
##            print('|||||||||||||||||||||||||||||||||||||||||||')
##            print('|||||||||||||||||||||||||||||||||||||||||||')
##            print('|||||||||||||||||||||||||||||||||||||||||||')
##            print('|||||||||||||||||||||||||||||||||||||||||||')
            break
        print('//////////////////////////////////////////////////////////////////////////////')
        print('//////////////////////////////////////////////////////////////////////////////')
        print('//////////////////////////////////////////////////////////////////////////////')
        print('//////////////////////////////////////////////////////////////////////////////')
        print('|||||||||||NUMBER OF TEXT||||||||||||')
        print(k)
        print('|||||||||||NUMBER OF TEXT||||||||||||')
        print()
        text = item[0]
#        print('|||||||||||||||||||||||||||||||BEGIN TEXT with trash|||||||||||||||||||||||||||')
#        print(text)
#        print('|||||||||||||||||||||||||||||||END TEXT with trash|||||||||||||||||||||||||||')
#        print()
#        print()
        list_of_bugs_descriptions_and_stack_trace_flags[k] = filter_pattern(arr_patterns, text)  
        
    list_of_all_projects_cleaned_bugs_descriptions_with_stack_trace_flags = list_of_all_projects_cleaned_bugs_descriptions_with_stack_trace_flags + list_of_bugs_descriptions_and_stack_trace_flags
#    print('-------------------THIS IS THE END-----------------------')
    str_for_print = 'Number of descriptions in %d project: ' % i
    print(str_for_print)
    print(len(list_of_bugs_descriptions_and_stack_trace_flags))


#print(list_of_all_projects_cleaned_bugs_descriptions_with_stack_trace_flags)
print('Number of all descriptions: ')
print(len(list_of_all_projects_cleaned_bugs_descriptions_with_stack_trace_flags))
#print(list_of_all_projects_cleaned_bugs_descriptions_with_stack_trace_flags)

#stem function
def stem(tokens, stop_words):
    #different stemm algorithms
    stemming_algorithms = {
    "stemmer1" : SnowballStemmer("english"),
    "stemmer2" : StemmerI,
    "stemmer3" : RegexpStemmer,
    "stemmer4" : LancasterStemmer,
    "stemmer5" : ISRIStemmer,
    "stemmer6" : PorterStemmer,
    "stemmer7" : SnowballStemmer,
    "stemmer8" : WordNetLemmatizer,
    "stemmer9" : RSLPStemmer}
    tokens = [stemming_algorithms['stemmer1'].stem(token) for token in tokens if (token not in stop_words)] 
    return tokens 
    
#lemmatize function   
def lem(tokens, stop_words):
    lmtzr = WordNetLemmatizer()
    tokens = [lmtzr.lemmatize(token) for token in tokens if (token not in stop_words)] 
    return tokens

#return tokens without stop words
def get_tokens(file_text):
    #cleaning words, making lowercase and tokenization
    tokens = list()
    #this regex find all words without symbols and numbers (,:. in the end of word and * at the beggining/end is an exception)
    #* - is a header tag in Jira (*... ... ...*)
    pattern = re.compile(r'^\*?([a-zA-Z]{2,15})(?:|\.|\:|\,)\*?$')
    tokens = [pattern.findall(i)[0].lower() for i in file_text.split() if (len(pattern.findall(i))>0)]
    #deleting stop_words and linux command
    variants_of_stopwords = {
    '429': ['a', 'about', 'above', 'across', 'after', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'among', 'an', 'and', 'another', 'any', 'anybody', 'anyone', 'anything', 'anywhere', 'are', 'area', 'areas', 'around', 'as', 'ask', 'asked', 'asking', 'asks', 'at', 'away', 'b', 'back', 'backed', 'backing', 'backs', 'be', 'became', 'because', 'become', 'becomes', 'been', 'before', 'began', 'behind', 'being', 'beings', 'best', 'better', 'between', 'big', 'both', 'but', 'by', 'c', 'came', 'can', 'cannot', 'case', 'cases', 'certain', 'certainly', 'clear', 'clearly', 'come', 'could', 'd', 'did', 'differ', 'different', 'differently', 'do', 'does', 'done', 'down', 'down', 'downed', 'downing', 'downs', 'during', 'e', 'each', 'early', 'either', 'end', 'ended', 'ending', 'ends', 'enough', 'even', 'evenly', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'f', 'face', 'faces', 'fact', 'facts', 'far', 'felt', 'few', 'find', 'finds', 'first', 'for', 'four', 'from', 'full', 'fully', 'further', 'furthered', 'furthering', 'furthers', 'g', 'gave', 'general', 'generally', 'get', 'gets', 'give', 'given', 'gives', 'go', 'going', 'good', 'goods', 'got', 'great', 'greater', 'greatest', 'group', 'grouped', 'grouping', 'groups', 'h', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 'herself', 'high', 'high', 'high', 'higher', 'highest', 'him', 'himself', 'his', 'how', 'however', 'i', 'if', 'important', 'in', 'interest', 'interested', 'interesting', 'interests', 'into', 'is', 'it', 'its', 'itself', 'j', 'just', 'k', 'keep', 'keeps', 'kind', 'knew', 'know', 'known', 'knows', 'l', 'large', 'largely', 'last', 'later', 'latest', 'least', 'less', 'let', 'lets', 'like', 'likely', 'long', 'longer', 'longest', 'm', 'made', 'make', 'making', 'man', 'many', 'may', 'me', 'member', 'members', 'men', 'might', 'more', 'most', 'mostly', 'mr', 'mrs', 'much', 'must', 'my', 'myself', 'n', 'necessary', 'need', 'needed', 'needing', 'needs', 'never', 'new', 'new', 'newer', 'newest', 'next', 'no', 'nobody', 'non', 'noone', 'not', 'nothing', 'now', 'nowhere', 'number', 'numbers', 'o', 'of', 'off', 'often', 'old', 'older', 'oldest', 'on', 'once', 'one', 'only', 'open', 'opened', 'opening', 'opens', 'or', 'order', 'ordered', 'ordering', 'orders', 'other', 'others', 'our', 'out', 'over', 'p', 'part', 'parted', 'parting', 'parts', 'per', 'perhaps', 'place', 'places', 'point', 'pointed', 'pointing', 'points', 'possible', 'present', 'presented', 'presenting', 'presents', 'problem', 'problems', 'put', 'puts', 'q', 'quite', 'r', 'rather', 'really', 'right', 'right', 'room', 'rooms', 's', 'said', 'same', 'saw', 'say', 'says', 'second', 'seconds', 'see', 'seem', 'seemed', 'seeming', 'seems', 'sees', 'several', 'shall', 'she', 'should', 'show', 'showed', 'showing', 'shows', 'side', 'sides', 'since', 'small', 'smaller', 'smallest', 'so', 'some', 'somebody', 'someone', 'something', 'somewhere', 'state', 'states', 'still', 'still', 'such', 'sure', 't', 'take', 'taken', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'therefore', 'these', 'they', 'thing', 'things', 'think', 'thinks', 'this', 'those', 'though', 'thought', 'thoughts', 'three', 'through', 'thus', 'to', 'today', 'together', 'too', 'took', 'toward', 'turn', 'turned', 'turning', 'turns', 'two', 'u', 'under', 'until', 'up', 'upon', 'us', 'use', 'used', 'uses', 'v', 'very', 'w', 'want', 'wanted', 'wanting', 'wants', 'was', 'way', 'ways', 'we', 'well', 'wells', 'went', 'were', 'what', 'when', 'where', 'whether', 'which', 'while', 'who', 'whole', 'whose', 'why', 'will', 'with', 'within', 'without', 'work', 'worked', 'working', 'works', 'would', 'x', 'y', 'year', 'years', 'yet', 'you', 'young', 'younger', 'youngest', 'your', 'yours', 'z'],
    '319': ['a', 'about', 'above', 'across', 'after', 'afterwards', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'amoungst', 'amount', 'an', 'and', 'another', 'any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere', 'are', 'around', 'as', 'at', 'back', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'below', 'beside', 'besides', 'between', 'beyond', 'bill', 'both', 'bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant', 'co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de', 'describe', 'detail', 'do', 'done', 'down', 'due', 'during', 'each', 'eg', 'eight', 'either', 'eleven', 'else', 'elsewhere', 'empty', 'enough', 'etc', 'even', 'ever', 'every', 'everyone', 'everything', 'everywhere', 'except', 'few', 'fifteen', 'fify', 'fill', 'find', 'fire', 'first', 'five', 'for', 'former', 'formerly', 'forty', 'found', 'four', 'from', 'front', 'full', 'further', 'get', 'give', 'go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herse"', 'him', 'himse"', 'his', 'how', 'however', 'hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed', 'interest', 'into', 'is', 'it', 'its', 'itse"', 'keep', 'last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made', 'many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine', 'more', 'moreover', 'most', 'mostly', 'move', 'much', 'must', 'my', 'myse"', 'name', 'namely', 'neither', 'never', 'nevertheless', 'next', 'nine', 'no', 'nobody', 'none', 'noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of', 'off', 'often', 'on', 'once', 'one', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'part', 'per', 'perhaps', 'please', 'put', 'rather', 're', 'same', 'see', 'seem', 'seemed', 'seeming', 'seems', 'serious', 'several', 'she', 'should', 'show', 'side', 'since', 'sincere', 'six', 'sixty', 'so', 'some', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhere', 'still', 'such', 'system', 'take', 'ten', 'than', 'that', 'the', 'their', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'therefore', 'therein', 'thereupon', 'these', 'they', 'thick', 'thin', 'third', 'this', 'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'top', 'toward', 'towards', 'twelve', 'twenty', 'two', 'un', 'under', 'until', 'up', 'upon', 'us', 'very', 'via', 'was', 'we', 'well', 'were', 'what', 'whatever', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who', 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with', 'within', 'without', 'would', 'yet', 'you', 'your', 'yours', 'yourself', 'yourselves'],
    '667': ['a', 'able', 'about', 'above', 'abst', 'accordance', 'according', 'accordingly', 'across', 'act', 'actually', 'added', 'adj', 'affected', 'affecting', 'affects', 'after', 'afterwards', 'again', 'against', 'ah', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'an', 'and', 'announce', 'another', 'any', 'anybody', 'anyhow', 'anymore', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apparently', 'approximately', 'are', 'aren', 'arent', 'arise', 'around', 'as', 'aside', 'ask', 'asking', 'at', 'auth', 'available', 'away', 'awfully', 'b', 'back', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'begin', 'beginning', 'beginnings', 'begins', 'behind', 'being', 'believe', 'below', 'beside', 'besides', 'between', 'beyond', 'biol', 'both', 'brief', 'briefly', 'but', 'by', 'c', 'ca', 'came', 'can', 'cannot', "can't", 'cause', 'causes', 'certain', 'certainly', 'co', 'com', 'come', 'comes', 'contain', 'containing', 'contains', 'could', 'couldnt', 'd', 'date', 'did', "didn't", 'different', 'do', 'does', "doesn't", 'doing', 'done', "don't", 'down', 'downwards', 'due', 'during', 'e', 'each', 'ed', 'edu', 'effect', 'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end', 'ending', 'enough', 'especially', 'et', 'et-al', 'etc', 'even', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'except', 'f', 'far', 'few', 'ff', 'fifth', 'first', 'five', 'fix', 'followed', 'following', 'follows', 'for', 'former', 'formerly', 'forth', 'found', 'four', 'from', 'further', 'furthermore', 'g', 'gave', 'get', 'gets', 'getting', 'give', 'given', 'gives', 'giving', 'go', 'goes', 'gone', 'got', 'gotten', 'h', 'had', 'happens', 'hardly', 'has', "hasn't", 'have', "haven't", 'having', 'he', 'hed', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes', 'hi', 'hid', 'him', 'himself', 'his', 'hither', 'home', 'how', 'howbeit', 'however', 'hundred', 'i', 'id', 'ie', 'if', "i'll", 'im', 'immediate', 'immediately', 'importance', 'important', 'in', 'inc', 'indeed', 'index', 'information', 'instead', 'into', 'invention', 'inward', 'is', "isn't", 'it', 'itd', "it'll", 'its', 'itself', "i've", 'j', 'just', 'k', 'keep', 'keeps', 'kept', 'kg', 'km', 'know', 'known', 'knows', 'l', 'largely', 'last', 'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', 'lets', 'like', 'liked', 'likely', 'line', 'little', "'ll", 'look', 'looking', 'looks', 'ltd', 'm', 'made', 'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'me', 'mean', 'means', 'meantime', 'meanwhile', 'merely', 'mg', 'might', 'million', 'miss', 'ml', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs', 'much', 'mug', 'must', 'my', 'myself', 'n', 'na', 'name', 'namely', 'nay', 'nd', 'near', 'nearly', 'necessarily', 'necessary', 'need', 'needs', 'neither', 'never', 'nevertheless', 'new', 'next', 'nine', 'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone', 'nor', 'normally', 'nos', 'not', 'noted', 'nothing', 'now', 'nowhere', 'o', 'obtain', 'obtained', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'omitted', 'on', 'once', 'one', 'ones', 'only', 'onto', 'or', 'ord', 'other', 'others', 'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'owing', 'own', 'p', 'page', 'pages', 'part', 'particular', 'particularly', 'past', 'per', 'perhaps', 'placed', 'please', 'plus', 'poorly', 'possible', 'possibly', 'potentially', 'pp', 'predominantly', 'present', 'previously', 'primarily', 'probably', 'promptly', 'proud', 'provides', 'put', 'q', 'que', 'quickly', 'quite', 'qv', 'r', 'ran', 'rather', 'rd', 're', 'readily', 'really', 'recent', 'recently', 'ref', 'refs', 'regarding', 'regardless', 'regards', 'related', 'relatively', 'research', 'respectively', 'resulted', 'resulting', 'results', 'right', 'run', 's', 'said', 'same', 'saw', 'say', 'saying', 'says', 'sec', 'section', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sent', 'seven', 'several', 'shall', 'she', 'shed', "she'll", 'shes', 'should', "shouldn't", 'show', 'showed', 'shown', 'showns', 'shows', 'significant', 'significantly', 'similar', 'similarly', 'since', 'six', 'slightly', 'so', 'some', 'somebody', 'somehow', 'someone', 'somethan', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specifically', 'specified', 'specify', 'specifying', 'still', 'stop', 'strongly', 'sub', 'substantially', 'successfully', 'such', 'sufficiently', 'suggest', 'sup', 'sure', 't', 'take', 'taken', 'taking', 'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', "that'll", 'thats', "that've", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'thered', 'therefore', 'therein', "there'll", 'thereof', 'therere', 'theres', 'thereto', 'thereupon', "there've", 'these', 'they', 'theyd', "they'll", 'theyre', "they've", 'think', 'this', 'those', 'thou', 'though', 'thoughh', 'thousand', 'throug', 'through', 'throughout', 'thru', 'thus', 'til', 'tip', 'to', 'together', 'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', 'ts', 'twice', 'two', 'u', 'un', 'under', 'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up', 'upon', 'ups', 'us', 'use', 'used', 'useful', 'usefully', 'usefulness', 'uses', 'using', 'usually', 'v', 'value', 'various', "'ve", 'very', 'via', 'viz', 'vol', 'vols', 'vs', 'w', 'want', 'wants', 'was', 'wasnt', 'way', 'we', 'wed', 'welcome', "we'll", 'went', 'were', 'werent', "we've", 'what', 'whatever', "what'll", 'whats', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whim', 'whither', 'who', 'whod', 'whoever', 'whole', "who'll", 'whom', 'whomever', 'whos', 'whose', 'why', 'widely', 'willing', 'wish', 'with', 'within', 'without', 'wont', 'words', 'world', 'would', 'wouldnt', 'www', 'x', 'y', 'yes', 'yet', 'you', 'youd', "you'll", 'your', 'youre', 'yours', 'yourself', 'yourselves', "you've", 'z', 'zero'],
    '167': stopwords.words('english')
    }
    try:
        stop_words = variants_of_stopwords['319']
    except KeyError as e:
        raise ValueError('Undefined unit: {}'.format(e.args[1]))
    #call stem or lem function
    stem_or_lem = {
    "stem" : lem(tokens, stop_words),
    "lem" : stem(tokens, stop_words)                
    }
    tokens = stem_or_lem["lem"]
    return tokens 

#return bigrams
def get_bigrams(file_text):
    tokens = get_tokens(file_text)
    return list(ngrams(tokens,2))

#call tokenazation (and bigram) function with text of bug description as a parametr              
list_tokens_with_stack_trace_flag = [[get_tokens(x[0]),x[1]] for x in list_of_all_projects_cleaned_bugs_descriptions_with_stack_trace_flags ]
list_bigrams_with_stack_trace_flag = [[get_bigrams(x[0]),x[1]] for x in list_of_all_projects_cleaned_bugs_descriptions_with_stack_trace_flags ] 

                                       
#print('---------num of tokens-----------')
#print(len(list_tokens_with_stack_trace_flag))   
#print('---------num of bigrams-----------')                                   
#print(len(list_bigrams_with_stack_trace_flag))                                       
                                       
#Saving tokens in text file
thefile_words = open('F:\\mygit\\words.txt', 'w', encoding='utf-8')
for item in list_tokens_with_stack_trace_flag:
    temp_str = ', '.join(item[0])
    thefile_words.write("%r\n" % temp_str)
    thefile_words.write("%s\n" % str(item[1]))
thefile_words.close()
#Saving bigrams in text file
thefile_bigrams = open('F:\\mygit\\bigrams.txt', 'w', encoding='utf-8')
for item in list_bigrams_with_stack_trace_flag:
    my_str = ' '
    for x in item[0]:
        temp_str = ' / '.join(x)
        my_str = my_str + ' , ' + temp_str
    thefile_bigrams.write("%r\n" % my_str)
    thefile_bigrams.write("%s\n" % str(item[1]))
thefile_bigrams.close()


corpus = list() #array with strings
for item in list_tokens_with_stack_trace_flag:
    temp_str = ' '.join(item[0])
    corpus.append(temp_str)

from sklearn.feature_extraction.text import CountVectorizer
bigram_vectorizer = CountVectorizer(ngram_range=(1, 2))
X = bigram_vectorizer.fit_transform(corpus)
#print(len(bigram_vectorizer.get_feature_names()))

from sklearn.feature_extraction.text import TfidfTransformer
transformer = TfidfTransformer(smooth_idf=True)
tfidf = transformer.fit_transform(X)

#228-241 must be commented!!!




