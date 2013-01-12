"""

This software is licensed under the Modified BSD License:

Copyright (c) 2013, Sigve Tjora
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the <organization> nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import OSC
import time
import threading

def request_x32_to_send_change_notifications(client):
    """request_x32_to_send_change_notifications sends /xremote repeatedly to
    mixing desk to make sure changes are transmitted to our server.
    """
    while True:
        client.send(OSC.OSCMessage("/xremote"))
        time.sleep(7)

def print_all_x32_change_messages(x32_address, server_udp_port, filename):
    if filename is not None:
        outputfile = open(filename, "wt")
    else:
        outputfile = None

    def msgPrinter_handler(addr, tags, data, client_address):
        txt = 'OSCMessage("%s", %s)' % (addr, data)
        print txt
        if outputfile is not None:
            outputfile.write(txt+"\n")

    server = OSC.OSCServer(("", server_udp_port))
    server.addMsgHandler("default", msgPrinter_handler)
    client = OSC.OSCClient(server=server) #This makes sure that client and server uses same socket. This has to be this way, as the X32 sends notifications back to same port as the /xremote message came from
    
    client.connect((x32_address, 10023))
    
    thread = threading.Thread(target=request_x32_to_send_change_notifications, kwargs = {"client": client})
    thread.start()
    server.serve_forever()

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Dump all change/state messages from Behringer X32 mixing desk. This tool can be used to find undocumented messages.")
    parser.add_argument('--address', required = True,                        
                        help='name/ip-address of Behringer X32 mixing desk')
    parser.add_argument('--filename', default = None,                         
                        help='File to write all messages to.')
    parser.add_argument('--port', default = 10300,                        
                        help='UDP-port to open on this machine.')

    args = parser.parse_args()
    print_all_x32_change_messages(x32_address = args.address, server_udp_port = args.port, filename = args.filename)
    