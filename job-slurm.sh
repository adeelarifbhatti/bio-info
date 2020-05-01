#!/bin/bash
#SBATCH --time=15:00
#SBATCH --account=nn9988k --mem-per-cpu=2G
#SBATCH --job-name question_one
#SBATCH --nodes=1
#SBATCH --ntasks=2
mkdir data
mkdir ref
mkdir script
cd script
ln -s /cluster/projects/nn9988k/norbis/exam_2020/programs/compare.py .
cd ../data
ln -s /cluster/projects/nn9988k/norbis/exam_2020/data/control.fq .
ln -s /cluster/projects/nn9988k/norbis/exam_2020/data/subject.fq .
cd ../ref
ln -s /cluster/projects/nn9988k/norbis/exam_2020/ref/ref.fa .
ln -s /cluster/projects/nn9988k/norbis/exam_2020/ref/TruSeq3-SE.fa .
module load FastQC/0.11.8-Java-1.8
module load Trimmomatic/0.38-Java-1.8
module load BWA/0.7.17-intel-2018b
module load SAMtools/1.9-intel-2018b
module load BCFtools/1.9-intel-2018b
bwa index ref.fa
samtools faidx ref.fa
cd ../data
fastqc -t 2 control.fq subject.fq
java -jar $EBROOTTRIMMOMATIC/trimmomatic-0.38.jar SE control.fq  control.trim.fq   SLIDINGWINDOW:4:20 MINLEN:25 ILLUMINACLIP:../ref/TruSeq3-SE.fa:2:40:15
java -jar $EBROOTTRIMMOMATIC/trimmomatic-0.38.jar SE subject.fq subject.trim.fq   SLIDINGWINDOW:4:20 MINLEN:25 ILLUMINACLIP:../ref/TruSeq3-SE.fa:2:40:15
bwa mem -t 2 ../ref/ref.fa control.trim.fq > control.sam
bwa mem -t 2 ../ref/ref.fa subject.trim.fq > subject.sam
samtools view -S -b control.sam > control.bam
samtools view -S -b subject.sam > subject.bam
samtools sort -o control.sorted.bam control.bam -@2
samtools sort -o subject.sorted.bam subject.bam -@2
samtools index control.sorted.bam -@2
samtools index subject.sorted.bam -@2
bcftools mpileup -O b --threads 2 -o control.raw.bcf -f ../ref/ref.fa control.sorted.bam
bcftools mpileup -O b --threads 2 -o subject.raw.bcf -f ../ref/ref.fa subject.sorted.bam
bcftools call --ploidy 1 -m -v --threads 2 -o control.variants.vcf control.raw.bcf
bcftools call --ploidy 1 -m -v --threads 2 -o subject.variants.vcf subject.raw.bcf
../script/compare.py control.variants.vcf subject.variants.vcf
