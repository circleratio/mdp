DEST=~/bin
FILES='mdsplit mdsplit-tag mdfzf'

echo Installing at ${DEST}
for f in ${FILES}; do
    LINK=$(readlink -f ${f})
    echo ${LINK}
    (cd ${DEST} ; ln -s ${LINK})
done

LINK=$(readlink -f mdp.py)
(cd ${DEST} ; ln -s ${LINK} mdp)
