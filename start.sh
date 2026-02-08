#!/bin/bash

# GOD v1.0.0 - Linux/Mac Server Launcher

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
PURPLE='\033[0;35m'
NC='\033[0m'

echo ""
echo "===================================================================="
echo -e "${PURPLE}   GOD v1.0.0 - Starting Server${NC}"
echo "===================================================================="
echo ""

if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo -e "${RED}[ERROR] Python is not installed!${NC}"
    echo ""
    echo "Please install Python 3:"
    echo "  Ubuntu/Debian: sudo apt install python3"
    echo "  macOS: brew install python3"
    echo ""
    exit 1
fi

PYTHON_CMD=$(command -v python3 || command -v python)

echo -e "${GREEN}[OK] Python found!${NC}"
echo ""

if [ ! -f "index.html" ]; then
    echo -e "${RED}[ERROR] index.html not found!${NC}"
    echo "Make sure you're running this from the GOD v1.0.0 folder"
    echo ""
    exit 1
fi

echo -e "${GREEN}[OK] Files found!${NC}"
echo ""
echo "Starting server..."
echo ""

$PYTHON_CMD server.py
