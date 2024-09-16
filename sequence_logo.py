import logomaker
import pandas as pd
from collections import Counter

# Example aligned DNA sequences
sequences = ['ACGT', 'ACGA', 'ACGT', 'ACTT', 'ACGG', 'ACGA']

# Step 1: Calculate nucleotide frequencies per position
def nucleotide_frequencies(sequences):
    sequence_length = len(sequences[0])
    freqs = {pos: Counter([seq[pos] for seq in sequences]) for pos in range(sequence_length)}
    freq_matrix = pd.DataFrame(freqs).T
    return freq_matrix.div(freq_matrix.sum(axis=1), axis=0).fillna(0)

# Step 2: Create a frequency matrix
freq_matrix = nucleotide_frequencies(sequences)

# Step 3: Generate the sequence logo using logomaker
logo = logomaker.Logo(freq_matrix)

# Customize the appearance
logo.style_spines(visible=False)
logo.style_xticks(rotation=0, fmt='%d', anchor=0)
logo.ax.set_ylabel("Probability")

# Display the sequence logo
logo.fig.show()
