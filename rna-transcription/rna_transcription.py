def to_rna(dna_strand: str) -> str:
    return dna_strand.replace("G", "X")\
        .replace("C", "G")\
        .replace("X", "C")\
        .replace("A", "U")\
        .replace("T", "A")

