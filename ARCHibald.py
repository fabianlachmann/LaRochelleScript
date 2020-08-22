from LaRochelle import *
from Timecode import *
from Glasgow_Fetch import *
from MergeScript import *
from Reykjavik_Fetch import *
from pathlib import Path

# `cwd`: current directory is straightforward
cwd = Path.cwd()

# `mod_path`: According to the accepted answer and combine with future power
# if we are in the `helper_script.py`
mod_path = Path(__file__).parent

# `src_path`: with the future power, it's just so straightforward

# hier werden die ganzen file-locations definiert
InputFile_LaRochelle = (mod_path / "Workingfiles/LaRochelleInput.CSV").resolve()
OutputFile_LaRochelle =(mod_path / "Workingfiles/OutputLaRochelle.CSV").resolve()
APIKeyGlasgow = "Workingfiles/APIKeyGlasgow.CSV"# wenn wir noch eine liste mit api-keys machen sollten
APIKeyReykjavik = "Workingfiles/APIKeyReykjavik.CSV"
GlasgowDumpfile = "Workingfiles/GlasgowDumpfile.CSV"
ReykjavikDumpfile = "Workingfiles/ReykjavikDumpfile.CSV"




# ----------------- MAIN ----------------------

LaRochelle(InputFile_LaRochelle,OutputFile_LaRochelle)
Glasgow_Fetch(Timecodes(OutputFile_LaRochelle),GlasgowDumpfile,APIKeyGlasgow)
Reykjavik_Fetch(GlasgowDumpfile,ReykjavikDumpfile,TimecodesDays(GlasgowDumpfile),APIKeyReykjavik)
MergewithLaRochelle(ReykjavikDumpfile,OutputFile_LaRochelle)

print("ARCHibald finished")











