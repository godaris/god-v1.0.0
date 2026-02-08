#!/usr/bin/env python3
"""
GOD v1.0.0 - Development Server
Professional local development server with auto-reload and enhanced features
"""

import http.server
import socketserver
import webbrowser
import socket
import os
import sys
from pathlib import Path

PORT = 8000
HOST = "localhost"
DIRECTORY = Path(__file__).parent

class GODHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Enhanced HTTP request handler with better MIME types and CORS"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)
    
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()
    
    def log_message(self, format, *args):
        message = format % args
        if '200' in message:
            print(f"\033[92m✓\033[0m {message}")
        elif '404' in message:
            print(f"\033[91m✗\033[0m {message}")
        else:
            print(f"\033[94mℹ\033[0m {message}")

def get_local_ip():
    """Get local IP address for network access"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def find_available_port(start_port=8000):
    """Find an available port"""
    for port in range(start_port, start_port + 10):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((HOST, port))
                return port
        except OSError:
            continue
    return None

def print_banner(port):
    """Print startup banner"""
    print("\n" + "="*70)
    print("\033[95m")
    print("   _____ ____  _____   ")
    print("  / ____|  _ \\|  __ \\  ")
    print(" | |  __| |_) | |  | | ")
    print(" | | |_ |  _ <| |  | | ")
    print(" | |__| | |_) | |__| | ")
    print("  \\_____|____/|_____/  ")
    print("\033[0m")
    print("  v1.0.0 - Professional AI Assistant")
    print("="*70)
    print(f"\n\033[92m✓ Server is running!\033[0m\n")
    print(f"  🌐 Local:   \033[96mhttp://localhost:{port}\033[0m")
    print(f"  🌐 Network: \033[96mhttp://{get_local_ip()}:{port}\033[0m")
    print(f"\n  📁 Serving: {DIRECTORY}")
    print(f"\n  \033[93m⌨  Press Ctrl+C to stop\033[0m\n")
    print("="*70 + "\n")

def check_files():
    """Check if required files exist"""
    required_files = ['index.html', 'styles.css', 'app.js']
    missing = []
    
    for file in required_files:
        if not (DIRECTORY / file).exists():
            missing.append(file)
    
    if missing:
        print(f"\n\033[91m⚠ Warning: Missing files:\033[0m")
        for file in missing:
            print(f"  ✗ {file}")
        print(f"\n\033[93mMake sure you're in the correct directory!\033[0m\n")
        return False
    return True

def main():
    """Start the server"""
    try:
        if not check_files():
            sys.exit(1)
        
        port = find_available_port(PORT)
        if port is None:
            print(f"\033[91m✗ Error: No available ports found!\033[0m")
            sys.exit(1)
        
        with socketserver.TCPServer((HOST, port), GODHTTPRequestHandler) as httpd:
            print_banner(port)
            
            try:
                webbrowser.open(f'http://localhost:{port}')
                print("✓ Browser opened automatically\n")
            except:
                print("⚠ Could not open browser automatically")
                print(f"  Please open: http://localhost:{port}\n")
            
            print("Server logs:\n")
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\n" + "="*70)
        print("\033[93m⏹  Server stopped\033[0m")
        print("="*70 + "\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n\033[91m✗ Error: {e}\033[0m\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
