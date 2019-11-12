
# cp "$sample1"-Canu/"$sample1"_canu.contigs.fasta Assembly-9/"$sample1"_canu.contigs.fasta
# \" + str(x) + \"
# print("\"")
# \" + str(x) + \"

out = ""

# Type here the code to convert from bash to python. Careful, the script will convert every "1" in the variable "x"
P = """gzip -d "$sample1".fastq.gz"""
for letter in P:
    if letter is "\"":
        out = out + "\\"
    if letter is "1":
            out = out + "\" + str(x) + \""
    else:
        out = out + letter
print(out)

#
x = 0
t=1
while t<24:
    x=x+1
    print("echo \"$sample" + str(x) + "\"")
    print("gzip \"$sample" + str(x) + "\".fastq")
    #print("cp \"$sample" + str(x) + "\".fastq.gz \"$sample" + str(x) + "\"-cut.fastq.gz")
    print("gunzip -c \"$sample" + str(x) + "\".fastq.gz | NanoFilt -l 750 -q 6 --readtype 1D > \"$sample" + str(x) + "\"_cut.fastq")
    print("gzip -d \"$sample" + str(x) + "\".fastq.gz")
    print("\n")
    t=t+1

