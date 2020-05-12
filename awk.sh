FILE=count.txt
if test -f "$FILE"; then
    echo "$FILE exist"
    echo "deleting $FILE"
    rm ./count.txt
fi
cat control.variants.vcf > sample.data
cat subject.variants.vcf >> sample.data


while IFS=$'\t' read -r column1 column2 column3 ; do
awk -v col3="${column3}" -v col2="$column2" '{if ($2 >= col2 && $2<=col3) print $2}' sample.data >> count.txt
done < "intervals.bed"

wc -l count.txt
