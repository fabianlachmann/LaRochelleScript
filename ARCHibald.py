from LaRochelle import *
from Timecode import *
from Glasgow_Fetch import *
from MergeScript import *
from Reykjavik_Fetch import *

# hier werden die ganzen file-locations definiert
InputFile_LaRochelle = ""
OutputFile_LaRochelle = ""
API_keys = ""# wenn wir noch eine liste mit api-keys machen sollten
GlasgowDumpfile = ""
ReykjavikDumpfile = ""




# ----------------- MAIN ----------------------

LaRochelle(InputFile_LaRochelle,OutputFile_LaRochelle)
Glasgow_Fetch(Timecodes(OutputFile_LaRochelle),GlasgowDumpfile)
Reykjavik_Fetch(GlasgowDumpfile,ReykjavikDumpfile)
MergewithLaRochelle(ReykjavikDumpfile,OutputFile_LaRochelle)

print("finished")











