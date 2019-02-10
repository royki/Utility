
To rm all but u,p in bash just type:
rm !(u|p)


This requires the following option to be set:
shopt -s extglob
