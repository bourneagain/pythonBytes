def sol(file_name):
    
    """
    
    Jan 20 03:25:08 fakehost logrotate: ALERT exited abnormally with [1]
    Jan 20 03:25:08 fakehost run-parts(/etc/cron.daily)[20447]: finished logrotate
    Jan 20 03:26:21 fakehost anacron[28969]: Job 'cron.daily' terminated
    
    
    Jan 20 03:30:01 fakehost CROND[31461]: (root) CMD (/var/system/bin/sys-cmd -F > /dev/null 2>&1)
    Jan 20 05:03:03 fakehost ntpd[3705]: synchronized to time.faux.biz, stratum 2
    Jan 20 05:20:01 fakehost rsyslogd: [origin software="rsyslogd" swVersion="5.8.10" x-pid="20438" x-                info="http://www.rsyslog.com"] start
    
    minute,total_count,rsyslogd,cs3,ACCT_ADD
    Jan 20 05:20,1,1,0,0
    Jan 20 05:22,6,0,5,1 

    """
    op_dict={}
    with open(file_name) as f:
        for lines in f:
            line_list=lines.split(' ')
            _str=' '.join(line_list[:3])
            #_str=Jan 20 03:26:<sec>
            _str=':'.join(_str.split(':')[:2])
            text=' '.join(line_list[4:])
            text=text.split(':')
            
            if len(text.split('(') > 1:
                process_name=text.split('(')[0]
            elif len(text.split['[']) > 1:
                     process_name=text.split('[')[0]
            else:
                process_name=text
                    
                    
            if _str not in op_dict:
                op_dict[_str]
            else:
                op_dict[_str]+=1
     
     print "minute, number_of_messages"
     for key,values in op_dict.iteritems():
         print key+","+values


            
