
import commands

filename = "C:\Python_programs\IGWMNDSE.txt"
string_to_search = "PDM"

extract  = (commands.getstatusoutput("grep -C 10 '%s' %s"%(string_to_search,filename)))[1]

print(extract)
