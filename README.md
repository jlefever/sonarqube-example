1. Start the SonarQube server and database.
```
docker-compose up
```
On linux, you may get an error from ElasticSearch, running `sudo sysctl -w vm.max_map_count=262144` will fix it. See [here](https://stackoverflow.com/questions/42300463/elasticsearch-bootstrap-checks-failing) for more info.

2. Open http://localhost:9000/ in your browser and log in with default credentials (username and password are both "admin").

3. Navigate to User > My Account > Security and click "Generate" to create a security token. Copy this to your clipboard.

4. It appears you have to build the project before you can analyze it. So for [deltaspike](https://github.com/apache/deltaspike), run
```
mvn clean package -DskipTests -Drat.skip
```

5. Once that completes, you can run SonarScanner using maven.
```
mvn org.sonarsource.scanner.maven:sonar-maven-plugin:3.7.0.1746:sonar -Dsonar.login=<your token from step 3> -Dsonar.host.url=http://localhost:9000

```
For other non-maven or non-Java projects, the user will have to follow different SonarScanner instructions.

6. When the scanner completes it will upload to the server.

7. Now you can run the example python script. (You may have to `pip3 install psycopg`)
```
python3 example.py
```
This will print a csv to stdout. You will probably have to adjust the SQL query by joining to a few tables to get the project name and any other information you want.