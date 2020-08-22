from LaRochelle import *
from Timecode import *
from Glasgow_Fetch import *
from MergeScript import *
from Reykjavik_Fetch import *

# hier werden die ganzen file-locations definiert
InputFile_LaRochelle = ""
OutputFile_LaRochelle = ""
APIKeyGlasgow = ""# wenn wir noch eine liste mit api-keys machen sollten
APIKeyReykjavik = ""
GlasgowDumpfile = ""
ReykjavikDumpfile = ""




# ----------------- MAIN ----------------------

LaRochelle(InputFile_LaRochelle,OutputFile_LaRochelle)
Glasgow_Fetch(Timecodes(OutputFile_LaRochelle),GlasgowDumpfile,APIKeyGlasgow)
Reykjavik_Fetch(GlasgowDumpfile,ReykjavikDumpfile,TimecodesDays(GlasgowDumpfile),APIKeyReykjavik)
MergewithLaRochelle(ReykjavikDumpfile,OutputFile_LaRochelle)

print("ARCHibald finished")











