# -*- mode: python -*-

block_cipher = None


a = Analysis(['count_and_say_sequence.py'],
             pathex=['C:\\Users\\eduar\\Dropbox\\Documents\\Python\\python_projects\\count_and_say_20190809'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='count_and_say_sequence',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='C:\\Users\\eduar\\Dropbox\\Documents\\Python\\python_projects\\count_and_say_20190809\\Papirus-Team-Papirus-Apps-Alc.ico')
