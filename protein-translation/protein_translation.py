sequenceMap = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAC': 'Tyrosine',
    'UAU': 'Tyrosine',
    'UGC': 'Cysteine',
    'UGU': 'Cysteine',
    'UGG': 'Tryptophan',
    'UAA': 'STOP',
    'UAG': 'STOP',
    'UGA': 'STOP',
}


def proteins(strand: str):
    polypeptide = []
    for n in [strand[x:x + 3] for x in range(0, len(strand), 3)]:
        codon = sequenceMap.get(n)
        if codon == 'STOP':
            return polypeptide

        polypeptide.append(codon)

    return polypeptide
