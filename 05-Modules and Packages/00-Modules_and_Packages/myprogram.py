from MyMainPackage.some_main_script import report_main
from MyMainPackage.SubPackage import mysubscript

from MyMainPackage.SubPackage.mysubscript import *
sub_report()


report_main()

mysubscript.sub_report()

