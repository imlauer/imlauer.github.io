#!/usr/bin/bash

if [[ -z $1 ]]; then
echo "Falta commit";
exit;
fi

for html in *.html; do 
	rm $html;
done
for markdown in *.md; do 
	filename_only="${markdown%.*}"
	#(
	#echo '<!DOCTYPE html>'
	#echo '<html lang="en">'
	#echo '<head>'
	#echo '  <meta charset="UTF-8">'
	#echo "  <title>Imlauer | $filename_only </title>"
	#echo '</head>'
	#echo '<body>'
	#cmark $markdown;
	#echo '</body>'
	#echo '</html>'
	#) | tee $filename_only.html &&
	#cp $filename_only.html neocities/ 
	pandoc -s $markdown | tee $filename_only.html
	cp $filename_only.html neocities/
done ;

git add . && git commit -m $1 && git push
