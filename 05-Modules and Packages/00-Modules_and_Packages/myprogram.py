from MyMainPackage.some_main_script import report_main
report_main()


from MyMainPackage.SubPackage import mysubscript
mysubscript.sub_report()


from MyMainPackage.SubPackage.mysubscript import sub_report
sub_report()


from MyMainPackage.SubPackage.mysubscript import *
sub_report()




