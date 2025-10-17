#!/usr/bin/bash
rm index.html  &&
(
echo '<!DOCTYPE html>'
echo '<html lang="en">'
echo '<head>'
echo '  <meta charset="UTF-8">'
echo '  <title>Imlauer</title>'
echo '</head>'
echo '<body>'
cmark index.md
echo '</body>'
echo '</html>'
) | tee index.html &&
git add . && git commit -m index && git push
