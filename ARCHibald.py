from LaRochelle import *
from Reykjavik_Fetch import *
from Glasgow_Fetch import *
from MergeScript import *


InputFile_LaRochelle = ""
OutputFile_LaRochelle = ""
API_keys = ""# wenn wir noch eine liste mit api-keys machen sollten

LaRochelle(InputFile_LaRochelle,OutputFile_LaRochelle)
Glasgow_Fetch(Timecodes(OutputFile_LaRochelle))#Output als File oder Liste?












