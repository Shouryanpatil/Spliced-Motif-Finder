from Bio import SeqIO

def find_all_spliced_motif_indices(s, t):
    all_paths = []

    def backtrack(path, s_index, t_index):
        if t_index == len(t):
            all_paths.append(path[:])  # Found full match
            return
        current_char = t[t_index]
        for i in range(s_index, len(s)):
            if s[i] == current_char:
                path.append(i + 1)  # 1-based indexing
                backtrack(path, i + 1, t_index + 1)
                path.pop()  # Backtrack

    backtrack([], 0, 0)
    return all_paths

def main():
    records = list(SeqIO.parse("spliced_motif.txt", "fasta"))
    s = str(records[0].seq)
    t = str(records[1].seq)

    all_paths = find_all_spliced_motif_indices(s, t)

    # Print each path
    for path in all_paths:
        print(" ".join(map(str, path)))

if __name__ == "__main__":
    main()
