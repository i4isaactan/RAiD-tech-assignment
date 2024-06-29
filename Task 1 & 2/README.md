README

Introduction
For task 1 & 2, I had decided to use cloud formation by AWS. However, after successfully deploying my cloud formation template, I wanted to explore other tools such as ansible and terraform. The following paragraphs will detail my experience and logic while doing this task.


Using Cloudformation

URL:http://static-website-updated2-851725612577-ap-southeast-2.s3-website-ap-southeast-2.amazonaws.com/

I started off with using cloudformation as I was more familiar with AWS services and tools than Azure, GCP or terraform. 

Logic
Here is the logic breakdown behind the cloud formation template I have come up with: 
1. Deploy 2 S3 buckets, one to host the static website and one to store Code Pipeline artefacts
2. Deploy Code Pipeline with its action to access the GitHub repository, retrieve the necessary files and store the intermediate artefacts in the artefacts bucket. 
3. At the end of the pipeline, CodePipeline deploys the final website files (e.g., HTML, CSS, JavaScript) to the other bucket, making them publicly accessible as a static website.
4. To enable automation whenever a change is committed, I set up a GitHub workflow, which will sync with the Static website whenever a change to the repository is detected.

Difficulties
As this was my first time using GitHub as my source of a static website, it took me a while to adjust to the necessary permissions to allow pipeline to interact with GitHub. Moreover, I had to read up on many Github documentation to fully understand how to use Github actions to sync the bucket with GitHub.


Using Terraform

URL:http://terrabucketauto.s3-website-ap-southeast-2.amazonaws.com/

Next, I wanted to also experiment with terraform to improve my skillset, as despite cloudformation being a useful tool, terraform was able to interact with other cloud services easily. Moreover to me, terraform seemed simpler to use and handle, with its syntax being much more straight forward and intuitive. . Again, I used AWS cloud to set up my s3 bucket using terraform.

Logic
This is the logic behind my terraform template

1. Terraform deploys a S3 bucket with an empty index.html and error.html file.
2. Using a similar GitHub action as before, I commit a change, which syncs the empty bucket with the GitHub repository, creating a static website which will continue to sync with whatever changes put forth.

Difficulties
During the deployment process, there were issues with the .git directory being included in the upload to S3. This was resolved by excluding the .git directory in the aws s3 sync command in the GitHub Actions workflow. There were also issues with configuring public access for the S3 bucket. Initially, the acl attribute was used, which caused errors due to the bucket's object ownership settings. This was resolved by configuring the bucket policy to allow public read access instead of using ACLs.


Using Ansible

Lastly, I tried out Ansible, which was a powerful configuring	tool which works on multiple cloud platforms too.

Logic
Here is the logic:
1. Deploy ec2 instance to host the website
2. Using ansible, I configured the instances to download apache(to act as a web server), as well as git(to retrieve files from GitHub).
3. This will then clone the github repository to set up a static website as needed.


