while IFS=$'\t' read -r column1 column2 column3 ; do

awk -v col3="${column3}" -v col2="$column2" '{if ($2 >= col2 && $2<=col3) print $2}' subject.variants.vcf >> Arif.txt
awk -v col3="${column3}" -v col2="$column2" '{if ($2 >= col2 && $2<=col3) print $2}' control.variants.vcf >> Arif.txt
done < "intervals.bed"

wc -l Arif.txt
