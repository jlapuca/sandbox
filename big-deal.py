#!/usr/bin/python
#-*- coding: utf-8 -*-

# Итак наша задача.
# Составить таблицу из двух столбцов:
# входящий номер:номер на который идет редирект (или не номер а ivr какой-нибудь)

# Примечание: если это внутренний четырехзначный экстеншен то находить его в файле 'users.conf'
# и вытаскивать имя, записи в 'users.conf' хранятся в таком виде:
# [3301](dub,c7942)
# fullname = John Kennedy
# email = John.Kennedy@mail.ru
# callerid = "John Kennedy" <3301>
# Определить, что это внутренний четырехзначный экстеншен можно по следующим признакам:
# 1) ...

# Эту ценную информацию мы можем почерпнуть из конфигурационного файла extensions.conf
# среди директив: exten => bla-bla-bla

# Типы директив:
# 1) exten => 01900000,1,Macro(internalq-calls,3301,vm)
# входящий номер = 01900000
# редирект на номер = 3301
# 2) exten => 3290000,1,Dial(Local/2100@internal-lookup)
# входящий номер =
# редирект на номер =
# 3) exten => 458000,1,Dial(SIP/lync/+781240000)
# входящий номер =
# редирект на номер =
# 4) exten => 6110000,1,Dial(SIP/2202)
# входящий номер =
# редирект на номер =
# 5) exten => 6110001,1,Goto(rusivr,s,1)
# входящий номер =
# редирект на номер =
# 6) exten=> 00063000,1,Set(CHANNEL(language)=ru)
#    same => n,Set(CALLERID(all)="RU" <${CALLERID(num)}>)
#    same => n,Goto(supportivr,s,1)
# входящий номер =
# редирект на номер =
# 7) exten => 006126100000,1,Queue(2110)
# входящий номер =
# редирект на номер =
# 8) exten => 0061260000,1,Macro(internalcalls,2100)
# входящий номер =
# редирект на номер =

# если для одного внутреннего четырехзначного номера больше одного входящего ->  новый столбик?
# формат выходного файла : NAME : ext : DID1 : DID2 : DID3 : ...
#


