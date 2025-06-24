#!/bin/bash

echo "🚀 Installing Blackice Firewall & Scanner..."

# Make sure required packages are installed
pkg update -y
pkg install -y python git
pip install termcolor

# Clone the project if it doesn't exist
mkdir -p ~/termux-firewall
cd ~/termux-firewall

if [ ! -d "Blackice-fw" ]; then
    git clone https://github.com/warlocksoo1/Blackice-fw.git
fi

# === Setup CLI Aliases ===

# Alias for firewall
ALIAS_CMD="alias firewall='python ~/termux-firewall/Blackice-fw/firewall.py'"
grep -qxF "$ALIAS_CMD" ~/.bashrc || echo "$ALIAS_CMD" >> ~/.bashrc

# Alias for scanner
SCANNER_ALIAS="alias scanner='python ~/termux-firewall/Blackice-fw/scanner.py'"
grep -qxF "$SCANNER_ALIAS" ~/.bashrc || echo "$SCANNER_ALIAS" >> ~/.bashrc

# Source .bashrc so aliases work immediately
source ~/.bashrc

# Create default rules file if not found
if [ ! -f ~/termux-firewall/Blackice-fw/rules.json ]; then
    echo '[80, 443]' > ~/termux-firewall/Blackice-fw/rules.json
fi

echo ""
echo "✅ Blackice Firewall & Scanner installed!"
echo "🛡️  Use: firewall --test"
echo "🔍 Use: scanner 8.8.8.8 --start 80 --end 100"
