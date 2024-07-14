# Projet Hadoop IABD1 groupe 11

## Mise en place de l'environement

### Création de l'utilisateur Hadoop et attribution des droits

```bash
sudo useradd -m -s /bin/bash hadoop
sudo passwd hadoop
sudo usermod -aG sudo hadoop
id hadoop
sudo chown -R hadoop:hadoop /usr/local/hadoop
hdfs dfs -mkdir -p /user/hadoop/
ssh-keygen -t rsa -P ""
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
chmod 700 ~/.ssh
```

- Ajout des lignes nécessaires dans la config hadoop
```bash
nano ~/.bashrc
  # Hadoop environment variables
  export HADOOP_HOME=/usr/local/hadoop
  export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
```
- Copie du fichier puis lister les fichiers dans hadoop
```bash
hdfs dfs -put chemin/nomdufichier /user/hadoop/
hdfs dfs -ls /user/hadoop/
```

## Python
### Librairies et dépendances

### Mise en place de PySpark

### Premier test avec Plotly

### Commande Hadoop utile 
```bash
start-dfs.sh # Lancement name et data nodes
start-yarn.sh # Lancement ressource manager et yarn manager
hdfs dfsadmin -report # Rapport détaillé sur le système de fichier HDFS
```
