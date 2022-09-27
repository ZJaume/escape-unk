from argparse import ArgumentParser
import sentencepiece as sp
import sys

def main():
    parser = ArgumentParser()
    parser.add_argument('-m','--spm_model', required=True)
    args = parser.parse_args()

    def encode(text, output_type=str):
        return spm.encode(text, add_bos=False, add_eos=False,
                          out_type=output_type)

    #TODO choose escape delimiters based on spm vocab to avoid OOV
    spm = sp.SentencePieceProcessor(args.spm_model)

    for line in sys.stdin:
        escaped = []
        ids = encode(line.strip('\n'), int)
        pieces = encode(line.strip('\n'))
        for id_, piece in zip(ids, pieces):
            if spm.is_unknown(id_):
                # Escape
                escaped.append('[[' + str(ord(piece)) + ']]')
            else:
                escaped.append(piece)

        # Detokenize manually to void spm introducing spaces in escaped text
        # lstrip to remove initial space that is removed by spm.decode
        print(''.join(escaped).replace('▁', ' ').lstrip())

if __name__ == "__main__":
    main()
