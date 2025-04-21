# Spliced Motif Finder

This repository contains a Python script to solve the "Finding a Spliced Motif" problem from bioinformatics, specifically as posed by Rosalind.

## Problem Statement

Given two DNA strings `s` and `t` in FASTA format:

- `s`: A long DNA sequence
- `t`: A shorter DNA sequence

The task is to find one or all valid index paths in `s` where the characters of `t` appear as a **subsequence**, maintaining order but not necessarily contiguity.

### Example

**Input (FASTA):**

```
>Rosalind_14
ACGTACGTGACG
>Rosalind_18
GTA
```

**Valid Outputs:**

- `3 4 5`
- `3 8 10`
- `7 8 10`
- etc.

## Files

- `spliced_motif.txt`: Input FASTA file containing sequences `s` and `t`.
- `spliced_motif_solver.py`: Finds **all** valid index paths.

## Requirements

- Python 3.x
- Biopython (`pip install biopython`)

## Usage

### 1. All Possible Solutions

```bash
python spliced_motif_solver.py
```

## Output

Each script prints 1-based index positions showing where the subsequence `t` appears in `s`. The "all paths" version prints one valid path per line.

## License

This project is open source and free to use under the MIT License.

## Author

Shouryan Patil

