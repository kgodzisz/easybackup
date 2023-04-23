<p>This Dockerfile with a simple script written in Python allows to back up a specified folder. I create by it a Docker image, which I use. However, if you want, I also provide the script itself. Therefore, you can run it using Python installed on your local system. </p><br />

<p><strong>Downloading files from GitHub:</strong></p>
<p><code>git clone https://github.com/kgodzisz/easybackup.git</code></p><br />

<p><strong>Creating your own image in your local repository:</strong></p>
<p><code>docker build -t easybackup .</code></p><br />

<p><strong>Running the tool:</strong></p>
<p><code>docker run --rm -v /path/to/where/storage/backups:/backups -v /path/to/data/to/backup:/data easybackup</code></p><br />

<p><strong>The second way is to download the prepared file from the Docker Hub repository:</strong></p>
<p><code>docker run --rm -v /path/to/where/storage/backups:/backups -v /path/to/data/to/backup:/data kgodzisz/easybackup</code></p><br />

<p><strong>Description of options used in commands: </strong></p>
<p><code>--rm </code>- the container will be automatically removed after exiting;</p> 
<p><code>-v /path/to/where/storage/backups:/backups </code>- path to the folder where backups should be stored;</p> 
<p><code>-v /path/to/data/to/backup:/data </code>- path to the folder with data that should be backed up; </p>
<p><code>easybackup </code>- the name of the created image that we want to use; </p>
<p><code>kgodzisz/easybackup </code>- the address of the image on the DockerHub platform.</p><br />

<p><strong>Blog:</strong> <a href="https://dockeryzacjaswiata.pl" target="_blank">https://dockeryzacjaswiata.pl</a></p>
<p><strong>Docker Hub:</strong> <a href="https://hub.docker.com/r/kgodzisz/easybackup" target="_blank">https://hub.docker.com/r/kgodzisz/easybackup</a></p>
