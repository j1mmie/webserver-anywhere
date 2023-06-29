#!/usr/bin/env python3
# Drop this in /usr/local/bin, and chmod o+x
#
# Usage:
#   webserver # Starts a webserver in the current directory on port 8000
#   webserver --port 9090 --path dist # Webserver on port 9090 serving content out of ./dist


from http.server import HTTPServer, SimpleHTTPRequestHandler, test
import sys
import argparse

class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

def main():
    parser=argparse.ArgumentParser()

    parser.add_argument("--port", help="Port to run the webserver on (default 8000)", default=8000)
    parser.add_argument("--path", help="Path to serve documents from (default .)", default=".")

    args=parser.parse_args()

    print(f"Args: {vars(args)}")

    test(CORSRequestHandler, HTTPServer, port=int(args.port))

if __name__ == '__main__':
    main()
