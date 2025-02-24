Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "python -m game.main", 0, False
Set WshShell = Nothing
