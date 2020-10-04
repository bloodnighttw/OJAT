# ~/.local/bin
echo "[+]ojat setup script[+]"
echo "[-]Removing old file[-]"
rm ~/.local/bin/argcc
rm ~/.local/bin/ojatlib.py
echo "[+]copying new file [+]"
cp ojatlib.py ~/.local/bin
cp atgcc.py ~/.local/bin

mv ~/.local/bin/atgcc.py ~/.local/bin/atgcc

chmod 777 ~/.local/bin/atgcc
chmod 777 ~/.local/bin/ojatlib.py
echo "DONE!"
