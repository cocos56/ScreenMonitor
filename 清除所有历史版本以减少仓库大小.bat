git checkout --orphan latest_branch
git add -A
git commit -am "���������ʷ�汾�Լ��ٲֿ��С�������´�Զ�̿����˲ֿ�"
git branch -D master
git branch -m master
git push -f origin master
