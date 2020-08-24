from LaRochelle import *
from Timecode import *
from Glasgow_Fetch import *
from MergeScript import *
from Reykjavik_Fetch import *
from pathlib import Path
from Cleanup import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename



cwd = Path.cwd()
mod_path = Path(__file__).parent

Tk().withdraw()
# hier werden die ganzen file-locations definiert
InputFile_LaRochelle = askopenfilename()#(mod_path / "Workingfiles/LaRochelleInput.CSV").resolve()
OutputFile_LaRochelle =(mod_path / "Workingfiles/OutputLaRochelle.CSV").resolve()
APIKeyGlasgow =(mod_path /  "Workingfiles/APIKeyGlasgow.CSV").resolve()# wenn wir noch eine liste mit api-keys machen sollten
APIKeyReykjavik = (mod_path /  "Workingfiles/APIKeyReykjavik.CSV").resolve()
GlasgowDumpfile = (mod_path /  "Workingfiles/GlasgowDumpfile.CSV").resolve()
ReykjavikDumpfile = (mod_path /  "Workingfiles/ReykjavikDumpfile.CSV").resolve()
Output = askopenfilename()


print(Output)
# ----------------- MAIN ----------------------

LaRochelle(InputFile_LaRochelle,OutputFile_LaRochelle)
Glasgow_Fetch(Timecodes(OutputFile_LaRochelle),GlasgowDumpfile,APIKeyGlasgow)
Reykjavik_Fetch(GlasgowDumpfile,ReykjavikDumpfile,TimecodesDays(GlasgowDumpfile),APIKeyReykjavik)
MergewithLaRochelle(ReykjavikDumpfile,OutputFile_LaRochelle)
Cleanup(OutputFile_LaRochelle,GlasgowDumpfile,ReykjavikDumpfile,Output)

print("ARCHibald finished")











