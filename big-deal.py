#!/usr/bin/python
#-*- coding: utf-8 -*-

# Итак наша задача.
# Составить таблицу из двух столбцов:
# входящий номер:номер на который идет редирект (или не номер а ivr какой-нибудь)
# если это внутренний четырехзначный экстеншен то находить его в файле 'users.conf'
# и вытаскивать имя, записи в 'users.conf' хранятся в таком виде:
# [3301](dub,c7942)
# fullname = John Kennedy
# email = John.Kennedy@mail.ru
# callerid = "John Kennedy" <3301>
#
# Информацию о входящих номерах мы можем почерпнуть из конфигурационного файла XXXX.conf среди директив:
# exten => bla-bla-bla
# в части файла ограниченного
# [incoming]
# ....
# [название другого контекста]

# Типы директив:
# 1) exten => 01900000,1,Macro(internalq-calls,3301,vm)
# входящий номер = 01900000
# редирект на номер = 3301
# 2) exten => 3294432,1,Dial(Local/2188@internal-lookup)
#
#
# 3) exten => 4588786,1,Dial(SIP/lync/+78124588786)
#
#
# 4) exten => 6110034,1,Dial(SIP/2202)
#
#
# 5) exten => 6110035,1,Goto(rusivr,s,1)
#
#
# 6) exten=> 00063305,1,Set(CHANNEL(language)=ru)
#    same => n,Set(CALLERID(all)="RU" <${CALLERID(num)}>)
#    same => n,Goto(supportivr,s,1)
#
#
# 7) exten => 0061261084359,1,Queue(2110)
#
#
# 8) exten => 0061261084360,1,Macro(internalcalls,2138)
#
#


