import HTSeq
import argparse





parser = argparse.ArgumentParser() #simplifys the wording of using argparse as stated in the python tutorial


# Basic input output files
parser.add_argument("-i", type=str, action='store',  dest='input', help="Input the FASTA/Q file") # allows input of the forward read
parser.add_argument("-b", type=str, action='store',  dest='blastfile', help="Input the BLAST output") # allows input of the forward read
parser.add_argument("-o", type=str, action='store',  dest='outputfile', help="Name for the output files") # allows input of the forward read



args = parser.parse_args()



# Place each of the input into a simple variable to call
fastafile = str(args.input)
blast = str(args.blastfile)
output = str(args.outputfile)




for line in open(blast,'r'):
    if line.startswith('#'):
        continue
    else:
        last = line.split('\t')[0]
  
print last

outputting = open(output,'w')
todo = False
for read in HTSeq.FastaReader(fastafile):
    if todo == False:
        if read.name == last:
            outputting.write('>' + read.name + '\n')
            outputting.write(read.seq + '\n')
        else:
            continue
    else:
        outputting.write('>' + read.name + '\n')
        outputting.write(read.seq + '\n')


outputting.close()






