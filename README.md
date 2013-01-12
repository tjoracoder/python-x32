python-x32
==========

Python library to interact with Behringer X32 digital mixing desk using OSC-messages (open sound control).

The Behringer X32 has quite good documentation of OSC-messages, but not all messages are documented. Messages that control what 
page the user has selected on the desk are not documented.

See http://www.behringer.com/EN/Products/X32.aspx

Using dumpmessages.py is quite easy to find some undocumented OSC-messages. 
Messages can also be captured by Wireshark and XControl, but using dumpmessages.py is easier.

Undocumented messages
---------------------

This is just a listing of some undocumented messages. Most undocumented messages start with /-

/xremote

Used by the Behringer Windows-application XRemote to instruct the Behringer X32 to send all state changes to allow
XRemote to follow all user selections.

-stat prefix is used to signal gui-things, like what fader layer is selected or the screen visible

OSCMessage("/-stat/chfaderbank", [0]): What main channel fader bank is selected
 - 0: CH 1-16
 - 1: CH 17-32
 - 2: Aux in /USB / FX returns
 - 3: Bus masters
 
 OSCMessage("/-stat/grpfaderbank", [0]): Group channel bank selected
  - 0: DCA 1-8
  - 1: BUS 1-8
  - 2: BUS 9-16
  - 3: Matrix 1-6, Main C
  
OSCMessage("/-stat/selidx", [0]): Select channel index
 - 0-31 Ch 1-32
 - 32-63 Ch 33-64
 - 64-47: Aux in /USB
 - 48-63: Bus master
 - 64-69: Matrix 1-6
 - 70: L/R
 - 71: Mono/Center

OSCMessage("/-stat/solosw/01", [0]): 0/1 Is on/off of soloswitch
 - 01: Same id as used for selidx, but +1
 
OSCMessage("/-show/show/A/003/name", ['AAAAA']): Name of a show

OSCMessage("/-stat/screen/screen", [0]): Set active screen, eg. Home, Meters, Routing, Setup, Library

OSCMessage("/-stat/screen/screen", [6]): Monitor page (Monitor, talkback A, B and Osc)

OSCMessage("/-stat/screen/screen", [8]): Scene configuration screen

OSCMessage("/-stat/screen/screen", [9]): User bank configuration screen

OSCMessage("/-stat/screen/CHAN/page", [0]): Select channel page in "Home"-screen

OSCMessage("/-stat/screen/METER/page", [0]): Select meter page

OSCMessage("/-stat/screen/ROUTE/page", [1]): Routing page

OSCMessage("/-stat/screen/SETUP/page", [1])

OSCMessage("/-stat/screen/LIB/page", [0])

OSCMessage("/-stat/screen/FX/page", [1])

OSCMessage("/-stat/screen/mutegrp", [0]):
 - 0: Turn off mutegrp screen
 - 1: Turn on mutegrp screen

OSCMessage("/-stat/screen/utils", [0]): 
 - 0: Turn off utils screen
 - 1: Turn on utils screen

OSCMessage("/-stat/userbank", [0]):
 - 0: User bank A
 - 1: User bank B
 - 2: User bank C
 


