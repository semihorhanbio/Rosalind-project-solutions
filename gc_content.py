import re

with open("/path/to/file/<filename>", "r") as file:
    fasta_file = file.read()

def extract_header(fasta_file):
    """extract headers from given fasta file from website of rosalind"""
    
    return re.findall('Rosalind_\d+', fasta_file)

def extract_seq(fasta_file):
    """extract sequences from given fasta file"""    
    
    seqs = re.split('>Rosalind_\d+', fasta_file)[1:]
    return [s.replace('\n', '') for s in seqs]

def percent_gc(seq):
    """find gc amount of given seq"""
    
    return (seq.count('G') + seq.count('C')) / len(seq) * 100

def highest_GC(fasta_file):
    """find highest gc content and give its related header file"""
    
    header_list = extract_header(fasta_file)
    seqs_list = extract_seq(fasta_file)
    gc_contents = [*map(percent_gc, seqs_list)]
    max_gc = max(gc_contents)
    return f'{header_list[gc_contents.index(max_gc)]}\n{max_gc:.6f}'
