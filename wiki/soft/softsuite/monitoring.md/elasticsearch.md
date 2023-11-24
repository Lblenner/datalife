# Elastic search

Mostly open source ? -> à vérfier

[Guide suivi](https://www.elastic.co/blog/how-to-monitor-nginx-web-servers-with-the-elastic-stack)

Suite de logiciel 

metricbeat - collecte de metrics ( notamment nginx)
filebeat - collecte des logs
elasticsearch - the main thing used by above
kibana - visualisateur de data ? 

Lien de telechargeent pour arm64

-  https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.11.1-arm64.deb
-  https://artifacts.elastic.co/downloads/beats/metricbeat/metricbeat-8.11.1-arm64.deb
-  https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.11.1-arm64.deb
-  https://artifacts.elastic.co/downloads/kibana/kibana-8.11.1-arm64.deb


/etc/ pour les differentes configs

Finalement, elastic-agent semble plus approprié que d'avoir metricbeat et filebeat.
https://www.elastic.co/guide/en/fleet/current/elastic-agent-installation.html

On obtient plusieurs dashboard avec de jolies diagrammes sur kibana 
Mais les trois service (elasticsearch, kibana et elastic-agent) utilisent tellement de ressources 
Pas réussie à avoir des stats pas sites pour nginx T_T

Pas worth-it pour ma raspi -> Kill

Il faudrait voir pour une installe auto avec docker mais bof outil pour mes besoins

-> Intéréssant pour gerer plusieurs serveurs par contre 




