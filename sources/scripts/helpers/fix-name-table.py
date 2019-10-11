import argparse
from fontTools import ttLib
from fontTools.ttLib.tables._n_a_m_e import NameRecord

description = 'path to ttf file'
parser = argparse.ArgumentParser(description=description)
parser.add_argument('ttf_font', help="Font in OpenType (TTF) format")

def main():
    args = parser.parse_args()
    font = ttLib.TTFont(args.ttf_font)

    print('[INFO] Fixing name table...')
    #print(font)
    #print(font['name'])
    #nameTable = font['name'].names
    #print(nameTable)

    print('[INFO] Adding new records...')

    one = NameRecord()
    one.nameID = 1
    one.platformID = 3
    one.platEncID = 1
    one.langID = 0x409
    one.string = 'Changa ExtraLight'

    sixteen = NameRecord()
    sixteen.nameID = 16
    sixteen.platformID = 0
    sixteen.platEncID = 1
    sixteen.langID = 0x409
    sixteen.string = 'Changa'

    seventeen = NameRecord()
    seventeen.nameID = 17
    seventeen.platformID = 0
    seventeen.platEncID = 1
    seventeen.langID = 0x409
    seventeen.string = 'ExtraLight'

    font['name'].names.append(one)
    font['name'].names.append(sixteen)
    font['name'].names.append(seventeen)
    font.save(args.ttf_font)

    print('[INFO] Done fixing name table...')
    #nameTable = font['name'].names
    #print(nameTable)

if __name__ == '__main__':
    main()
