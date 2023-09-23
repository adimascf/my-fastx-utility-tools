import pyfastx
from collections import defaultdict
import click


def counter_single_end(fastq1, topn):
    """Counts unique reads from given file"""

    uniqe_reads_count = defaultdict(int)
    fq1 = pyfastx.Fastq(fastq1)
    fq1 = pyfastx.Fastq(fastq1, build_index=False)
    print(f"{fastq1} {len(fq1)} reads")

    for name, seq, qual in fq1:
        uniqe_reads_count[seq] += 1

    sorted_reads_count = sorted(
        uniqe_reads_count.items(), key=lambda x: x[1], reverse=True
    )
    sorted_reads_count = dict(sorted_reads_count)
    for idx, item in enumerate(sorted_reads_count):
        if idx == int(topn):
            break
        print(f"{item}: {sorted_reads_count[item]}")
    print("\n")


def counter_paired_end(fastq1, fastq2, topn):
    """Counts unique reads from given files"""

    counter_single_end(fastq1, topn)
    counter_single_end(fastq2, topn)


@click.command()
@click.option("--paired", is_flag=True, help="Paired end fastq files")
@click.option("--fastq1", help="The fastq read 1 path file")
@click.option("--fastq2", help="The fastq read 2 path file")
@click.option("--topn", help="Display top N unique read(s) with the count")
def counter(paired, fastq1, fastq2, topn):
    if paired == False:
        counter_single_end(fastq1, topn)
    elif paired == True:
        counter_paired_end(fastq1, fastq2, topn)


if __name__ == "__main__":
    counter()
